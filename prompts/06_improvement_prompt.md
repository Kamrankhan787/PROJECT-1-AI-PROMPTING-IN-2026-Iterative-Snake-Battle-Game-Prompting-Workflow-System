# Step 6: Improvement & Re-scoring Prompt

## Human Prompt
```text
Implement the highest-impact improvements from the rubric.

Then score the game again using exactly the same criteria.

Compare the new results with the previous results.

Continue improving until the project reaches the quality
level required by the human reviewer.

The human reviewer decides when to stop.
```

## Prompt Engineering Context (2026 Methodology)
* **Goal**: Closed-loop iterative refinement and human-in-the-loop completion.
* **Key Concept**: "Re-score and iterate until human approval." The system measures progress before and after each intervention. Crucially, the model does not declare completion on its own: the human retains final quality authority and determines when the artifact is ready to ship.
* **Expected Output**:
  - Implementation of targeted improvements identified in the rubric evaluation.
  - Comparative re-scoring table demonstrating delta improvements.
  - Presentation to the human reviewer for final release decision.
