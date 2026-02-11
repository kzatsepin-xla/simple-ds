# SDS Recipes

This directory stores machine-readable page/block recipes used by agents.

## Required workflow

1. Parse prompt to `PageSpec` (`docs/specs/page-spec.schema.json`).
2. Resolve closest recipe with `python scripts/resolve_recipe.py <page-spec.json>`.
3. If needed, create or update a recipe JSON that validates against `page-recipe.schema.json`.
4. Implement in React (`.tsx`) using `src/components` and `var(--sds-*)` tokens.
5. Run `docs/qa/sds-page-audit-checklist.md` and keep all items passing.
6. Final recipe deliverables must keep `knownGaps` empty.

## Delivery constraints

- Do not deliver standalone page implementations as raw `.html` + custom root-level `.css`.
- Do not claim SDS component compliance when only CSS class contracts are copied into static markup.

## Minimal recipe file example

```json
{
  "id": "example.shop-page",
  "figma": {
    "fileKey": "RBJcfVy3QAUyfxSVRqPI1V",
    "canvasNodeId": "7641:2142",
    "recipeNodes": ["Examples/Shop", "Hero Basic", "Card Grid Pricing"]
  },
  "platforms": ["desktop", "mobile"],
  "sectionSequence": ["Header", "Hero", "CardGrid", "Panel", "Footer"],
  "componentUsage": ["Button", "Input", "Checkbox", "Text"],
  "responsiveRules": ["desktop-major-minor", "mobile-single-column"],
  "knownGaps": []
}
```

