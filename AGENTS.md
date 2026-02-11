# SDS Agent Operating Contract

This repository uses strict design-system generation rules.

## Non-negotiable build flow

1. Identify source recipe in Figma and record exact anchors (`fileKey`, `nodeId`, variant names).
2. Map layout to SDS composition + sections + forms rules.
3. Implement in React (`.tsx`) with `src/components` and `var(--sds-*)` only.
4. Validate against `docs/qa/sds-page-audit-checklist.md`.
5. If critical rule inputs cannot be verified, stop and request clarification (no silent assumptions).

## Definition of done

- No duplicate primitive controls outside `src/components`.
- Desktop/mobile parity follows selected SDS recipe.
- Tokens are used for all visual decisions.
- Recipe traceability is documented in `docs/recipes/`.
- No standalone page deliverables in raw `.html` + custom root `.css`.
- `knownGaps` is empty for final recipe deliverables.

