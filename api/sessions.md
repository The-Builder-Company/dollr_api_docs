---
title: "Sessions"
description: "Declare checkout, payout, transfer, or refund intent before executing funds movement."
---

# Sessions

A **session** records intent to move money. Create the right session type, then [execute](/api/executions) before it expires.

<Note>
**Try in API Reference:** [Checkout](/api-reference/sessions/create-checkout-session) · [Payout](/api-reference/sessions/create-payout-session) · [Transfer](/api-reference/sessions/create-transfer-session) · [Refund](/api-reference/sessions/create-refund-session)
</Note>

## Session types

| Type | Endpoint | Use with execution |
|------|----------|-------------------|
| Checkout | `POST /v1/sessions/checkout` | `POST /v1/executions/collection` |
| Payout | `POST /v1/sessions/payout` | `POST /v1/executions/payout` |
| Transfer | `POST /v1/sessions/transfer` | `POST /v1/executions/transfer` |
| Refund | `POST /v1/sessions/refund` | `POST /v1/executions/refund` |

Checkout sessions require `source_id` + `source_type` (`INVOICE` or `ORDER`).

## Minimal example (checkout)

```bash
curl -X POST "https://api.heydollr.app/v1/sessions/checkout" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"source_id": 101, "source_type": "INVOICE"}'
```

## Related

- [Sessions & executions (concept)](/concepts/sessions-and-executions)
- [Integration guide](/guides/integration)
