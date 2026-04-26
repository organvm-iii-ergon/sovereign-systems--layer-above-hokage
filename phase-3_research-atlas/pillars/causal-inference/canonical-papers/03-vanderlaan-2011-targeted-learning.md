# van der Laan & Rose (2011) — Targeted Learning

## Metadata

| Field | Value |
|-------|-------|
| Title | *Targeted Learning: Causal Inference* |
| Authors | Mark van der Laan, Sherri Rose |
| Year | 2011 |
| Publisher | Springer |
| Pages | 350 |

---

## Core Framework

### TMLE: Targeted Minimum Loss Estimation

Two-stage estimator that targets the causal parameter:

```
Stage 1: Initial estimate (using Superlearner)
Stage 2: Targeted bias reduction
```

### Superlearner

Ensemble of multiple algorithms:

| Algorithm | Weight (default) |
|-----------|-----------------|
| Linear regression | 0.1 |
| Lasso | 0.1 |
| Random Forest | 0.3 |
| GBM | 0.3 |
| Neural Network | 0.2 |

---

## For Sovereign: Application

### When to Use TMLE

| Scenario | Method |
|---|---|
| High-dimensional confounders | TMLE |
| Multiple treatments | TMLE |
| Censoring/death | TMLE with IPCW |
| Small sample size | TMLE with bound |

### Implementation

```python
from targeted_learning import TMLE

tmle = TMLE(
    outcome_model=RandomForest(),
    treatment_model=LogisticRegression(),
    censor_model=CoxPH()
)

estimate = tmle.fit(
    data=df,
    treatment="vacuum_detection",
    outcome="coordination_time",
    confounders=["complexity", "experience", "volume"]
)
```

---

## Personal Notes

*[To be filled in as you read]*

---

## Cross-References

- Hernán (2020) — G-methods foundation
- Imbens (2015) — Potential outcomes