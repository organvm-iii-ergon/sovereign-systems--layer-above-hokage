# Phase 1: Full-Stack — Repository Architecture

## Purpose
Production-grade Sovereign layer with full multi-service orchestration.

## $MODE: full-stack (multi-service, production-grade)
## $DEPTH: operator-grade
## $NEXT: SERVICE-BY-SERVICE CODE SCAFFOLD + FIRST DEPLOYMENT SCRIPTS

---

## File Tree

```
phase-1_full-stack/
├── sovereignty-production/
│   ├── services/
│   │   ├── vacuum-detector-svc/
│   │   │   ├── main.py
│   │   │   ├── Dockerfile
│   │   │   └── requirements.txt
│   │   ├── seam-mapper-svc/
│   │   │   ├── main.py
│   │   │   ├── Dockerfile
│   │   │   └── requirements.txt
│   │   ├── escalation-router-svc/
│   │   │   ├── main.py
│   │   │   ├── Dockerfile
│   │   │   └── requirements.txt
│   │   ├── portfolio-arbitrator-svc/
│   │   │   ├── main.py
│   │   │   ├── Dockerfile
│   │   │   └── requirements.txt
│   │   └── reflexive-audit-svc/
│   │       ├── main.py
│   │       ├── Dockerfile
│   │       └── requirements.txt
│   ├── orchestration/
│   │   ├── service_mesh.yaml
│   │   ├── load_balancer.yaml
│   │   └── circuit_breaker.yaml
│   ├── monitoring/
│   │   ├── prometheus.yaml
│   │   ├── grafana/
│   │   └── alerts.yaml
│   ├── deployment/
│   │   ├── kubernetes/
│   │   │   ├── deployment.yaml
│   │   │   ├── service.yaml
│   │   │   └── ingress.yaml
│   │   ├── docker-compose.yaml
│   │   └── deploy.sh
│   ├── src/
│   │   ├── operators/ (mirrors lean-mvp + production hardening)
│   │   ├── observatory/ (mirrors lean-mvp + scaling)
│   │   └── api/
│   │       ├── v1/
│   │       │   ├── vacuum.yaml
│   │       │   ├── seams.yaml
│   │       │   └── escalation.yaml
│   │       └── gateway.py
│   ├── tests/
│   │   ├── integration/
│   │   ├── e2e/
│   │   └── load/
│   ├── pyproject.toml
│   ├── README.md
│   └── seed.yaml
├── CLAUDE.md
├── AGENTS.md
├── docker-compose.yaml
└── kubernetes.yaml
```

---

## Environment Variables

```bash
# Sovereign Production Environment
SOV_EPOCH=2026-04-26
SOV_MODE=full-stack
SOV_DEPTH=operator-grade
SOV_LOG_LEVEL=DEBUG
SOV_ENVIRONMENT=production

# Service Mesh
MESH_SERVICE_DISCOVERY=consul
MESH_LOAD_BALANCER=envoy
MESH_CIRCUIT_BREAKER_THRESHOLD=5

# Observatory Settings
OBSERVATORY_VACUUM_THRESHOLD=0.80
OBSERVATORY_SEAM_SENSITIVITY=high
OBSERVATORY_ESCALATION_BOUNDARY=auto
OBSERVATORY_DISTRIBUTED_SENSING=true

# Operator Settings (Scaled)
OPERATOR_SELFISH_ALTRUISTIC_THRESHOLD=0.6
OPERATOR_MAGNETIC_POLE=dynamic
OPERATOR_PORTFOLIO_MAX_DOMAINS=50
OPERATOR_REFLEXIVE_ITERATIONS=5
OPERATOR_REFLEXIVE_ANCHOR=human

# Integration
INTEGRATION_HOKAGE_REGISTRY_URL=http://consul:8500
INTEGRATION_IRF_ENDPOINT=http://irf:8081
INTEGRATION_PROMETHEUS=http://prometheus:9090
INTEGRATION_GRAFANA=http://grafana:3000
```

---

## Service: Vacuum Detector (Production)

```python
# services/vacuum-detector-svc/main.py
from fastapi import FastAPI
from pydantic import BaseModel
import asyncio

app = FastAPI()

class VacuumScanner(BaseModel):
    domain: str
    scan_depth: int = 3

@app.post("/scan")
async def scan_vacuum(request: VacuumScanner):
    """Distributed vacuum detection."""
    # Scale: parallel scanning across Hokage domains
    results = await asyncio.gather(*[
        scan_domain(domain) for domain in get_all_hokage_domains()
    ])
    return {"vacuum_radiation": results, "score": calculate_radiation_score(results)}

@app.get("/health")
def health():
    return {"status": "healthy", "service": "vacuum-detector"}
```

---

## Kubernetes Deployment

```yaml
# kubernetes.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: sovereign-vacuum-detector
spec:
  replicas: 3
  selector:
    matchLabels:
      app: sovereign-vacuum-detector
  template:
    metadata:
      labels:
        app: sovereign-vacuum-detector
    spec:
      containers:
      - name: detector
        image: sovereign/vacuum-detector:latest
        resources:
          requests:
            memory: "512Mi"
            cpu: "500m"
          limits:
            memory: "1Gi"
            cpu: "1000m"
---
apiVersion: v1
kind: Service
metadata:
  name: sovereign-vacuum-detector
spec:
  selector:
    app: sovereign-vacuum-detector
  ports:
  - port: 8080
    targetPort: 8080
```

---

## Decision Log

| Decision | Rationale |
|---|---|
| Microservices architecture | Scale independently |
| Kubernetes first | Production-grade orchestration |
| Consul service mesh | Distributed discovery |
| Prometheus + Grafana | Full observability |