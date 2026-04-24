# Executions

An Execution submits a Session for payment processing. All execution endpoints return an `ExecutionResponse`.

!!! warning "Idempotency"
    The `reference_id` you provide is your idempotency key. If you are uncertain whether a request was received (e.g., due to a network timeout), do not generate a new `reference_id`. Query the transaction status with the original one before retrying.

## Collect

```http
POST /v1/executions/collection
```

| Field | Type | Required | Description |
|---|---|---|---|
| `session_id` | string | Yes | ID of the active checkout session |
| `payment_account_id` | string | Yes | Payment account ID to charge |
| `currency` | string | Yes | ISO 4217 currency code |
| `reference_id` | string | Yes | Your unique UUID v4 idempotency key |

#### Code Examples

=== "cURL"

    ```bash
    curl -X POST "https://api.heydollr.app/v1/executions/collection" \
      -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
      -H "Content-Type: application/json" \
      -d '{
        "session_id":         "55",
        "payment_account_id": "18",
        "currency":           "USD",
        "reference_id":       "550e8400-e29b-41d4-a716-446655440000"
      }'
    ```

=== "Python"

    ```python
    import uuid
    import requests

    BASE_URL = "https://api.heydollr.app"
    headers  = {"Authorization": "Bearer YOUR_ACCESS_TOKEN", "Content-Type": "application/json"}

    reference_id = str(uuid.uuid4())  # store this before calling
    response = requests.post(
        f"{BASE_URL}/v1/executions/collection",
        headers=headers,
        json={
            "session_id":         "55",
            "payment_account_id": "18",
            "currency":           "USD",
            "reference_id":       reference_id,
        },
    )
    execution = response.json()
    print("Status:", execution["status"])
    print("Reference:", execution["reference_id"])
    ```

=== "Node.js"

    ```javascript
    import { randomUUID } from "crypto";

    const BASE_URL = "https://api.heydollr.app";
    const TOKEN    = "YOUR_ACCESS_TOKEN";

    const referenceId = randomUUID(); // store this before calling
    const response = await fetch(`${BASE_URL}/v1/executions/collection`, {
      method: "POST",
      headers: {
        Authorization:  `Bearer ${TOKEN}`,
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        session_id:         "55",
        payment_account_id: "18",
        currency:           "USD",
        reference_id:       referenceId,
      }),
    });
    const execution = await response.json();
    console.log("Status:", execution.status);
    ```

=== "PHP"

    ```php
    // Generate a UUID v4
    $referenceId = sprintf(
        '%04x%04x-%04x-%04x-%04x-%04x%04x%04x',
        mt_rand(0, 0xffff), mt_rand(0, 0xffff),
        mt_rand(0, 0xffff),
        mt_rand(0, 0x0fff) | 0x4000,
        mt_rand(0, 0x3fff) | 0x8000,
        mt_rand(0, 0xffff), mt_rand(0, 0xffff), mt_rand(0, 0xffff)
    );

    $ch = curl_init("https://api.heydollr.app/v1/executions/collection");
    curl_setopt_array($ch, [
        CURLOPT_RETURNTRANSFER => true,
        CURLOPT_POST           => true,
        CURLOPT_HTTPHEADER     => [
            "Authorization: Bearer YOUR_ACCESS_TOKEN",
            "Content-Type: application/json",
        ],
        CURLOPT_POSTFIELDS => json_encode([
            "session_id"         => "55",
            "payment_account_id" => "18",
            "currency"           => "USD",
            "reference_id"       => $referenceId,
        ]),
    ]);
    $execution = json_decode(curl_exec($ch), true);
    curl_close($ch);
    echo "Status: " . $execution["status"];
    ```

=== "Java"

    ```java
    import java.util.UUID;
    import java.net.URI;
    import java.net.http.*;
    import java.net.http.HttpRequest.BodyPublishers;

    String referenceId = UUID.randomUUID().toString(); // store before calling
    String body = String.format("""
        {
          "session_id":         "55",
          "payment_account_id": "18",
          "currency":           "USD",
          "reference_id":       "%s"
        }
        """, referenceId);

    HttpClient client = HttpClient.newHttpClient();
    HttpRequest request = HttpRequest.newBuilder()
        .uri(URI.create("https://api.heydollr.app/v1/executions/collection"))
        .header("Authorization", "Bearer YOUR_ACCESS_TOKEN")
        .header("Content-Type", "application/json")
        .POST(BodyPublishers.ofString(body))
        .build();

    HttpResponse<String> response = client.send(request, HttpResponse.BodyHandlers.ofString());
    System.out.println(response.body());
    ```

=== "Go"

    ```go
    // go get github.com/google/uuid
    package main

    import (
        "bytes"
        "encoding/json"
        "fmt"
        "io"
        "net/http"

        "github.com/google/uuid"
    )

    func main() {
        referenceId := uuid.New().String() // store before calling

        payload := map[string]string{
            "session_id":         "55",
            "payment_account_id": "18",
            "currency":           "USD",
            "reference_id":       referenceId,
        }
        body, _ := json.Marshal(payload)

        req, _ := http.NewRequest("POST",
            "https://api.heydollr.app/v1/executions/collection",
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

## Payout

```http
POST /v1/executions/payout
```

| Field | Type | Required | Description |
|---|---|---|---|
| `session_id` | string | Yes | ID of the active payout session |
| `reference_id` | string | Yes | Your unique UUID v4 idempotency key |

#### Code Examples

=== "cURL"

    ```bash
    curl -X POST "https://api.heydollr.app/v1/executions/payout" \
      -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
      -H "Content-Type: application/json" \
      -d '{
        "session_id":   "88",
        "reference_id": "660e8400-e29b-41d4-a716-446655440111"
      }'
    ```

=== "Python"

    ```python
    response = requests.post(
        f"{BASE_URL}/v1/executions/payout",
        headers=headers,
        json={
            "session_id":   "88",
            "reference_id": str(uuid.uuid4()),
        },
    )
    print(response.json())
    ```

=== "Node.js"

    ```javascript
    const response = await fetch(`${BASE_URL}/v1/executions/payout`, {
      method: "POST",
      headers: {
        Authorization:  `Bearer ${TOKEN}`,
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        session_id:   "88",
        reference_id: randomUUID(),
      }),
    });
    console.log(await response.json());
    ```

=== "PHP"

    ```php
    $ch = curl_init("https://api.heydollr.app/v1/executions/payout");
    curl_setopt_array($ch, [
        CURLOPT_RETURNTRANSFER => true,
        CURLOPT_POST           => true,
        CURLOPT_HTTPHEADER     => [
            "Authorization: Bearer YOUR_ACCESS_TOKEN",
            "Content-Type: application/json",
        ],
        CURLOPT_POSTFIELDS => json_encode([
            "session_id"   => "88",
            "reference_id" => $referenceId,
        ]),
    ]);
    $result = json_decode(curl_exec($ch), true);
    curl_close($ch);
    print_r($result);
    ```

=== "Java"

    ```java
    String body = String.format("""
        {
          "session_id":   "88",
          "reference_id": "%s"
        }
        """, UUID.randomUUID().toString());

    HttpRequest request = HttpRequest.newBuilder()
        .uri(URI.create("https://api.heydollr.app/v1/executions/payout"))
        .header("Authorization", "Bearer YOUR_ACCESS_TOKEN")
        .header("Content-Type", "application/json")
        .POST(BodyPublishers.ofString(body))
        .build();

    HttpResponse<String> response = client.send(request, HttpResponse.BodyHandlers.ofString());
    System.out.println(response.body());
    ```

=== "Go"

    ```go
    payload := map[string]string{
        "session_id":   "88",
        "reference_id": uuid.New().String(),
    }
    body, _ := json.Marshal(payload)

    req, _ := http.NewRequest("POST",
        "https://api.heydollr.app/v1/executions/payout",
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

## Transfer

```http
POST /v1/executions/transfer
```

| Field | Type | Required | Description |
|---|---|---|---|
| `session_id` | string | Yes | ID of the active transfer session |
| `reference_id` | string | Yes | Your unique UUID v4 idempotency key |

## Refund

```http
POST /v1/executions/refund
```

| Field | Type | Required | Description |
|---|---|---|---|
| `session_id` | string | Yes | ID of the active refund session |
| `reference_id` | string | Yes | Your unique UUID v4 idempotency key |

## ExecutionResponse Schema

| Field | Type | Description |
|---|---|---|
| `reference_id` | string | Your supplied idempotency key — use to query status |
| `status` | string | Current status — e.g. `PENDING`, `PROCESSING`, `COMPLETED`, `FAILED` |
| `operation_type` | enum | `COLLECTION`, `PAYOUT`, `TRANSFER`, or `REFUND` |
| `payer_amount` | number | Amount charged to the payer |
| `payer_currency` | string | Currency of the payer's amount |
| `payee_amount` | number | Amount received by the payee after fees |
| `payee_currency` | string | Currency of the payee's amount |
| `provider_transaction_id` | string \| null | Transaction ID from the payment provider |
| `gateway_message` | string \| null | Status message from the gateway |
| `wallet_message` | string \| null | Status message from the wallet system |

---
