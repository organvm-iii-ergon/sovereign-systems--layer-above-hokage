# Vacuum Detector — Core Algorithm

## The Law

> *"If there's no data or statistics to prove whichever answer is the best one, then it's an opportunity for studying and figuring it out. So that means all of it."*

This algorithm operationalizes that law.

---

## Types of Vacuum

| Type | Definition | Signal |
|---|---|---|
| **Structural** | No data exists at all | Evidence base has 0 coverage |
| **Measurement** | Data exists but not captured | Evidence present, stats missing |
| **Inference** | Missing causal links | Coverage exists, no causal tests |
| **Attribution** | Unknown value drivers | Outcomes observed, drivers unknown |
| **Interface** | Knowledge not embedded | Query returns empty/low relevance |

---

## Algorithm

```python
# vacuum_detector.py
from dataclasses import dataclass
from enum import Enum
from typing import Optional
import numpy as np

class VacuumType(Enum):
    STRUCTURAL = "structural"
    MEASUREMENT = "measurement"
    INFERENCE = "inference"
    ATTRIBUTION = "attribution"
    INTERFACE = "interface"

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
    has_observations: bool
    has_statistics: bool
    has_causal_tests: bool
    has_attribution: bool
    sample_size: Optional[int] = None
    coverage: float = 0.0  # Composite score

class VacuumDetector:
    """
    Detects vacuum radiation — knowledge gaps that need study.
    
    Law: If there's no data to prove it, study it.
    """
    
    def __init__(
        self,
        evidence_threshold: float = 0.05,
        causal_evidence_weight: float = 0.4,
        measurement_evidence_weight: float = 0.3,
        attribution_evidence_weight: float = 0.3
    ):
        self.threshold = evidence_threshold
        self.causal_weight = causal_evidence_weight
        self.measurement_weight = measurement_evidence_weight
        self.attribution_weight = attribution_evidence_weight
    
    def detect(
        self,
        claims: list[Claim],
        evidence_base: dict[str, Evidence]
    ) -> list[Vacuum]:
        """Detect vacuums in claims."""
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
                    priority=self._priority(claim, 0.0),
                    affected_domains=claim.domains,
                    detected_at=self._timestamp(),
                    recommended_action="collect_baseline_data"
                ))
            else:
                # Calculate composite coverage
                coverage = self._calculate_coverage(evidence)
                
                if coverage < self.threshold:
                    # Determine type by what's missing
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
            # Has quantitative data
            score += 0.3
        
        if evidence.has_statistics:
            # Has statistics
            score += self.measurement_weight
        
        if evidence.has_causal_tests:
            # Has causal tests
            score += self.causal_weight
        
        if evidence.has_attribution:
            # Has attribution
            score += self.attribution_weight
        
        return score
    
    def _classify_vacuum(self, evidence: Evidence) -> VacuumType:
        """Classify the type of vacuum."""
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
        
        # Fewer domains = more focused = higher priority for now
        # Expanded to cover all domains = lower priority per-domain
        if len(claim.domains) == 1:
            return "high"
        return "medium"
    
    def _recommend(self, vacuum_type: VacuumType) -> str:
        """Recommend action based on type."""
        recommendations = {
            VacuumType.STRUCTURAL: "baseline_data_collection",
            VacuumType.MEASUREMENT: "instrumentation_and_capture",
            VacuumType.INFERENCE: "design_causal_study",
            VacuumType.ATTRIBUTION: "build_attribution_model",
            VacuumType.INTERFACE: "embed_and_retrieve"
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
        """Get timestamp."""
        from datetime import datetime
        return datetime.now().isoformat()
```

---

## Detector Configuration

```yaml
# detector.yaml
vacuum_detector:
  version: "1.0"
  
  thresholds:
    evidence: 0.05      # Minimum evidence to not be a vacuum
    measurement: 0.30    # Minimum for measurement
    causal: 0.40         # Minimum for causal inference
    attribution: 0.30     # Minimum for attribution
  
  weights:
    causal_evidence: 0.4
    measurement_evidence: 0.3
    attribution_evidence: 0.3
  
  priority_rules:
    critical:
      - evidence_coverage: 0.0
      - affected_domains: "*"  # All domains
    high:
      - evidence_coverage: < 0.05
      - single_domain_impact
    medium:
      - evidence_coverage: < 0.30
      - multiple_domains
  
  action_mapping:
    structural: baseline_data_collection
    measurement: instrumentation
    inference: causal_study_design
    attribution: attribution_model
    interface: embedding_pipeline
```

---

## Integration with Operators

The vacuum detector feeds the four Sovereign operators:

```
┌─────────────────────────────────────────┐
│           VACUUM DETECTOR               │
└────────────────┬────────────────────────┘
                 │
     ┌───────────┼───────────┬───────────┐
     ▼           ▼           ▼           ▼
┌─────────┐ ┌─────────┐ ┌─────────┐ ┌─────────┐
│SELFISH- │ │MAGNETIC │ │PORTFOLIO│ │REFLEXIVE│
│ALTRUIST │ │MEMBRANE│ │OPERATOR │ │  LOOP  │
│  LOOP   │ │        │ │        │ │        │
└────┬────┘ └────┬────┘ └───┬─────┘ └──┬────┘
     │           │           │          │
     └───────────┴─────┬─────┴──────────┘
                      ▼
              ┌─────────────┐
              │   PHASE    │
              │ EXECUTION  │
              └───────────┘

Each operator handles its type of vacuum:
- Selfish-altruistic: Structural vacuums
- Magnetic membrane: Inference vacuums  
- Portfolio: Attribution vacuums
- Reflexive: Interface vacuums
```

---

## Quality Gates

| Gate | Requirement |
|---|---|
| Coverage calculation | Reproducible from evidence base |
| Type classification | At least 80% accurate |
| Priority alignment | 3/4 domain experts agree |
| Action mapping | Leads to insight |

---

## Decision Log

| Date | Decision | Rationale |
|---|---|---|
| 2026-04-26 | Detector as law operationalization | Law needs algorithm |
| 2026-04-26 | Five vacuum types | Covers all evidence gaps |
| 2026-04-26 | Feeds four operators | Each operator handles its type |
| 2026-04-26 | Priority ranking | Focus resources on impact |

---

*The detector is the instrument. Every vacuum is a call to study.*