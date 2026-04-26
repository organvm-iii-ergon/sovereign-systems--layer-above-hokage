# Hernán & Robins (2020) — What If: Causal Inference

## Metadata

| Field | Value |
|-------|-------|
| Title | *What If: Causal Inference* |
| Authors | Miguel Hernán, James Robins |
| Year | 2020 |
| Publisher | CRC Press |
| Pages | 400 |

---

## Core Framework

### G-Methods

Four methods for causal inference with time-varying confounding:

| Method | Acronym | Key Idea |
|-------|--------|---------|
| G-formula | Standardization | Weight by inverse probability |
| IPTW | Inverse Probability Treatment Weighting | Re-weight entire population |
| G-estimation | Structural nested models | Estimate nested effects |
| Collaborative G-estimation | Causal sufficient SVMS | Doubly robust |

### The Target Trial Framework

```
Every observational study should emulate a hypothetical trial:

1. Specify eligibility
2. Assign treatment (start of follow-up)
3. Define treatment strategies (start vs defer)
4. Specify causal contrast (ITT, per-protocol)
5. Define follow-up
6. Specify outcomes
7. Specify censoring plan
```

---

## For Sovereign: Application

### Our Target Trial

> "Does vacuum detection improve coordination?"

```yaml
eligibility:
  - domain_active: true
  - session_count: > 5

treatment_strategies:
  - start: vacuum_detection = true (at baseline)
  - defer: vaccuum_detection = false (until end)

causal_contrast: intent_to_treat

follow_up: 90 days

outcomes:
  - coordination_time
  - vacuum_detections
  - escalations

censoring:
  - lost_to_follow_up
  - domain_shutdown
```

### Handling Time-Varying Confounders

| Confounder | Type | Solution |
|---|---|---|
| Domain complexity | Time-varying | Adjust via IPTW |
| Operator experience | Time-varying | G-estimation |
| Session volume | Time-varying | Stratify by period |

---

## Key Quotes

> "The question 'What if?' is fundamentally a causal question."

> "We don't need to intervene to answer causal questions, but we must think as if we intervened."

> "Every method has assumptions. Know yours."

---

## Personal Notes

*[To be filled in as you read]*

---

## Mathematical Reference

### G-Formula

```
E[Y(a)] = Σ E[Y | A=a, L=l] × P(L=l)
```

### IPTW

```
 weight = Π_t Π( treatment_t / product)
                  P( treatment_t | past)
```

---

## Cross-References

- Level 1: Pearl — DAGs are the structural basis
- Level 2: Imbens — Potential outcomes framework
- Level 3: van der Laan — TMLE extends G-methods