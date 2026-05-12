# Module 5 — Glossary

Module-specific terms from M5.

---

**Agent.** A system that pursues a goal by reasoning, calling tools, observing results, and iterating.

**Agent Control Panel.** The five levers a PM specs and watches: triggers, tools, memory scope, stop conditions, observability.

**Agent Spectrum.** Tool → Assistant → Agent → Autonomous Agent.

**Agent Workflow Spec (AWSpec).** The product spec for an agent. Nine sections: goal, trigger, inputs, tools, memory, pattern, stop conditions, handoff rules, eval hooks.

**Agentic memory.** State persisted across turns or sessions. Four types: short-term, long-term, episodic, semantic.

**Audit trail.** The visible record of agent actions, with reasoning, tool calls, and outcomes.

**Autonomous Agent.** The highest spectrum level — operates over long horizons unsupervised.

**Boundary contract.** What the PM Decision Triangle creates — the explicit line where AI hands off to a human.

**Cascading errors.** A failure mode where one wrong tool call causes downstream tool calls to be wrong.

**Drift (agentic).** Behaviour pulled off-spec over time, usually via long-term memory accumulating bad data.

**Episodic memory.** Memory of specific past events ("the user said X yesterday").

**Eval hooks.** The logging points inside an agent flow that feed the M6 eval stack.

**Handoff rules.** The explicit conditions under which the agent stops and escalates to a human.

**Hallucinated tool call.** A failure mode where the agent invents an API or tool that doesn't exist.

**Iteration.** One of the four traits of agency — observing results and re-planning.

**Langflow.** A no-code agent builder. Used in the optional M5 post-class lab.

**Long-term memory.** State persisted across sessions.

**Memory poisoning.** A failure mode where bad data gets stored as fact in agentic memory.

**Planner-Executor.** Multi-agent pattern: one agent plans, one or many execute, planner re-plans on failure.

**PM Decision Triangle.** The three modes for any step: AI alone / AI + human / human alone.

**ReAct.** *Reason → Act → Observe → loop.* Single-agent reasoning pattern.

**Runaway loop.** A failure mode where the agent retries without a stop condition.

**Semantic memory.** General knowledge memory (domain facts, org context).

**Short-term memory.** State within one task / one turn.

**Silent handoff failure.** A failure mode where the agent should have escalated but didn't.

**Stop condition.** A spec'd rule for when the agent ends a workflow. Includes success, failure, escalation, timeout.

**Tool.** A callable function the agent can invoke (API, DB query, file write).

**Tool scope.** What a tool is permitted to do — read-only, write, etc.

**Trigger.** The condition that activates an agent workflow.
