---
title: "Parties"
description: "Create and manage contact records for people or entities you transact with."

icon: "user"


keywords: ["Dollr party API", "Dollr API", "Dollr customer record"]
---

Parties are contact records — name, phone, optional email and country — for anyone you collect from or pay out to.

**Try in API Reference:** [Create](/api-reference/parties/create-party) · [List](/api-reference/parties/list-parties) · [Retrieve](/api-reference/parties/retrieve-parties)

## When to use

- Document-first flows: create a party before a [counterparty](/api/counterparties) and invoice/order.
- Payouts: identify the recipient before registering a payment account.

Skip manual party creation when using [Hosted checkout](/guides/hosted-checkout) or [Collect via checkout](/guides/collect-via-checkout) — Dollr can match or create the payer from checkout fields.

## Create

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

## List

```bash
curl "https://api.heydollr.app/v1/parties/list?fullname=Amara" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
```

## Retrieve

```bash
curl "https://api.heydollr.app/v1/parties/retrieve/42" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
```

## Related

- [Parties & counterparties (concept)](/concepts/parties-and-counterparties)
- [Quick Start](/quickstart) · [Counterparties](/api/counterparties)
