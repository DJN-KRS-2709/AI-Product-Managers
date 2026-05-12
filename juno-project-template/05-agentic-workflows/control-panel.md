# Juno PM — Agent Control Panel

_Version 0.1 — placeholder. Replace via M5 Agent Control Panel tool._

> The PM-facing dashboard for an agent: what to watch, what to throttle, what to roll back. Defines the on-call surface for Juno in production.

## Observability — what we trace

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
| Concurrency | _ | _ |
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
