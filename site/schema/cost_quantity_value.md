---
search:
  boost: 5.0
---

# Slot: cost_quantity_value 


_Quantity magnitude used as basis for this cost calculation._



<div data-search-exclude markdown="1">



URI: [pbs:cost_quantity_value](https://schema.pragmaticbim.ch/cost_quantity_value)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [CostRecord](CostRecord.md) | Cost record for estimation, catalog pricing, and calculation. Use cost_record_role to distinguish catalog cost/price (on Product) from project estimate/actual lines. Populate component_cost_items to act as an assembly (aggregated unit price). Either amount (lump sum) or unit_cost (rate per cost quantity) must be present. The cost stage (early_estimate, approved_budget, contract_amendment, expectation) is a Classification entry with classification_scheme cost-stages; a record with cost_record_role estimate carries at most one cost-stages classification. Cost-stage mappings (SKOS closeMatch unless noted): early_estimate (Kostenschätzung) to sia-phases 31, DIN 276 Kostenschätzung, RIBA Stage 2 / NRM1 cost plan 1; approved_budget (Kostenvoranschlag) to sia-phases 32, DIN 276 Kostenberechnung, RIBA Stage 3 / NRM1 cost plan 2; contract_amendment (Nachtrag) relatedMatch sia-phases 51-53, VOB/B § 2 Nachtrag, RIBA Stage 5 variation; expectation (Kostenerwartung) relatedMatch sia-phases 52-53, DIN 276 Kostenprognose, RIBA Stage 5 anticipated final cost. Details: https://github.com/pragmaticBIM/pragmatic-bim-data-contract/blob/main/contract/README.md#cost-stages |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Double](Double.md) |
| Domain Of | [CostRecord](CostRecord.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Value Constraints

| Property | Value |
| --- | --- |
| Minimum Value | 0 |












## Identifier and Mapping Information





### Schema Source


* from schema: https://schema.pragmaticbim.ch




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pbs:cost_quantity_value |
| native | pbs:cost_quantity_value |




## LinkML Source

<details>
```yaml
name: cost_quantity_value
description: Quantity magnitude used as basis for this cost calculation.
from_schema: https://schema.pragmaticbim.ch
rank: 1000
domain_of:
- CostRecord
range: double
minimum_value: 0

```
</details></div>