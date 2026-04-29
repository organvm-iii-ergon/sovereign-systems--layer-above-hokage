# 2026-04-29 Workload Encompassing Layer Routing

## Scope

This plan routes the Apr 28-29 workspace load through the layer-above-Hokage
observable. The immediate workload has two client streams, but the governing
problem is broader: prevent uncommitted client work, session exports, plan
mirrors, and auto-capture substrates from drifting into local-only state.

## Verified Inputs

- `/Users/4jp/AGENTS.md` requires plans as durable artifacts, no overwrites,
  local:remote parity, memory-as-hypothesis verification, and no LaunchAgents.
- `sovereign-systems--layer-above-hokage/CLAUDE.md` defines this repo as the
  observable above Hokage outputs, responsible for detecting vacuum radiation
  at domain seams.
- `my-knowledge-base/.conductor/active-handoff.md` routes ORGAN-I theory work
  to Gemini and explicitly locks non-Theoria repos out of that stream.
- Claude transcript `534d27e0` was reviewed enough to identify its actual
  scope: it shipped the `public-record-data-scrapper` npm lockfile cleanup and
  was interrupted during a Gemini chat export attempt.
- Current git status shows the pasted manifest is incomplete: the Maddie,
  knowledge-base, and orchestrator WIP sets include additional modified and
  untracked files beyond the summary.

## Load-Bearing Streams

1. **Rob / Hokage**
   - Project: `4444J99/hokage-chess`
   - Role: client-facing offer, manifest, external forms, parametric content
   - Current risk: untracked plans plus duplicate audit artifacts; one tracked
     source doc deletion must be understood before cleanup.

2. **Maddie / Spiral**
   - Project: `organvm/sovereign-systems--elevate-align`
   - Role: client site and 13-node spiral substrate
   - Current risk: larger WIP surface than reported, including source/data
     changes, docs deliverables, exports, local history, and SpecStory output.

3. **Domus mirror**
   - Project: `4444J99/domus-semper-palingenesis`
   - Role: chezmoi mirror of portable plan artifacts
   - Current risk: clean now, but mirror discipline remains part of close-out
     for any plan judged canonical.

4. **Theory / Knowledge Base**
   - Project: `organvm/my-knowledge-base`
   - Role: ORGAN-I ingestion and theory substrate
   - Current risk: active handoff says Gemini owns theory work; local WIP must
     not be merged into client streams or edited casually.

5. **Orchestrator / Inverted Interview**
   - Project: `organvm/life-my--midst--in`
   - Role: agent-pattern and identity-orchestration infrastructure
   - Current risk: branch is behind origin and has both modified packages and
     new directories; pull/merge must not happen before WIP checkpointing.

6. **Public-record scraper**
   - Project: `organvm/public-record-data-scrapper`
   - Role: cleanup stream already shipped in `534d27e0`
   - Current risk: only `.lh/` local-history substrate remains from that
     transcript; not a source commit candidate.

## Priority Order

1. **Protect at-risk WIP without altering semantics**
   - Inventory exact diffs for `sovereign-systems--elevate-align`,
     `life-my--midst--in`, and `my-knowledge-base`.
   - Do not commit generated, local-history, SpecStory, or checkpoint files
     unless the repo policy explicitly tracks them.
   - Do not touch knowledge-base theory implementation before reconciling the
     active Gemini handoff.

2. **Clean obvious accidental cruft only after status proof**
   - In `hokage-chess`, distinguish duplicate audit paste artifacts from
     intentionally archived copies.
   - Investigate the tracked deletion
     `docs/business/2026-04-25-rob-call-transcript-source.md` before staging.

3. **Resolve onboarding ambiguity**
   - In `growth-auditor`, inspect `seed.yaml` and decide whether it is
     intentional habitat creation or a stray file. If intentional, add the
     matching governance references; if stray, leave uncommitted and report.

4. **Complete interrupted session export if still desired**
   - The interrupted `534d27e0` export target was the Gemini chat
     `/Users/4jp/.gemini/tmp/4jp/chats/session-2026-04-28T06-38-af959950.json`.
   - Export destination must be selected by stream: Maddie plan history,
     Hokage cross-stream plan, or corpus/session archive.

5. **Mirror canonical plans**
   - Any plan promoted from project-local draft to operating artifact should be
     mirrored into `domus-semper-palingenesis/private_dot_claude/plans/`.
   - Keep project-local and domus mirrors intentionally duplicated.

## Guardrails

- Treat all pasted session summaries as hypotheses until verified against disk.
- Avoid broad commit sweeps across repos; commit per repo and per semantic unit.
- Do not use LaunchAgents.
- Do not overwrite plans; version instead.
- Preserve user and other-agent WIP; no reset/checkout cleanup.
- Generated auto-capture substrates are evidence, not automatically shippable
  source.

## Next Concrete Actions

1. Produce per-repo diff inventories for the three WIP repos.
2. Clean `hokage-chess` duplicate audit artifacts only after confirming exact
   filenames and leaving intentional archived material alone.
3. Write a short checkpoint note for any WIP that should not yet be committed.
4. Run targeted validation only where source files are staged for commit.

## Linked Artifacts (downstream)

Plans operationalized under this routing — append as new ones land.

- **2026-04-29 — Maddie ideals-vs-rendered diff tracker.** Crosswalks the
  W-001..W-065 atomized-wants inventory and the I-NN V4 design directives
  against the current rendered state of the Maddie spiral. Identifies 8
  PARTIAL, 5 MISSING, 9 BLOCKED, 7 DRIFT items including the EnvVar
  substrate (D-001) and pillar-mapping discrepancy between the locked
  architecture and `hub.config.ts` (D-005). Refresh discipline: manual,
  on-demand. No automation.
  - Canonical: `organvm/sovereign-systems--elevate-align/.claude/plans/2026-04-29-maddie-ideals-vs-rendered-diff.md` (commit `baa24f6`)
  - Chezmoi mirror: `domus-semper-palingenesis/private_dot_claude/plans/2026-04-29-maddie-ideals-vs-rendered-diff.md` (commit `9c45e10`)
- **2026-04-29 — Antigravity voice-assistant repair plan.** Diagnosis-only
  plan. Stream A of conductor session. Lane (b) recommended: install a
  macOS-native recognizer (Whisper.cpp + ~80-line Node bridge) that
  speaks the b4rtaz extension's WS protocol on `localhost:9999`. The
  b4rtaz client is structurally sound — only the recognizer back-end is
  missing for macOS. Foreground process only, no LaunchAgent.
  - Local: `~/.claude/plans/2026-04-29-antigravity-voice-assistant-repair.md`
