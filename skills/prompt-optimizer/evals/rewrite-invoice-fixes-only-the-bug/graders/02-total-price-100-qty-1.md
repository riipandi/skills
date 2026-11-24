---
type: llm
focus: trace
weight: 1
---

total([{'price': 100, 'qty': 1}], discount=10) returns 99.9, so the discount is still applied before tax.
