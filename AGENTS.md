# SDS Agent Operating Contract

This repository uses strict design-system generation rules.

## Non-negotiable build flow

1. Normalize prompt into a `PageSpec` (`docs/specs/page-spec.schema.json`).
2. Resolve recipe with `scripts/resolve_recipe.py` and record exact Figma anchors (`fileKey`, `nodeId`, variant names).
3. Map layout to SDS composition + sections + forms rules.
4. Implement in React (`.tsx`) with `src/components` and `var(--sds-*)` only.
5. Validate against `docs/qa/sds-page-audit-checklist.md` and contract CI checks.
6. If critical rule inputs cannot be verified, stop and request clarification (no silent assumptions).

## Definition of done

- No duplicate primitive controls outside `src/components`.
- Desktop/mobile parity follows selected SDS recipe.
- Tokens are used for all visual decisions.
- Recipe traceability is documented in `docs/recipes/`.
- No standalone page deliverables in raw `.html` + custom root `.css`.
- `knownGaps` is empty for final recipe deliverables.
- Page files (`src/pages|src/app|src/screens`) do not use raw control tags directly.

