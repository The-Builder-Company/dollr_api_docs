---
title: "Fees"
description: "Gateway, platform, and merchant tier fee information."

icon: "percent"

keywords: ["Dollr API fees", "Dollr pricing", "Dollr API"]
---

# Fees

Understand how Dollr calculates gateway and platform fees before and after transactions.

<Note>
**Try in API Reference:** [Gateway fees](/api-reference/fees/get-gateway-fees) · [Platform fees](/api-reference/fees/get-platform-fees) · [Merchant tier](/api-reference/fees/get-merchant-fee-tier) · [List tiers](/api-reference/fees/list-fee-tier)
</Note>

## When to use

- Display fee breakdown in your checkout UI
- Reconcile settlements with [Predictions](/api/predictions) for live quotes

Fee bearer on invoices/orders (`PAYER` vs `PAYEE`) controls whether the customer pays fees on top of the total.

## Related

- [Predictions](/api/predictions)
- [Payments by market](/reference/payments-by-market)
