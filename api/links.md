---
title: "Payment Links"
description: "Generate hosted payment and receipt URLs for invoices and orders."

icon: "link"


keywords: ["Dollr payment link", "Dollr API", "Dollr hosted checkout"]
---

# Payment Links

Turn published invoices or orders into shareable URLs customers can pay without a Dollr account.

<Note>
**Try in API Reference:** [Payment link](/api-reference/links/get-payment-link) · [Receipt link](/api-reference/links/get-receipt-link)
</Note>

## When to use

- Send a pay link by SMS, email, or WhatsApp
- Redirect customers after checkout to a receipt page

Requires the source to be published (`ACTIVE` or later). See [Invoices](/api/invoices) and [Orders](/api/orders).

## Related

- [Quick Start](/quickstart) — `as_payment_link: true` on create
- [Integration guide](/guides/integration)
