"""
Prompt manager responsible for loading, formatting, and presenting prompts
from the canonical 2026 prompting sequence.
"""

import os
from pathlib import Path
from typing import Dict, List, Optional


class PromptManager:
    """Manages the library of 6 core prompts that guide project evolution."""

    PROMPT_FILES = [
        ("01", "01_initial_prompt.md", "Initial Snake request"),
        ("02", "02_customization_prompt.md", "Color & appearance customization"),
        ("03", "03_battle_prompt.md", "AI battle rules & dead-snake corpse fruit"),
        ("04", "04_feedback_prompt.md", "Playtesting feedback resolution"),
        ("05", "05_rubric_prompt.md", "Rubric self-scoring & weakest area detection"),
        ("06", "06_improvement_prompt.md", "High-impact refinement & re-scoring loop")
    ]

    def __init__(self, prompts_dir: Optional[str] = None):
        if prompts_dir is None:
            # Default to prompts/ folder at project root
            base_dir = Path(__file__).resolve().parent.parent.parent
            self.prompts_dir = base_dir / "prompts"
        else:
            self.prompts_dir = Path(prompts_dir)

    def get_prompt_content(self, filename: str) -> str:
        filepath = self.prompts_dir / filename
        if filepath.exists():
            return filepath.read_text(encoding="utf-8")
        return f"[Error: Prompt file '{filename}' not found at {filepath}]"

    def list_prompts(self) -> List[Dict[str, str]]:
        result = []
        for step, filename, desc in self.PROMPT_FILES:
            filepath = self.prompts_dir / filename
            exists = filepath.exists()
            result.append({
                "step": step,
                "filename": filename,
                "description": desc,
                "exists": exists,
                "path": str(filepath)
            })
        return result

    def get_all_prompts_text(self) -> str:
        lines = [
            "=" * 60,
            " AI PROMPTING 2026 - CANONICAL PROMPT LIBRARY",
            "=" * 60
        ]
        for p in self.list_prompts():
            lines.append(f"Prompt #{p['step']}: {p['filename']} ({p['description']})")
            content = self.get_prompt_content(p['filename'])
            lines.append("-" * 40)
            lines.append(content.strip())
            lines.append("-" * 60)
        return "\n".join(lines)
