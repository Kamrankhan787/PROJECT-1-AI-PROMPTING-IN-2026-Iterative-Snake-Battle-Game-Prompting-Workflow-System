# PROJECT 1 — AI PROMPTING IN 2026
### Iterative Snake Battle Game + Prompting Workflow System

[![Version](https://img.shields.io/badge/Version-1.0.0-00ff88.svg)](#)
[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](#)
[![License](https://img.shields.io/badge/License-MIT-purple.svg)](#)
[![Prompting](https://img.shields.io/badge/Methodology-2026%20Iterative%20Loop-ff0055.svg)](#)

---

## 1. Project Overview

**Project 1 — AI Prompting in 2026** is a comprehensive educational and engineering showcase demonstrating the paradigm shift from single-shot waterfall prompting to **closed-loop, experience-first iterative co-creation**.

Rather than treating AI as a code vending machine where one inputs a monolithic prompt and hopes for a perfect application, the 2026 methodology approaches software as an evolving interactive artifact. Developers:
1. Start with a tactile experience.
2. Build an immediate baseline.
3. Play and observe friction points.
4. Provide surgical feedback and change game rules.
5. Apply rigorous multi-dimensional rubric scoring to isolate bottlenecks.
6. Implement high-leverage refinements until the human reviewer approves deployment.

To demonstrate this system, this repository contains both:
* **The Playable Artifact**: A modern, cyberpunk-neon **Snake Battle** game with multi-agent AI competitors, Rule 5 corpse-to-fruit conversion, Web Audio synthesizer effects, and mobile touch controls.
* **The Workflow & Evaluation Engine**: A Python architecture featuring CLI tooling (`main.py`), prompt libraries, execution logs, rubric evaluators, headless arena simulations, and automated unit tests.

---

## 2. Learning Objective

By exploring and running this project, you will learn how to:
1. **Move beyond single-prompt engineering**: Understand why large, upfront specifications produce fragile software and why experience-driven feedback yields superior UX.
2. **Execute Rule Changes**: Learn how shifting rules (e.g. from single-player survival to battle-royale corpse harvesting) completely transforms player engagement.
3. **Operationalize Rubrics**: Use standardized 7-criteria evaluation matrices to mathematically isolate the weakest facet of an application and focus AI effort where it produces the highest return on investment.
4. **Preserve Human Oversight**: Understand why autonomous AI agents must never unilaterally declare a project finished, preserving the human developer's role as the final arbiter of quality and readiness.

---

## 3. AI Prompting Method

The project implements the canonical 12-step prompting methodology:

```text
USER GOAL
   ↓
INITIAL PROMPT
   ↓
AI BUILDS FIRST VERSION
   ↓
PLAY / TEST
   ↓
USER OBSERVES EXPERIENCE
   ↓
SPECIFIC FEEDBACK / WISH
   ↓
AI MODIFIES PROJECT
   ↓
PLAY / TEST AGAIN
   ↓
RUBRIC SELF-EVALUATION
   ↓
IDENTIFY WEAKEST AREA
   ↓
IMPLEMENT HIGH-IMPACT IMPROVEMENT
   ↓
RE-SCORE
   ↓
FINAL QUALITY CHECK
   ↓
SHIP / DEPLOY
```

### The Core Loop
```text
BUILD → PLAY → NOTICE → DESCRIBE → CHANGE → PLAY AGAIN → SCORE → IMPROVE → REPEAT
```

See [`workflow/workflow.md`](file:///d:/AI%20prompting%20in%202026/PROJECT%201%20Iterative%20Snake%20Battle%20Game%20+%20Prompting%20Workflow%20System/workflow/workflow.md) and [`workflow/improvement-loop.md`](file:///d:/AI%20prompting%20in%202026/PROJECT%201%20Iterative%20Snake%20Battle%20Game%20+%20Prompting%20Workflow%20System/workflow/improvement-loop.md) for full deep-dive documentation.

---

## 4. Game Features

* **Real-time Multi-Agent Battle**: Compete against 1 to 4 computer-controlled AI snakes in a shared 30x30 arena.
* **Distinct AI Personalities**:
  * *Balanced*: Efficient fruit seeker with balanced perimeter margins.
  * *Aggressive*: Actively hunts player snakes and ambushes corpse fruit drops.
  * *Cautious*: Prioritizes defensive wall clearance and evades close opponent heads.
* **Rule 5 (Dead Snake → Fruit Mechanic)**:
  ```text
  DEAD SNAKE
       ↓
  BODY SEGMENTS
       ↓
  CONVERT INTO FRUIT
       ↓
  OTHER SNAKES CAN EAT THEM
  ```
  Whenever any snake hits a wall or another snake's body, 100% of its body segments immediately materialize into glowing golden/colored fruit orbs (15 points each), sparking a feeding frenzy.
* **Pre-Game Customization Lobby**:
  * Real-time Snake Color Picker + preset neon skins.
  * Fruit Color Picker + preset harvest orbs.
  * Opponent Count Selector (1, 2, 3, or 4).
  * Speed Mode Selector: **Easy** (140ms), **Normal** (105ms), **Fast** (75ms), **Frenzy** (48ms).
* **Game Controls & UI**:
  * HUD Stats: **SCORE**, **BEST**, **LENGTH**, **TIME**, **OPPONENTS**, **SPEED**.
  * Action controls: **PAUSE / RESUME**, **SOUND (Mute / Unmute)**, **RESTART**.
  * Multi-Input Steering: Arrow Keys, WASD, and large responsive touch D-Pad (`↑`, `←`, `↓`, `→`).
* **Web Audio API Synthesizer**: Zero external audio dependencies. Generates retro-futuristic sound effects for fruit bites, collision explosions, and victory fanfares directly through browser oscillator synthesis.
* **Juice & Visual FX**: Screen shake, glowing snake eyes, trail alpha gradients, and canvas particle explosions upon impact.

---

## 5. Complete Project Structure

```text
PROJECT-1-AI-PROMPTING-2026/
│
├── README.md                      # Comprehensive project manual
├── main.py                        # Python CLI entry point
├── requirements.txt               # Minimal dependency specification
├── .gitignore                     # Git exclusion rules
│
├── app/                           # Core Python application package
│   ├── __init__.py
│   ├── game/                      # Snake game logic & simulation
│   │   ├── __init__.py
│   │   ├── game_state.py          # State orchestrator & simulation
│   │   ├── snake.py               # Snake entity & Rule 5 corpse conversion
│   │   ├── player.py              # Human-controlled snake
│   │   ├── ai_snake.py            # AI opponents (Balanced, Aggressive, Cautious)
│   │   ├── fruit.py               # Fruit spawning & corpse orbs
│   │   ├── collision.py           # Wall, self, & opponent collisions
│   │   ├── scoring.py             # Score tracker & high scores
│   │   └── game_loop.py           # Headless simulation loop
│   │
│   ├── prompting/                 # Prompting workflow & self-evaluation system
│   │   ├── __init__.py
│   │   ├── prompt_manager.py      # Prompt library reader
│   │   ├── iteration.py           # Iteration log & history model
│   │   ├── feedback.py            # Playtesting feedback tracker
│   │   └── rubric.py              # 7-dimension rubric evaluator
│   │
│   └── config/                    # Settings & arena constants
│       ├── __init__.py
│       └── settings.py
│
├── web/                           # Playable Web Game (HTML5 Canvas + Web Audio)
│   ├── index.html                 # Arena markup, start screen, HUD & D-Pad
│   ├── style.css                  # Cyberpunk neon glassmorphism stylesheet
│   └── script.js                  # Game loop, AI, Rule 5, Audio synthesizer
│
├── prompts/                       # Canonical 2026 Prompt Library
│   ├── 01_initial_prompt.md       # Step 1: Initial Snake request
│   ├── 02_customization_prompt.md # Step 2: Customization prompt
│   ├── 03_battle_prompt.md        # Step 3: AI Battle & Rule 5 prompt
│   ├── 04_feedback_prompt.md      # Step 4: Playtesting feedback prompt
│   ├── 05_rubric_prompt.md        # Step 5: Rubric evaluation prompt
│   └── 06_improvement_prompt.md   # Step 6: Improvement & re-scoring prompt
│
├── workflow/                      # Prompting Methodology Documentation
│   ├── workflow.md                # 12-step methodology breakdown
│   ├── workflow-diagram.md        # Architecture & state progression
│   └── improvement-loop.md        # Build -> Play -> Notice -> Change loop
│
├── evidence/                      # Historical Development & Evaluation Logs
│   ├── initial-build.md           # Baseline MVP logs
│   ├── iteration-01.md            # Lobby customization logs
│   ├── iteration-02.md            # Battle royale & Rule 5 logs
│   ├── iteration-03.md            # Playtesting feedback fix logs
│   ├── iteration-04.md            # Rubric optimization & audio logs
│   ├── rubric-results.md          # Multi-dimensional score delta table
│   └── final-validation.md        # Verification and audit checklist
│
├── tests/                         # Automated Unit Tests
│   ├── __init__.py
│   ├── test_snake.py              # Movement, growth, Rule 5 tests
│   ├── test_fruit.py              # Spawning & corpse fruit tests
│   ├── test_collision.py          # Wall, self, & opponent collision tests
│   ├── test_scoring.py            # Points & elimination tests
│   └── test_prompting_workflow.py # Rubric, iteration, & prompt tests
│
└── assets/                        # Standalone Assets
    └── diagrams/
        └── prompting-workflow.svg # Vector workflow diagram
```

---

## 6. Workflow Diagram

A standalone high-resolution SVG diagram is located at:
[`assets/diagrams/prompting-workflow.svg`](file:///d:/AI%20prompting%20in%202026/PROJECT%201%20Iterative%20Snake%20Battle%20Game%20+%20Prompting%20Workflow%20System/assets/diagrams/prompting-workflow.svg)

```text
┌─────────────────────┐
│      USER GOAL      │
└──────────┬──────────┘
           ↓
┌─────────────────────┐
│   INITIAL PROMPT    │
└──────────┬──────────┘
           ↓
┌─────────────────────┐
│    AI BUILDS V1     │
└──────────┬──────────┘
           ↓
┌─────────────────────┐
│     PLAY / TEST     │◄──────────────┐
└──────────┬──────────┘               │
           ↓                          │
┌─────────────────────┐               │
│ OBSERVE EXPERIENCE  │               │
└──────────┬──────────┘               │
           ↓                          │
┌─────────────────────┐               │
│ SPECIFIC FEEDBACK   │               │
└──────────┬──────────┘               │
           ↓                          │
┌─────────────────────┐               │
│    AI BUILDS V2     │               │
└──────────┬──────────┘               │
           ↓                          │
┌─────────────────────┐               │
│   RUBRIC SCORING    │               │
└──────────┬──────────┘               │
           ↓                          │
┌─────────────────────┐               │
│ FIND WEAKEST AREA   │               │
└──────────┬──────────┘               │
           ↓                          │
┌─────────────────────┐               │
│ HIGH-IMPACT FIX     │               │
└──────────┬──────────┘               │
           │                          │
           └───────────────┐          │
                           ↓          │
                    ┌──────────────┐  │
                    │  RE-SCORE    │  │
                    └──────┬───────┘  │
                           │          │
                           └──── LOOP ┘
                           (If below threshold)
                           │
                           ▼
                    ┌──────────────┐
                    │ SHIP / DEPLOY│
                    └──────────────┘
```

---

## 7. Prompt Iterations

The canonical sequence of prompts created during development is organized under [`prompts/`](file:///d:/AI%20prompting%20in%202026/PROJECT%201%20Iterative%20Snake%20Battle%20Game%20+%20Prompting%20Workflow%20System/prompts):

1. **`01_initial_prompt.md`**: Initial baseline request:
   ```text
   Let's build and play a game where a snake eats fruit balls to grow.
   ```
2. **`02_customization_prompt.md`**: Customization feedback:
   ```text
   Can I pick my snake's color before the game starts?
   ```
3. **`03_battle_prompt.md`**: Rule pivot & battle mechanics:
   ```text
   Now make it a battle: add computer-controlled snakes,
   and when a snake dies its body turns into fruit
   the others can eat.
   ```
4. **`04_feedback_prompt.md`**: Numbered surgical playtesting feedback:
   ```text
   I played the game and found these issues:
   1. The opponents are difficult to distinguish.
   2. The first fruit appears too slowly.
   3. The death animation is unclear.
   Fix all three issues.
   ```
5. **`05_rubric_prompt.md`**: Rubric scoring & weakest-area isolation:
   ```text
   Score this game from 1-10 on:
   1. Gameplay clarity, 2. Fun factor, 3. Difficulty curve, 4. Visual polish, 5. Game feel
   Give one sentence explaining each score.
   Then identify the weakest score and explain the single change that would improve it the most.
   ```
6. **`06_improvement_prompt.md`**: Closed-loop refinement & human decision authority:
   ```text
   Implement the highest-impact improvements from the rubric.
   Then score the game again using exactly the same criteria.
   Compare the new results with the previous results.
   Continue improving until the project reaches the quality level required by the human reviewer.
   The human reviewer decides when to stop.
   ```

---

## 8. Rubric

The project is continuously evaluated across 7 standardized criteria (1 to 10 scale):

| Criterion | Baseline Score (V1) | Production Score (V4) | Delta | Description |
| :--- | :---: | :---: | :---: | :--- |
| **Gameplay Clarity** | 6 / 10 | **9 / 10** | +3 | Full stats HUD, opponent badges, distinct neon contrast |
| **Fun Factor** | 5 / 10 | **10 / 10** | +5 | Multi-agent combat with Rule 5 corpse fruit feeding frenzies |
| **Difficulty Curve** | 5 / 10 | **9 / 10** | +4 | 4 speed modes (Easy, Normal, Fast, Frenzy) & 1–4 AI opponents |
| **Visual Polish** | 4 / 10 | **9 / 10** | +5 | Cyberpunk neon aesthetic, glowing fruit cores, particle bursts |
| **Game Feel** | 4 / 10 | **9 / 10** | +5 | Web Audio API synthesizer for fruit eats, explosions, victory |
| **Responsiveness** | 7 / 10 | **9 / 10** | +2 | Zero-latency Arrow/WASD keys + responsive touch D-Pad |
| **Stability** | 8 / 10 | **10 / 10** | +2 | 100% passing test suite; zero runtime crashes |
| **OVERALL AVERAGE** | **5.57 / 10** | **9.29 / 10** | **+3.72** | *Substantial quality progression* |

---

## 9. Testing

Automated tests cover all core game physics, Rule 5 corpse conversion, AI behaviors, and workflow modules.

Run the test suite via standard python:
```bash
python -m unittest discover tests
```

Or run tests directly through `main.py`:
```bash
python main.py --test
```

---

## 10. Running the Python Project

The primary command line entry point is `main.py`:

```bash
python main.py
```

### CLI Menu Options:
1. **Run project validation**: Audits all 40+ files and directories.
2. **Show prompting workflow**: Displays the complete 12-step methodology guide.
3. **Show project structure**: Displays the annotated file directory tree.
4. **Run tests**: Executes unit tests across all game and prompting modules.
5. **Show rubric**: Compares baseline vs. production rubric scores and reports weakest areas.
6. **Show iteration history**: Prints the full chronological development log.
7. **Show prompt library**: Inspects all 6 canonical prompt files.
8. **Exit**: Closes the CLI.

---

## 11. Running the Web Game

The playable game runs in any modern browser without needing a build step, node modules, or local servers.

### How to Play:
1. Navigate to the `web/` directory.
2. Double-click or open `index.html` in your favorite web browser (Chrome, Edge, Firefox, Safari).
   ```bash
   # Or from command line:
   start web/index.html   # On Windows
   open web/index.html    # On macOS
   ```
3. Configure your snake color, fruit color, opponent count, and speed preset in the **SNAKE BATTLE** lobby.
4. Click **START BATTLE**!

### Controls:
* **Steer**: Arrow Keys (`↑`, `←`, `↓`, `→`) or `W`, `A`, `S`, `D`.
* **Touch Steering**: Tap the virtual D-Pad buttons below the canvas on mobile/tablet.
* **Pause / Resume**: Spacebar or `P`.
* **Sound Toggle**: `M` key or Sound button.
* **Restart**: `R` key or Restart button.

---

## 12. Deployment

Because the web game is built entirely with vanilla HTML, CSS, and modern JavaScript, it can be shipped and hosted anywhere as a static web application:

1. **GitHub Pages**:
   * Push the repository to GitHub.
   * In repository settings, navigate to **Pages** and set the source branch to root or `/web`.
2. **Netlify / Vercel**:
   * Drag and drop the `web/` folder into Netlify Drop, or connect the repository with publish directory set to `web`.
3. **Single-File Bundling**:
   * If desired, the CSS and JS can be inlined directly inside `web/index.html` to create a 100% self-contained portable HTML game file.

---

## License
MIT License &copy; 2026 AI Prompting in 2026 Project 1 Authors.
