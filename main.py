#!/usr/bin/env python3
"""
PROJECT 1 — AI PROMPTING IN 2026
Interactive Snake Battle Game + Prompting Workflow System
Primary CLI Entry Point
"""

import os
import sys
import unittest
from pathlib import Path

# Ensure workspace root is in python path
WORKSPACE_ROOT = Path(__file__).resolve().parent
if str(WORKSPACE_ROOT) not in sys.path:
    sys.path.insert(0, str(WORKSPACE_ROOT))

from app.config.settings import Settings
from app.prompting.rubric import get_current_production_rubric, get_default_baseline_rubric
from app.prompting.iteration import IterationHistory
from app.prompting.prompt_manager import PromptManager


def show_banner():
    """Displays the Project 1 banner and system subtitle."""
    banner = f"""
============================================================
  {Settings.PROJECT_NAME}
============================================================
  {Settings.PROJECT_SUBTITLE}
  Version: {Settings.VERSION}  |  Platform: Python 3.8+ / HTML5 Canvas
============================================================
"""
    print(banner)


def validate_project_structure():
    """
    Verifies that all required directories, prompts, evidence, tests,
    and assets exist in the workspace.
    """
    print("\n--- RUNNING PROJECT STRUCTURE VALIDATION ---")
    
    required_files = [
        "README.md",
        "main.py",
        "requirements.txt",
        ".gitignore",
        "app/__init__.py",
        "app/config/__init__.py",
        "app/config/settings.py",
        "app/game/__init__.py",
        "app/game/snake.py",
        "app/game/player.py",
        "app/game/ai_snake.py",
        "app/game/fruit.py",
        "app/game/collision.py",
        "app/game/scoring.py",
        "app/game/game_state.py",
        "app/game/game_loop.py",
        "app/prompting/__init__.py",
        "app/prompting/rubric.py",
        "app/prompting/iteration.py",
        "app/prompting/feedback.py",
        "app/prompting/prompt_manager.py",
        "web/index.html",
        "web/style.css",
        "web/script.js",
        "prompts/01_initial_prompt.md",
        "prompts/02_customization_prompt.md",
        "prompts/03_battle_prompt.md",
        "prompts/04_feedback_prompt.md",
        "prompts/05_rubric_prompt.md",
        "prompts/06_improvement_prompt.md",
        "workflow/workflow.md",
        "workflow/workflow-diagram.md",
        "workflow/improvement-loop.md",
        "evidence/initial-build.md",
        "evidence/iteration-01.md",
        "evidence/iteration-02.md",
        "evidence/iteration-03.md",
        "evidence/iteration-04.md",
        "evidence/rubric-results.md",
        "evidence/final-validation.md",
        "tests/__init__.py",
        "tests/test_snake.py",
        "tests/test_fruit.py",
        "tests/test_collision.py",
        "tests/test_scoring.py",
        "tests/test_prompting_workflow.py",
        "assets/diagrams/prompting-workflow.svg"
    ]

    all_passed = True
    passed_count = 0

    for rel_path in required_files:
        full_path = WORKSPACE_ROOT / rel_path
        if full_path.exists():
            print(f"  [PASS] {rel_path}")
            passed_count += 1
        else:
            print(f"  [FAIL] Missing: {rel_path}")
            all_passed = False

    print("-" * 60)
    print(f"Validation Result: {passed_count}/{len(required_files)} files verified.")
    if all_passed:
        print("[SUCCESS] All core directories, files, and assets are present.\n")
    else:
        print("[WARNING] Missing files detected. Please review the output above.\n")
    return all_passed


def show_workflow():
    """Presents the 12-step prompting methodology and iterative loop."""
    workflow_file = WORKSPACE_ROOT / "workflow" / "workflow.md"
    if workflow_file.exists():
        print("\n" + workflow_file.read_text(encoding="utf-8") + "\n")
    else:
        print("\nWorkflow file not found at workflow/workflow.md\n")


def show_project_structure():
    """Prints the comprehensive project directory hierarchy."""
    structure_text = """
PROJECT-1-AI-PROMPTING-2026/
│
├── README.md                      # Complete project documentation & guide
├── main.py                        # Primary Python CLI entry point
├── requirements.txt               # Dependencies (standard library)
├── .gitignore                     # Git exclusions
│
├── app/                           # Core Python application package
│   ├── __init__.py
│   ├── game/                      # Snake game engine & battle rules
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
│   ├── 01_initial_prompt.md       # "Let's build and play a game..."
│   ├── 02_customization_prompt.md # "Can I pick my snake's color..."
│   ├── 03_battle_prompt.md        # "Now make it a battle: AI snakes + Rule 5..."
│   ├── 04_feedback_prompt.md      # "I played the game and found these issues..."
│   ├── 05_rubric_prompt.md        # "Score this game from 1-10 on..."
│   └── 06_improvement_prompt.md   # "Implement highest-impact improvements..."
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
"""
    print(structure_text)


def run_tests():
    """Runs the full unittest test suite."""
    print("\n--- EXECUTING TEST SUITE (tests/) ---")
    loader = unittest.TestLoader()
    suite = loader.discover(start_dir=str(WORKSPACE_ROOT / "tests"), pattern="test_*.py")
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    print("-" * 60)
    if result.wasSuccessful():
        print(f"[TEST PASS] All {result.testsRun} automated tests passed successfully!\n")
    else:
        print(f"[TEST FAIL] Failures: {len(result.failures)}, Errors: {len(result.errors)}\n")
    return result.wasSuccessful()


def show_rubric():
    """Displays the 7-dimension rubric comparison and weakest area report."""
    print("\n--- 1. BASELINE RUBRIC (Initial Build) ---")
    baseline = get_default_baseline_rubric()
    print(baseline.generate_report())

    print("\n--- 2. CURRENT PRODUCTION RUBRIC (Post-Iterations) ---")
    production = get_current_production_rubric()
    print(production.generate_report())
    print()


def show_iteration_history():
    """Presents the chronological iteration log showing prompt evolution."""
    history = IterationHistory()
    print("\n" + history.get_summary() + "\n")


def show_prompt_library():
    """Prints all 6 canonical prompts from the prompt library."""
    pm = PromptManager()
    print("\n" + pm.get_all_prompts_text() + "\n")


def print_menu():
    print("""
=============================================
 PROJECT 1 — AI PROMPTING 2026
=============================================

Interactive Snake Battle + Improvement Loop

1. Run project validation
2. Show prompting workflow
3. Show project structure
4. Run tests
5. Show rubric
6. Show iteration history
7. Show prompt library
8. Exit
""")


def main():
    show_banner()
    
    # If run in non-interactive mode with an argument
    if len(sys.argv) > 1:
        arg = sys.argv[1].lower()
        if arg in ("--validate", "-v", "1"):
            success = validate_project_structure()
            sys.exit(0 if success else 1)
        elif arg in ("--test", "-t", "4"):
            success = run_tests()
            sys.exit(0 if success else 1)
        elif arg in ("--workflow", "-w", "2"):
            show_workflow()
            sys.exit(0)
        elif arg in ("--structure", "-s", "3"):
            show_project_structure()
            sys.exit(0)
        elif arg in ("--rubric", "-r", "5"):
            show_rubric()
            sys.exit(0)
        elif arg in ("--history", "-h", "6"):
            show_iteration_history()
            sys.exit(0)

    # Interactive Loop
    while True:
        print_menu()
        choice = input("Select an option (1-8): ").strip()
        
        if choice == "1":
            validate_project_structure()
        elif choice == "2":
            show_workflow()
        elif choice == "3":
            show_project_structure()
        elif choice == "4":
            run_tests()
        elif choice == "5":
            show_rubric()
        elif choice == "6":
            show_iteration_history()
        elif choice == "7":
            show_prompt_library()
        elif choice in ("8", "exit", "q", "quit"):
            print("\nExiting Snake Battle Workflow System. Keep iterating!\n")
            break
        else:
            print("\n[Invalid Selection] Please choose a number between 1 and 8.\n")


if __name__ == "__main__":
    main()
