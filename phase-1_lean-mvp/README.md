# Phase 1: Lean MVP — Repository Architecture

## Purpose
Fastest path to deployable Sovereign layer. Minimal viable product with core operators implemented.

## $MODE: lean-mvp
## $DEPTH: operator-grade
## $NEXT: SERVICE-BY-SERVICE CODE SCAFFOLD + FIRST DEPLOYMENT SCRIPTS

---

## File Tree

```
phase-1_lean-mvp/
├── sovereignty-learner-mvp/
│   ├── src/
│   │   ├── operators/
│   │   │   ├── selfish_altruistic_loop.py
│   │   │   ├── magnetic_membrane.py
│   │   │   ├── portfolio_operator.py
│   │   │   └── reflexive_loop.py
│   │   ├── observatory/
│   │   │   ├── vacuum_detector.py
│   │   │   ├── seam_mapper.py
│   │   │   └── escalation_router.py
│   │   └── cli/
│   │       └── sovereign_cli.py
│   ├── tests/
│   │   ├── test_operators.py
│   │   └── test_observatory.py
│   ├── scripts/
│   │   ├── deploy.sh
│   │   └── bootstrap.sh
│   ├── env.example
│   ├── pyproject.toml
│   ├── README.md
│   └── seed.yaml
├── CLAUDE.md
└── AGENTS.md
```

---

## Environment Variables

```bash
# Sovereign MVP Environment
SOV_EPOCH=2026-04-26
SOV_MODE=lean-mvp
SOV_DEPTH=operator-grade
SOV_LOG_LEVEL=INFO

# Observatory Settings
OBSERVATORY_VACUUM_THRESHOLD=0.75
OBSERVATORY_SEAM_SENSITIVITY=high
OBSERVATORY_ESCALATION_BOUNDARY=auto

# Operator Settings
OPERATOR_SELFISH_ALTRUISTIC_THRESHOLD=0.5
OPERATOR_MAGNETIC_POLE=attract
OPERATOR_PORTFOLIO_MAX_DOMAINS=10
OPERATOR_REFLEXIVE_ITERATIONS=3
OPERATOR_REFLEXIVE_ANCHOR=human

# Integration
INTEGRATION_HOKAGE_REGISTRY_URL=http://localhost:8080
INTEGRATION_IRF_ENDPOINT=http://localhost:8081
```

---

## Core Service: Vacuum Detector

```python
# src/observatory/vacuum_detector.py
class VacuumDetector:
    """Detects vacuum radiation from Hokage actions."""
    
    def __init__(self, threshold: float = 0.75):
        self.threshold = threshold
        self.radiation_map = {}
    
    def scan_hokage_output(self, hokage_domain: str) -> list[Vacuum]:
        """Scan a Hokage domain for vacuum radiation."""
        # Implementation: Parse Hokage artifacts, find unsaid gaps
        pass
    
    def classify_vacuum(self, vacuum: Vacuum) -> str:
        """Classify vacuum severity."""
        if vacuum.radiation_score > self.threshold:
            return "CRITICAL"
        return "LOW"
```

---

## Deployment Script

```bash
#!/bin/bash
# scripts/deploy.sh
set -e

echo "🚀 Deploying Sovereign Lean MVP..."

# Bootstrap
bash scripts/bootstrap.sh

# Start services
python -m src.cli.sovereign_cli serve --port 8080

echo "✅ Sovereign MVP deployed at http://localhost:8080"
```

---

## Decision Log

| Decision | Rationale |
|---|---|
| Lean MVP first | Fastest path to validation |
| Operator-grade depth | Enough to test, not dissertation |
| Service-by-service | Incremental, not big-bang |