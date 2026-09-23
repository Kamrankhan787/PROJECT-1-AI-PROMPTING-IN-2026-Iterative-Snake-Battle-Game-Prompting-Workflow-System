# The 2026 AI Prompting Methodology: 12-Step Workflow

In 2026, building software with generative AI has evolved far beyond writing a monolithic prompt and praying for a finished product. Superior results are achieved through **iterative, experience-first co-creation**, treating software artifacts as living systems shaped through play, observation, structured scoring, and continuous refinement.

This document details the canonical 12-step prompting methodology demonstrated in Project 1.

---

## The 12-Step Framework

### Step 1: Start with an Experience
Do not begin by writing an exhaustive 50-page software requirements specification. Instead, define the core visceral experience you want to create or test.
* *Example*: "Let's build and play a game where a snake eats fruit balls to grow."
* *Why it works*: It minimizes cognitive overhead and gets a runnable artifact into your hands in seconds.

### Step 2: Build the First Version
Direct the AI to construct the minimal viable interactive artifact. Keep constraints focused on foundational physics, loop execution, and core interactivity.
* *Output*: A functioning web canvas with snake movement, single fruit rendering, and simple boundary checking.

### Step 3: Play the Result
Immediately interact with the generated artifact. Do not just read the code—run it, press the keys, click the buttons, test edge cases, and experience the tactile reality of the software.

### Step 4: Notice What You Wish Were Different
Pay close attention to your instinctual reactions during play:
* Where does the game feel dull or frustrating?
* What visual cues are missing?
* What custom options would make it feel personalized?

### Step 5: Give Specific Feedback
Translate your subjective impressions into crisp, actionable, unambiguous instructions. Avoid vague statements like "make it cooler."
* *Example*: "Can I pick my snake's color before the game starts?"

### Step 6: Modify the Artifact
Instruct the AI to apply surgical changes while preserving existing working functionality. Verify that new UI controls (such as color inputs or speed selectors) integrate smoothly.

### Step 7: Change Rules When Necessary
Software design is not static. If the original mechanics hit an engagement ceiling, pivot the rules to create emergent excitement.
* *The Snake Battle Pivot*: "Now make it a battle: add computer-controlled snakes, and when a snake dies its body turns into fruit the others can eat."
* *Emergent Fun*: Transforming dead opponents into harvestable resources immediately creates dynamic risk/reward tension.

### Step 8: Score the Result
Step back from unstructured play and conduct an objective multi-dimensional self-evaluation. Use a standardized rubric evaluating:
1. Gameplay Clarity
2. Fun Factor
3. Difficulty Curve
4. Visual Polish
5. Game Feel
6. Responsiveness
7. Stability

### Step 9: Identify the Weakest Area
Analyze the score breakdown to find the lowest-scoring dimension.
* *The Leverage Principle*: Elevating the weakest criterion (e.g., raising Visual Polish from 4/10 to 8/10) produces a dramatically higher perceived quality leap than tweaking an already strong area.

### Step 10: Implement the Highest-Impact Improvement
Formulate a targeted prompt specifically addressing the bottleneck identified in Step 9.
* *Example*: Adding glowing neon aesthetics, responsive touch controls, and Web Audio synthesized sound effects to address Visual Polish and Game Feel.

### Step 11: Re-Score
Re-evaluate the artifact using the exact same rubric criteria.
* Compare pre- and post-iteration scores.
* Verify that the intended dimension improved without regressing stability or responsiveness.

### Step 12: Decide When the Project Is Ready (Human Reviewer Authority)
AI models must never be permitted to unilaterally declare a project "finished." The human developer/player holds exclusive authority to declare when quality standards have been satisfied and the project is ready to ship and deploy.

---

## Summary Diagram

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
