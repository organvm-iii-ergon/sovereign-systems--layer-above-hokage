# Pillar 1: Causal Inference

## Purpose

To rigorously determine what causes what, and to prove it with data.

**Core Question**: *"Does Sovereign vacuum detection improve domain coordination?"*

### The Epistemological Frame

We don't assume causality. We test for it.

| Assumption | Requirement |
|---|---|
| X causes Y | Randomized trial or natural experiment |
| X is necessary for Y | Knockout study |
| X moderates Y | Interaction analysis |
| X mediates Z | Mediation analysis |

---

## Reading Ladder (Progressive Depth)

### Level 1: Foundations (Weeks 1-2)

**Goal**: Build mental models for causality

| Source | Author | Year | Core Concept | Time |
|-------|--------|------|---|---|
| *The Book of Why* | Pearl & Mackenzie | 2019 | DAGs, do-calculus, ladder of causation | 8h |
| *Causal Inference in Statistics* | Pearl et al. | 2019 | Structural equations, identifiability | 12h |
| *Introduction to Causal Inference* | Hernán & Robins | 2023 | G-methods overview | 6h |

**Output**: Draw your first DAG. Identify confounders.

### Level 2: Methods (Weeks 3-5)

**Goal**: Master identification strategies

| Source | Author | Year | Core Concept | Time |
|-------|--------|------|---|---|
| *What If* | Hernán & Robins | 2020 | IPW, g-formula, g-estimation | 15h |
| *Causal Inference* | Imbens & Rubin | 2015 | Potential outcomes, SUTVA | 12h |
| *Econometrics of Matched Samples* | Abadie & Cattaneo | 2010 | Matching, weighting | 8h |

**Output**: Run your first propensity score analysis.

### Level 3: Advanced (Weeks 6-8)

**Goal**: Address bias, get credible intervals

| Source | Author | Year | Core Concept | Time |
|-------|--------|------|---|---|
| *Targeted Learning* | van der Laan & Rose | 2011 | TMLE, superlearner | 10h |
| *Causal Mediation Analysis* | VanderWeele & Vansteelandt | 2015 | Direct/indirect effects | 8h |
| *Sensitivity Analysis* | Cinelli et al. | 2020 | Hidden bias, E-values | 6h |

**Output**: Run causal mediation analysis.

### Level 4: Cutting Edge (Weeks 9+)

**Goal**: Contribute to knowledge

| Source | Author | Year | Core Concept | Time |
|-------|--------|------|---|---|
| *Longitudinal Causal Inference* | Bor et al. | 2023 | Target trial emulation | 6h |
| *Causal Benchmarking* | Kallus et al. | 2018 | Causal inference on bandit data | 8h |
| *DAGs with Unmeasured Confounding* | Textor et al. | 2021 | DAG sensitivity | 4h |

**Output**: Your own research question.

---

## Canonical Papers (Detailed Notes)

### 01: Pearl (2019) — The Book of Why

**Key Insights**:

1. **The Ladder of Causation**
   - Level 1: Association (seeing) — P(Y|X)
   - Level 2: Intervention (doing) — P(Y|do(X))
   - Level 3: Counterfactual (imagining) — P(Y|X, X')

2. **Do-Calculus**
   - Three rules for identifying causal effects from observational data
   - Backdoor criterion
   - Front-door criterion

3. **Mediation Formula**
   - Direct effect: P(Y|do(X), Z)
   - Indirect effect: Sum over mediator Z

**Application to Sovereign**:
- Draw the DAG for "vacuum detection → domain coordination"
- Identify confounders (domain complexity, operator type, etc.)
- Test for direct effects through operators

**Notes by section**:

```
Chapter 1: Prelude
- Simpsons paradox as causal vs statistical
- Correlation ≠ causation (but we need to know HOW to tell)

Chapter 2: Mechanics of Inference
- do(x) operator is key
- Glesener: causation is in the intervention

Chapter 3: From Buils to Do
- backdoor criterion
- sufficient set

Chapter 4: Counterfactuals
- Potential outcomes framework
-do(x) defines the intervention

Chapter 5: Discovery
- Learning DAGs from data
- Conditional independence tests
```

### 02: Hernán & Robins (2020) — What If

**Key Insights**:

1. **G-Methods**
   - G-formula (standardization)
   - Inverse probability weighting (IPW)
   - G-estimation

2. **Time-varying Confounders**
   - Collapsible bias
   - Marginality

3. **Target Trial Framework**
   - Emulate RCTs from observational data
   - Intention-to-treat vs per-protocol

**Application to Sovereign**:
- Handle operators as treatments
- Time-varying confounders (as domain state changes)
- Pre-register target trials

**Notes by section**:

```
Chapter 2: Conceptual
- Causal inference vs prediction
- No causation without manipulation

Chapter 3: Randomized Experiments
-Intent-to-treat
- Per-protocol

Chapter 4: G-Methods
- Standardization
-IPW vs standardization

Chapter 12: G-Estimation
- Structural nested models
- Rank preservers
```

### 03: van der Laan & Rose (2011) — Targeted Learning

**Key Insights**:

1. **Targeted Minimum Loss Estimation (TMLE)**
   - Two-stage estimator
   - Bias-variance tradeoff

2. **Superlearner**
   - Ensemble of algorithms
   - Cross-validation based

3. **Causal Inference Pipeline**
   - Define parameter
   - Identify
   - Estimate
   - Validate

**Application to Sovereign**:
- Better estimates than naive regression
- Handle high-dimensional confounders

### 04: VanderWeele (2015) — Mediation Analysis

**Key Insights**:

1. **Mediation Formula**
   - Controlled direct effect (CDE)
   - Natural direct/indirect effect

2. **Interaction**
   - Interaction between treatment and mediator
   - Proportion mediated

3. **Sensitivity Analysis**
   - Unmeasured mediator-outcome confounder

**Application to Sovereign**:
- Is effect through selfish-altruistic loop or other operators?
- Which operator carries the effect?

---

## Experiment Templates

### Template 1: Randomized Trial

```yaml
# experiment-templates/randomized-trial.yaml
name: sovereign_vacuum_detection_rct
type: randomized_controlled_trial
version: "1.0"

purpose: >
  Test if Sovereign vacuum detection improves domain coordination time

design:
  assignment: random
  unit: domain
  sample_size: 
    method: power_analysis
    effect_size: 0.5  # Cohen's d
    power: 0.80
    alpha: 0.05
    n_per_arm: 64
  
  arms:
    control:
      name: standard_operations
      description: No Sovereign vacuum detection
    treatment:
      name: sovereign_active
      description: Sovereign vacuum detection enabled

metrics:
  primary:
    name: coordination_time_minutes
    type: continuous
    direction: lower_is_better
  
  secondary:
    - name: vacuum_detections
      type: count
      direction: higher_is_better
    - name: escalation_count
      type: count
      direction: lower_is_better
  
  safety:
    - name: false_positive_rate
      type: rate
      threshold: < 0.10

analysis:
  intention_to_treat: true
  sensitivity:
    - per_protocol
    - as_treated
    - instrumental_variable
  
  methods:
    - t_test
    - regression_adjustment
    - propensity_score_weighting
  
  missing_data:
    strategy: multiple_imputation
    sensitivity: pattern_mix

pre_registration:
  platform: OSF
  date: "{{date}}"
  hypothesis_locked: true
  analysis_plan_locked: true

ethics:
  IRB_exemption: likely
  monitoring: interim_analysis_enabled
```

### Template 2: Instrumental Variable

```yaml
# experiment-templates/instrumental-variable.yaml
name: sovereign_iv_analysis
type: instrumental_variable
version: "1.0"

purpose: >
  Estimate causal effect using domain complexity as instrument

iv_conditions:
  relevance:
    test: correlation(iv, treatment)
    threshold: r > 0.3
  
  independence:
    test: correlation(iv, confounders)
    threshold: r < 0.1
  
  exclusion:
    test: iv → outcome (through treatment only)
    justification: "Domain complexity affects coordination only through vacuum detection"

estimation:
  method: two_stage_least_squares
  robust_se: heteroskedasticity_robust

sensitivity:
  - weak_iv_test
  - partial_r2
  - Angrist-Pischke F
```

### Template 3: Regression Discontinuity

```yaml
# experiment-templates/regression-discontinuity.yaml
name: sovereign_rdd
type: regression_discontinuity_design
version: "1.0"

purpose: >
  Estimate effect at threshold of vacuum detection activation

running_variable:
  name: domain_complexity_score
  threshold: 7.0  # Above this, Sovereign activates
  
bandwidth:
  selection: mse_opt
  sensitivity: [0.5x, 1.5x, 2x]

identification:
  assumption: continuity
  test: manipulation_test
  test_name: mccrary

estimation:
  local_linear_regression: true
  kernel: triangular
  robust_se: true

placebo_tests:
  - at_threshold: 0
    expected_null: true
  - at_other_thresholds: 
    expected_null: true
```

### Template 4: Difference-in-Differences

```yaml
# experiment-templates/difference-in-differences.yaml
name: sovereign_did
type: difference_in_differences
version: "1.0"

purpose: >
  Estimate effect using phase-in as natural experiment

timing:
  pre_periods: 4
  post_periods: 4
  
parallel_trends:
  test: pre_trends_test
  method: event_study
  visualization: event_plot

estimation:
  two_way_fixed_effects: true
  cluster_se: by_domain

heterogeneity:
  - by_operator_type
  - by_domain_complexity
```

---

## Data Schemas

### Experiment Schema

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Causal Inference Experiment",
  "type": "object",
  "required": ["name", "design", "metrics", "analysis"],
  "properties": {
    "name": {"type": "string"},
    "design": {
      "type": "object",
      "required": ["assignment", "arms"],
      "properties": {
        "assignment": {"enum": ["random", "observational"]},
        "arms": {"type": "array", "items": {"type": "object"}}
      }
    },
    "metrics": {
      "type": "object",
      "properties": {
        "primary": {"type": "object"},
        "secondary": {"type": "array"},
        "safety": {"type": "array"}
      }
    },
    "analysis": {
      "type": "object",
      "required": ["intention_to_treat"],
      "properties": {
        "intention_to_treat": {"type": "boolean"},
        "sensitivity": {"type": "array"}
      }
    }
  }
}
```

---

## ROS Specification

### Workflow

```
1. HYPOTHESIS
   a. Identify claim from vacuum detector
   b. Map to causal estimand
   c. Draw DAG
   d. Identify confounders

2. DESIGN
   a. Choose method (RCT, IV, RDD, DiD, etc.)
   b. Calculate sample size
   c. Pre-register

3. DATA
   a. Collect per protocol
   b. Lock dataset
   c. Document deviations

4. ANALYSIS
   a. Run locked analysis
   b. Sensitivity analysis
   c. Heterogeneity exploration

5. SYNTHESIS
   a. Report effect size + CI
   b. Interpret in context
   c. Update DAG
   d. Feed to operators
```

### Quality Gates

| Gate | Requirement |
|---|---|
| SUTVA | Stable unit treatment value assumption |
| Positivity | All treatment levels have probability > 0 |
| Overlap | Common support across arms |
| Power | ≥ 0.80 |
| Pre-registration | Before any analysis |

---

## Decision Log

| Date | Decision | Rationale |
|---|---|---|
| 2026-04-26 | Causal inference first pillar | Prove causation, not assumption |
| 2026-04-26 | 4-level reading ladder | Progressive depth |
| 2026-04-26 | Multiple methods | Different causal questions |
| 2026-04-26 | Pre-registration required | Prevent p-hacking |

---

*Every causal claim needs a test. Every test needs a pre-registration.*