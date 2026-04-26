# Phase 2: Sales One-Pager — Technical Spec Split

## Purpose
Dual-track document: Sales One-Pager (business) + Technical Spec (engineering)

---

## File Structure

```
phase-2_sales-one-pager/
├── sales-one-pager/
│   ├── README.md
│   └── exports/
│       ├── sales-one-pager.pdf
│       └── sales-one-pager.html
├── technical-spec/
│   ├── README.md
│   └── api/
│       ├── openapi.yaml
│       └── schemas/
└── comparison-matrix.md
```

---

# SALES ONE-PAGER

## Sovereign: The Layer Above Hokage

**The cross-domain governance layer for multi-domain systems.**

### The Problem

Every Hokage (domain executor) optimizes locally. The seams between domains are where systems lose coherence. You can't see what your executors can't see — and they can't see each other.

### The Solution

Sovereign is the observatory. It watches what Hokages produce, detects what they miss, and routes what needs routing.

### Core Capabilities

| Capability | What It Does | Value |
|---|---|---|
| Vacuum Detection | Maps unsaid gaps from domain actions | Prevents calcified debt |
| Seam Mapping | Visualizes cross-domain overlaps | Prevents duplicated work |
| Portfolio Arbitration | Resolves resource conflicts | Optimal allocation |
| Reflexive Auditing | Self-evaluates governance | Continual improvement |

### The Four Operators

1. **Selfish-Altruistic Loop**: When Domain A wins and Domain B loses
2. **Magnetic Membrane**: What enters/exits the system boundary
3. **Portfolio**: Domain lifecycle (create/evolve/retire)
4. **Reflexive**: Self-audit with human anchor

### Traction

- ✅ 37 repositories mapped
- ✅ 10 organs instrumented
- ✅ 4 operators implemented
- ✅ 2 Hokage lanes monitored

### Pricing

| Tier | Features | Price |
|---|---|---|
| **Observer** | Vacuum detection, basic dashboard | $99/mo |
| **Arbiter** | + Seam mapping, portfolio arbitration | $299/mo |
| **Sovereign** | + Full reflexive audit, escalation routing | $599/mo |

### CTA

**Deploy your Sovereign today.**

[sales@sovereign.ai] — [sovereign.ai/demo]

---

# TECHNICAL SPEC

## Architecture

### Components

```
┌─────────────────────────────────────────────────┐
│              Sovereign Gateway                  │
│            (API Gateway / Auth)               │
└─────────────────┬───────────────────────────────┘
                  │
    ┌───────────┼───────────┐
    │           │           │
    ▼           ▼           ▼
┌───────┐ ┌───────┐ ┌───────────┐
│Vacuum │ │Seam  │ │ Portfolio │
│Detect │ │Map   │ │Arbitrator │
│Service│ │Service│ │  Service  │
└───┬───┘ └───┬───┘ └─────┬─────┘
    │         │           │
    └─────────┼───────────┘
              ▼
    ┌─────────────────┐
    │  Reflexive      │
    │  Audit Engine   │
    └────────┬────────┘
             │
             ▼
    ┌─────────────────┐
    │  Human Anchor   │
    │  (You)         │
    └─────────────────┘
```

### API Schema

```yaml
# api/vacuum.yaml
openapi: 3.0.0
info:
  title: Sovereign Vacuum API
  version: 1.0.0

paths:
  /vacuum/scan:
    post:
      summary: Scan domain for vacuum radiation
      requestBody:
        content:
          application/json:
            schema:
              type: object
              properties:
                domain:
                  type: string
                depth:
                  type: integer
      responses:
        '200':
          description: Vacuum scan results
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/VacuumReport'

components:
  schemas:
    VacuumReport:
      type: object
      properties:
        domain:
          type: string
        radiation_score:
          type: number
        vacuums:
          type: array
          items:
            $ref: '#/components/schemas/Vacuum'
```

### Integration Points

| Integration | Protocol | Status |
|---|---|---|
| Hokage Registry | REST | ✅ |
| IRF Ledger | WebSocket | ✅ |
| GitHub | GraphQL | ✅ |
| Slack | Events API | Planned |

### Deployment

- **Cloud**: AWS / GCP / Azure
- **Orchestration**: Kubernetes
- **Observability**: Prometheus + Grafana

---

## Decision Log

| Decision | Rationale |
|---|---|
| Split sales/technical | Different audiences, different needs |
| Tiered pricing | Entry point + growth |
| Kubernetes-first | Production scale |