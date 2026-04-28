# Integration Guide

## Collect Payment via Invoice

This guide covers the document-first collection flow (party → counterparty → invoice → session → payment account → execution). To create a checkout source directly from payer details, see API Reference → Checkouts.

The standard flow for invoicing a customer and collecting payment via mobile money.

### Step 1 — Authenticate

```http
POST /v1/jwt/client/obtain/token
```

Exchange your Client ID and Client Secret for a Bearer token. Store the `access_token` and its `expires_in` value. Implement proactive refresh before the token expires.

### Step 2 — Create a Party

```http
POST /v1/parties/create
```

Create a contact record for the customer. Store the returned `party.id`.

### Step 3 — Create a Counterparty

```http
POST /v1/counterparties/create
```

Link the Party to your merchant account with `relationship_type: "CUSTOMER"`. Store the returned `counterparty.id`.

### Step 4 — Create an Invoice

```http
POST /v1/invoices/create
```

Pass `counterparty_id`, `currency`, `note`, `fee_bearer`, and `as_payment_link`. Store the returned `invoice.id`.

### Step 5 — Add Line Items

```http
POST /v1/invoices/{invoice_id}/items/add
```

Repeat for each line item (`name`, `currency`, `qty`, `amount`).

### Step 6 — Publish the Invoice

```http
PUT /v1/invoices/publish/{id}
```

Transitions the invoice from `IDLE` to `ACTIVE`. Editing is locked after this point.

### Step 7 — (Optional) Preview Fees

```http
GET /v1/predictions/amount-and-fees
```

Validate fee calculations and FX rates before funds move.

### Step 8 — (Optional) Detect MMO from Phone

```http
GET /v1/predictions/mmo-provider-info
```

Pass the customer's phone number to get the recommended `payment_method` and `gateway_provider`.

### Step 9 — Create a Checkout Session

```http
POST /v1/sessions/checkout
```

Pass `source_id: invoice.id` and `source_type: "INVOICE"`. Store the returned `session.id`.

### Step 10 — Create a Payment Account

```http
POST /v1/payment-accounts/create?operation_type=COLLECTION
```

Register the customer's mobile wallet. Store the returned `payment_account.id`.

### Step 11 — Execute the Collection

```http
POST /v1/executions/collection
```

!!! danger "Store your reference_id first"
    Generate a UUID v4 and persist it **before** calling this endpoint. If the HTTP response is lost due to a network error, you will need this ID to query the transaction status before retrying.

Pass `session_id`, `payment_account_id`, `currency`, and your pre-generated `reference_id`.

### Step 12 — Monitor Status

```http
GET /v1/status/collection/{reference_id}
```

Poll for status, or use a Realtime Key (`POST /v1/realtime-keys/collection`) for live push updates. Mobile money payments may remain in `PROCESSING` for several minutes — do not cancel or retry during this window.

### Step 13 — Retrieve Receipt

```http
GET /v1/invoices/receipt/{id}
```

Retrieve the receipt once the collection execution is successful and the source status is `PAID`. The receipt includes amounts, fees, FX rate, provider, and line items.

---

## Issue a Payout

### Step 1 — Authenticate

Obtain a Bearer token via `POST /v1/jwt/client/obtain/token`.

### Step 2 — Ensure Recipient Exists

Confirm the recipient has a Party and Counterparty record, or create them.

### Step 3 — Create a Payment Account for the Recipient

```http
POST /v1/payment-accounts/create?operation_type=PAYOUT
```

### Step 4 — Create a Payout Session

```http
POST /v1/sessions/payout
```

Pass `wallet_id`, `payment_account_id`, `amount`, `currency`, and `expires_at`.

### Step 5 — Execute the Payout

```http
POST /v1/executions/payout
```

Pass `session_id` and a freshly generated `reference_id` (UUID v4).

### Step 6 — Monitor Status

```http
GET /v1/status/payout/{reference_id}
```

---
