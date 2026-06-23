---
title: "Orders"
description: "Payment documents for retail and e-commerce without formal invoice numbering."

icon: "box"


keywords: ["Dollr order API", "Dollr checkout", "Dollr API", "Dollr e-commerce payments"]
---

Orders are like invoices but without a formal invoice number or required due date — suited for e-commerce and retail checkouts.

**Try in API Reference:** [Create](/api-reference/orders/create-order) · [List](/api-reference/orders/list-order) · [Publish](/api-reference/orders/publish-order) · [Receipt](/api-reference/orders/retrieve-order-receipt-by-id)

## When to use

- Storefront checkouts where a formal invoice is unnecessary
- Payment links for one-off product purchases — see [Hosted checkout](/guides/hosted-checkout)

## Lifecycle

Same source statuses as invoices: `IDLE` → `ACTIVE` → `PROCESSING` → `PAID` | `CANCELED`.

## Typical flow

1. `POST /v1/orders/create`
2. `POST /v1/orders/{order_id}/items/add`
3. `PUT /v1/orders/publish/{id}`
4. Collect via hosted link or API-embedded session → execute → poll status

Or use [Collect via checkout](/guides/collect-via-checkout) to skip manual party setup.

## Create

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

## List

```bash
curl "https://api.heydollr.app/v1/orders/list?currency=USD&status=ACTIVE" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
```

## Retrieve

```bash
curl "https://api.heydollr.app/v1/orders/retrieve/201" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN"

curl "https://api.heydollr.app/v1/orders/retrieve/number/ORD-2025-0099" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
```

## Update

```bash
curl -X PUT "https://api.heydollr.app/v1/orders/update/201" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"note": "Updated order", "fee_bearer": "PAYEE"}'
```

## Line items

```bash
curl -X POST "https://api.heydollr.app/v1/orders/201/items/add" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"name": "T-Shirt", "currency": "USD", "qty": 2, "amount": 25.00}'

curl -X PUT "https://api.heydollr.app/v1/orders/201/items/5/update" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"qty": 3}'

curl -X DELETE "https://api.heydollr.app/v1/orders/201/items/5/remove" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
```

## Publish & cancel

```bash
curl -X PUT "https://api.heydollr.app/v1/orders/publish/201" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN"

curl -X DELETE "https://api.heydollr.app/v1/orders/cancel/201" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
```

## Receipt

```bash
curl "https://api.heydollr.app/v1/orders/receipt/201" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN"

curl "https://api.heydollr.app/v1/orders/receipt/number/ORD-2025-0099" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
```

## Related

- [Hosted checkout](/guides/hosted-checkout) · [Invoices](/api/invoices) · [Sessions](/api/sessions)
