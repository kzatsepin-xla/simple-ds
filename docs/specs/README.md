# SDS Page Specs

`PageSpec` is a normalized intent object that agents must create from any free-form prompt.

## Why this exists

- Free-text prompts are ambiguous.
- `PageSpec` ensures deterministic recipe selection and generation flow.
- It enables universal page generation across intents, not only pre-baked page names.

## Flow

1. Parse user prompt into `PageSpec`.
2. Resolve best matching recipe from `docs/recipes/*.json` via `scripts/resolve_recipe.py`.
3. If no strong match exists, create a new recipe from Figma-backed section rules.
4. Implement React page using `src/components` and `var(--sds-*)`.
5. Pass audit and contract validation.

## Resolver usage

```bash
python scripts/resolve_recipe.py docs/specs/<page-spec>.json
```

