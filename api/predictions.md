---
title: "Predictions"
description: "Preview fees, FX, and mobile-money operator detection before executing payments."
icon: "chart-line"
---

# Predictions

Read-only endpoints to validate amounts and infer MoMo routing before money moves.

<Note>
**Try in API Reference:** [Amount & fees](/api-reference/predictions/predict-amount-and-fee) · [MMO provider](/api-reference/predictions/predict-mmo-provider-info) · [Source amount & fees](/api-reference/predictions/predict-payment-source-amount-and-fee)
</Note>

## Common calls

| Endpoint | Purpose |
|----------|---------|
| `GET /v1/predictions/mmo-provider-info` | Map phone → `method` + `provider` for collections/payouts |
| `GET /v1/predictions/amount-and-fees` | Fee breakdown for an amount |
| `GET /v1/predictions/payment-source-amount-and-fees` | Fees for a specific invoice/order |

## Minimal example (MMO detection)

```bash
curl "https://api.heydollr.app/v1/predictions/mmo-provider-info?phone=231771234567&operation_type=COLLECTION" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
```

Use returned `payment_method` and `gateway_provider` when creating [payment accounts](/api/payment-accounts).

## Related

- [Fees](/api/fees) · [Payments by market](/reference/payments-by-market)
- [Invalid method/provider](/knowledge-base/validation-422)
