# Analysis Pipeline

## Purpose

Standardized analysis workflow for Sovereign research.

---

## Pipeline Stages

```
┌─────────────────────────────────────────────────────────────────────┐
│                    ANALYSIS PIPELINE                         │
└─────────────────────────────────────────────────────────────────────┘
                              │
        ┌─────────────────────┼─────────────────────┐
        ▼                     ▼                     ▼
┌─────────────┐         ┌─────────────┐         ┌─────────────┐
│   STAGE 1   │         │   STAGE 2   │         │   STAGE 3   │
│   VERIFY    │────────▶│   RUN      │────────▶│   DOCUMENT │
│            │         │            │         │            │
│ - Pre-reg  │         │ - Primary  │         │ - Results  │
│ - Data     │         │ - Sensit.   │         │ - Figures  │
│ - Code     │         │ - Heterog.  │         │ - Report   │
└─────────────┘         └─────────────┘         └─────────────┘
        │                     │                     │
        ▼                     ▼                     ▼
┌─────────────┐         ┌─────────────┐         ┌─────────────┐
│   PASS/FAIL │         │   PASS/FAIL │         │   PASS/FAIL │
│            │         │            │         │            │
│ Proceed    │         │ Proceed    │         │ Complete   │
└─────────────┘         └─────────────┘         └─────────────┘
```

---

## Stage 1: Verify

### Pre-Registration Check

```python
def verify_preregistration(study_id):
    prereg = load_preregistration(study_id)
    assert prereg.hypothesis_locked
    assert prereg.analysis_plan_locked
    assert prereg.url is not None
    return prereg
```

### Data Lock Check

```python
def verify_data_lock(dataset):
    assert dataset.hash == dataset.locked_hash
    assert dataset.created_at < study.start_date
    assert no_new_data_added()
    return metadata
```

### Code Check

```python
def verify_code(analysis_code):
    assert code.runs_without_error()
    assert seed_is_set()
    assert reproduce_results()
    return verification
```

---

## Stage 2: Run

### Primary Analysis

```python
def run_primary(data, code):
    np.random.seed(code.seed)
    
    result = code.primary_method(
        data=data,
        treatment=data.treatment,
        outcome=data.outcome,
        confounders=data.confounders
    )
    
    return {
        "effect_size": result.effect,
        "ci_95": result.ci,
        "p_value": result.p,
        "n": result.n
    }
```

### Sensitivity Analyses

```python
def run_sensitivity(data, code, primary):
    results = []
    
    for method in ["per_protocol", "as_treated"]:
        result = getattr(code, method)(data)
        results.append({
            "method": method,
            "effect_size": result.effect,
            "ci_95": result.ci
        })
    
    # Missing data
    if data.has_missing:
        for strategy in ["mi", "complete_case"]:
            result = code.missing(strategy)(data)
            results.append({"strategy": strategy, **result})
    
    return results
```

### Heterogeneity

```python
def run_heterogeneity(data, code):
    results = []
    
    for stratum in ["domain", "operator", "complexity"]:
        result = code.stratify(stratum)(data)
        results.append({
            "stratum": stratum,
            "effect_size": result.effect,
            "interaction_p": result.interaction_p
        })
    
    return results
```

---

## Stage 3: Document

### Results Table

```markdown
| Analysis | Effect | 95% CI | p | N |
|----------|--------|--------|---|---|
| Primary (ITT) | -0.45 | [-0.68, -0.22] | 0.001 | 126 |
| Per-protocol | -0.42 | [-0.66, -0.18] | 0.002 | 118 |
| As-treated | -0.51 | [-0.75, -0.27] | <0.001 | 110 |
| Bootstrap | -0.45 | [-0.70, -0.20] | 0.001 | 126 |
```

### Figure Generation

```python
def generate_figures(results):
    figures = []
    
    # Forest plot
    figures.append(plot_forest(results))
    
    # Heterogeneity plot
    figures.append(plot_heterogeneity(results))
    
    # Sensitivity plot
    figures.append(plot_sensitivity(results))
    
    return figures
```

### Report Generation

```python
def generate_report(study, results, figures):
    report = f"""
# Study: {study.study_id}
# Results
    
## Primary Analysis
    
{results.primary}
    
## Sensitivity
    
{results.sensitivity}
    
## Heterogeneity
    
{results.heterogeneity}
    
## Figures
    
{figures}
    """
    return report
```

---

## Pipeline Automation

```yaml
# pipeline.yaml
name: sovereign_analysis_pipeline
version: "1.0"

stages:
  - name: verify
    checks:
      - pre_registration
      - data_lock
      - code_verification
    
  - name: run
    analyses:
      - primary
      - sensitivity
      - heterogeneity
    
  - name: document
    outputs:
      - results_table
      - figures
      - report

runner: mlflow
```

---

## Quality Gates

| Stage | Gate | Requirement |
|---|---|---|
| 1 Verify | Pre-reg locked | URL exists, HP+AP locked |
| 1 Verify | Data locked | Hash matches |
| 1 Verify | Code runs | Reproduces test results |
| 2 Run | Primary | Runs without error |
| 2 Run | Sensitivity | All complete |
| 3 Document | Complete | All sections present |