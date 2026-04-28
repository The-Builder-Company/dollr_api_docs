# Dollr Open API

**Version:** v1.0 &nbsp;|&nbsp; **Base URL:** `https://api.heydollr.app`

---

# Overview

Dollr is a modern payment infrastructure platform built for businesses operating in Africa. It enables merchants to collect payments, send payouts, process transfers, and issue refunds through a single unified API — abstracting the complexity of mobile money operators and card networks into a clean, consistent interface.

The Dollr Open API is a RESTful HTTP API that returns JSON responses. It is designed to be embedded in merchant applications, e-commerce storefronts, ERPs, and any software that needs to send or receive money in the markets Dollr supports.

### What You Can Build

- Accept mobile money and card payments from customers (Collections)
- Send money out to mobile wallets or bank accounts (Payouts)
- Move funds between wallets within Dollr (Transfers)
- Issue partial or full refunds on prior transactions (Refunds)
- Generate invoices and payment orders with line items
- Share payment links that customers pay without a Dollr account
- Manage counterparties — customers, suppliers, employees, and more
- Preview fees and FX rates before committing to a transaction

### Supported Payment Methods

| Method | Identifier | Market |
|---|---|---|
| MTN Mobile Money | `MTN_MOMO_LBR` | Liberia |
| Orange Money | `ORANGE_MONEY_LBR` | Liberia |
| Airtel Money | `AIRTEL_RWA` | Rwanda |
| MTN Mobile Money | `MTN_MOMO_RWA` | Rwanda |
| Orange Money | `ORANGE_MONEY_RWA` | Rwanda |
| Credit / Debit Card | `CREDIT_CARD` | International (via Stripe) |
| Dollr Wallet | `WALLET` | Internal platform transfers |

---

# Prerequisites

Before making any API calls, you must have a verified Dollr merchant account.

### Create a Merchant Account

Register at [https://merchant.heydollr.app](https://merchant.heydollr.app) and choose your account type during sign-up.

**Sole Proprietorship / Unregistered Business** — For individuals, freelancers, and informal businesses without official registration documents. This is the faster onboarding path, requiring only individual identity verification.

**Registered Business / Organization** — For officially registered companies, NGOs, and other formal entities. This requires both business verification (KYB) and a designated contact person verification (KYC), completed in two steps.

### Onboarding Requirements (Liberia)

#### Sole Proprietorship

| Requirement | Details |
|---|---|
| Business Name | Name you operate under (min. 2 characters) |
| Business Email | A valid email address |
| Phone Number | Carried over from your Dollr account |
| Government-Issued ID | Passport, National ID, or Driver License |
| ID Document Number | Number on your chosen ID (min. 4 characters) |
| Photo or Scan of ID | JPG, PNG, or PDF — max 5 MB, clear and legible |
| Business Description | Optional. Min. 10 characters if provided |

#### Registered Business / Organization

**Step 1 — Business Information:** Company name, registration number, country, business address, email, phone, business description (20–500 characters), and a copy of the registration certificate.

**Step 2 — Contact Person:** Full legal name, phone, email, government-issued ID (Passport, National ID, or Driver License), and acceptance of the Terms of Service.

All uploaded documents must be JPG, PNG, or PDF, max 5 MB per document, and clearly legible.

### Verification Timeline

After submitting your documents, your account enters a compliance review. The typical turnaround is **1 to 72 hours**. You will receive an email notification when approved.

!!! note
    The following features are restricted until your account is fully verified: transfers, payouts, payment links, team member management, API key generation, and refund processing.

### Generate API Credentials

Once your account is approved:

1. Log in at [https://merchant.heydollr.app](https://merchant.heydollr.app)
2. Navigate to **Settings > Developer > API Keys**
3. Generate a new **Client ID** and **Client Secret**
4. Store your Client Secret securely — it is only shown once

!!! danger "Security Warning"
    Never expose your Client Secret in client-side code, mobile app binaries, or public repositories. All API calls must be made server-side.

---

# Authentication

The Dollr API uses the **OAuth 2.0 Client Credentials** flow. You exchange your Client ID and Client Secret for a short-lived JWT Bearer token, then include that token in the `Authorization` header of all subsequent requests.

## Obtain an Access Token

```http
POST /v1/jwt/client/obtain/token
```

This endpoint does not require a prior Bearer token.

#### Request Body

| Field | Type | Required | Description |
|---|---|---|---|
| `client_id` | string | Yes | Your API Client ID from the Merchant Portal |
| `client_secret` | string | Yes | Your API Client Secret |

#### Response Fields

| Field | Type | Description |
|---|---|---|
| `access_token` | string | JWT Bearer token for subsequent API requests |
| `expires_in` | integer | Token validity in **minutes** |

#### Example Response

```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "expires_in": 60
}
```

#### Code Examples

=== "cURL"

    ```bash
    curl -X POST "https://api.heydollr.app/v1/jwt/client/obtain/token" \
      -H "Content-Type: application/json" \
      -d '{
        "client_id": "your-client-id",
        "client_secret": "your-client-secret"
      }'
    ```

=== "Python"

    ```python
    import requests

    BASE_URL = "https://api.heydollr.app"

    response = requests.post(
        f"{BASE_URL}/v1/jwt/client/obtain/token",
        json={
            "client_id":     "your-client-id",
            "client_secret": "your-client-secret",
        },
    )
    data = response.json()
    access_token = data["access_token"]
    expires_in   = data["expires_in"]  # minutes
    print(f"Token: {access_token}")
    ```

=== "Node.js"

    ```javascript
    const BASE_URL = "https://api.heydollr.app";

    const response = await fetch(`${BASE_URL}/v1/jwt/client/obtain/token`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        client_id:     "your-client-id",
        client_secret: "your-client-secret",
      }),
    });

    const { access_token, expires_in } = await response.json();
    console.log("Token:", access_token);
    ```

=== "PHP"

    ```php
    $ch = curl_init("https://api.heydollr.app/v1/jwt/client/obtain/token");
    curl_setopt_array($ch, [
        CURLOPT_RETURNTRANSFER => true,
        CURLOPT_POST           => true,
        CURLOPT_HTTPHEADER     => ["Content-Type: application/json"],
        CURLOPT_POSTFIELDS     => json_encode([
            "client_id"     => "your-client-id",
            "client_secret" => "your-client-secret",
        ]),
    ]);
    $response    = json_decode(curl_exec($ch), true);
    $accessToken = $response["access_token"];
    $expiresIn   = $response["expires_in"]; // minutes
    curl_close($ch);
    ```

=== "Java"

    ```java
    import java.net.URI;
    import java.net.http.*;
    import java.net.http.HttpRequest.BodyPublishers;

    HttpClient client = HttpClient.newHttpClient();

    String body = """
        {
          "client_id":     "your-client-id",
          "client_secret": "your-client-secret"
        }
        """;

    HttpRequest request = HttpRequest.newBuilder()
        .uri(URI.create("https://api.heydollr.app/v1/jwt/client/obtain/token"))
        .header("Content-Type", "application/json")
        .POST(BodyPublishers.ofString(body))
        .build();

    HttpResponse<String> response = client.send(request, HttpResponse.BodyHandlers.ofString());
    System.out.println(response.body());
    ```

=== "Go"

    ```go
    package main

    import (
        "bytes"
        "encoding/json"
        "fmt"
        "io"
        "net/http"
    )

    func main() {
        payload := map[string]string{
            "client_id":     "your-client-id",
            "client_secret": "your-client-secret",
        }
        body, _ := json.Marshal(payload)

        resp, _ := http.Post(
            "https://api.heydollr.app/v1/jwt/client/obtain/token",
            "application/json",
            bytes.NewBuffer(body),
        )
        defer resp.Body.Close()

        var result map[string]interface{}
        data, _ := io.ReadAll(resp.Body)
        json.Unmarshal(data, &result)
        fmt.Println("Token:", result["access_token"])
    }
    ```

## Use the Bearer Token

Include the token in the `Authorization` header for every protected request:

```http
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
```

Tokens expire after the period stated in `expires_in`. Implement proactive refresh logic to obtain a new token before the current one expires. Requests with an expired or invalid token return `HTTP 401`.

---

# API Conventions

## Base URL and Versioning

All endpoints are prefixed with the API version. The current version is `v1`.

```
https://api.heydollr.app/v1/{resource}
```

Future breaking changes will be introduced under a new version prefix.

## Request Format

- All requests and responses use JSON (`Content-Type: application/json`)
- Timestamps must be ISO 8601 format (e.g., `2025-06-01T14:30:00Z`)
- Currency codes must be 3-letter ISO 4217 codes in UPPERCASE (e.g., `USD`, `LRD`)
- Phone numbers must be E.164 format **without** the leading `+` (e.g., `231771234567`)
- Amount values are positive numbers; minimum is `0.01` for decimals, `1` for integers
- `reference_id` values must be version-4 UUIDs

## Validation Errors (HTTP 422)

```json
{
  "detail": [
    {
      "loc": ["body", "currency"],
      "msg": "field required",
      "type": "value_error.missing"
    }
  ]
}
```

## HTTP Status Codes

| Code | Status | Meaning |
|---|---|---|
| `200` | OK | Request succeeded |
| `401` | Unauthorized | Missing or invalid Bearer token |
| `403` | Forbidden | Token valid but insufficient permissions |
| `404` | Not Found | Resource does not exist |
| `422` | Unprocessable Entity | Payload failed validation — see `detail` array |
| `429` | Too Many Requests | Rate limit exceeded — back off and retry |
| `500` | Internal Server Error | Unexpected server error |

---

# Core Concepts

## Parties and Counterparties

**Party** — A contact record: a person or entity identified by name, phone number, and optionally email.

**Counterparty** — Links a Party to your merchant account with a defined relationship type, describing the nature of the association (e.g., `CUSTOMER`, `SUPPLIER`, `EMPLOYEE`).

For direct invoice and order endpoints (the document-first flow), create a Counterparty before creating invoices or orders because those documents require a `counterparty_id`. If you use the checkout-source shortcut (`POST /v1/checkouts/create`), Dollr can create or match the Party and Counterparty automatically from the payer details.

## Invoices vs. Orders

**Invoice** — A formal billing document with an auto-generated invoice number, due date, and optional line items. Can optionally be shared as a payment link.

**Order** — A payment document similar to an invoice but without a formal invoice number or due date. Suited for retail and e-commerce. Can also be shared as a payment link.

!!! info "Key fact"
    Customers do not need a Dollr account to pay via a payment link. Payment is completed directly in a browser using mobile money or a credit card.

## Sessions and Executions

**Session** — Declares the intent to perform a payment operation (checkout, payout, transfer, or refund). Sessions expire if not executed within the time window.

**Execution** — Submits an active session for processing. Pass the `session_id` and a unique `reference_id` (a version-4 UUID you generate) to trigger the actual movement of funds.

Execution status tracks the movement of funds (execution lifecycle). Source status (invoice/order) tracks the document lifecycle (IDLE, ACTIVE, PROCESSING, PAID, CANCELED). Keep these state models distinct when building polling or receipt logic.

!!! warning "Idempotency"
    Always generate a unique `reference_id` per execution attempt. This is your idempotency key. If a network error occurs, query the transaction status using this `reference_id` before retrying.

## Fee Bearers

- **`PAYER`** — The customer pays fees on top of the invoice total. The merchant receives the full amount.
- **`PAYEE`** — The merchant absorbs the fees. The customer pays the invoice total and the merchant receives less after fees are deducted.

## Payment Methods and Providers

provider = routing network or gateway (e.g. `PAWAPAY`, `STRIPE`, `PLATFORM`)

method = payment instrument identifier (e.g. `MTN_MOMO_LBR`, `ORANGE_MONEY_RWA`, `CREDIT_CARD`, `WALLET`)

| Payment Method | Provider | Notes |
|---|---|---|
| `MTN_MOMO_LBR`, `MTN_MOMO_RWA` | `PAWAPAY` | Routed via PawaPay |
| `ORANGE_MONEY_LBR`, `ORANGE_MONEY_RWA` | `PAWAPAY` | Routed via PawaPay |
| `AIRTEL_RWA` | `PAWAPAY` | Routed via PawaPay |
| `CREDIT_CARD` | `STRIPE` | International card processing |
| `WALLET` | `PLATFORM` | Internal Dollr wallet balance |
