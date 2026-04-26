# SOP 003: Statistical Analysis Execution

## Status: ACTIVE | Version: 1.0

**Purpose**: Execute locked analysis plan without p-hacking.

---

## Procedure

### 1. VERIFY PRE-REGISTRATION

```
□ Fetch pre-registration URL
□ Verify hypothesis = locked
□ Verify analysis = locked
□ Note any permitted deviations
```

### 2. PREPARE DATA

```
□ Load locked dataset
□ Verify no new data added
□ Apply exclusion criteria
□ Document final N
```

### 3. RUN PRIMARY ANALYSIS

```
□ Execute locked code
□ Record exact statistics
□ Record exact confidence interval
□ Record exact p-value
```

### 4. RUN SENSITIVITY ANALYSES

```
□ Per-protocol analysis
□ As-treated analysis
□ Multiple imputation (if missing)
□ Bootstrap (if small N)
□ Remove each confounder
```

### 5. HETEROGENEITY EXPLORATION

```
□ By domain
□ By operator type
□ By complexity
□ Pre-registered interactions only
```

### 6. DOCUMENT

```
□ Complete results table
□ All sensitivity results
□ All heterogeneity results
□ Exact code + seed
```

---

## Output Template

```yaml
results:
  study_id: SOVEREIGN-2026-001-CAUSTAL
  analysis_locked: true
  analysis_date: "{{date}}"
  
  sample:
    assigned: 128
    analyzed: 126
    excluded: 2
  
  primary:
    effect_size: -0.45
    ci_95: [-0.68, -0.22]
    p_value: 0.001
    method: intent_to_treat
  
  sensitivity:
    - name: per_protocol
      effect_size: -0.42
      ci_95: [-0.66, -0.18]
    - name: as_treated
      effect_size: -0.51
      ...
  
  heterogeneity:
    - stratum: high_complexity
      effect_size: -0.62
    - stratum: low_complexity
      effect_size: -0.28
```

---

## Prohibited Actions

| Action | Why |
|---|---|
| Add outcome | P-hacking |
| Remove outliers | P-hacking |
| Add covariates | P-hacking |
| Change method | P-hacking |
| Subset by result | P-hacking |

---

## Quality Gate

| Check | Requirement |
|---|---|
| Pre-registration | Verified |
| Code | Runs without error |
| Results | Complete |
| Sensitivity | All run |

---

## References

- SOP 001: Pre-Registration
- SOP 007: Null Findings