#!/usr/bin/env python3
"""Minimal CI checks for SDS agent contract."""

from __future__ import annotations

import json
import re
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
    ".cursor/rules/sds-universal-page-generation.mdc",
    ".cursor/rules/sds-designer-friendly-prompts.mdc",
    "AGENTS.md",
    "docs/qa/sds-page-audit-checklist.md",
    "docs/recipes/page-recipe.schema.json",
    "docs/recipes/README.md",
    "docs/specs/page-spec.schema.json",
    "docs/specs/README.md",
    "scripts/resolve_recipe.py",
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

    if "knownGaps" in data:
        known_gaps = data.get("knownGaps")
        if not isinstance(known_gaps, list):
            fail(f"{rel_path}: knownGaps must be an array when present")
            ok = False
        elif len(known_gaps) > 0:
            fail(f"{rel_path}: knownGaps must be empty for final delivery")
            ok = False

    return ok


def validate_react_only_delivery() -> bool:
    ok = True
    forbidden_html = [
        p
        for p in (list(ROOT.glob("*.html")) + list(ROOT.glob("*.htm")))
        if p.name.lower() != "index.html"
    ]
    forbidden_css = list(ROOT.glob("*.css"))

    for path in sorted(forbidden_html):
        rel = path.relative_to(ROOT).as_posix()
        fail(f"Forbidden standalone HTML deliverable detected: {rel}")
        ok = False

    for path in sorted(forbidden_css):
        rel = path.relative_to(ROOT).as_posix()
        fail(f"Forbidden root-level CSS deliverable detected: {rel}")
        ok = False

    return ok


def page_base_name(page_path: Path) -> str:
    """Convert `GameWebshopPage.tsx` -> `game-webshop`."""
    stem = page_path.stem
    if stem.endswith("Page"):
        stem = stem[:-4]
    kebab = re.sub(r"(?<!^)(?=[A-Z])", "-", stem).lower()
    return kebab


def find_page_files() -> list[Path]:
    candidates: list[Path] = []
    patterns = [
        "src/pages/**/*.tsx",
        "src/app/**/*.tsx",
        "src/screens/**/*.tsx",
    ]
    for pattern in patterns:
        candidates.extend(ROOT.glob(pattern))
    return sorted({path for path in candidates if "src/components/" not in path.as_posix()})


def validate_page_contract_files() -> bool:
    page_files = find_page_files()
    if not page_files:
        print("Validated page contract files: 0 (no page files found; skipped)")
        return True

    ok = True
    for page_file in page_files:
        base = page_base_name(page_file)
        rel_page = page_file.relative_to(ROOT).as_posix()

        expected_css = page_file.with_suffix(".css")
        expected_spec = ROOT / "docs" / "specs" / f"{base}.page-spec.json"
        expected_recipe = ROOT / "docs" / "recipes" / f"{base}.catalog.json"
        expected_audit = ROOT / "docs" / "qa" / f"{base}-audit.md"

        for expected in [expected_css, expected_spec, expected_recipe, expected_audit]:
            if not expected.exists():
                fail(
                    f"{rel_page}: missing required page contract file "
                    f"{expected.relative_to(ROOT).as_posix()}"
                )
                ok = False

    print(f"Validated page contract files: {len(page_files)}")
    return ok


def validate_react_pages_use_ds() -> bool:
    page_files = find_page_files()
    if not page_files:
        print("Validated page TSX files: 0 (no page files found; skipped)")
        return True

    ok = True
    raw_control_pattern = re.compile(r"<\s*(button|input|select|textarea)\b", re.IGNORECASE)
    ds_import_pattern = re.compile(r"from\s+['\"][^'\"]*components[^'\"]*['\"]")
    h1_pattern = re.compile(r"<\s*h1\b", re.IGNORECASE)
    title_page_component_pattern = re.compile(
        r"<[A-Za-z0-9_]*Text[^>]*variant=\"titlePage\"[^>]*>",
        re.IGNORECASE,
    )

    for path in page_files:
        rel = path.relative_to(ROOT).as_posix()
        text = path.read_text(encoding="utf-8")

        if raw_control_pattern.search(text):
            fail(f"{rel}: raw form/control tags detected in page file; use SDS components")
            ok = False

        if not ds_import_pattern.search(text):
            fail(f"{rel}: no components import detected; page must compose SDS components")
            ok = False

        explicit_h1_count = len(h1_pattern.findall(text))
        if explicit_h1_count > 1:
            fail(f"{rel}: multiple <h1> tags detected")
            ok = False

        title_page_nodes = title_page_component_pattern.findall(text)
        title_page_without_as = sum(1 for node in title_page_nodes if " as=" not in node and " as =" not in node)
        if title_page_without_as > 1:
            fail(
                f"{rel}: multiple titlePage text components without explicit `as` prop "
                "(default becomes multiple h1)"
            )
            ok = False

    print(f"Validated page TSX files: {len(page_files)}")
    return ok


def validate_page_css_composition() -> bool:
    page_files = find_page_files()
    if not page_files:
        print("Validated page CSS composition: 0 (no page files found; skipped)")
        return True

    ok = True
    required_patterns = [
        re.compile(r"1200px|max-width:\s*1200", re.IGNORECASE),
        re.compile(r"768px|max-width:\s*768", re.IGNORECASE),
        re.compile(r"375px|max-width:\s*375", re.IGNORECASE),
        re.compile(r"1152px|720px|327px", re.IGNORECASE),
        re.compile(r"24px|space-600|padding-xl", re.IGNORECASE),
    ]

    for page_file in page_files:
        css_file = page_file.with_suffix(".css")
        rel = css_file.relative_to(ROOT).as_posix()
        if not css_file.exists():
            # covered by validate_page_contract_files
            continue
        css_text = css_file.read_text(encoding="utf-8")
        for pattern in required_patterns:
            if not pattern.search(css_text):
                fail(
                    f"{rel}: missing composition invariant for pattern `{pattern.pattern}` "
                    "(check container widths/gutters/content math)"
                )
                ok = False

    print(f"Validated page CSS composition: {len(page_files)}")
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
    checks = [
        require_files(),
        validate_recipes(),
        validate_react_only_delivery(),
        validate_page_contract_files(),
        validate_react_pages_use_ds(),
        validate_page_css_composition(),
    ]
    if all(checks):
        print("SDS contract validation passed.")
        return 0
    print("SDS contract validation failed.")
    return 1


if __name__ == "__main__":
    sys.exit(main())

