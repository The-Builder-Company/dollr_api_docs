---
title: "Integration Guide"
description: "End-to-end walkthrough of collection and payout flows."

icon: "map"


keywords: ["Dollr API integration guide", "Dollr collect API", "Dollr payout API"]
---

**API Reference flows:** [Collect](/api-reference/executions/collect) · [Payout](/api-reference/executions/payout)

For **hosted checkout** (customer pays on a Dollr page with mobile money or card), see [Hosted checkout](/guides/hosted-checkout) — you can skip payment-account registration and server-side execution.

## Collect Payment via Invoice (API-embedded)

This guide covers the document-first collection flow (party → counterparty → invoice → session → payment account → execution). To create a checkout source directly from payer details, see [Collect via checkout](/guides/collect-via-checkout).

The standard flow for invoicing a customer and collecting payment via mobile money or card from your own UI.

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

Validate fee calculations and FX rates before funds move. Required query params include `base_amount`, `base_currency`, `target_currency`, `payment_method`, `operation_type`, `provider`, and `fee_bearer`.

For a published invoice or order, use:

```http
GET /v1/predictions/payment-source/amount-and-fees
```

Pass `source_type` (`INVOICE` or `ORDER`), `source_id`, `target_currency`, `payment_method`, and `provider`.

### Step 8 — (Optional) Detect payment method

**Mobile money:**

```http
GET /v1/predictions/mmo-provider-info
```

Pass the customer's phone number to get the recommended `payment_method` and `gateway_provider`.

**Card:**

```http
GET /v1/predictions/card-provider-info
```

Pass `payment_method_id` (from your Stripe Elements integration) and `operation_type=COLLECTION`.

### Step 9 — Create a Checkout Session

```http
POST /v1/sessions/checkout
```

Pass `source_id: invoice.id` and `source_type: "INVOICE"`. Store the returned `session.id`.

### Step 10 — Create a Payment Account

```http
POST /v1/payment-accounts/create?operation_type=COLLECTION
```

Register the customer's mobile wallet or card. Store the returned `payment_account.id`.

### Step 11 — Execute the Collection

```http
POST /v1/executions/collection
```

**Store your reference_id first**

Generate a UUID v4 and persist it **before** calling this endpoint. If the HTTP response is lost due to a network error, you will need this ID to query the transaction status before retrying.

Pass `session_id`, `payment_account_id`, `currency`, and your pre-generated `reference_id`.

For **card** payments, the response may include `requires_action: true` and a `client_secret` for Stripe 3D Secure. Complete authentication in your UI before polling status.

### Step 12 — Monitor Status

```http
GET /v1/status/collection/{reference_id}
```

Poll for status, or use a Realtime Key (`POST /v1/realtime-keys/collection`) for live push updates. Mobile money payments may remain in `PROCESSING` for several minutes — do not cancel or retry during this window.

You can also check source lifecycle:

```http
GET /v1/status/source?source_type=INVOICE&source_id={id}
```

### Step 13 — Retrieve Receipt

```http
GET /v1/invoices/receipt/{id}
GET /v1/orders/receipt/{id}
```

Retrieve the receipt once the collection execution is successful and the source status is `PAID`. The receipt includes amounts, fees, FX rate, provider, and line items. Use `/v1/invoices/receipt/\{id\}` for invoices and `/v1/orders/receipt/\{id\}` for orders.

Receipts are also available by document number:

```http
GET /v1/invoices/receipt/number/{invoice_number}
GET /v1/orders/receipt/number/{order_number}
```

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

Register the beneficiary's mobile wallet. Use [MMO prediction](/api/predictions) to resolve `method` and `provider` from phone.

### Step 4 — Create a Payout Session

```http
POST /v1/sessions/payout
```

Pass `payout_account_id`, `amount`, and `currency`. The response includes `expires_at` and the debiting `wallet_id`.

### Step 5 — Execute the Payout

```http
POST /v1/executions/payout
```

Pass `session_id`, `payout_account_id`, a freshly generated `reference_id` (UUID v4), and **`passcode`** (merchant verification with device metadata). See [Payout with Node.js](/guides/payout-with-nodejs) for the full payload shape.

### Step 6 — Monitor Status

```http
GET /v1/status/payout/{reference_id}
```

---
