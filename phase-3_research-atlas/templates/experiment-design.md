# Experiment Design Template

## Overview

Use this template for every confirmatory study in Sovereign's Research Atlas.

---

## Template Structure

```yaml
experiment:
  # METADATA
  study_id: SOVEREIGN-YYYY-###-PILLAR
  title: "[Descriptive title]"
  version: "1.0"
  status: draft
  created: "{{date}}"
  updated: "{{date}}"
  
  # PURPOSE
  purpose: >
    [One sentence on what we're testing]
  
  background: |
    [Why this matters]
  
  hypothesis:
    primary: >
      [Falsifiable primary hypothesis]
    secondary: |
      [Secondary hypotheses, optional]
    null: |
      [Explicit null hypothesis]
  
  # DESIGN
  design:
    type: [rct|iv|rdd|did|single_arm|observational]
    assignment: [random|quasi|natural]
    unit: [domain|session|operator|user]
    
  arms:
    control:
      name: "[name]"
      description: "[what happens here]"
    treatment:
      name: "[name]"
      description: "[what happens here]"
  
  sample_size:
    method: power_analysis
    effect_size: 0.5  # Cohen's d or relevant
    power: 0.80
    alpha: 0.05
    n_per_arm: 64
    calculation: |
      [Reference or formula]
  
  # MEASUREMENTS
  metrics:
    primary:
      name: "[metric]"
      type: [continuous|count|rate|binary]
      direction: [higher_is_better|lower_is_better]
      source: "[where data comes from]"
    
    secondary:
      - name: "[metric]"
        type: ...
        source: ...
    
    safety:
      - name: "[metric]"
        threshold: [value]
  
  # ANALYSIS (LOCK BEFORE RUNNING)
  analysis:
    intention_to_treat: true
    
    primary_analysis:
      method: [t_test|regression|survival...]
      covariables: [list]
    
    sensitivity:
      - name: per_protocol
      - name: as_treated
      - name: heterogeneous_effects
    
    missing_data:
      strategy: [multiple_imputation|complete_case...]
      sensitivity: ...
  
  # PRE-REGISTRATION
  pre_registration:
    platform: [OSF|GitHub|...]
    url: "[url]"
    date: "{{date}}"
    hypothesis_locked: true
    analysis_plan_locked: true
  
  # EXECUTION
  execution:
    start_date: "[date]"
    end_date: "[date]"
    status: [planned|running|completed]
  
  # RESULTS
  results:
    effect_size: ...
    ci_95: [...]
    p_value: ...
    n_observed: ...
    conclusion: [confirmed|not_confirmed|inconclusive]
  
  # TEAM
  team:
    PI: "[name]"
    analysts: [list]
    reviewers: [list]
```

---

## Example: RCT Design

```yaml
experiment:
  study_id: SOVEREIGN-2026-001-CAUSTAL
  title: Effect of vacuum detection on domain coordination time
  version: "1.0"
  status: pre_registered
  
  purpose: >
    Test if activating Sovereign vacuum detection
    reduces domain coordination time
  
  hypothesis:
    primary: >
      Domains with vacuum detection active will have
      30% lower coordination time than control
    null: >
      No difference in coordination time between
      vacuum detection active and control
  
  design:
    type: randomized_controlled_trial
    assignment: random
    unit: domain
    
  arms:
    control:
      name: standard_operations
      description: No vacuum detection
    treatment:
      name: sovereign_active
      description: Vacuum detection enabled
  
  sample_size:
    method: power_analysis
    effect_size: 0.5
    power: 0.80
    alpha: 0.05
    n_per_arm: 64
    calculation: |
      Using G*Power 3.1, two-tailed t-test,
      effect size d=0.5, power=0.80, alpha=0.05
  
  metrics:
    primary:
      name: coordination_time_minutes
      type: continuous
      direction: lower_is_better
      source: session_logs.coordination_duration
    
    secondary:
      - name: vacuum_detections
        type: count
        source: sovereign.vacuums
      - name: escalation_count
        type: count
        source: session_logs.escalations
    
    safety:
      - name: false_positive_rate
        threshold: 0.10
  
  analysis:
    intention_to_treat: true
    
    primary_analysis:
      method: linear_regression
      covariables: [domain_complexity, time_period]
    
    sensitivity:
      - name: per_protocol
      - name: bootstrap_ci
  
  pre_registration:
    platform: OSF
    url: https://osf.io/xxxxx
    date: "2026-04-26"
    hypothesis_locked: true
    analysis_plan_locked: true
```

---

## Checklist

Before starting:

- [ ] Study ID assigned
- [ ] Hypothesis is falsifiable
- [ ] Sample size calculated
- [ ] Metrics defined with sources
- [ ] Analysis plan locked
- [ ] Pre-registered
- [ ] IRB exemption confirmed (if applicable)

After collecting data:

- [ ] Dataset locked
- [ ] Analysis runs
- [ ] Sensitivity analysis runs
- [ ] Results logged (positive + negative)
- [ ] Peer review complete
- [ ] Synthesis written

---

*Every experiment needs this template. Every template needs pre-registration.*