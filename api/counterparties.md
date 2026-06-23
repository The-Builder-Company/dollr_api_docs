---
title: "Counterparties"
description: "Link parties to your merchant account with relationship types."

icon: "users"


keywords: ["Dollr counterparty API", "Dollr API"]
---

A counterparty links a [party](/api/parties) to your merchant with a relationship type.

**Try in API Reference:** [Create](/api-reference/counterparties/create-counterparty) · [List](/api-reference/counterparties/list-counterparties) · [Retrieve](/api-reference/counterparties/retrieve-counterparties) · [Update](/api-reference/counterparties/update-counterparty)

## Relationship types

| Type | Typical use |
|------|-------------|
| `CUSTOMER` | Paying you |
| `SUPPLIER` | You pay them |
| `EMPLOYEE` | Payroll |
| `BENEFICIARY` | Payout recipient |
| `FRIEND` | Personal contact |
| `FAMILY` | Family member |
| `DONOR` | Donation source |
| `DONEE` | Donation recipient |
| `CONTACT` | General contact |
| `SERVICE_PROVIDER` | Vendor or contractor |
| `PARTNER` | Business partner |
| `SELF` | Your own entity |

## When to use

Required for `POST /v1/invoices/create` and `POST /v1/orders/create` in the document-first flow. Not required when using `POST /v1/checkouts/create` with payer details.

## Create

```bash
curl -X POST "https://api.heydollr.app/v1/counterparties/create" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"relationship_type": "CUSTOMER", "party_id": 42}'
```

## List

```bash
curl "https://api.heydollr.app/v1/counterparties/list?fullname=Amara&relationship_type=CUSTOMER" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
```

Optional filters: `fullname`, `relationship_type`.

## Retrieve

```bash
curl "https://api.heydollr.app/v1/counterparties/retrieve/15" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
```

Returns the counterparty with embedded `party` details.

## Update

```bash
curl -X PUT "https://api.heydollr.app/v1/counterparties/update/15" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"relationship_type": "SUPPLIER"}'
```

## Related

- [Parties](/api/parties) · [Invoices](/api/invoices) · [Orders](/api/orders)
- [Parties & counterparties (concept)](/concepts/parties-and-counterparties)
