# SDS Recipes

This directory stores machine-readable page/block recipes used by agents.

## Required workflow

1. Select the closest source recipe from Figma (`Composition guide`, `Sections`, `Forms`, `Examples`).
2. Create or update a JSON recipe file that validates against `page-recipe.schema.json`.
3. Implement using `src/components` and `var(--sds-*)` tokens.
4. Run `docs/qa/sds-page-audit-checklist.md` and keep all items passing.

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

