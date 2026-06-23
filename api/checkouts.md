---
title: "Checkouts"
description: "Create checkout sources directly from payer details without a prior invoice."

icon: "bag-shopping"


keywords: ["Dollr checkout API", "Dollr collect payment", "Dollr API", "Dollr hosted checkout"]
---

One-call shortcut: create party, counterparty, payment source (invoice or order), and checkout context from payer details.

**Try in API Reference:** [Create checkout source](/api-reference/checkouts/create-checkout-source)

## When to use

- Faster integration than the [document-first Quick Start](/quickstart)
- [Hosted checkout](/guides/hosted-checkout) with `mode: "HOSTED"` — customer pays with mobile money or card on a Dollr page
- API-embedded collection — continue with sessions → payment account → execute

Request body uses `source_kind`; session and execution calls use `source_type` for the same concept (`INVOICE` or `ORDER`).

## Required fields

| Field | Description |
|-------|-------------|
| `mode` | `HOSTED` for Dollr-hosted payment page |
| `source_kind` | `INVOICE` or `ORDER` |
| `party_phone` | Payer phone (E.164 without `+`) |
| `currency` | ISO 4217 code |
| `items` | Line items (`name`, `currency`, `amount`) |

## Hosted checkout example

```bash
curl -X POST "https://api.heydollr.app/v1/checkouts/create" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "mode": "HOSTED",
    "source_kind": "INVOICE",
    "party_name": "Amara Kamara",
    "party_phone": "231771234567",
    "party_email": "amara@example.com",
    "currency": "USD",
    "items": [{ "name": "Consulting", "currency": "USD", "amount": 250 }],
    "success_url": "https://yourstore.com/success",
    "cancel_url": "https://yourstore.com/cancel"
  }'
```

**Response highlights:**

| Field | Description |
|-------|-------------|
| `url` | Hosted payment URL — redirect customer here |
| `hosted_path_or_token` | Path/token for the hosted session |
| `source_id` | Invoice or order ID |
| `source_number` | Document number for link APIs |
| `success_url` / `cancel_url` | Post-payment redirects |

## API-embedded flow

After creating a checkout source, continue with [sessions](/api/sessions) → [payment accounts](/api/payment-accounts) → [executions](/api/executions). See [Quick Start](/quickstart).

## Checkout `mode` values

| Mode | Behavior |
|------|----------|
| `HOSTED` | Returns `url` — customer pays on Dollr page (MoMo + card). See [Hosted checkout](/guides/hosted-checkout). |
| Other values | Contact Dollr if you need a non-hosted integration mode. Default API-embedded flow: create source without `HOSTED`, then session → payment account → execute. |

## `url` vs `hosted_path_or_token`

Use **`url`** for customer redirects. `hosted_path_or_token` is for internal Dollr routing — prefer `url` unless support directs otherwise.

## Optional fields

`party_name`, `party_email`, `party_relationship`, `reference_id`, `note`, `due_date`, `expires_at`, `counterparty_id`.

## Related

- [Hosted checkout](/guides/hosted-checkout) · [Collect via checkout](/guides/collect-via-checkout)
- [Choose your integration](/guides/choose-integration)
