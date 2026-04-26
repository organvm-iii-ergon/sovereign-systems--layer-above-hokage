# vacuum_detector/algorithm.py
"""
Vacuum Detector — Core Algorithm

Law: "If there's no data or statistics to prove whichever answer is 
the best one, then it's an opportunity for studying and figuring it out."

This module operationalizes that law.
"""

from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from typing import Optional, Protocol, runtime_checkable
import json


class VacuumType(Enum):
    """Types of vacuum (knowledge gaps)."""
    STRUCTURAL = "structural"      # No data exists
    MEASUREMENT = "measurement"    # Data exists, not captured
    INFERENCE = "inference"      # Missing causal links
    ATTRIBUTION = "attribution"   # Unknown value drivers
    INTERFACE = "interface"      # Knowledge not embedded


@dataclass
class Vacuum:
    """A vacuum — a knowledge gap requiring study."""
    id: str
    type: VacuumType
    claim: str
    evidence_coverage: float  # 0.0 to 1.0
    priority: str  # critical, high, medium, low
    affected_domains: list[str]
    detected_at: str
    recommended_action: str
    
    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "type": self.type.value,
            "claim": self.claim,
            "evidence_coverage": self.evidence_coverage,
            "priority": self.priority,
            "affected_domains": self.affected_domains,
            "detected_at": self.detected_at,
            "recommended_action": self.recommended_action
        }


@dataclass
class Claim:
    """A claim that can be tested."""
    id: str
    statement: str
    domains: list[str]
    evidentiary_threshold: float = 0.05


@dataclass  
class Evidence:
    """Evidence for a claim."""
    claim_id: str
    has_observations: bool = False
    has_statistics: bool = False
    has_causal_tests: bool = False
    has_attribution: bool = False
    sample_size: Optional[int] = None
    coverage: float = 0.0
    
    @classmethod
    def from_dict(cls, data: dict) -> "Evidence":
        return cls(
            claim_id=data.get("claim_id", ""),
            has_observations=data.get("has_observations", False),
            has_statistics=data.get("has_statistics", False),
            has_causal_tests=data.get("has_causal_tests", False),
            has_attribution=data.get("has_attribution", False),
            sample_size=data.get("sample_size"),
            coverage=data.get("coverage", 0.0)
        )


class VacuumDetector:
    """
    Detects vacuum radiation — knowledge gaps that need study.
    
    Law: If there's no data to prove it, study it.
    
    Example:
        >>> detector = VacuumDetector()
        >>> claims = [Claim(id="c1", statement="Research improves ROI", domains=["research"])]
        >>> evidence = {"c1": Evidence(claim_id="c1", has_observations=True, has_statistics=False)}
        >>> vacuums = detector.detect(claims, evidence)
        >>> print(vacuums[0].type)  # MEASUREMENT
    """
    
    def __init__(
        self,
        evidence_threshold: float = 0.05,
        causal_weight: float = 0.4,
        measurement_weight: float = 0.3,
        attribution_weight: float = 0.3
    ):
        self.threshold = evidence_threshold
        self.causal_weight = causal_weight
        self.measurement_weight = measurement_weight
        self.attribution_weight = attribution_weight
    
    def detect(
        self,
        claims: list[Claim],
        evidence_base: dict[str, Evidence]
    ) -> list[Vacuum]:
        """Detect vacuums in claims.
        
        Args:
            claims: List of claims to check
            evidence_base: Evidence for each claim by ID
            
        Returns:
            List of detected vacuums, ranked by priority
        """
        vacuums = []
        
        for claim in claims:
            evidence = evidence_base.get(claim.id)
            
            if evidence is None:
                # No evidence at all = structural vacuum
                vacuums.append(Vacuum(
                    id=f"vac-{claim.id}",
                    type=VacuumType.STRUCTURAL,
                    claim=claim.statement,
                    evidence_coverage=0.0,
                    priority="critical",
                    affected_domains=claim.domains,
                    detected_at=self._timestamp(),
                    recommended_action="collect_baseline_data"
                ))
            else:
                coverage = self._calculate_coverage(evidence)
                
                if coverage < claim.evidentiary_threshold:
                    vacuum_type = self._classify_vacuum(evidence)
                    priority = self._priority(claim, coverage)
                    
                    vacuums.append(Vacuum(
                        id=f"vac-{claim.id}",
                        type=vacuum_type,
                        claim=claim.statement,
                        evidence_coverage=coverage,
                        priority=priority,
                        affected_domains=claim.domains,
                        detected_at=self._timestamp(),
                        recommended_action=self._recommend(vacuum_type)
                    ))
        
        return self._rank_by_impact(vacuums)
    
    def _calculate_coverage(self, evidence: Evidence) -> float:
        """Calculate composite evidence coverage."""
        score = 0.0
        
        if evidence.sample_size and evidence.sample_size > 30:
            score += 0.3
        
        if evidence.has_statistics:
            score += self.measurement_weight
        
        if evidence.has_causal_tests:
            score += self.causal_weight
        
        if evidence.has_attribution:
            score += self.attribution_weight
        
        return min(score, 1.0)  # Cap at 1.0
    
    def _classify_vacuum(self, evidence: Evidence) -> VacuumType:
        """Classify the type of vacuum based on what's missing."""
        if not evidence.has_observations:
            return VacuumType.STRUCTURAL
        if not evidence.has_statistics:
            return VacuumType.MEASUREMENT
        if not evidence.has_causal_tests:
            return VacuumType.INFERENCE
        if not evidence.has_attribution:
            return VacuumType.ATTRIBUTION
        return VacuumType.INTERFACE
    
    def _priority(self, claim: Claim, coverage: float) -> str:
        """Determine priority by impact."""
        if coverage == 0.0:
            return "critical"
        
        if len(claim.domains) == 1:
            return "high"
        return "medium"
    
    def _recommend(self, vacuum_type: VacuumType) -> str:
        """Recommend action based on vacuum type."""
        recommendations = {
            VacuumType.STRUCTURAL: "collect_baseline_data",
            VacuumType.MEASUREMENT: "add_instrumentation",
            VacuumType.INFERENCE: "design_causal_study",
            VacuumType.ATTRIBUTION: "build_attribution_model",
            VacuumType.INTERFACE: "build_embedding_pipeline"
        }
        return recommendations.get(vacuum_type, "investigate")
    
    def _rank_by_impact(self, vacuums: list[Vacuum]) -> list[Vacuum]:
        """Rank vacuums by domain impact."""
        priority_order = {"critical": 0, "high": 1, "medium": 2, "low": 3}
        
        return sorted(
            vacuums,
            key=lambda v: (
                priority_order.get(v.priority, 4),
                len(v.affected_domains)
            )
        )
    
    def _timestamp(self) -> str:
        return datetime.now().isoformat()


class BatchVacuumDetector:
    """Batch vacuum detector for processing multiple claims."""
    
    def __init__(self, config: Optional[dict] = None):
        self.detector = VacuumDetector(
            evidence_threshold=config.get("evidence_threshold", 0.05) if config else 0.05,
            causal_weight=config.get("causal_weight", 0.4) if config else 0.4,
            measurement_weight=config.get("measurement_weight", 0.3) if config else 0.3,
            attribution_weight=config.get("attribution_weight", 0.3) if config else 0.3
        )
    
    def detect_from_file(self, claims_file: str, evidence_file: str) -> list[Vacuum]:
        """Load claims and evidence from files, detect vacuums."""
        # Load claims
        with open(claims_file) as f:
            claims_data = json.load(f)
        claims = [Claim(**c) for c in claims_data.get("claims", [])]
        
        # Load evidence
        with open(evidence_file) as f:
            evidence_data = json.load(f)
        evidence_base = {
            k: Evidence.from_dict(v) 
            for k, v in evidence_data.get("evidence", {}).items()
        }
        
        return self.detector.detect(claims, evidence_base)
    
    def export_vacuums(self, vacuums: list[Vacuum], output_file: str):
        """Export vacuums to JSON file."""
        data = {
            "exported_at": datetime.now().isoformat(),
            "count": len(vacuums),
            "vacuums": [v.to_dict() for v in vacuums]
        }
        with open(output_file, "w") as f:
            json.dump(data, f, indent=2)


if __name__ == "__main__":
    # Quick test
    claims = [
        Claim(id="c1", statement="Research improves ROI", domains=["research"]),
        Claim(id="c2", statement="Vacuum detection improves coordination", domains=["hokage"]),
        Claim(id="c3", statement="Attribution is correct", domains=["commerce"]),
    ]
    
    evidence = {
        "c1": Evidence(claim_id="c1", has_observations=True, has_statistics=False),
        "c2": Evidence(claim_id="c2", has_observations=False),
        "c3": Evidence(claim_id="c3", has_observations=True, has_statistics=True, has_causal_tests=False),
    }
    
    detector = VacuumDetector()
    vacuums = detector.detect(claims, evidence)
    
    print(f"Detected {len(vacuums)} vacuums:")
    for v in vacuums:
        print(f"  [{v.priority.upper()}] {v.type.value}: {v.claim[:50]}... → {v.recommended_action}")