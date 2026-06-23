---
title: "Payment Links"
description: "Generate hosted payment and receipt URLs for invoices and orders."

icon: "link"


keywords: ["Dollr payment link", "Dollr API", "Dollr hosted checkout"]
---

Turn published invoices or orders into shareable URLs customers can pay on a Dollr-hosted page with **mobile money** or **card** — no Dollr account required.

**Try in API Reference:** [Payment link](/api-reference/links/get-payment-link) · [Receipt link](/api-reference/links/get-receipt-link)

## When to use

- Send a pay link by SMS, email, or WhatsApp
- Redirect customers after checkout to a receipt page
- Hosted checkout without building your own payment form — see [Hosted checkout](/guides/hosted-checkout)

Requires the source to be published (`ACTIVE` or later). See [Invoices](/api/invoices) and [Orders](/api/orders).

## Query parameters

| Parameter | Required | Description |
|-----------|----------|-------------|
| `source_type` | Yes | `INVOICE` or `ORDER` (`SUBSCRIPTION` reserved — not yet supported) |
| `source_number` | Yes | Document number (e.g. `INV-2025-0042`) |

## Payment link

```bash
curl "https://api.heydollr.app/v1/links/pay?source_type=INVOICE&source_number=INV-2025-0042" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
```

**Response:** `{ "url": "https://..." }` — redirect or share this URL. The customer completes payment on Dollr's hosted page.

## Receipt link

```bash
curl "https://api.heydollr.app/v1/links/receipt?source_type=INVOICE&source_number=INV-2025-0042" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
```

Available after the source reaches `PAID` status.

## Related

- [Hosted checkout](/guides/hosted-checkout)
- [Quick Start](/quickstart) — `as_payment_link: true` on create
