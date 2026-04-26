# Publication & Dissemination Pipeline

## Purpose

Turn research into knowledge that spreads.

---

## Publication Types

### Internal Publications

| Type | Audience | Distribution | Review |
|------|----------|--------------|--------|
| **Memo** | Core team | Slack | 1 reviewer |
| **Brief** | Org | Wiki | 2 reviewers |
| **Report** | All | Wiki + Email | 3 reviewers |

### External Publications

| Type | Audience | Venue | Review |
|------|---------|-------|--------|
| **Blog Post** | Public | Blog | 2 + editor |
| **Paper** | Academic | journal/conference | Peer review |
| **Tool** | Developers | GitHub | CI + users |

---

## Pipeline Stages

```
┌─────────────────────────────────────────────────────────────────┐
│              PUBLICATION PIPELINE                    │
└─────────────────────────────────────────────────────────────────┘
                        │
    ┌───────────────────┼───────────────────┐
    ▼                   ▼                   ▼
┌──────────┐      ┌──────────┐      ┌──────────┐
│  STAGE 1 │      │  STAGE 2 │      │  STAGE 3  │
│  DRAFT   │─────▶│  REVIEW  │─────▶│ PUBLISH  │
│          │      │          │      │          │
│ - Write  │      │ -Internal│      │ -Internal│
│ - Figures│      │ -Peer    │      │ -External│
│ - Code   │      │ -Public  │      │ -GitHub  │
└──────────┘      └──────────┘      └──────────┘
    │                   │                   │
    ▼                   ▼                   ▼
┌──────────┐      ┌──────────┐      ┌──────────┐
│ COMPLETE │      │ CHANGES │      │ DISTRIBUT│
│         │      │         │      │         │
│ Pass to │      │ Address │      │ -Slack  │
│ review  │      │ review  │      │ -Wiki   │
│         │      │         │      │ -Blog   │
└──────────┘      └──────────┘      └──────────┘
```

---

## Stage 1: Draft

### Template: Research Memo

```markdown
# Research Memo: [Study ID]

## TL;DR
[One sentence finding]

## Background
[Why this matters]

## Study
**ID**: SOVEREIGN-2026-XXX
**Question**: [Hypothesis]
**Method**: [Design]
**N**: [Sample size]

## Findings

### Primary
| Metric | Effect | 95% CI | p |
|-------|--------|--------|---|
| ... | ... | ... | ... |

### Sensitivity
| Analysis | Effect | 95% CI |
|----------|--------|--------|
| ... | ... | ... |

## Interpretation
[What this means]

## Next Steps
[Recommendations]

## Appendix
- Pre-registration: [URL]
- Code: [URL]
- Data: [URL]
```

### Template: Figures

```python
def generate_figures(results):
    figures = []
    
    # 1. Effect size forest plot
    forest = alt.Chart(results).mark_boxplot().encode(
        x="effect",
        y="analysis",
        color="significant:Q"
    )
    figures.append(forest)
    
    # 2. Heterogeneity heatmap
    heatmap = alt.Chart(heterogeneity).mark_rect().encode(
        x="stratum",
        y="metric",
        color="effect"
    )
    figures.append(heatmap)
    
    # 3. Sensitivity robustness
    robustness = alt.Chart(sensitivity).mark_point().encode(
        x="method",
        y="effect",
        yError="ci"
    )
    figures.append(robustness)
    
    return figures
```

---

## Stage 2: Review

### Internal Review Checklist

```
□ Methods correct
□ Reproducible
□ Interpretation reasonable
□ Writing clear
□ Conclusions match results

Reviewers:
- [ ] Technical (methods expert)
- [ ] Domain (Sovereign expert)  
- [ ] Independent (fresh eyes)

Timeline:
- Assign: Day 0
- Review due: Day 5
- Revisions due: Day 7
- Decision: Day 10
```

### Revision Template

```markdown
# Review Response

## Reviewer 1: [Name]
### Comments
[Reviewer comments]

### Response
[Author response]

## Changes Made
- [Change 1]: Made/unmade because [reason]
- [Change 2]: ...
```

---

## Stage 3: Publish

### Distribution Checklist

| Channel | Type | Done |
|---------|------|------|
| Slack | Memo link | ☐ |
| Wiki | Full report | ☐ |
| Blog | Public summary | ☐ |
| GitHub | Code + data | ☐ |
| OSF | Pre-reg + data | ☐ |

### Metadata

```yaml
publication:
  study_id: SOVEREIGN-2026-001-CAUSTAL
  type: memo
  title: "Effect of vacuum detection on coordination time"
  date: "{{date}}"
  authors: [list]
  reviewers: [list]
  license: CC-BY-4.0
  doias: 10.5281/zenodo.xxx
```

---

## Impact Tracking

### Metrics

| Metric | Target | Current |
|-------|--------|---------|
| Internal memos/year | 12 | — |
| External posts/year | 4 | — |
| Citations | 10 | — |
| Reproductions | 2 | — |

### Attribution

```python
def cite_study(study_id):
    return f"""
{study_id}: {study.title}
{authors}, {year}
doi: {doi}
link: {pre_registration_url}
    """
```

---

## Automation

```yaml
# publication-pipeline.yaml
pipeline:
  stages:
    - draft:
        template: memo.md
        auto_generate: true
        
    - review:
        assign: round_robin
        reminder: 3 days
        
    - publish:
        channels: [slack, wiki, github]
        automatic: true if level >= 2
        
  templates:
    memo: templates/memo.md
    brief: templates/brief.md
    report: templates/report.md
```

---

## Quality Gate

| Stage | Gate | Requirement |
|-------|------|------------|
| 1 Draft | Complete | All sections filled |
| 2 Review | Approved | 2+ reviewers approve |
| 3 Publish | Distributed | 2+ channels |