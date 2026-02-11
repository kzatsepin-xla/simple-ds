# SDS Page Audit Checklist

Use this checklist before considering any page/block implementation complete.

## 1) Recipe traceability

- [ ] Figma file key recorded
- [ ] Canvas/page node IDs recorded
- [ ] Recipe/variant names recorded for desktop and mobile
- [ ] Section sequence mapped to SDS section families

## 2) Composition fidelity

- [ ] Container width and gutters match Composition guide
- [ ] Desktop/tablet/mobile behavior matches selected recipe
- [ ] No contradictory breakpoint logic

## 3) Component fidelity

- [ ] Uses SDS components from `src/components` (no duplicate primitives)
- [ ] Form controls use SDS state/variant model
- [ ] Text uses SDS text variants

## 4) Token fidelity

- [ ] Colors use `var(--sds-color-*)`
- [ ] Spacing/sizing uses `var(--sds-size-*)`
- [ ] Typography uses `var(--sds-typography-*)`
- [ ] No unexplained hardcoded visual values

## 5) Delivery gate

- [ ] All checklist sections pass
- [ ] Known gaps explicitly listed as TODO with reason
- [ ] No unresolved assumptions remain

