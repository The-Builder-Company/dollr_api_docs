---
title: "Predictions"
description: "Preview fees, FX, and mobile-money operator detection before executing payments."

icon: "chart-line"


keywords: ["Dollr API", "Dollr mobile money detection", "Dollr fees preview"]
---

Read-only endpoints to validate amounts and infer payment routing before money moves.

**Try in API Reference:** [Amount & fees](/api-reference/predictions/predict-amount-and-fee) · [MMO provider](/api-reference/predictions/predict-mmo-provider-info) · [Card provider](/api-reference/predictions/predict-card-provider-info) · [Source amount & fees](/api-reference/predictions/predict-payment-source-amount-and-fee)

## Common calls

| Endpoint | Purpose |
| -------- | ------- |
| `GET /v1/predictions/mmo-provider-info` | Map phone → `method` + `provider` for MoMo |
| `GET /v1/predictions/card-provider-info` | Validate card routing from Stripe `payment_method_id` |
| `GET /v1/predictions/amount-and-fees` | Fee breakdown for a specific amount |
| `GET /v1/predictions/payment-source/amount-and-fees` | Fees for a published invoice or order |

## Mobile money detection

```bash
curl "https://api.heydollr.app/v1/predictions/mmo-provider-info?phone=231771234567&operation_type=COLLECTION" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
```

Use returned `payment_method` and `gateway_provider` when creating [payment accounts](/api/payment-accounts).

## Card provider info

```bash
curl "https://api.heydollr.app/v1/predictions/card-provider-info?payment_method_id=pm_xxx&operation_type=COLLECTION&provider=STRIPE" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
```

Returns `brand`, `country`, `currencies`, and routing metadata. See [Collect with card](/guides/collect-with-card).

## Amount and fees

```bash
curl "https://api.heydollr.app/v1/predictions/amount-and-fees?base_amount=250&base_currency=USD&target_currency=USD&payment_method=MTN_MOMO_LBR&operation_type=COLLECTION&provider=PAWAPAY&fee_bearer=PAYER" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
```

Optional: `owner_type` (`USER`, `MICRO_ORGANIZATION`, `ORGANIZATION`) and `owner_id` for merchant-specific tier pricing.

## Payment source fees

For a published invoice or order:

```bash
curl "https://api.heydollr.app/v1/predictions/payment-source/amount-and-fees?source_type=INVOICE&source_id=101&target_currency=USD&payment_method=CREDIT_CARD&provider=STRIPE" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
```

## Related

- [Fees](/api/fees) · [Hosted checkout](/guides/hosted-checkout)
- [Payments by market](/reference/payments-by-market)
- [Invalid method/provider](/knowledge-base/validation-422)
