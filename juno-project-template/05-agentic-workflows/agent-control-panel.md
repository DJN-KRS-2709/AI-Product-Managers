# Juno PM — Agent Control Panel

_Version 0.1 — placeholder. Replace via `M5 - Agent Control Panel.html`._

> The PM-facing dashboard for an agent: what to watch, what to throttle, what to roll back. Companion to `awspec.md`.

---

## Four levers

### 1. Stop Conditions

_(set max_steps, wall-clock timeout, repeated-failure abort)_

### 2. Tool Outputs

_(what shape does each tool return? include confidence/score fields)_

### 3. Confidence Thresholds

_(map confidence ranges to actions: auto-post / queue / require approval)_

### 4. North Star

_(single goal sentence the agent re-reads every loop, to prevent drift)_

---

## Rules of engagement

| Rule | Spec |
|---|---|
| Agency Permission | _(autonomy threshold; what the agent can draft vs send)_ |
| Access Control | _(read/write boundaries per tool + database)_ |
| Fallback Protocols | _(what happens when loops break or gates trigger)_ |
| Checkpoints | _(red-zone triggers for human intervention)_ |

---

## Observability — what we trace (carry-over to M6)

| Field | Notes |
|---|---|
| Trace ID | |
| Trigger payload | |
| Retrieved chunks | |
| Tool calls | |
| Outputs | |
| Confidence per risk | |
| Latency (p95) | |
| Tokens + cost | |

## Throttles

| Lever | Default | When to change |
|---|---|---|
| Concurrency | 1 | _ |
| Max tokens / run | _ | _ |
| Tool-call budget / run | _ | _ |
| Per-day spend cap | _ | _ |

## Kill switches

- _(named feature flag → off when this triggers)_
- _(rollback path)_

## On-call playbook

1. _(symptom)_
2. _(first check)_
3. _(remediation)_
4. _(escalation path)_

---

## Self-review

- [ ] Stop conditions include `max_steps` + a wall-clock timeout.
- [ ] Tool outputs include a confidence/score field per retrieval tool.
- [ ] Confidence thresholds map to actions, not just labels.
- [ ] North Star is one sentence, re-read every loop.
- [ ] Each rule of engagement names something the agent CANNOT do.
