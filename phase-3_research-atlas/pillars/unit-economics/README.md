# Pillar 2: Unit Economics

## Purpose

To measure, prove, and optimize value creation and capture.

**Core Question**: *"What is the ROI of research vs execution, and can we prove it?"*

### The Value Equation

```
Value = (Revenue - Cost) × Attribution × Time
```

We need to know:
- Where value comes from (attribution)
- How long it lasts (cohort analysis)
- How much it costs to acquire (CAC)
- How much it generates (LTV)

---

## Reading Ladder (Progressive Depth)

### Level 1: Fundamentals (Weeks 1-2)

| Source | Author | Year | Core Concept | Time |
|-------|--------|------|---|---|
| *The SaaS Metrics* | KPCB | 2018 | LTV, CAC, payback | 4h |
| *Zero to One* | Thiel | 2014 | Economics of scale | 6h |
| *Traction* | Fried & Heinemeier | 2012 | 19 channels | 5h |
| *Lean Analytics* | Croll & Yoskovitz | 2014 | One metric that matters | 6h |

**Total**: 21 hours

**Deliverable**: Your first LTV/CAC calculation

### Level 2: Advanced Methods (Weeks 3-4)

| Source | Author | Year | Core Concept | Time |
|-------|--------|------|---|---|
| *Marketing Metrics* | Armstrong | 2020 | Attribution models | 8h |
| *Multi-Touch Attribution* | Jin et al. | 2014 | Data-driven | 6h |
| *Customer-Based Corporate Finance* | Anand | 2017 | CBSC, LTV:CAC | 10h |
| *Platform Economics* | Parker et al. | 2016 | Network effects | 8h |

**Total**: 32 hours

**Deliverable**: Your own attribution model

### Level 3: Cutting Edge (Weeks 5+)

| Source | Author | Year | Core Concept | Time |
|-------|--------|------|---|---|
| *Blitzscaling* | Hoffman & Chaparro | 2016 | Growth economics | 6h |
| *The Cold Start Problem* | Murray | 2020 | Network effects | 6h |
| *Subadditive Aggregation* | Kak et al. | 2022 | LTV at scale | 8h |

**Total**: 20 hours

**Deliverable**: Network effects model

---

## Experiment Templates

### Template 1: Cohort Analysis

```yaml
# experiment-templates/cohort-analysis.yaml
name: sovereign_cohort_analysis
type: longitudinal_cohort
version: "1.0"

purpose: >
  Track value creation by cohort over time

Cohorts:
  definition: monthly_signup
  retention_windows: [1, 3, 6, 12, 24 months]
  
cohort_attributes:
  - source
  - acquisition_channel
  - domain_complexity
  - operator_type

metrics_by_window:
  1m:
    - activation_rate
    - first_action
  
  3m:
    - repeat_action_rate
    - engagement_score
  
  6m:
    - revenue (if applicable)
    - NRR
  
  12m:
    - LTV_estimate
    - total_value
  
  24m:
    - LTV_final
    - Cohort_LTV

visualization:
  retention_heatmap: true
  cohort_curves: true
  histogram: tenure_distribution
```

### Template 2: Attribution Model

```yaml
# experiment-templates/attribution-model.yaml
name: sovereign_attribution
type: multi_touch_attribution
version: "1.0"

purpose: >
  Attribute conversion to touchpoints using Shapley values

touchpoints:
  - research_study
  - execution_action
  - operator_selection
  - vacuum_detection
  - coordination_improvement

model_types:
  data_driven:
    method: shapley_value
    sample_iterations: 1000
    random_seed: 42
  
  rules_based:
    - first_touch
    - last_touch
    - linear
    - time_decay

sensitivity:
  - exclude_touchpoint
  - add_noise
  - bootstrap_CI

output:
  per_touchpoint:
    - raw_shapley
    - normalized
    - confidence_interval
  
  global:
    - model_r2
    - validation_error
```

### Template 3: LTV Calculation

```yaml
# experiment-templates/ltv-calculation.yaml
name: sovereign_ltv
type: lifetime_value
version: "1.0"

formula: >
  LTV = ARPU × Gross Margin × (1 / Churn Rate)

components:
  ARPU:
    calculation: total_revenue / unique_users
    frequency: monthly
  
  Gross Margin:
    calculation: (revenue - COGS) / revenue
    frequency: quarterly
  
  Churn Rate:
    calculation: users_lost / users_at_start
    frequency: monthly
    types:
      - Logo churn (cancelled)
      - Revenue churn (dropped)
      - Net Revenue Retention: (MRR + Expansion - Churn) / MRR

time_horizons:
  short: 12 months
  medium: 24 months
  long: 60 months (or historical max)

sensitivity:
  - +10% churn
  - -10% ARPU
  - +5% expansion
  - +5% contraction
```

---

## Mathematical Framework

### Shapley Value Attribution

```python
# attribution_model.py
from itertools import combinations
import numpy as np

class ShapleyAttribution:
    """
    Calculate Shapley values for multi-touch attribution.
    
    The Shapley value is the average marginal contribution
    of each player (touchpoint) to the game (conversion).
    """
    
    def __init__(self, touchpoints: list[str], n_samples: int = 1000):
        self.touchpoints = touchpoints
        self.n_samples = n_samples
    
    def calculate(self, conversion_data: list[set[str]]) -> dict[str, float]:
        """Calculate Shapley values for touchpoints."""
        
        shapley_values = {tp: 0.0 for tp in self.touchpoints}
        
        for conversion_touchpoints in conversion_data:
            # For each coalition containing this touchpoint
            for tp in conversion_touchpoints:
                marginal_contributions = []
                
                for subset_size in range(len(conversion_touchpoints)):
                    for subset in combinations(
                        conversion_touchpoints - {tp}, 
                        subset_size
                    ):
                        # Value with tp
                        v_with = self._value(set(subset) | {tp})
                        # Value without tp
                        v_without = self._value(set(subset))
                        
                        marginal = v_with - v_without
                        marginal_contributions.append(marginal)
                
                if marginal_contributions:
                    avg_marginal = np.mean(margular_contributions)
                    shapley_values[tp] += avg_marginal
        
        # Normalize
        n_conversions = len(conversion_data)
        return {
            tp: value / n_conversions 
            for tp, value in shapley_values.items()
        }
    
    def _value(self, coalition: set[str]) -> float:
        """
        Value of coalition.
        
        In this simple version: 1 if non-empty, 0 if empty.
        Replace with actual conversion data.
        """
        return 1.0 if coalition else 0.0
```

### LTV Calculation

```python
# ltv_calculation.py
class LTVCaculator:
    """
    Calculate Lifetime Value for each cohort.
    """
    
    def __init__(self, time_horizon_months: int = 24):
        self.horizon = time_horizon_months
    
    def calculate(
        self, 
        cohort_data: dict
    ) -> float:
        """Calculate LTV for a cohort."""
        
        # ARPU
        arpu = cohort_data['total_revenue'] / cohort_data['unique_users']
        
        # Gross margin
        gross_margin = (
            cohort_data['revenue'] - cohort_data['cogs']
        ) / cohort_data['revenue']
        
        # Churn rate (simplified —use actual in production)
        churn_rate = cohort_data.get('churn_rate', 0.05)
        
        # Simple LTV
        if churn_rate > 0:
            simple_ltv = arpu * gross_margin * (1 / churn_rate)
        else:
            # Use observed data if no churn
            simple_ltv = cohort_data.get('observed_ltv', 0)
        
        # Cap at time horizon
        monthly_ltv = arpu * gross_margin
        capped_ltv = min(
            simple_ltv, 
            monthly_ltv * self.horizon
        )
        
        return capped_ltv
    
    def calculate_cac_ratio(self, ltv: float, cac: float) -> float:
        """Calculate LTV:CAC ratio."""
        return ltv / cac if cac > 0 else 0
    
    def payback_period(
        self, 
        arpu: float, 
        cac: float,
        gross_margin: float
    ) -> float:
        """Calculate payback period in months."""
        monthly_margin = arpu * gross_margin
        return cac / monthly_margin if monthly_margin > 0 else float('inf')
```

---

## ROS Specification

### What We Need to Prove

| Claim | Evidence Required | Method |
|-------|----------------|--------|
| Research improves execution | LTV difference by research exposure | Cohort analysis |
| Vacuum detection adds value | A/B test on vacuum active | RCT |
| Operator type matters | Effect by operator | Regression |
| Attribution is correct | Sensitivity analysis | Shapley robustness |

### Quality Gates

| Gate | Threshold |
|---|---|
| LTV:CAC | > 3.0 |
| Payback period | < 12 months |
| NRR | > 100% |
| Churn | < 5% monthly |

---

## Decision Log

| Date | Decision | Rationale |
|---|---|---|
| 2026-04-26 | Unit economics as pillar 2 | Need attribution, not assumption |
| 2026-04-26 | Shapley attribution | Fair marginal contribution |
| 2026-04-26 | Cohort analysis | Time-series value tracking |
| 2026-04-26 | LTV:CAC > 3 | Standard SaaS benchmark |

---

*Every dollar of value needs a proven source. Every source needs attribution.*