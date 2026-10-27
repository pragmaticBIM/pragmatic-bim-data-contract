---
search:
  boost: 5.0
---

# Slot: related_product 


_Optional catalog product this deliverable implements or this cost record is priced from._



<div data-search-exclude markdown="1">



URI: [pbs:related_product](https://schema.pragmaticbim.ch/related_product)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Deliverable](Deliverable.md) | Outcome or handover item produced within a project. |  yes  |
| [CostRecord](CostRecord.md) | Cost record for estimation, catalog pricing, and calculation. Use cost_record_role to distinguish catalog cost/price (on Product) from project estimate/actual lines. Populate component_cost_items to act as an assembly (aggregated unit price). Either amount (lump sum) or unit_cost (rate per cost quantity) must be present. The cost stage (early_estimate, approved_budget, contract_amendment, expectation) is a Classification entry with classification_scheme cost-stages; a record with cost_record_role estimate carries at most one cost-stages classification. Cost-stage mappings (SKOS closeMatch unless noted): early_estimate (Kostenschätzung) to sia-phases 31, DIN 276 Kostenschätzung, RIBA Stage 2 / NRM1 cost plan 1; approved_budget (Kostenvoranschlag) to sia-phases 32, DIN 276 Kostenberechnung, RIBA Stage 3 / NRM1 cost plan 2; contract_amendment (Nachtrag) relatedMatch sia-phases 51-53, VOB/B § 2 Nachtrag, RIBA Stage 5 variation; expectation (Kostenerwartung) relatedMatch sia-phases 52-53, DIN 276 Kostenprognose, RIBA Stage 5 anticipated final cost. Details: https://github.com/pragmaticBIM/pragmatic-bim-data-contract/blob/main/contract/README.md#cost-stages |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Product](Product.md) |
| Domain Of | [Deliverable](Deliverable.md), [CostRecord](CostRecord.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://schema.pragmaticbim.ch




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pbs:related_product |
| native | pbs:related_product |




## LinkML Source

<details>
```yaml
name: related_product
description: Optional catalog product this deliverable implements or this cost record
  is priced from.
from_schema: https://schema.pragmaticbim.ch
rank: 1000
domain_of:
- Deliverable
- CostRecord
range: Product
inlined: false

```
</details></div>