---
title: "Fees"
description: "Gateway, platform, and merchant tier fee information."

icon: "percent"


keywords: ["Dollr API fees", "Dollr pricing", "Dollr API"]
---

Understand how Dollr calculates gateway and platform fees before and after transactions.

**Try in API Reference:** [Gateway fees](/api-reference/fees/get-gateway-fees) · [Platform fees](/api-reference/fees/get-platform-fees) · [Merchant tier](/api-reference/fees/get-merchant-fee-tier) · [List tiers](/api-reference/fees/list-fee-tier)

## When to use

- Display fee breakdown in your checkout UI
- Reconcile settlements with [Predictions](/api/predictions) for live quotes

Fee bearer on invoices/orders (`PAYER` vs `PAYEE`) controls whether the customer pays fees on top of the total.

## Gateway fees

Per payment method and operation type:

```bash
curl "https://api.heydollr.app/v1/fees/gateway?payment_method=MTN_MOMO_LBR&operation_type=COLLECTION" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
```

`payment_method` values include `MTN_MOMO_LBR`, `ORANGE_MONEY_LBR`, `AIRTEL_RWA`, `MTN_MOMO_RWA`, `ORANGE_MONEY_RWA`, `CREDIT_CARD`, and `WALLET`.

## Platform fees

```bash
curl "https://api.heydollr.app/v1/fees/platform?operation_type=COLLECTION&fee_tier_name=default" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
```

## Merchant fee tier

```bash
curl "https://api.heydollr.app/v1/fees/merchant-tier?owner_type=ORGANIZATION&owner_id=42" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
```

`owner_type`: `USER`, `MICRO_ORGANIZATION`, or `ORGANIZATION`.

## List all tiers

```bash
curl "https://api.heydollr.app/v1/fees/tiers" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
```

Returns all platform fee tiers with `name`, `is_default`, and timestamps.

## Related

- [Predictions](/api/predictions)
- [Payments by market](/reference/payments-by-market)
