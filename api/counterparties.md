---
title: "Counterparties"
description: "Link parties to your merchant account with relationship types."

icon: "users"

keywords: ["Dollr counterparty API", "Dollr API"]
---

# Counterparties

A counterparty links a [party](/api/parties) to your merchant with a relationship type (`CUSTOMER`, `SUPPLIER`, `EMPLOYEE`, `BENEFICIARY`, `OTHER`).

<Note>
**Try in API Reference:** [Create counterparty](/api-reference/counterparties/create-counterparty) · [List](/api-reference/counterparties/list-counterparties) · [Retrieve](/api-reference/counterparties/retrieve-counterparties)
</Note>

## When to use

Required for `POST /v1/invoices/create` and `POST /v1/orders/create` in the document-first flow. Not required when using `POST /v1/checkouts/create` with payer details.

## Minimal example

```bash
curl -X POST "https://api.heydollr.app/v1/counterparties/create" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"relationship_type": "CUSTOMER", "party_id": 42}'
```

## Related

- [Parties](/api/parties) · [Invoices](/api/invoices) · [Orders](/api/orders)
- [Parties & counterparties (concept)](/concepts/parties-and-counterparties)
