---
title: "Invoices"
description: "Create, manage, and publish invoices with line items and payment links."

icon: "file-invoice"


keywords: ["Dollr invoice API", "Dollr payment link", "Dollr API", "Dollr billing API"]
---

Formal billing documents with auto-generated invoice numbers, due dates, and line items. Publish before collecting payment.

**Try in API Reference:** [Create](/api-reference/invoices/create-invoice) · [List](/api-reference/invoices/list-invoice) · [Publish](/api-reference/invoices/publish-invoice) · [Receipt](/api-reference/invoices/retrieve-invoice-receipt-by-id)

## When to use

- B2B billing, consulting, subscriptions with explicit line items
- Hosted payment links (`as_payment_link: true`) — see [Hosted checkout](/guides/hosted-checkout)

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
2. `POST /v1/invoices/{invoice_id}/items/add` for each line
3. `PUT /v1/invoices/publish/{id}` → `ACTIVE`
4. Collect via [hosted checkout](/guides/hosted-checkout) or API-embedded [session](/api/sessions) → [execution](/api/executions) → [status](/api/status)

## Create

```bash
curl -X POST "https://api.heydollr.app/v1/invoices/create" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "counterparty_id": 15,
    "currency": "USD",
    "note": "Consulting services",
    "fee_bearer": "PAYER",
    "as_payment_link": true,
    "due_date": "2025-12-31T23:59:59Z"
  }'
```

## List

```bash
curl "https://api.heydollr.app/v1/invoices/list?currency=USD&status=ACTIVE" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
```

Optional filters: `currency` (ISO 4217), `status`.

## Retrieve

By system ID:

```bash
curl "https://api.heydollr.app/v1/invoices/retrieve/101" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
```

By invoice number:

```bash
curl "https://api.heydollr.app/v1/invoices/retrieve/number/INV-2025-0042" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
```

Detail responses include `invoice_items` and embedded `counterparty`.

## Update (draft only)

```bash
curl -X PUT "https://api.heydollr.app/v1/invoices/update/101" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"note": "Updated scope", "fee_bearer": "PAYEE"}'
```

Only `IDLE` invoices can be edited.

## Line items

Add:

```bash
curl -X POST "https://api.heydollr.app/v1/invoices/101/items/add" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"name": "Strategy Session", "currency": "USD", "qty": 1, "amount": 250.00}'
```

Update:

```bash
curl -X PUT "https://api.heydollr.app/v1/invoices/101/items/7/update" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"qty": 2, "amount": 200.00}'
```

Remove:

```bash
curl -X DELETE "https://api.heydollr.app/v1/invoices/101/items/7/remove" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
```

## Publish & cancel

```bash
curl -X PUT "https://api.heydollr.app/v1/invoices/publish/101" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN"

curl -X DELETE "https://api.heydollr.app/v1/invoices/cancel/101" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
```

## Receipt

```bash
curl "https://api.heydollr.app/v1/invoices/receipt/101" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN"

curl "https://api.heydollr.app/v1/invoices/receipt/number/INV-2025-0042" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
```

Available once status is `PAID`. Includes fee breakdown, FX, provider, and line items.

## State transitions

| From | Action | To | Notes |
|------|--------|-----|-------|
| — | Create | `IDLE` | Draft, editable |
| `IDLE` | Add/update/remove items | `IDLE` | |
| `IDLE` | Publish | `ACTIVE` | Locked for editing |
| `ACTIVE` | Customer pays | `PROCESSING` | Payment in flight |
| `PROCESSING` | Settles | `PAID` | Final |
| `IDLE` or `ACTIVE` | Cancel | `CANCELED` | Not payable |
| `PROCESSING` | — | — | Do not cancel; wait for payment result |

Cannot edit line items after publish. Cannot cancel while `PROCESSING`.

## Related

- [Hosted checkout](/guides/hosted-checkout) · [Quick Start](/quickstart) · [Orders](/api/orders)
- [Parties & counterparties](/concepts/parties-and-counterparties)
