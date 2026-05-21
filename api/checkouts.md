---
title: "Checkouts"
description: "Create checkout sources directly from payer details without a prior invoice."

icon: "bag-shopping"

keywords: ["Dollr checkout API", "Dollr collect payment", "Dollr API"]
---

# Checkouts

One-call shortcut: create party, counterparty, payment source (invoice or order), and checkout context from payer details.

<Note>
**Try in API Reference:** [Create checkout source](/api-reference/checkouts/create-checkout-source)
</Note>

## When to use

- Faster integration than the [document-first Quick Start](/quickstart)
- Hosted checkout with `success_url` / `cancel_url`

<Warning>
Request body uses `source_kind`; session and execution calls use `source_type` for the same concept (`INVOICE` or `ORDER`).
</Warning>

## Minimal example

```bash
curl -X POST "https://api.heydollr.app/v1/checkouts/create" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "mode": "HOSTED",
    "source_kind": "INVOICE",
    "party_name": "Amara Kamara",
    "party_phone": "231771234567",
    "currency": "USD",
    "items": [{ "name": "Consulting", "currency": "USD", "amount": 250 }]
  }'
```

Then continue with [sessions](/api/sessions) → [executions](/api/executions).

## Related

- [Collect via checkout](/guides/collect-via-checkout)
- [Choose your integration](/guides/choose-integration)
