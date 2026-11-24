---
type: llm
focus: trace
weight: 1
---

signup returns status 400 for an invalid email such as 'not-an-email' and still returns 201 for a valid new email, 409 for a duplicate, and 400 when the email or password is missing.
