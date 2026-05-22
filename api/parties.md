---
title: "Parties"
description: "Create and manage contact records for people or entities you transact with."

icon: "user"


keywords: ["Dollr party API", "Dollr API", "Dollr customer record"]
---

# Parties

Parties are contact records — name, phone, optional email and country — for anyone you collect from or pay out to.

<Note>
**Try in API Reference:** [Create Party](/api-reference/parties/create-party) · [List Parties](/api-reference/parties/list-parties) · [Retrieve Party](/api-reference/parties/retrieve-parties)
</Note>

## When to use

- Document-first flows: create a party before a [counterparty](/api/counterparties) and invoice/order.
- Payouts and transfers: identify the recipient before registering a payment account.

Skip manual party creation when using [Collect via checkout](/guides/collect-via-checkout) — Dollr can match or create the payer from checkout fields.

## Minimal example

```bash
curl -X POST "https://api.heydollr.app/v1/parties/create" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "fullname": "Amara Kamara",
    "phone": "231771234567",
    "email": "amara@example.com",
    "country_code": "LR"
  }'
```

Phone numbers use E.164 **without** the leading `+`. See [API conventions](/api-conventions).

## Related

- [Parties & counterparties (concept)](/concepts/parties-and-counterparties)
- [Quick Start](/quickstart) · [Collect with Node.js](/guides/collect-with-nodejs)
- [Counterparties](/api/counterparties)
