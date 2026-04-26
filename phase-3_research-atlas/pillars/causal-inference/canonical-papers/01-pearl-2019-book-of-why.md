# The Book of Why (Pearl, 2019)

## Metadata

| Field | Value |
|-------|-------|
| Title | *The Book of Why: The Causal Revolution* |
| Author | Judea Pearl, Dana Mackenzie |
| Year | 2019 |
| Publisher | Basic Books |
| Pages | 400 |
| ISBN | 978-0465097607 |

---

## Core Framework

### The Ladder of Causation

| Level | Name | Question | Example |
|-------|-----|----------|---------|
| 1 | Association | What if I see X? | P(Y|X) |
| 2 | Intervention | What if I do X? | P(Y|do(X)) |
| 3 | Counterfactual | What if X had not happened? | P(Y|X, X') |

**Key insight**: Most ML is stuck at Level 1. Causal inference requires Level 2.

### Do-Calculus

Three rules for transforming causal queries:

```
Rule 1 (Insertion/Deletion): 
  P(Y|do(X), Z) = P(Y|X, Z)  if X ⊥ Z | adj(Z)

Rule 2 (Action/Observation Exchange):
  P(Y|do(X), do(Z), W) = P(Y|X, do(Z), W)  if Y ⊥ do(Z) | X, W

Rule 3 (Trivial):
  P(Y|do(X), do(Z)) = P(Y|do(X), Z)  if Z = f(X)
```

---

## For Sovereign: Application

### The Causal Question

> "Does Sovereign vacuum detection improve domain coordination?"

### DAG Construction

```
                    ┌─────────────────┐
                    │  Domain         │
                    │  Complexity     │
                    └───────┬────────┘
                            │
                            ▼
              ┌─────────────┴─────────────┐
              │  Vacuum Detection     │
              │  Active               │
              └───────┬───────────────┘
                      │
        ┌─────────────┼─────────────┐
        ▼           ▼           ▼
┌───────────┐ ┌───────────┐ ┌───────────┐
│Coord.Time│ │Escalation │ │ Vacuum   │
│         │ │          │ │ Detections│
└─────────┘ └─────────┘ └─────────┘
```

### Confounders to Control

| Confounder | Source | Strategy |
|-----------|--------|---------|
| Domain complexity | Direct measure | Stratification |
| Operator type | Randomize or adjust | Block design |
| Time period | Fixed effects | Control for period |
| Prior domain history | Covariate | PSM |

---

## Key Quotes

> "Causation is the only way to answer 'what if' questions."

> "The ladder of causation describes the cognitive gap between prediction and understanding."

> "Simpson's paradox is not a paradox — it's a reminder that correlation is not causation."

---

## Personal Notes

*[To be filled in as you read]*

---

## Cross-References

- Level 2: Hernán (2020) — G-methods implement do-calculus
- Level 2: Imbens (2015) — Potential outcomes as complementary framework
- Level 3: VanderWeele (2015) — Mediation uses counterfactuals