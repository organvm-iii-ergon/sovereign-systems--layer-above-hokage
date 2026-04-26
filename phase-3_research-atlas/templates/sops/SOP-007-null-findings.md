# SOP 007: Null Findings

## Status: ACTIVE | Version: 1.0

**Purpose**: Report null findings with the same rigor as positive findings.

---

## Why Nulls Matter

| Claim | Implication |
|---|---|
| "No effect found" ≠ "No effect exists" | Could be underpowered |
| Null findings inform future studies | Sample size decisions |
| Nulls prevent waste | Don't repeat failed approaches |
| Publication bias harms science | We report everything |

---

## Procedure

### 1. VERIFY

```
□ Null confirmed? (p > 0.05 / CI includes 0)
□ Power adequate? (≥ 0.80)
□ Study quality acceptable? (no major flaws)
```

### 2. QUALIFY

```
□ Calculate power achieved
□ Calculate MDE we could detect
□ Check CI width
□ Note if CI is informative
```

### 3. DOCUMENT

```
□ All null results → study report
□ Power analysis section
□ MDE section
□ Recommendations for future
```

### 4. INTEGRATE

```
□ Update vacuum detector (new evidence)
□ Note in claim evidence base
□ Flag as "studied, null"
```

---

## Template: Null Finding Report

```yaml
study: SOVEREIGN-2026-005-ECONOMICS
hypothesis: Research exposure improves LTV

results:
  effect_size: 0.12
  ci_95: [-0.15, 0.39]
  p_value: 0.38
  power_achieved: 0.82
  mde_detectable: 0.35

interpretation: |
  We cannot reject the null hypothesis.
  With 80% power, we could detect an effect
  of d=0.35 or larger.
  
  The observed effect (d=0.12, CI [-0.15, 0.39])
  is consistent with no effect, but also
  with a meaningful positive effect.

recommendations: |
  - Study underpowered for small effects
  - Consider longer follow-up
  - Consider different outcome measure
```

---

## Decision Matrix

| Power | MDE Detectable | CI Width | Interpretation |
|-------|--------------|---------|--------------|
| High (>0.80) | Small | Narrow | Reliable null |
| Low (<0.80) | Large | Wide | Underpowered |
| Very Low (<0.50) | Very Large | Very Wide | Inconclusive |

---

## Quality Gate

| Check | Requirement |
|---|---|
| Power reported | Yes |
| MDE reported | Yes |
| CI reported | Yes |
| Recommendations | Yes |

---

## References

- SOP 001: Pre-Registration
- SOP 003: Analysis Execution