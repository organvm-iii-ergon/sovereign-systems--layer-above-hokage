# Hypothesis Template

## Structure

```
HYPOTHESIS_ID: SOVEREIGN-[YEAR]-[###]-[PILLAR]
Created: {{date}}
Status: [draft|pre_registered|tested|retired]

## QUESTION
[One sentence research question]

## HYPOTHESIS

### Primary (H1)
[What we believe is true]

### Null (H0)
[What we need to test against]

## RATIONALE
[Why we believe this]

### Evidence Base
- [Prior study 1]
- [Prior study 2]
- [Theoretical reason]

## OPERATIONALIZATION

### Treatment
[What exactly is being tested]

### Control
[What we're comparing against]

### Outcome
[How we measure success]

### Confounders
| Confounder | Strategy |
|---|---|
| [1] | [adjust/match/stratify] |
| [2] | ... |

## ANALYSIS

### Method
[Statistical approach]

### Power Calculation
[Reference or formula]

### Sensitivity
- [Check 1]
- [Check 2]

## PRE-REGISTRATION
Platform: [OSF|GitHub|...]
URL: [link]
Date: [date]
```

---

## Example: Causal Hypothesis

```yaml
hypothesis_id: SOVEREIGN-2026-001-CAUSTAL
title: Vacuum detection improves coordination

question: >
  Does enabling Sovereign vacuum detection improve 
  domain coordination time?

hypothesis:
  primary: |
    Domains with vacuum detection active will show
    at least 30% reduction in coordination time.
  null: |
    There is no difference in coordination time
    between active and control domains.

rationale:
  evidence_base: |
    - Prior analysis of session data suggests coordination
      slows during domain transitions
    - Vacuum detection identifies transition points
    - Operators are designed to handle transitions

operationalization:
  treatment: >
    sovereign.vacuum_detection.enabled = true
    
  control: >
    sovereign.vacuum_detection.enabled = false
    
  outcome: >
    coordination_time_minutes from session_logs
    
  confounders:
    - domain_complexity: stratify by score
    - operator_type: block randomization
    - time_period: fixed effects

analysis:
  method: intent_to_treat linear regression
  
  power:
    effect_size: 0.5
    power: 0.80
    alpha: 0.05
    n_required: 128
    
  sensitivity:
    - per_protocol analysis
    - bootstrap confidence intervals

pre_registration:
  platform: OSF
  url: https://osf.io/xxxxx
  date: 2026-04-26
```

---

## Example: Economics Hypothesis

```yaml
hypothesis_id: SOVEREIGN-2026-002-ECONOMICS
title: Research exposure improves LTV

question: >
  Does exposure to research increase lifetime value?

hypothesis:
  primary: |
    Cohorts with research exposure will show LTV:CAC
    ratio > 3.0 within 12 months.
  null: |
    No difference in LTV between research-exposed
    and non-research cohorts.

rationale:
  evidence_base: |
    - SaaS benchmarks show research improves retention
    - Internal pilot showed 20% engagement lift

operationalization:
  treatment: >
    session.research_access = true
    (accessed 3+ research items)
    
  control: >
    session.research_access = false
    
  outcome: >
    LTV calculated at 12 months
    
  confounders:
    - acquisition_channel: stratify
    - domain_complexity: adjust

analysis:
  method: cox regression with exposure as time-varying
  
  power:
    effect_size: hazard_ratio_2.0
    power: 0.80
    n_required: 200
```

---

## Example: Interface Hypothesis

```yaml
hypothesis_id: SOVEREIGN-2026-003-INTERFACE
title: CLIP extraction accuracy

question: >
  Can CLIP-based extraction identify relevant clips
  from session transcripts?

hypothesis:
  primary: |
    CLIP extraction will achieve >80% precision
    on top-5 relevant clips.
  null: |
    Precision ≤80% (baseline performance)

rationale:
  evidence_base: |
    - BGE-large achieves >80% on MTEB
    - Session transcripts contain structured content

operationalization:
  treatment: >
    CLIP extraction with bge-large-en-v1.5
    
  control: >
    Random chunk selection
    
  outcome: >
    Precision@5 calculated from human eval
    
  confounders:
    - transcript_complexity: stratify
    - query_type: fix

analysis:
  method: precision_at_k with human evaluation
  
  power:
    effect_size: 0.3
    power: 0.80
    n_queries: 100
```

---

*Every hypothesis needs this form. Every form needs pre-registration.*