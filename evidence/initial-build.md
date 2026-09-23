# Evidence: Initial Build (Iteration 0)

## Objective
Establish a runnable baseline Snake game in minimal time so interactive human playtesting can begin immediately.

## Prompt Used
```text
Let's build and play a game where a snake eats fruit balls to grow.
```

## Observed Result
* An HTML canvas element rendering an emerald green snake of length 4.
* Arrow key keyboard handlers controlling direction (Up, Down, Left, Right).
* Single red circle fruit spawning randomly on a 30x30 grid.
* When the snake collides with the fruit, score increases by 10 and length increases by 1.
* Hitting boundary walls or self-body triggers an abrupt reset.

## Problem Discovered
* Visuals are generic and unbranded.
* No way to personalize snake appearance or customize the arena.
* Single-player survival quickly becomes repetitive without competition or adversary pressure.
* Reset is jarring without a start menu or pause state.

## Change Requested
Enable user customization before entering the game loop: allow custom player color selection and fruit color configuration.

## Change Implemented
Constructed the initial lobby UI with interactive color pickers and game state transition machine (`MENU` -> `PLAYING`).

## Validation
* Successfully ran in browser: HTML canvas rendered cleanly at 60 FPS.
* Keyboard inputs responded instantaneously.
* Confirmed baseline score counter incremented correctly upon fruit collision.
