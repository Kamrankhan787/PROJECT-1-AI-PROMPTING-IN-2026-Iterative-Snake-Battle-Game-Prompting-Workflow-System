# Prompting Workflow Architecture & Diagram

This document illustrates the iterative loop architecture that powers modern AI-assisted engineering. Software improvement in 2026 is fundamentally cyclical rather than linear.

---

## Visual Workflow Diagram

```text
┌───────────────────────────────────────────────┐
│                   USER GOAL                   │
└───────────────────────┬───────────────────────┘
                        │
                        ▼
┌───────────────────────────────────────────────┐
│                INITIAL PROMPT                 │
└───────────────────────┬───────────────────────┘
                        │
                        ▼
┌───────────────────────────────────────────────┐
│                 AI BUILDS V1                  │
└───────────────────────┬───────────────────────┘
                        │
                        ▼
┌───────────────────────────────────────────────┐
│                  PLAY / TEST                  │◄──────────────┐
└───────────────────────┬───────────────────────┘               │
                        │                                       │
                        ▼                                       │
┌───────────────────────────────────────────────┐               │
│              OBSERVE EXPERIENCE               │               │
└───────────────────────┬───────────────────────┘               │
                        │                                       │
                        ▼                                       │
┌───────────────────────────────────────────────┐               │
│               SPECIFIC FEEDBACK               │               │
└───────────────────────┬───────────────────────┘               │
                        │                                       │
                        ▼                                       │
┌───────────────────────────────────────────────┐               │
│                 AI BUILDS V2                  │               │
└───────────────────────┬───────────────────────┘               │
                        │                                       │
                        ▼                                       │
┌───────────────────────────────────────────────┐               │
│                RUBRIC SCORING                 │               │
└───────────────────────┬───────────────────────┘               │
                        │                                       │
                        ▼                                       │
┌───────────────────────────────────────────────┐               │
│              FIND WEAKEST AREA                │               │
└───────────────────────┬───────────────────────┘               │
                        │                                       │
                        ▼                                       │
┌───────────────────────────────────────────────┐               │
│                HIGH-IMPACT FIX                │               │
└───────────────────────┬───────────────────────┘               │
                        │                                       │
                        └───────────────┐                       │
                                        ▼                       │
                                ┌──────────────┐                │
                                │   RE-SCORE   │                │
                                └───────┬──────┘                │
                                        │                       │
                                        └────────── LOOP ───────┘
                                                (If below threshold)
                                        │
                                        ▼
                                ┌──────────────┐
                                │ HUMAN REVIEW │
                                │ & SHIP / DEPLOY
                                └──────────────┘
```

---

## Mermaid State Progression

```mermaid
flowchart TD
    UG([User Goal]) --> IP[Initial Prompt]
    IP --> BV1[AI Builds V1]
    BV1 --> PT[Play / Test]
    
    subgraph IterationLoop [Continuous Improvement Cycle]
        PT --> OE[Observe Experience]
        OE --> SF[Specific Feedback / Wish]
        SF --> BV2[AI Modifies Artifact]
        BV2 --> RS[Rubric Self-Evaluation]
        RS --> FWA[Find Weakest Area]
        FWA --> HIF[Implement High-Impact Fix]
        HIF --> RES[Re-Score Criteria]
        RES --> CHK{Human Reviewer<br/>Satisfied?}
        CHK -- No: Continue Refining --> PT
    end
    
    CHK -- Yes: Ready to Ship --> SHIP([Ship / Deploy Static Web App])

    classDef primary fill:#00ff88,stroke:#00aa55,stroke-width:2px,color:#000;
    classDef loop fill:#1a1e29,stroke:#00d4ff,stroke-width:2px,color:#fff;
    classDef decision fill:#ff0055,stroke:#ff5588,stroke-width:2px,color:#fff;
    class UG,SHIP primary;
    class PT,OE,SF,BV2,RS,FWA,HIF,RES loop;
    class CHK decision;
```

---

## Key Takeaways

1. **Anti-Waterfall**: No single prompt, however elaborate, can anticipate real human gameplay feel. Iteration is the primary driver of quality.
2. **Looping Mechanism**: The transition from `RE-SCORE` back to `PLAY / TEST` prevents premature stagnation and catches regressions early.
3. **Dedicated SVG Asset**: For standalone visual documentation, reference the vector graphic at `assets/diagrams/prompting-workflow.svg`.
