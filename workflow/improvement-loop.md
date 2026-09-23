# The Core Improvement Loop

At the heart of the 2026 AI Prompting Workflow is the tight feedback loop between human intent, direct observation, and machine iteration.

---

## The Cycle

```text
BUILD
  ↓
PLAY
  ↓
NOTICE
  ↓
DESCRIBE
  ↓
CHANGE
  ↓
PLAY AGAIN
  ↓
SCORE
  ↓
IMPROVE
  ↓
REPEAT
```

---

## Deep Dive: Phase by Phase

| Phase | Agent / Actor | Action | Output |
| :--- | :--- | :--- | :--- |
| **BUILD** | AI Assistant | Generates code, runs file operations, builds initial functional artifact. | Executable code files (`web/`, `app/`). |
| **PLAY** | Human User | Launches the game, inputs commands, tests boundaries, evaluates physical feel. | Direct visceral sensory experience. |
| **NOTICE** | Human User | Catches points of friction, sluggishness, awkwardness, or missing delights. | Intuitive friction list. |
| **DESCRIBE** | Human User | Converts impressions into precise, actionable prompts (e.g. `prompts/04_feedback_prompt.md`). | Numbered, unambiguous feedback prompt. |
| **CHANGE** | AI Assistant | Executes targeted refactorings and adds requested mechanics without breaking prior features. | Updated code artifact. |
| **PLAY AGAIN**| Human User | Retests specifically to verify the fix and discover second-order effects. | Validation of improvement. |
| **SCORE** | AI & Human | Evaluates artifact across 7 objective rubric dimensions (1–10 scale). | Numerical evaluation matrix & report. |
| **IMPROVE** | AI & Human | Isolates lowest criterion and implements high-impact targeted resolution. | High-leverage enhancement. |
| **REPEAT** | Combined Loop | Continues iteration cycle until the human reviewer deems quality standards met. | Continuous quality ascent. |

---

## The Human-in-the-Loop Principle

> **Crucial Rule**: The human user remains exclusively responsible for deciding when the result is good enough.

Autonomous tools can calculate scores, run regression test suites, and suggest fixes; however, **gameplay delight, aesthetic cohesion, and product readiness cannot be delegated to an automated exit condition**. The human reviewer retains final authority to say: *"This is ready to ship."*
