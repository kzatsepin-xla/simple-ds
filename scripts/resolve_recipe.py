#!/usr/bin/env python3
"""Resolve the best SDS page recipe from a normalized PageSpec."""

from __future__ import annotations

import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RECIPES_DIR = ROOT / "docs" / "recipes"
SCHEMA_NAME = "page-recipe.schema.json"


def normalize(values: list[str]) -> set[str]:
    return {v.strip().lower() for v in values if isinstance(v, str) and v.strip()}


def score_recipe(spec: dict, recipe: dict) -> float:
    score = 0.0

    spec_sections = normalize(spec.get("sections", []))
    recipe_sections = normalize(recipe.get("sectionSequence", []))
    if spec_sections and recipe_sections:
        overlap = len(spec_sections & recipe_sections) / max(len(spec_sections), 1)
        score += overlap * 0.45

    spec_platforms = normalize(spec.get("platforms", []))
    recipe_platforms = normalize(recipe.get("platforms", []))
    if spec_platforms and recipe_platforms:
        overlap = len(spec_platforms & recipe_platforms) / max(len(spec_platforms), 1)
        score += overlap * 0.25

    spec_page_type = str(spec.get("pageType", "")).strip().lower()
    recipe_id = str(recipe.get("id", "")).strip().lower()
    if spec_page_type and spec_page_type in recipe_id:
        score += 0.15

    intent = str(spec.get("intent", "")).strip().lower()
    if intent:
        intent_terms = {term for term in intent.replace("/", " ").replace("-", " ").split() if term}
        recipe_terms = {term for term in recipe_id.replace("/", " ").replace("-", " ").split() if term}
        if intent_terms and recipe_terms:
            overlap = len(intent_terms & recipe_terms) / max(len(intent_terms), 1)
            score += overlap * 0.15

    return round(score, 4)


def load_recipes() -> list[dict]:
    recipes: list[dict] = []
    for path in RECIPES_DIR.glob("*.json"):
        if path.name == SCHEMA_NAME:
            continue
        data = json.loads(path.read_text(encoding="utf-8"))
        if isinstance(data, dict):
            data["_path"] = str(path.relative_to(ROOT).as_posix())
            recipes.append(data)
    return recipes


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: python scripts/resolve_recipe.py <page-spec.json>")
        return 1

    spec_path = Path(sys.argv[1]).resolve()
    if not spec_path.exists():
        print(f"ERROR: PageSpec file not found: {spec_path}")
        return 1

    spec = json.loads(spec_path.read_text(encoding="utf-8"))
    recipes = load_recipes()
    if not recipes:
        print("ERROR: No recipes found in docs/recipes/")
        return 1

    ranked = sorted(
        ((score_recipe(spec, recipe), recipe) for recipe in recipes),
        key=lambda item: item[0],
        reverse=True,
    )
    best_score, best_recipe = ranked[0]

    result = {
        "specPath": str(spec_path),
        "bestRecipePath": best_recipe.get("_path"),
        "bestRecipeId": best_recipe.get("id"),
        "score": best_score,
        "scoreThresholdMet": best_score >= 0.5,
    }
    print(json.dumps(result, ensure_ascii=True, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

