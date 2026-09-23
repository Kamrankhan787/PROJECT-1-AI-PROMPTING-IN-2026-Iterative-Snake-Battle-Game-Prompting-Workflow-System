# Evidence: Iteration 01 (Customization & Pre-Game Lobby)

## Objective
Provide user agency over aesthetics before entering gameplay to elevate initial visual ownership and engagement.

## Prompt Used
```text
Can I pick my snake's color before the game starts?
```

## Observed Result
* A start screen was introduced with title **SNAKE BATTLE** and subtitle **Grow. Survive. Outplay.**
* Color input selectors for Snake Color and Fruit Color.
* "START BATTLE" button transitions from configuration screen to active game canvas.

## Problem Discovered
* While visual identity was resolved, the core loop remained a solitary, isolated snake eating solitary apples.
* Lacked tactical drama, adversary interference, and risk-reward pacing.

## Change Requested
Pivot mechanics to a competitive arena: introduce computer-controlled AI snakes and transform defeated snakes into fruit corpses for survivors to feast upon.

## Change Implemented
Drafted battle system design:
* Integrated AI snake controllers.
* Formulated Rule 5: Dead snake body segments convert into high-yield fruit orbs.

## Validation
* Tested color pickers across various hex combinations (`#00ff88`, `#ff0055`, `#00d4ff`).
* Canvas successfully re-rendered snake and fruit sprites in real-time according to picked colors.
