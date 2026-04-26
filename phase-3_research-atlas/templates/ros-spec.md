# Research Operating System (ROS) Spec

## Version: 1.0

**Purpose**: Operationalize the research infrastructure for Sovereign.

---

## Core Principles

| Principle | Description |
|---|---|
| Reproducibility first | All experiments must be reproducible |
| Pre-registration | Lock hypothesis before data collection |
| Open science | Share methods within the org |
| Peer review | Internal review before publication |
| Meta-study | Research that studies research |

---

## Workflows

### 1. EXPLORATORY

```
a. VACUUM DETECTION
   └─ Vacuum detector identifies knowledge gaps
   
b. HYPOTHESIS GENERATION
   └─ Gap → Testable claim
   
c. DATA MINING
   └─ Search existing logs, transcripts, notes
   
d. PATTERN DETECTION
   └─ Anomaly detection, clustering
   
e. PRE-REGISTRATION
   └─ Lock hypothesis + analysis plan
   
f. RESEARCH PROPOSAL
   └─ Document expected findings
```

### 2. CONFIRMATORY

```
a. PRE-REGISTERED STUDY
   └─ Open in experiment tracker
   
b. DATA COLLECTION
   └─ Per protocol, document deviations
   
c. ANALYSIS EXECUTION
   └─ Locked analysis plan runs
   
d. RESULTS LOG
   └─ Document all findings (positive + negative)
   
e. SENSITIVITY ANALYSIS
   └─ Multiple robustness checks
   
f. PEER REVIEW
   └─ Internal review before conclusions
```

### 3. SYNTHESIS

```
a. META-ANALYSIS
   └─ Combine across studies
   
b. CROSS-PILLAR INTEGRATION
   └─ Causal + Economics + Interface
   
c. KNOWLEDGE BASE UPDATE
   └─ Update what we know
   
d. PUBLICATION
   └─ Internal memo or external paper
   
e. DECISION UPDATE
   └─ Feed to operators
```

---

## Tool Stack

| Function | Tool | Version |
|---|---|---|
| Experiment tracking | MLflow | 2.x |
| Data versioning | DVC | 3.x |
| Notebooks | Jupyter | 6.x |
| Statistics | R + Python | 4.x |
| Collaboration | GitHub Issues + PRs | |
| Knowledge base | Obsidian | |

---

## Quality Gates

### Pre-Research

| Gate | Requirement |
|---|---|
| Vacuum confirmed | Vacuum detector flagged it |
| Hypothesis testable | Falsifiable claim |
| Resources available | Time + data + tools |
| Priority | Ranks in research backlog |

### During Research

| Gate | Requirement |
|---|---|
| Pre-registration | Before data collection |
| Protocol adherence | Document deviations |
| Power ≥ 0.80 | Sample size calculated |
| Effect size | Minimum detectable set |

### Post-Research

| Gate | Requirement |
|---|---|
| Null reported | Even if null findings |
| Sensitivity passed | Multiple robustness checks |
| Replication | On new data (when possible) |
| Effect interpretation | Practical significance |

---

## Experiment Lifecycle

```
 ┌─────────────────────────────────────────────────────────┐
 │                     RESEARCH LIFECYCLE                 │
 └─────────────────────────────────────────────────────────┘
                              │
                              ▼
                    ┌─────────────────┐
                    │  1. HYPOTHESIS  │
                    │  Generate from  │
                    │  vacuum         │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │  2. DESIGN    │
                    │  Choose method │
                    │  Calculate N  │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │  3. PRE-REG    │
                    │  Lock HP + AP  │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │  4. COLLECT    │
                    │  Per protocol  │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │  5. ANALYZE     │
                    │  Locked plan    │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │  6. REPORT     │
                    │  All findings  │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │  7. SYNTHESIZE │
                    │  Update base   │
                    └─────────────────┘
```

---

## Versioning

Each study gets:
- Unique ID: `SOVEREIGN-[YEAR]-[SEQ]-[PILLAR]`
  - Example: `SOVEREIGN-2026-001-CAUSAL`
- Version: Semver
- Status: `draft` | `pre-registered` | `active` | `completed` | `abandoned`

---

## Directory Structure

```
analysis/
├── exploratory/
│   └── 2026-01-vacuum-001/
│       ├── proposal.md
│       ├── notes.ipynb
│       └── hypothesis.yaml
├── confirmatory/
│   └── 2026-02-rct-001/
│       ├── pre-registration.yaml
│       ├── analysis.R
│       ├── results.md
│       └── sensitivity/
└── outputs/
    ├── figures/
    └── tables/
```

---

## Metadata Schema

```yaml
# study.yaml
study_id: SOVEREIGN-2026-001-CAUSAL
title: Effect of vacuum detection on coordination time
version: "1.0"
status: pre_registered

hypothesis:
  primary: "Vacuum detection reduces coordination time by >30%"
  secondary: "False positive rate < 10%"

design:
  type: randomized_controlled_trial
  method: intent_to_treat
  n_required: 128

pre_registration:
  platform: OSF
  url: "https://osf.io/..."
  date: "2026-01-15"
  hypothesis_locked: true
  analysis_plan_locked: true

results:
  effect_size: 0.45
  ci_95: [0.22, 0.68]
  p_value: 0.001
  
conclusion: "Hypothesis confirmed"
```

---

## Peer Review Protocol

### Reviewer Assignment

1. Technical reviewer (methods expert)
2. Domain reviewer (Sovereign expert)
3. Independent reviewer (fresh eyes)

### Review Criteria

| Criteria | Weight |
|---|---|
| Methods correct | 30% |
| Reproducibility | 25% |
| Interpretation | 25% |
| Writing clarity | 20% |

### Review Timeline

- Assign: Within 48 hours
- Review: 7 days
- Revision: 3 days
- Decision: Final

---

## Decision Log

| Date | Decision | Rationale |
|---|---|---|
| 2026-04-26 | ROS as operational layer | Research needs process |
| 2026-04-26 | Pre-registration required | Prevent p-hacking |
| 2026-04-26 | Three workflow types | Different research goals |
| 2026-04-26 | MLflow + DVC | Proven tool stack |

---

*The ROS is the substrate. Every study runs on it. Every result feeds back to it.*