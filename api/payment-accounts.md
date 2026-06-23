---
title: "Payment Accounts"
description: "Register customer or recipient wallets and cards for collections and payouts."

icon: "wallet"


keywords: ["Dollr payment account", "Dollr wallet API", "Dollr API"]
---

Payment accounts bind a [party](/api/parties) to a `method` + `provider` (e.g. `MTN_MOMO_LBR` + `PAWAPAY`) for use in executions.

**Try in API Reference:** [Create payment account](/api-reference/payment-accounts/create-payment-account)

<Info>
For **hosted checkout**, you do not need to create payment accounts — Dollr collects payment details on the hosted page. See [Hosted checkout](/guides/hosted-checkout).
</Info>

## When to use

- **Collections (API-embedded):** register the payer's MoMo wallet or card before `executions/collection`
- **Payouts:** register the beneficiary account before `executions/payout`

## Operation types

Pass `operation_type` as a query parameter:

| Value | Use |
|-------|-----|
| `COLLECTION` | Customer paying you |
| `PAYOUT` | You sending to a beneficiary |
| `TRANSFER` | Wallet-to-wallet transfers |
| `REFUND` | Refunding a prior collection |

## Mobile money example

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

Infer MoMo operator from phone via [Predictions](/api/predictions).

## Card example

```bash
curl -X POST "https://api.heydollr.app/v1/payment-accounts/create?operation_type=COLLECTION" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "account_name": "Customer Card",
    "provider": "STRIPE",
    "method": "CREDIT_CARD",
    "party_id": 42
  }'
```

See [Collect with card](/guides/collect-with-card) for the full card flow.

## Reusing payment accounts

| Method | Reuse? | Guidance |
|--------|--------|----------|
| Mobile money | Yes | Cache per party + phone + method; reuse `id` across collections for same wallet |
| Card | No | Create a new payment account per card attempt |
| Payout | Yes | Reuse beneficiary account for repeat payouts to same party |

Payment accounts include `is_active` — inactive accounts cannot be used in executions.

## Related

- [Hosted checkout](/guides/hosted-checkout) · [Payments by market](/reference/payments-by-market)
- [Quick Start](/quickstart)
