# Simple DS

Simple DS is a React component library generated from the SDS Figma UI kit.

## Goals

- Extract component structure, variants, and tokens from Figma MCP
- Build reusable React + TypeScript components
- Use CSS custom properties for theming via `--sds-*` tokens

## Planned Components

- Button
- Input
- Text
- Checkbox
- Switch

## AI Layout Rules

Cursor rules are stored in `.cursor/rules/` and are derived from the SDS Figma pages:

- `Composition guide` for responsive grid composition
- `Sections` for reusable section families and platform variants
- `Forms` for fieldset and form assembly patterns
- `Examples` for full-page recipe selection

## Quality Gates

- Agent operating contract: `AGENTS.md`
- Universal page generation rule: `.cursor/rules/sds-universal-page-generation.mdc`
- Prompt normalization schema: `docs/specs/page-spec.schema.json`
- Recipe resolver: `scripts/resolve_recipe.py`
- Recipe format and workflow: `docs/recipes/README.md`
- Recipe schema: `docs/recipes/page-recipe.schema.json`
- Mandatory page audit checklist: `docs/qa/sds-page-audit-checklist.md`
- PR template enforcing SDS traceability: `.github/pull_request_template.md`
- CI contract validator: `.github/workflows/ds-contract.yml`
- Delivery mode: React-only (`.tsx`), no standalone page `.html` + root `.css`
