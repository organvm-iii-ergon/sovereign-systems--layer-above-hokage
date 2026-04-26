# Research Scoring System

## Purpose

Score research quality, impact, and progress to prioritize effort.

---

## Score Dimensions

| Dimension | Weight | What It Measures |
|-----------|--------|----------------|
| **Evidence Gap** | 0.30 | How important is this to learn? |
| **Feasibility** | 0.25 | Can we actually do this? |
| **Impact** | 0.25 | What's the payoff if true? |
| **Novelty** | 0.20 | How new is this? |

---

## Scoring Algorithms

### 1. Evidence Gap Score (EGS)

```python
def evidence_gap_score(claim, evidence_base):
    """0-100: How much do we not know?"""
    
    evidence = evidence_base.get(claim.id)
    
    if evidence is None:
        return 100  # Complete vacuum
    
    gap = 0.0
    
    if not evidence.has_statistics:
        gap += 30
    if not evidence.has_causal_tests:
        gap += 30
    if not evidence.has_attribution:
        gap += 20
    if evidence.sample_size < 30:
        gap += 20
    
    return min(gap, 100)
```

### 2. Feasibility Score (FS)

```python
def feasibility_score(study_required, resources_available):
    """0-100: Can we actually do this?"""
    
    score = 100
    
    # Time
    if study_required.time > resources_available.time:
        score -= 30
    
    # Data
    if study_required.n > resources_available.data:
        score -= 25
    
    # Expertise
    if study_required.expertise not in resources_available.expertise:
        score -= 25
    
    # Tools
    if study_required.tools not in resources_available.tools:
        score -= 20
    
    return max(score, 0)
```

### 3. Impact Score (IS)

```python
def impact_score(claim, affected_domains, operator_importance):
    """0-100: What's the payoff?"""
    
    score = 0
    
    # Domain spread
    score += len(affected_domains) * 15
    
    # Operator importance
    for domain in affected_domains:
        score += operator_importance.get(domain, 0.5) * 30
    
    # Cascade potential
    score += claim.cascade_potential * 20
    
    return min(score, 100)
```

### 4. Novelty Score (NS)

```python
def novelty_score(claim, existing_claims):
    """0-100: How new is this?"""
    
    if claim in existing_claims:
        return 0
    
    similarity = max(
        text_similarity(claim, existing)
        for existing in existing_claims
    )
    
    return (1 - similarity) * 100
```

### Composite Score

```python
def research_score(claim):
    egs = evidence_gap_score(claim)
    fs = feasibility_score(claim)
    is_ = impact_score(claim)
    ns = novelty_score(claim)
    
    composite = (
        egs * 0.30 +
        fs * 0.25 +
        is_ * 0.25 +
        ns * 0.20
    )
    
    return {
        "composite": composite,
        "evidence_gap": egs,
        "feasibility": fs,
        "impact": is_,
        "novelty": ns
    }
```

---

## Priority Matrix

```
                    HIGH FEASIBILITY
                         │
              ┌──────────────┼──────────────┐
              │             │             │
              │    HIGH     │    HIGH    │
              │   IMPACT    │   IMPACT   │
              │  (DO NOW)   │ (PRIORITY) │
              │             │             │
LOW    ───────┼─────────────┼────────────┤HIGH  
FEASIBILITY   │             │             │   FEASIBILITY
              │    LOW     │    HIGH    │
              │   IMPACT   │   IMPACT    │
              │  (STUDY)   │ (IF TIME)   │
              │             │             │
              └──────────────┼──────────────┘
                         │
                    LOW FEASIBILITY
```

---

## Leaderboard

### Top Research Priorities

| Rank | Study | Score | EGS | FS | IS | NS |
|------|-------|-------|-----|-----|-----|-----|
| 1 | Vacuum → Coordination | 85 | 90 | 80 | 85 | 75 |
| 2 | Research → LTV | 72 | 70 | 75 | 80 | 60 |
| 3 | CLIP Extraction | 68 | 65 | 70 | 65 | 75 |
| 4 | Operator Effects | 55 | 60 | 50 | 60 | 50 |

---

## Automation

```yaml
# research-scorer.yaml
scorer:
  version: "1.0"
  
  dimensions:
    - name: evidence_gap
      weight: 0.30
      min_score: 0
      max_score: 100
    
    - name: feasibility
      weight: 0.25
    
    - name: impact
      weight: 0.25
    
    - name: novelty
      weight: 0.20
  
  schedule: daily
  output: leaderboard.json
  notification: slack #when score changes significantly
```

---

## Quality Gate

| Check | Requirement |
|---|---|
| All dimensions | Calculated |
| Weights sum | 1.0 |
| No zeros | Unless intentional |
| Review | Monthly calibration |