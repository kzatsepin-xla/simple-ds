## SDS Implementation PR

### What was implemented

- [ ] New page/block implementation
- [ ] Existing page/block update
- [ ] DS component update in `src/components`
- [ ] Recipe/rule update

### Figma traceability (required)

- File key:
- Canvas/page node id:
- Recipe/variant node names (desktop + mobile):

### Recipe contract

- [ ] Existing recipe was reused
- [ ] New recipe added in `docs/recipes/`
- Recipe file:
- PageSpec file:
- Resolver result (`scripts/resolve_recipe.py`):

### SDS compliance checklist (required)

- [ ] Uses SDS components (`src/components`) instead of duplicate primitives
- [ ] Page implementation is React (`.tsx`), no standalone `.html` + root `.css`
- [ ] Uses `var(--sds-*)` tokens for visual values
- [ ] Responsive behavior matches Composition/Sections recipe
- [ ] Forms follow fieldset/state model from SDS rules
- [ ] `docs/qa/sds-page-audit-checklist.md` completed with PASS

### Known gaps / explicit TODOs

- [ ] No known gaps
- [ ] Known gaps are documented below

Notes:

