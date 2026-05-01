---
title: "Orders"
description: "Create and manage payment orders for retail and e-commerce flows."
---

# Orders

Orders are informal payment documents — similar to invoices but without a formal invoice number or due date. They follow the same `IDLE > ACTIVE > PROCESSING > PAID / CANCELED` lifecycle.

## Create Order

```http
POST /v1/orders/create
```

| Field | Type | Required | Description |
|---|---|---|---|
| `counterparty_id` | integer | Yes | ID of the counterparty placing the order |
| `currency` | string | Yes | ISO 4217 currency code |
| `note` | string | Yes | Description or note |
| `fee_bearer` | enum | Yes | `PAYER` or `PAYEE` |
| `as_payment_link` | boolean | Yes | Whether to allow sharing as a payment link |
| `reference_id` | string \| null | No | Your internal reference |

#### Example Response

```json
{
  "id": 88,
  "order_number": "ORD-2025-00088",
  "status": "IDLE",
  "currency": "LRD",
  "note": "Market goods – Order #1042",
  "fee_bearer": "PAYEE",
  "as_payment_link": true,
  "counterparty_id": 7,
  "created_at": "2025-06-01T11:00:00Z",
  "updated_at": "2025-06-01T11:00:00Z"
}
```

#### Code Examples

<CodeGroup>

```bash cURL
curl -X POST "https://api.heydollr.app/v1/orders/create" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "counterparty_id": 7,
    "currency":        "LRD",
    "note":            "Market goods – Order #1042",
    "fee_bearer":      "PAYEE",
    "as_payment_link": true
  }'
```

```python Python
import requests

BASE_URL = "https://api.heydollr.app"
headers  = {"Authorization": "Bearer YOUR_ACCESS_TOKEN", "Content-Type": "application/json"}

response = requests.post(
    f"{BASE_URL}/v1/orders/create",
    headers=headers,
    json={
        "counterparty_id": 7,
        "currency":        "LRD",
        "note":            "Market goods – Order #1042",
        "fee_bearer":      "PAYEE",
        "as_payment_link": True,
    },
)
order = response.json()
print("Order ID:", order["id"])
```

```javascript Node.js
const BASE_URL = "https://api.heydollr.app";
const TOKEN    = "YOUR_ACCESS_TOKEN";

const response = await fetch(`${BASE_URL}/v1/orders/create`, {
  method: "POST",
  headers: {
    Authorization:  `Bearer ${TOKEN}`,
    "Content-Type": "application/json",
  },
  body: JSON.stringify({
    counterparty_id: 7,
    currency:        "LRD",
    note:            "Market goods – Order #1042",
    fee_bearer:      "PAYEE",
    as_payment_link: true,
  }),
});
const order = await response.json();
console.log("Order ID:", order.id);
```

```php PHP
$ch = curl_init("https://api.heydollr.app/v1/orders/create");
curl_setopt_array($ch, [
    CURLOPT_RETURNTRANSFER => true,
    CURLOPT_POST           => true,
    CURLOPT_HTTPHEADER     => [
        "Authorization: Bearer YOUR_ACCESS_TOKEN",
        "Content-Type: application/json",
    ],
    CURLOPT_POSTFIELDS => json_encode([
        "counterparty_id" => 7,
        "currency"        => "LRD",
        "note"            => "Market goods – Order #1042",
        "fee_bearer"      => "PAYEE",
        "as_payment_link" => true,
    ]),
]);
$order = json_decode(curl_exec($ch), true);
curl_close($ch);
echo "Order ID: " . $order["id"];
```

```java Java
import java.net.URI;
import java.net.http.*;
import java.net.http.HttpRequest.BodyPublishers;

HttpClient client = HttpClient.newHttpClient();

String body = """
    {
      "counterparty_id": 7,
      "currency":        "LRD",
      "note":            "Market goods – Order #1042",
      "fee_bearer":      "PAYEE",
      "as_payment_link": true
    }
    """;

HttpRequest request = HttpRequest.newBuilder()
    .uri(URI.create("https://api.heydollr.app/v1/orders/create"))
    .header("Authorization", "Bearer YOUR_ACCESS_TOKEN")
    .header("Content-Type", "application/json")
    .POST(BodyPublishers.ofString(body))
    .build();

HttpResponse<String> response = client.send(request, HttpResponse.BodyHandlers.ofString());
System.out.println(response.body());
```

```go Go
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
        "counterparty_id": 7,
        "currency":        "LRD",
        "note":            "Market goods – Order #1042",
        "fee_bearer":      "PAYEE",
        "as_payment_link": true,
    }
    body, _ := json.Marshal(payload)

    req, _ := http.NewRequest("POST",
        "https://api.heydollr.app/v1/orders/create",
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

</CodeGroup>

## Order Items

```http
POST   /v1/orders/{order_id}/items/add
PUT    /v1/orders/{order_id}/items/{id}/update
DELETE /v1/orders/{order_id}/items/{id}/remove
```

Item request and response schemas are identical to invoice items: `name`, `currency`, `qty`, and `amount` are required when adding an item.

## Other Order Endpoints

```http
PUT    /v1/orders/publish/{id}                       — Publish order (IDLE → ACTIVE)
PUT    /v1/orders/update/{id}                        — Update metadata while IDLE
GET    /v1/orders/list                               — List orders (filter by currency, status)
GET    /v1/orders/retrieve/{id}                      — Retrieve by system ID
GET    /v1/orders/retrieve/number/{order_number}     — Retrieve by order number
GET    /v1/orders/receipt/{id}                       — Receipt by system ID (post-payment)
GET    /v1/orders/receipt/number/{order_number}      — Receipt by order number
DELETE /v1/orders/cancel/{id}                        — Cancel an order
```

---
