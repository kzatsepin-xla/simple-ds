#!/usr/bin/env python3
"""Minimal CI checks for SDS agent contract."""

from __future__ import annotations

import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

REQUIRED_FILES = [
    ".cursor/rules/sds-composition-guide.mdc",
    ".cursor/rules/sds-sections-assembly.mdc",
    ".cursor/rules/sds-forms-and-blocks.mdc",
    ".cursor/rules/sds-page-recipes-from-examples.mdc",
    ".cursor/rules/sds-no-assumptions-gate.mdc",
    ".cursor/rules/sds-component-usage-enforcement.mdc",
    "AGENTS.md",
    "docs/qa/sds-page-audit-checklist.md",
    "docs/recipes/page-recipe.schema.json",
    "docs/recipes/README.md",
]


def fail(message: str) -> None:
    print(f"ERROR: {message}")


def require_files() -> bool:
    ok = True
    for rel in REQUIRED_FILES:
        if not (ROOT / rel).exists():
            fail(f"Missing required contract file: {rel}")
            ok = False
    return ok


def validate_recipe_object(data: dict, rel_path: str) -> bool:
    ok = True
    required_top = [
        "id",
        "figma",
        "platforms",
        "sectionSequence",
        "componentUsage",
        "responsiveRules",
    ]
    for key in required_top:
        if key not in data:
            fail(f"{rel_path}: missing key '{key}'")
            ok = False

    if not isinstance(data.get("id"), str) or len(data.get("id", "")) < 3:
        fail(f"{rel_path}: 'id' must be a non-empty string")
        ok = False

    figma = data.get("figma")
    if not isinstance(figma, dict):
        fail(f"{rel_path}: 'figma' must be an object")
        return False

    for key in ["fileKey", "canvasNodeId", "recipeNodes"]:
        if key not in figma:
            fail(f"{rel_path}: figma.{key} is required")
            ok = False

    if not isinstance(figma.get("fileKey"), str) or not figma.get("fileKey"):
        fail(f"{rel_path}: figma.fileKey must be a string")
        ok = False

    if not isinstance(figma.get("canvasNodeId"), str) or not figma.get("canvasNodeId"):
        fail(f"{rel_path}: figma.canvasNodeId must be a string")
        ok = False

    recipe_nodes = figma.get("recipeNodes")
    if not isinstance(recipe_nodes, list) or not recipe_nodes or not all(
        isinstance(x, str) and x for x in recipe_nodes
    ):
        fail(f"{rel_path}: figma.recipeNodes must be a non-empty string array")
        ok = False

    for list_key in ["platforms", "sectionSequence", "componentUsage", "responsiveRules"]:
        value = data.get(list_key)
        if not isinstance(value, list) or not value or not all(isinstance(x, str) and x for x in value):
            fail(f"{rel_path}: '{list_key}' must be a non-empty string array")
            ok = False

    platforms = data.get("platforms", [])
    allowed = {"desktop", "tablet", "mobile"}
    if isinstance(platforms, list) and any(p not in allowed for p in platforms):
        fail(f"{rel_path}: platforms must only contain desktop/tablet/mobile")
        ok = False

    return ok


def validate_recipes() -> bool:
    recipe_dir = ROOT / "docs" / "recipes"
    if not recipe_dir.exists():
        fail("Missing docs/recipes directory")
        return False

    recipe_files = [
        p for p in recipe_dir.glob("*.json") if p.name != "page-recipe.schema.json"
    ]

    ok = True
    for recipe in recipe_files:
        rel = recipe.relative_to(ROOT).as_posix()
        try:
            data = json.loads(recipe.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            fail(f"{rel}: invalid JSON ({exc})")
            ok = False
            continue

        if not isinstance(data, dict):
            fail(f"{rel}: root JSON value must be an object")
            ok = False
            continue

        ok = validate_recipe_object(data, rel) and ok

    print(f"Validated recipe files: {len(recipe_files)}")
    return ok


def main() -> int:
    checks = [require_files(), validate_recipes()]
    if all(checks):
        print("SDS contract validation passed.")
        return 0
    print("SDS contract validation failed.")
    return 1


if __name__ == "__main__":
    sys.exit(main())

