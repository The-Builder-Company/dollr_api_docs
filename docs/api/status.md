---
title: "Transaction Status"
description: "Query the status of any transaction by reference ID."
---

# Transaction Status

Use these endpoints to check the current status of any transaction using the `reference_id` supplied at execution time, or to poll the payment status of a specific invoice or order.

```http
GET /v1/status/collection/{reference_id}
GET /v1/status/payout/{reference_id}
GET /v1/status/transfer/{reference_id}
GET /v1/status/refund/{reference_id}
```

All four endpoints return an `ExecutionResponse` (see [ExecutionResponse Schema](executions.md#executionresponse-schema)).

To poll the payment status of an invoice or order directly, use [Check Payment Source Status](#check-payment-source-status).

#### Code Examples

<CodeGroup>

```bash cURL
curl "https://api.heydollr.app/v1/status/collection/550e8400-e29b-41d4-a716-446655440000" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
```

```python Python
import requests

BASE_URL     = "https://api.heydollr.app"
headers      = {"Authorization": "Bearer YOUR_ACCESS_TOKEN"}
reference_id = "550e8400-e29b-41d4-a716-446655440000"

response = requests.get(
    f"{BASE_URL}/v1/status/collection/{reference_id}",
    headers=headers,
)
result = response.json()
print("Status:", result["status"])
```

```javascript Node.js
const BASE_URL     = "https://api.heydollr.app";
const TOKEN        = "YOUR_ACCESS_TOKEN";
const referenceId  = "550e8400-e29b-41d4-a716-446655440000";

const response = await fetch(`${BASE_URL}/v1/status/collection/${referenceId}`, {
  headers: { Authorization: `Bearer ${TOKEN}` },
});
const result = await response.json();
console.log("Status:", result.status);
```

```php PHP
$referenceId = "550e8400-e29b-41d4-a716-446655440000";
$ch = curl_init(
    "https://api.heydollr.app/v1/status/collection/{$referenceId}"
);
curl_setopt_array($ch, [
    CURLOPT_RETURNTRANSFER => true,
    CURLOPT_HTTPHEADER     => ["Authorization: Bearer YOUR_ACCESS_TOKEN"],
]);
$result = json_decode(curl_exec($ch), true);
curl_close($ch);
echo "Status: " . $result["status"];
```

```java Java
import java.net.URI;
import java.net.http.*;

String referenceId = "550e8400-e29b-41d4-a716-446655440000";

HttpClient client = HttpClient.newHttpClient();
HttpRequest request = HttpRequest.newBuilder()
    .uri(URI.create(
        "https://api.heydollr.app/v1/status/collection/" + referenceId
    ))
    .header("Authorization", "Bearer YOUR_ACCESS_TOKEN")
    .GET()
    .build();

HttpResponse<String> response = client.send(request, HttpResponse.BodyHandlers.ofString());
System.out.println(response.body());
```

```go Go
package main

import (
    "fmt"
    "io"
    "net/http"
)

func main() {
    referenceId := "550e8400-e29b-41d4-a716-446655440000"

    req, _ := http.NewRequest("GET",
        "https://api.heydollr.app/v1/status/collection/"+referenceId,
        nil,
    )
    req.Header.Set("Authorization", "Bearer YOUR_ACCESS_TOKEN")

    client := &http.Client{}
    resp, _ := client.Do(req)
    defer resp.Body.Close()

    data, _ := io.ReadAll(resp.Body)
    fmt.Println(string(data))
}
```

</CodeGroup>

---

## Check Payment Source Status

Poll the current payment status of an invoice or order without needing a `reference_id`.

```http
GET /v1/status/source
```

#### Query Parameters

| Param | Type | Required | Description |
|---|---|---|---|
| `source_type` | enum | Yes | `INVOICE` or `ORDER` |
| `source_id` | integer | Yes | ID of the invoice or order |

#### Response — `PaymentSourceStatusResponse`

| Field | Type | Description |
|---|---|---|
| `source_id` | integer | ID of the invoice or order |
| `source_type` | enum | `INVOICE` or `ORDER` |
| `source_number` | string | Auto-generated source number (e.g. `INV-2025-00042`) |
| `status` | string | Current payment status (`IDLE`, `ACTIVE`, `PROCESSING`, `PAID`, `CANCELED`) |
| `currency` | string | ISO 4217 currency code |
| `total_amount` | number | Total amount of the payment source |
| `paid_at` | datetime \| null | Timestamp of payment confirmation, if paid |

#### Code Examples

<CodeGroup>

```bash cURL
curl "https://api.heydollr.app/v1/status/source?source_type=INVOICE&source_id=101" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
```

```python Python
import requests

BASE_URL = "https://api.heydollr.app"
headers  = {"Authorization": "Bearer YOUR_ACCESS_TOKEN"}

response = requests.get(
    f"{BASE_URL}/v1/status/source",
    headers=headers,
    params={
        "source_type": "INVOICE",
        "source_id":   101,
    },
)
result = response.json()
print("Status:", result["status"])
print("Paid at:", result["paid_at"])
```

```javascript Node.js
const BASE_URL = "https://api.heydollr.app";
const TOKEN    = "YOUR_ACCESS_TOKEN";

const params = new URLSearchParams({
  source_type: "INVOICE",
  source_id:   "101",
});

const response = await fetch(`${BASE_URL}/v1/status/source?${params}`, {
  headers: { Authorization: `Bearer ${TOKEN}` },
});
const result = await response.json();
console.log("Status:", result.status);
console.log("Paid at:", result.paid_at);
```

```php PHP
$params = http_build_query([
    "source_type" => "INVOICE",
    "source_id"   => 101,
]);
$ch = curl_init("https://api.heydollr.app/v1/status/source?{$params}");
curl_setopt_array($ch, [
    CURLOPT_RETURNTRANSFER => true,
    CURLOPT_HTTPHEADER     => ["Authorization: Bearer YOUR_ACCESS_TOKEN"],
]);
$result = json_decode(curl_exec($ch), true);
curl_close($ch);
echo "Status: " . $result["status"];
```

```java Java
import java.net.URI;
import java.net.http.*;

HttpClient client = HttpClient.newHttpClient();
HttpRequest request = HttpRequest.newBuilder()
    .uri(URI.create(
        "https://api.heydollr.app/v1/status/source?source_type=INVOICE&source_id=101"
    ))
    .header("Authorization", "Bearer YOUR_ACCESS_TOKEN")
    .GET()
    .build();

HttpResponse<String> response = client.send(request, HttpResponse.BodyHandlers.ofString());
System.out.println(response.body());
```

```go Go
package main

import (
    "fmt"
    "io"
    "net/http"
)

func main() {
    req, _ := http.NewRequest("GET",
        "https://api.heydollr.app/v1/status/source",
        nil,
    )
    q := req.URL.Query()
    q.Add("source_type", "INVOICE")
    q.Add("source_id",   "101")
    req.URL.RawQuery = q.Encode()
    req.Header.Set("Authorization", "Bearer YOUR_ACCESS_TOKEN")

    client := &http.Client{}
    resp, _ := client.Do(req)
    defer resp.Body.Close()

    data, _ := io.ReadAll(resp.Body)
    fmt.Println(string(data))
}
```

Note: The `GET /v1/status/source` endpoint returns the payment source (invoice/order) lifecycle status. Execution endpoints such as `GET /v1/status/collection/{reference_id}` return an `ExecutionResponse` that reflects funds-movement status. Treat source status and execution status as separate state models.

</CodeGroup>

---
