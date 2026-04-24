# Quick Start

Get from zero to your first successful payment collection in under 10 minutes.

**Base URL:** `https://api.heydollr.app`

---

## Before You Begin

You need a verified Dollr merchant account with API credentials. If you haven't done this yet:

1. Register at [merchant.heydollr.app](https://merchant.heydollr.app)
2. Complete identity verification (1–72 hours)
3. Go to **Settings → Developer → API Keys** and generate a **Client ID** and **Client Secret**

---

## Step 1 — Get an Access Token

Exchange your credentials for a JWT Bearer token. Every API call requires this token in the `Authorization` header.

```http
POST /v1/jwt/client/obtain/token
```

=== "cURL"

    ```bash
    curl -X POST "https://api.heydollr.app/v1/jwt/client/obtain/token" \
      -H "Content-Type: application/json" \
      -d '{
        "client_id":     "YOUR_CLIENT_ID",
        "client_secret": "YOUR_CLIENT_SECRET"
      }'
    ```

=== "Python"

    ```python
    import requests

    BASE_URL = "https://api.heydollr.app"

    res = requests.post(f"{BASE_URL}/v1/jwt/client/obtain/token", json={
        "client_id":     "YOUR_CLIENT_ID",
        "client_secret": "YOUR_CLIENT_SECRET",
    })
    token = res.json()["access_token"]
    headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}
    ```

=== "Node.js"

    ```javascript
    const BASE_URL = "https://api.heydollr.app";

    const { access_token } = await fetch(`${BASE_URL}/v1/jwt/client/obtain/token`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        client_id:     "YOUR_CLIENT_ID",
        client_secret: "YOUR_CLIENT_SECRET",
      }),
    }).then(r => r.json());

    const headers = {
      Authorization:  `Bearer ${access_token}`,
      "Content-Type": "application/json",
    };
    ```

**Response:**

```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "expires_in": 60
}
```

!!! tip
    Tokens expire after `expires_in` **minutes**. Refresh proactively — request a new token when less than 5 minutes remain.

---

## Step 2 — Create a Party

A Party is a contact record for the person you're collecting from.

```http
POST /v1/parties/create
```

=== "cURL"

    ```bash
    curl -X POST "https://api.heydollr.app/v1/parties/create" \
      -H "Authorization: Bearer $TOKEN" \
      -H "Content-Type: application/json" \
      -d '{
        "fullname":     "Amara Kamara",
        "phone":        "231771234567",
        "email":        "amara@example.com",
        "country_code": "LR"
      }'
    ```

=== "Python"

    ```python
    party = requests.post(f"{BASE_URL}/v1/parties/create", headers=headers, json={
        "fullname":     "Amara Kamara",
        "phone":        "231771234567",
        "email":        "amara@example.com",
        "country_code": "LR",
    }).json()

    party_id = party["id"]
    ```

=== "Node.js"

    ```javascript
    const party = await fetch(`${BASE_URL}/v1/parties/create`, {
      method: "POST", headers,
      body: JSON.stringify({
        fullname:     "Amara Kamara",
        phone:        "231771234567",
        email:        "amara@example.com",
        country_code: "LR",
      }),
    }).then(r => r.json());

    const partyId = party.id;
    ```

**Response:**

```json
{
  "id": 42,
  "fullname": "Amara Kamara",
  "phone": "231771234567",
  "email": "amara@example.com",
  "country_code": "LR",
  "created_at": "2025-06-01T10:00:00Z",
  "updated_at": "2025-06-01T10:00:00Z"
}
```

---

## Step 3 — Create a Counterparty

Link the Party to your merchant account with a relationship type.

```http
POST /v1/counterparties/create
```

=== "cURL"

    ```bash
    curl -X POST "https://api.heydollr.app/v1/counterparties/create" \
      -H "Authorization: Bearer $TOKEN" \
      -H "Content-Type: application/json" \
      -d '{"relationship_type": "CUSTOMER", "party_id": 42}'
    ```

=== "Python"

    ```python
    cp = requests.post(f"{BASE_URL}/v1/counterparties/create", headers=headers, json={
        "relationship_type": "CUSTOMER",
        "party_id":          party_id,
    }).json()

    counterparty_id = cp["id"]
    ```

=== "Node.js"

    ```javascript
    const cp = await fetch(`${BASE_URL}/v1/counterparties/create`, {
      method: "POST", headers,
      body: JSON.stringify({ relationship_type: "CUSTOMER", party_id: partyId }),
    }).then(r => r.json());

    const counterpartyId = cp.id;
    ```

---

## Step 4 — Create and Publish an Invoice

Create the invoice, add a line item, then publish it.

```http
POST /v1/invoices/create
```

=== "cURL"

    ```bash
    # Create invoice
    curl -X POST "https://api.heydollr.app/v1/invoices/create" \
      -H "Authorization: Bearer $TOKEN" \
      -H "Content-Type: application/json" \
      -d '{
        "counterparty_id": 15,
        "currency":        "USD",
        "note":            "Consulting services",
        "fee_bearer":      "PAYER",
        "as_payment_link": true
      }'

    # Add a line item (replace 101 with your invoice id)
    curl -X POST "https://api.heydollr.app/v1/invoices/101/items/add" \
      -H "Authorization: Bearer $TOKEN" \
      -H "Content-Type: application/json" \
      -d '{"name": "Strategy Session", "currency": "USD", "qty": 1, "amount": 250.00}'

    # Publish (locks the invoice and activates it for payment)
    curl -X PUT "https://api.heydollr.app/v1/invoices/publish/101" \
      -H "Authorization: Bearer $TOKEN"
    ```

=== "Python"

    ```python
    # Create invoice
    invoice = requests.post(f"{BASE_URL}/v1/invoices/create", headers=headers, json={
        "counterparty_id": counterparty_id,
        "currency":        "USD",
        "note":            "Consulting services",
        "fee_bearer":      "PAYER",
        "as_payment_link": True,
    }).json()
    invoice_id = invoice["id"]

    # Add a line item
    requests.post(f"{BASE_URL}/v1/invoices/{invoice_id}/items/add", headers=headers, json={
        "name":     "Strategy Session",
        "currency": "USD",
        "qty":      1,
        "amount":   250.00,
    })

    # Publish
    invoice = requests.put(f"{BASE_URL}/v1/invoices/publish/{invoice_id}", headers=headers).json()
    print("Status:", invoice["status"])  # ACTIVE
    ```

=== "Node.js"

    ```javascript
    // Create invoice
    const invoice = await fetch(`${BASE_URL}/v1/invoices/create`, {
      method: "POST", headers,
      body: JSON.stringify({
        counterparty_id: counterpartyId,
        currency:        "USD",
        note:            "Consulting services",
        fee_bearer:      "PAYER",
        as_payment_link: true,
      }),
    }).then(r => r.json());
    const invoiceId = invoice.id;

    // Add a line item
    await fetch(`${BASE_URL}/v1/invoices/${invoiceId}/items/add`, {
      method: "POST", headers,
      body: JSON.stringify({ name: "Strategy Session", currency: "USD", qty: 1, amount: 250.00 }),
    });

    // Publish
    const published = await fetch(`${BASE_URL}/v1/invoices/publish/${invoiceId}`, {
      method: "PUT", headers,
    }).then(r => r.json());
    console.log("Status:", published.status); // ACTIVE
    ```

---

## Step 5 — Collect Payment

Create a checkout session, register the customer's wallet, then execute.

!!! danger "Generate your reference_id before calling execute"
    Store the UUID before the network call. You'll need it to query status if the response is lost.

=== "cURL"

    ```bash
    # Detect payment method from phone (optional but recommended)
    curl "https://api.heydollr.app/v1/predictions/mmo-provider-info?phone=231771234567&operation_type=COLLECTION" \
      -H "Authorization: Bearer $TOKEN"

    # Create checkout session
    curl -X POST "https://api.heydollr.app/v1/sessions/checkout" \
      -H "Authorization: Bearer $TOKEN" \
      -H "Content-Type: application/json" \
      -d '{"source_id": 101, "source_type": "INVOICE"}'

    # Register customer wallet (use method/provider from prediction)
    curl -X POST "https://api.heydollr.app/v1/payment-accounts/create?operation_type=COLLECTION" \
      -H "Authorization: Bearer $TOKEN" \
      -H "Content-Type: application/json" \
      -d '{
        "account_name": "John Doe",
        "provider":     "MTN_MOMO_LBR",
        "method":       "MTN_MOMO_LBR",
        "party_id":     42,
        "country_code": "LR",
        "insensitive_account_number": "231771234567"
      }'

    # Execute — store reference_id FIRST
    REFERENCE_ID=$(python3 -c "import uuid; print(uuid.uuid4())")
    curl -X POST "https://api.heydollr.app/v1/executions/collection" \
      -H "Authorization: Bearer $TOKEN" \
      -H "Content-Type: application/json" \
      -d "{
        \"session_id\":         \"55\",
        \"payment_account_id\": \"18\",
        \"currency\":           \"USD\",
        \"reference_id\":       \"$REFERENCE_ID\"
      }"
    ```

=== "Python"

    ```python
    import uuid

    # Detect payment method from phone
    mmo = requests.get(f"{BASE_URL}/v1/predictions/mmo-provider-info", headers=headers, params={
        "phone": "231771234567", "operation_type": "COLLECTION",
    }).json()
    payment_method = mmo["payment_method"]
    provider       = mmo["gateway_provider"]

    # Create checkout session
    session = requests.post(f"{BASE_URL}/v1/sessions/checkout", headers=headers, json={
        "source_id":   invoice_id,
        "source_type": "INVOICE",
    }).json()
    session_id = session["id"]

    # Register customer wallet
    account = requests.post(
        f"{BASE_URL}/v1/payment-accounts/create",
        headers=headers,
        params={"operation_type": "COLLECTION"},
        json={
            "account_name":               "Amara MTN Wallet",
            "provider":                   provider,
            "method":                     payment_method,
            "party_id":                   party_id,
            "country_code":               "LR",
            "insensitive_account_number": "231771234567",
        },
    ).json()

    # Execute — generate and store reference_id BEFORE the call
    reference_id = str(uuid.uuid4())
    execution = requests.post(f"{BASE_URL}/v1/executions/collection", headers=headers, json={
        "session_id":         str(session_id),
        "payment_account_id": str(account["id"]),
        "currency":           "USD",
        "reference_id":       reference_id,
    }).json()
    print("Execution status:", execution["status"])
    ```

=== "Node.js"

    ```javascript
    import { randomUUID } from "crypto";

    // Detect payment method from phone
    const mmo = await fetch(
      `${BASE_URL}/v1/predictions/mmo-provider-info?phone=231771234567&operation_type=COLLECTION`,
      { headers }
    ).then(r => r.json());

    // Create checkout session
    const session = await fetch(`${BASE_URL}/v1/sessions/checkout`, {
      method: "POST", headers,
      body: JSON.stringify({ source_id: invoiceId, source_type: "INVOICE" }),
    }).then(r => r.json());

    // Register customer wallet
    const account = await fetch(
      `${BASE_URL}/v1/payment-accounts/create?operation_type=COLLECTION`,
      {
        method: "POST", headers,
        body: JSON.stringify({
          account_name:               "Amara MTN Wallet",
          provider:                   mmo.gateway_provider,
          method:                     mmo.payment_method,
          party_id:                   partyId,
          country_code:               "LR",
          insensitive_account_number: "231771234567",
        }),
      }
    ).then(r => r.json());

    // Execute — generate and store reference_id BEFORE the call
    const referenceId = randomUUID();
    const execution = await fetch(`${BASE_URL}/v1/executions/collection`, {
      method: "POST", headers,
      body: JSON.stringify({
        session_id:         String(session.id),
        payment_account_id: String(account.id),
        currency:           "USD",
        reference_id:       referenceId,
      }),
    }).then(r => r.json());
    console.log("Execution status:", execution.status);
    ```

---

## Step 6 — Check Payment Status

```http
GET /v1/status/collection/{reference_id}
```

=== "cURL"

    ```bash
    curl "https://api.heydollr.app/v1/status/collection/$REFERENCE_ID" \
      -H "Authorization: Bearer $TOKEN"
    ```

=== "Python"

    ```python
    status = requests.get(
        f"{BASE_URL}/v1/status/collection/{reference_id}",
        headers=headers,
    ).json()
    print(status["status"])  # PENDING → PROCESSING → COMPLETED
    ```

=== "Node.js"

    ```javascript
    const status = await fetch(`${BASE_URL}/v1/status/collection/${referenceId}`, { headers })
      .then(r => r.json());
    console.log(status.status); // PENDING → PROCESSING → COMPLETED
    ```

**Status progression:** `PENDING` → `PROCESSING` → `COMPLETED` (or `FAILED`)

!!! note
    Mobile money payments may stay in `PROCESSING` for several minutes while the carrier confirms. Do not retry during this window — query status instead.

---

## What's Next

| Task | Where to go |
|---|---|
| Full invoice and order management | [Invoices](api/invoices.md) · [Orders](api/orders.md) |
| Send payouts to mobile wallets | [Sessions](api/sessions.md) · [Executions](api/executions.md) |
| Preview fees before executing | [Predictions](api/predictions.md) |
| Live status push (no polling) | [Realtime Keys](api/realtime-keys.md) |
| Error handling and retries | [Error Handling](guides/error-handling.md) |
| Full step-by-step flows | [Integration Guide](guides/integration.md) |
| Term definitions | [Glossary](reference/glossary.md) |
