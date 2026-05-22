---
title: "Payment Accounts"
description: "Register customer or recipient wallets and cards for collections and payouts."

icon: "wallet"


keywords: ["Dollr payment account", "Dollr wallet API", "Dollr API"]
---

Payment accounts bind a [party](/api/parties) to a `method` + `provider` (e.g. `MTN_MOMO_LBR` + `PAWAPAY`) for use in executions.

**Try in API Reference:** [Create payment account](/api-reference/payment-accounts/create-payment-account)

## When to use

- **Collections:** register the payer's MoMo wallet or card before `executions/collection`
- **Payouts:** register the beneficiary account before `executions/payout`

Use `?operation_type=COLLECTION` or `PAYOUT` on create. Infer MoMo operator from phone via [Predictions](/api/predictions).

## Minimal example

```bash
curl -X POST "https://api.heydollr.app/v1/payment-accounts/create?operation_type=COLLECTION" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "account_name": "Amara MTN Wallet",
    "provider": "MTN_MOMO_LBR",
    "method": "MTN_MOMO_LBR",
    "party_id": 42,
    "country_code": "LR",
    "insensitive_account_number": "231771234567"
  }'
```

## Related

- [Payments by market](/reference/payments-by-market)
- [Quick Start](/quickstart)

