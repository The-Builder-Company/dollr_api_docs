# Sessions

Sessions declare payment intent before funds move. Create a session, then execute it. An unexecuted session cannot be used after it expires.

## Checkout Session

```http
POST /v1/sessions/checkout
```

| Field | Type | Required | Description |
|---|---|---|---|
| `source_id` | integer | Yes | ID of the invoice or order to collect payment for |
| `source_type` | enum | Yes | `INVOICE` or `ORDER` |

#### Response — `CheckoutSessionResponse`

| Field | Type | Description |
|---|---|---|
| `id` | integer | Session ID — required for the collection execution call |
| `source_id` | integer | ID of the linked invoice or order |
| `source_type` | enum | `INVOICE` or `ORDER` |
| `status` | string | Current session status |
| `payment_account_id` | integer \| null | Linked payment account, if already set |
| `expires_at` | datetime | Session expiry timestamp |
| `created_at` | datetime | Creation timestamp |
| `updated_at` | datetime | Last update timestamp |

#### Code Examples

=== "cURL"

    ```bash
    curl -X POST "https://api.heydollr.app/v1/sessions/checkout" \
      -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
      -H "Content-Type: application/json" \
      -d '{
        "source_id":   101,
        "source_type": "INVOICE"
      }'
    ```

=== "Python"

    ```python
    import requests

    BASE_URL = "https://api.heydollr.app"
    headers  = {"Authorization": "Bearer YOUR_ACCESS_TOKEN", "Content-Type": "application/json"}

    response = requests.post(
        f"{BASE_URL}/v1/sessions/checkout",
        headers=headers,
        json={
            "source_id":   101,
            "source_type": "INVOICE",
        },
    )
    session = response.json()
    print("Session ID:", session["id"])
    print("Expires at:", session["expires_at"])
    ```

=== "Node.js"

    ```javascript
    const BASE_URL = "https://api.heydollr.app";
    const TOKEN    = "YOUR_ACCESS_TOKEN";

    const response = await fetch(`${BASE_URL}/v1/sessions/checkout`, {
      method: "POST",
      headers: {
        Authorization:  `Bearer ${TOKEN}`,
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        source_id:   101,
        source_type: "INVOICE",
      }),
    });
    const session = await response.json();
    console.log("Session ID:", session.id);
    ```

=== "PHP"

    ```php
    $ch = curl_init("https://api.heydollr.app/v1/sessions/checkout");
    curl_setopt_array($ch, [
        CURLOPT_RETURNTRANSFER => true,
        CURLOPT_POST           => true,
        CURLOPT_HTTPHEADER     => [
            "Authorization: Bearer YOUR_ACCESS_TOKEN",
            "Content-Type: application/json",
        ],
        CURLOPT_POSTFIELDS => json_encode([
            "source_id"   => 101,
            "source_type" => "INVOICE",
        ]),
    ]);
    $session = json_decode(curl_exec($ch), true);
    curl_close($ch);
    echo "Session ID: " . $session["id"];
    ```

=== "Java"

    ```java
    import java.net.URI;
    import java.net.http.*;
    import java.net.http.HttpRequest.BodyPublishers;

    HttpClient client = HttpClient.newHttpClient();

    String body = """
        {
          "source_id":   101,
          "source_type": "INVOICE"
        }
        """;

    HttpRequest request = HttpRequest.newBuilder()
        .uri(URI.create("https://api.heydollr.app/v1/sessions/checkout"))
        .header("Authorization", "Bearer YOUR_ACCESS_TOKEN")
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
        payload := map[string]interface{}{
            "source_id":   101,
            "source_type": "INVOICE",
        }
        body, _ := json.Marshal(payload)

        req, _ := http.NewRequest("POST",
            "https://api.heydollr.app/v1/sessions/checkout",
            bytes.NewBuffer(body),
        )
        req.Header.Set("Authorization", "Bearer YOUR_ACCESS_TOKEN")
        req.Header.Set("Content-Type", "application/json")

        client := &http.Client{}
        resp, _ := client.Do(req)
        defer resp.Body.Close()

        data, _ := io.ReadAll(resp.Body)
        fmt.Println(string(data))
    }
    ```

## Payout Session

```http
POST /v1/sessions/payout
```

| Field | Type | Required | Description |
|---|---|---|---|
| `wallet_id` | integer | Yes | Merchant wallet ID to debit |
| `payment_account_id` | integer | Yes | Destination payment account ID |
| `amount` | number | Yes | Amount to send (positive, non-zero) |
| `currency` | string | Yes | ISO 4217 currency code |
| `expires_at` | datetime | Yes | Session expiry timestamp (ISO 8601) |

#### Code Examples

=== "cURL"

    ```bash
    curl -X POST "https://api.heydollr.app/v1/sessions/payout" \
      -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
      -H "Content-Type: application/json" \
      -d '{
        "wallet_id":          3,
        "payment_account_id": 18,
        "amount":             500.00,
        "currency":           "USD",
        "expires_at":         "2025-06-15T18:00:00Z"
      }'
    ```

=== "Python"

    ```python
    response = requests.post(
        f"{BASE_URL}/v1/sessions/payout",
        headers=headers,
        json={
            "wallet_id":          3,
            "payment_account_id": 18,
            "amount":             500.00,
            "currency":           "USD",
            "expires_at":         "2025-06-15T18:00:00Z",
        },
    )
    session = response.json()
    print("Payout Session ID:", session["id"])
    ```

=== "Node.js"

    ```javascript
    const response = await fetch(`${BASE_URL}/v1/sessions/payout`, {
      method: "POST",
      headers: {
        Authorization:  `Bearer ${TOKEN}`,
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        wallet_id:          3,
        payment_account_id: 18,
        amount:             500.00,
        currency:           "USD",
        expires_at:         "2025-06-15T18:00:00Z",
      }),
    });
    const session = await response.json();
    console.log("Payout Session ID:", session.id);
    ```

=== "PHP"

    ```php
    $ch = curl_init("https://api.heydollr.app/v1/sessions/payout");
    curl_setopt_array($ch, [
        CURLOPT_RETURNTRANSFER => true,
        CURLOPT_POST           => true,
        CURLOPT_HTTPHEADER     => [
            "Authorization: Bearer YOUR_ACCESS_TOKEN",
            "Content-Type: application/json",
        ],
        CURLOPT_POSTFIELDS => json_encode([
            "wallet_id"          => 3,
            "payment_account_id" => 18,
            "amount"             => 500.00,
            "currency"           => "USD",
            "expires_at"         => "2025-06-15T18:00:00Z",
        ]),
    ]);
    $session = json_decode(curl_exec($ch), true);
    curl_close($ch);
    echo "Session ID: " . $session["id"];
    ```

=== "Java"

    ```java
    String body = """
        {
          "wallet_id":          3,
          "payment_account_id": 18,
          "amount":             500.00,
          "currency":           "USD",
          "expires_at":         "2025-06-15T18:00:00Z"
        }
        """;

    HttpRequest request = HttpRequest.newBuilder()
        .uri(URI.create("https://api.heydollr.app/v1/sessions/payout"))
        .header("Authorization", "Bearer YOUR_ACCESS_TOKEN")
        .header("Content-Type", "application/json")
        .POST(BodyPublishers.ofString(body))
        .build();

    HttpResponse<String> response = client.send(request, HttpResponse.BodyHandlers.ofString());
    System.out.println(response.body());
    ```

=== "Go"

    ```go
    payload := map[string]interface{}{
        "wallet_id":          3,
        "payment_account_id": 18,
        "amount":             500.00,
        "currency":           "USD",
        "expires_at":         "2025-06-15T18:00:00Z",
    }
    body, _ := json.Marshal(payload)

    req, _ := http.NewRequest("POST",
        "https://api.heydollr.app/v1/sessions/payout",
        bytes.NewBuffer(body),
    )
    req.Header.Set("Authorization", "Bearer YOUR_ACCESS_TOKEN")
    req.Header.Set("Content-Type", "application/json")

    client := &http.Client{}
    resp, _ := client.Do(req)
    defer resp.Body.Close()

    data, _ := io.ReadAll(resp.Body)
    fmt.Println(string(data))
    ```

## Transfer Session

```http
POST /v1/sessions/transfer
```

| Field | Type | Required | Description |
|---|---|---|---|
| `from_wallet_id` | integer | Yes | Source wallet ID to debit |
| `to_counterparty_id` | integer | Yes | Counterparty ID of the recipient |
| `amount` | number | Yes | Amount to transfer |
| `currency` | string | Yes | ISO 4217 currency code |
| `expires_at` | datetime | Yes | Session expiry timestamp |

## Refund Session

```http
POST /v1/sessions/refund
```

| Field | Type | Required | Description |
|---|---|---|---|
| `original_payment_intent_id` | integer | Yes | ID of the original payment intent to refund |
| `amount` | number | Yes | Amount to refund (cannot exceed original amount) |
| `expires_at` | datetime | Yes | Session expiry timestamp |
| `reason` | string \| null | No | Reason for the refund |

---
