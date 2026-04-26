# SOP 002: Hypothesis Generation from Vacuum

## Status: ACTIVE | Version: 1.0

**Purpose**: Generate testable hypotheses from vacuum detector output.

---

## Procedure

### 1. IDENTIFY VACUUM

```
□ Run vacuum detector on claims list
□ Review top-ranked vacuums
□ Select candidate vacuum
□ Verify evidence_coverage < 0.05
```

### 2. FORMULATE

```
□ Write H1 (alternative):
  - Directional claim
  - Specific effect size
  - Clear outcome
□ Write H0 (null):
  - No effect / equal to control
□ Confirm falsifiability
```

### 3. OPERATIONALIZE

```
□ Define treatment precisely
□ Define control precisely
□ Define outcome measure
□ List confounders + strategy
□ Select statistical method
```

### 4. CALCULATE

```
□ Determine MDE
□ Calculate n required
□ Verify feasibility
□ Resource check (time, data, tools)
```

### 5. PRE-REGISTER

```
□ Follow SOP 001
□ Lock hypothesis + analysis
□ Assign study ID
```

---

## Example

```
VACUUM: No data on vacuum detection → coordination time

H1: Active vacuum detection reduces coordination time by ≥30%
H0: No difference in coordination time

TREATMENT: sovereign.vacuum_detection = true at baseline
CONTROL: sovereign.vacuum_detection = false
OUTCOME: coordination_time_minutes (session_logs)
CONFOUNDERS: domain_complexity, operator_type (adjust)
METHOD: ITT regression, power=0.80

N REQUIRED: 128 (d=0.5)
FEASIBILITY: Yes (existing data)
```

---

## Decision Matrix

| Vacuum Type | Hypothesis Type | Method |
|---|---|---|
| Structural | Descriptive, prevalence | Descriptive stats |
| Measurement | Association | Regression |
| Inference | Causal | RCT/IV/RDD |
| Attribution | Contribution | Shapley |
| Interface | Retrieval | Precision@K |

---

## Quality Gate

| Check | Requirement |
|---|---|
| Falsifiability | Can be rejected |
| Measurability | Operationalized |
| Feasibility | N achievable |
| Priority | Top-ranked vacuum |

---

## References

- SOP 001: Pre-Registration
- SOP 005: Statistical Analysis