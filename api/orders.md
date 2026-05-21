---
title: "Orders"
description: "Payment documents for retail and e-commerce without formal invoice numbering."

icon: "box"
---

# Orders

Orders are like invoices but without a formal invoice number or required due date — suited for e-commerce and retail checkouts.

<Note>
**Try in API Reference:** [Create](/api-reference/orders/create-order) · [Add item](/api-reference/orders/add-order-item) · [Publish](/api-reference/orders/publish-order) · [Receipt](/api-reference/orders/retrieve-order-receipt-by-id)
</Note>

## When to use

- Storefront checkouts where a formal invoice is unnecessary
- Payment links for one-off product purchases

## Lifecycle

Same source statuses as invoices: `IDLE` → `ACTIVE` → `PROCESSING` → `PAID` | `CANCELED`.

## Typical flow

1. `POST /v1/orders/create`
2. Add items → publish → checkout session → execute → poll status

Or use [Collect via checkout](/guides/collect-via-checkout) to skip manual party setup.

## Minimal example

```bash
curl -X POST "https://api.heydollr.app/v1/orders/create" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "counterparty_id": 15,
    "currency": "USD",
    "note": "Order #1042",
    "fee_bearer": "PAYER",
    "as_payment_link": true
  }'
```

## Related

- [Invoices](/api/invoices) · [Sessions](/api/sessions) · [Quick Start](/quickstart)
