---
title: "Invoices"
description: "Create, manage, and publish invoices with line items and payment links."

icon: "file-invoice"


keywords: ["Dollr invoice API", "Dollr payment link", "Dollr API", "Dollr billing API"]
---

Formal billing documents with auto-generated invoice numbers, due dates, and line items. Publish before collecting payment.

**Try in API Reference:** [Create](/api-reference/invoices/create-invoice) · [Add item](/api-reference/invoices/add-invoice-item) · [Publish](/api-reference/invoices/publish-invoice) · [Receipt](/api-reference/invoices/retrieve-invoice-receipt-by-id)

## When to use

- B2B billing, consulting, subscriptions with explicit line items
- Hosted payment links (`as_payment_link: true`)

## Lifecycle


| Status       | Meaning                  |
| ------------ | ------------------------ |
| `IDLE`       | Draft — editable         |
| `ACTIVE`     | Published — ready to pay |
| `PROCESSING` | Payment in flight        |
| `PAID`       | Settled                  |
| `CANCELED`   | No longer payable        |


## Typical flow

1. `POST /v1/invoices/create` (requires `counterparty_id`)
2. `POST /v1/invoices/:id/items/add` for each line
3. `PUT /v1/invoices/publish/:id` → `ACTIVE`
4. [Checkout session](/api/sessions) → [execution](/api/executions) → [status](/api/status)

## Minimal example

```bash
curl -X POST "https://api.heydollr.app/v1/invoices/create" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "counterparty_id": 15,
    "currency": "USD",
    "note": "Consulting services",
    "fee_bearer": "PAYER",
    "as_payment_link": true
  }'
```

## Related

- [Quick Start](/quickstart) · [Orders](/api/orders) · [Checkouts](/api/checkouts)
- [Parties & counterparties](/concepts/parties-and-counterparties)

