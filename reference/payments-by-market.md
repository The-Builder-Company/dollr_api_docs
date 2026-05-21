---
title: "Payments by Market"
description: "Payment methods, providers, currencies, and routing by country for the Dollr API."
keywords: ["payment methods", "mobile money", "Liberia", "Rwanda", "MTN", "Orange Money", "Dollr API"]

icon: "globe"
---

# Payments by Market

Use this page as the source of truth for which **payment methods** (`method`), **providers** (`provider`), and markets Dollr supports. Enum values and routing can change — check the [OpenAPI spec](https://api.heydollr.app/openapi.json) and [Predictions API](/api/predictions) before going live.

<Note>
**Provider vs method** — `provider` is the routing network (`PAWAPAY`, `STRIPE`, `PLATFORM`). `method` is the instrument (`MTN_MOMO_LBR`, `CREDIT_CARD`, etc.). Both appear on executions and payment accounts.
</Note>

---

## Method matrix

| Market | Country code | Method (enum) | Provider | Typical use |
|---|---|---|---|---|
| Liberia | `LR` | `MTN_MOMO_LBR` | `PAWAPAY` | Collections & payouts via MTN MoMo |
| Liberia | `LR` | `ORANGE_MONEY_LBR` | `PAWAPAY` | Collections & payouts via Orange Money |
| Rwanda | `RW` | `AIRTEL_RWA` | `PAWAPAY` | Collections & payouts via Airtel Money |
| Rwanda | `RW` | `MTN_MOMO_RWA` | `PAWAPAY` | Collections & payouts via MTN MoMo |
| Rwanda | `RW` | `ORANGE_MONEY_RWA` | `PAWAPAY` | Collections & payouts via Orange Money |
| International | — | `CREDIT_CARD` | `STRIPE` | Card checkout (customer not required to have MoMo) |
| Platform | — | `WALLET` | `PLATFORM` | Internal Dollr wallet transfers |

---

## Detecting the right mobile money method

Before creating a **payment account** or **execution**, detect the wallet operator from the payer phone number:

```http
GET /v1/predictions/mmo-provider-info?phone={e164_without_plus}&operation_type=COLLECTION
```

Use the returned `method` and `provider` in `POST /v1/payment-accounts/create` and collection executions. See [Predictions](/api/predictions) and [Try in API Reference: MMO provider](/api-reference/predictions/predict-mmo-provider-info).

---

## Currencies & amounts

- Send currency as **ISO 4217** uppercase (e.g. `USD`, `LRD`).
- Amounts are positive numbers; minimum **0.01** for decimals, **1** for integers unless your fee tier specifies otherwise.
- Preview totals and fees with [Predict amount and fees](/api-reference/predictions/predict-amount-and-fee) before executing.

---

## Operations by method

| Operation | MoMo (PAWAPAY) | Card (STRIPE) | Wallet (PLATFORM) |
|---|---|---|---|
| Collection | Yes | Yes | N/A (use wallet transfer) |
| Payout | Yes | Per merchant setup | Yes |
| Transfer | Via wallet / platform rules | — | Yes |
| Refund | Per original transaction method | Per card rules | Per platform rules |

---

## Onboarding by market

Merchant verification requirements differ by country (e.g. Liberia sole proprietorship vs registered business). See [Overview](/) for document checklists. Until verification completes, some features (payouts, API keys, refunds) may be restricted.

---

## Related docs

- [Overview](/) — authentication and conventions
- [Quick Start](/quickstart) — first collection
- [Fees](/api/fees) — gateway and platform fee schedules
- [Error catalog](/reference/error-catalog) — common validation and execution errors
- [Glossary](/reference/glossary) — term definitions
