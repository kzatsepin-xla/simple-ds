# SDS Agent Operating Contract

This repository uses strict design-system generation rules.

## Non-negotiable build flow

1. Identify source recipe in Figma and record exact anchors (`fileKey`, `nodeId`, variant names).
2. Map layout to SDS composition + sections + forms rules.
3. Implement with `src/components` and `var(--sds-*)` only.
4. Validate against `docs/qa/sds-page-audit-checklist.md`.
5. If any rule cannot be verified, stop and record a TODO (no silent assumptions).

## Definition of done

- No duplicate primitive controls outside `src/components`.
- Desktop/mobile parity follows selected SDS recipe.
- Tokens are used for all visual decisions.
- Recipe traceability is documented in `docs/recipes/`.

