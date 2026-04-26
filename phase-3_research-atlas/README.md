# Phase 3: Research Atlas — The Evidentiary Substrate

## The Law of the Land

**CORE PRINCIPLE**: *"If there's no data or statistics to prove whatever answer is best, then it's an opportunity for studying and figuring it out. So that means all of it."*

This is not a suggestion — this is the **constitutional basis** for Sovereign. Every decision, every route, every execution path flows from this law.

### Implications

| Statement | Consequence |
|---|---|
| No data → Study | Every gap becomes a research opportunity |
| No stats → Measure | Every assumption needs quantitative validation |
| "All of it" | No domain is excluded from study |
| "Best" requires proof | All paths need evidentiary support |

### The Recursive Principle

The Atlas also studies itself:

1. **Coverage audit**: What do we know? → Execute
2. **Gap detection**: What don't we know? → Study
3. **Meta-study**: How do we know what we know? → Recurse

---

## File Structure

```
phase-3_research-atlas/
├── README.md                    # This file
├── LAW.md                       # Constitutional basis
├── ros-spec.md                  # Research Operating System spec
├── pillars/
│   ├── causal-inference/
│   │   ├── README.md           # Pillar overview
│   │   ├── reading-ladder.md  # 4-level progressive reading
│   │   ├── canonical-papers/
│   │   │   ├── 01-pearl-2019-book-of-why.md
│   │   │   ├── 02-pearl-2019-causal-inference.md
│   │   │   ├── 03-hernan-2020-what-if.md
│   │   │   ├── 04-imbens-2015-causal-inference.md
│   │   │   ├── 05-vanderlaan-2011-targeted-learning.md
│   │   │   ├── 06-vanderweele-2015-mediation.md
│   │   │   └── ...
│   │   ├── experiment-templates/
│   │   │   ├── randomized-trial.yaml
│   │   │   ├── instrumental-variable.yaml
│   │   │   ├── regression-discontinuity.yaml
│   │   │   ├── difference-in-differences.yaml
│   │   │   └── synthetic-control.yaml
│   │   ├── data/
│   │   │   ├── schemas/
│   │   │   │   └── experiment.schema.json
│   │   │   └── inputs/
│   │   └── ros-spec.yaml
│   ├── unit-economics/
│   │   ├── README.md
│   │   ├── reading-ladder.md
│   │   ├── canonical-papers/
│   │   │   ├── 01-saas-metrics-kpcb.md
│   │   │   ├── 02-thiel-2014-zero-to-one.md
│   │   │   ├── 03-armstrong-2020-marketing-metrics.md
│   │   │   ├── 04-croll-2014-lean-analytics.md
│   │   │   ├── 05-parker-2016-platform-economics.md
│   │   │   └── ...
│   │   ├── experiment-templates/
│   │   │   ├── cohort-analysis.yaml
│   │   │   ├── attribution-model.yaml
│   │   │   ├── ltv-calculation.yaml
│   │   │   └── payback-period.yaml
│   │   ├── data/
│   │   │   └── schemas/
│   │   └── ros-spec.yaml
│   └── algorithmic-interface/
│       ├── README.md
│       ├── reading-ladder.md
│       ├── canonical-papers/
│       │   ├── 01-vaswani-2017-attention.md
│       │   ├── 02-devlin-2019-bert.md
│       │   ├── 03-karpukhin-2020-dpr.md
│       │   ├── 04-khattab-2020-colbert.md
│       │   ├── 05-thakur-2021-beir.md
│       │   └── ...
│       ├── experiment-templates/
│       │   ├── clip-extraction.yaml
│       │   ├── embedding-similarity.yaml
│       │   ├── retrieval-evaluation.yaml
│       │   └── reranking.yaml
│       ├── data/
│       │   └── schemas/
│       └── ros-spec.yaml
├── templates/
│   ├── experiment-design.md
│   ├── hypothesis-template.md
│   ├── results-log.md
│   ├── analysis-plan.md
│   ├── pre-registration.md
│   └── publication-template.md
├── source-list/
│   ├── peer-reviewed-canonical.json
│   ├── gray-literature.json
│   └── blog-tutorials.json
├── analysis/
│   ├── exploratory/
│   ├── confirmatory/
│   └── outputs/
└── vacuum-detector/
    ├── algorithm.py
    ├── detector.yaml
    └── README.md
```

---

## The Three Pillars

### Pillar 1: Causal Inference

**Question**: What causes what, and how do we know?

**Methods**:
- Randomized controlled trials (RCTs)
- Instrumental variables (IV)
- Regression discontinuity design (RDD)
- Difference-in-differences (DiD)
- Synthetic control methods (SCM)
- Targeted learning (TMLE)

**What we need to prove**:
- Does Sovereign vacuum detection improve coordination?
- Which operator (selfish-altruistic, magnetic membrane, portfolio, reflexive) has strongest effect?
- Is the effect stable across domains?

### Pillar 2: Unit Economics

**Question**: What is the value creation and capture equation?

**Metrics**:
- Lifetime value (LTV)
- Customer acquisition cost (CAC)
- Payback period
- Gross margin
- Net revenue retention (NRR)

**What we need to prove**:
- LTV/CAC ratio for each execution path
- Cohort behavior patterns
- Attribution to research vs execution

### Pillar 3: Algorithmic Interface

**Question**: How do we extract, embed, and retrieve knowledge?

**Methods**:
- CLIP-based embedding extraction
- Late interaction retrieval (ColBERT)
- Re-ranking models
- Evaluation benchmarks (MTEB, BEIR)

**What we need to prove**:
- Clip extraction accuracy on session transcripts
- Retrieval precision for knowledge gaps
- Interface responsiveness

---

## Research Operating System (ROS)

### Workflows

```
1. EXPLORATORY
   → Hypothesis generation (from vacuum detection)
   → Data mining (existing logs, transcripts)
   → Pattern detection (anomaly detection)
   → Pre-registration (before confirmation)

2. CONFIRMATORY
   → Pre-registered hypothesis
   → Locked analysis plan
   → Experiment execution
   → Results log + sensitivity analysis

3. SYNTHESIS
   → Meta-analysis
   → Cross-pillar integration
   → Publication (internal or external)
```

### Quality Gates

| Gate | Threshold |
|---|---|
| Statistical power | > 0.80 |
| Pre-registration | Before data collection |
| Sensitivity analysis | Multiple robustness checks |
| Replication | On new data (where possible) |
| Effect size | Cohen's d > 0.2 (minimum) |

### Tool Stack

| Function | Tool |
|---|---|
| Experiment tracking | MLflow |
| Data versioning | DVC |
| Notebooks | Jupyter |
| Statistical analysis | R + Python |
| Collaboration | GitHub Issues + PRs |

---

## Vacuum Detector

The core algorithm that detects "vacuum radiation" — knowledge gaps that need study.

### Definition

**Vacuum** = An unsaid gap at domain seams, discovered through absence of evidence.

**Types**:
1. **Structural vacuum**: No data exists
2. **measurement vacuum**: Data exists but not captured
3. **inference vacuum**: Missing causal links
4. **attribution vacuum**: Unknown value drivers

### Algorithm

```python
# vacuum-detector/algorithm.py
class VacuumDetector:
    """
    Detects vacuum radiation — knowledge gaps requiring study.
    
    Law: If there's no data to prove it, study it.
    """
    
    def __init__(self, evidence_threshold: float = 0.05):
        self.threshold = evidence_threshold
    
    def detect(
        self, 
        domain_claims: list[Claim], 
        evidence_base: EvidenceBase
    ) -> list[Vacuum]:
        """Detect vacuums in domain claims."""
        vacuums = []
        
        for claim in domain_claims:
            evidence = evidence_base.query(claim)
            
            if evidence.coverage < self.threshold:
                vacuums.append(Vacuum(
                    type="structural",
                    claim=claim,
                   Evidence=evidence.coverage,
                    priority=self._priority(claim)
                ))
                
            elif not evidence.has_statistics(claim):
                vacuums.append(Vacuum(
                    type="measurement",
                    claim=claim,
                   Evidence=evidence.stats_present,
                    priority="high"
                ))
                
            elif not evidence.has_causal_inference(claim):
                vacuums.append(Vacuum(
                    type="inference",
                    claim=claim,
                    evidence=evidence.causal_tests,
                    priority="critical"
                ))
        
        return self._rank_by_impact(vacuums)
    
    def _priority(self, claim: Claim) -> str:
        """Rank by domain impact."""
        # Critical: affects multiple domains
        # High: affects one domain significantly  
        # Medium: affects sub-domain
        # Low: edge case
        pass
```

---

## Decision Log

| Date | Decision | Rationale |
|---|---|---|
| 2026-04-26 | Atlas first, all else second | Law of the land: no proof = study |
| 2026-04-26 | Three pillars | Cover causes, value, interface |
| 2026-04-26 | Recursive principle | Atlas studies itself |
| 2026-04-26 | Vacuum detector as core | Operationalizes the law |

---

## Next Steps

1. **Reading ladders** — 30-80 sources per pillar (progressive depth)
2. **Canonical paper notes** — Annotations for each source
3. **Experiment templates** — Pre-built designs for common methods
4. **Pre-registration SOP** — How to lock analysis before running
5. **Vacuum detector implementation** — Python code for gap detection

---

*The Atlas is never complete. Every completion radiates new vacuums.*