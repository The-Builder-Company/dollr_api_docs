---
title: "Invoices"
description: "Create, manage, and publish invoices with line items and payment links."
---

# Invoices

Invoices are formal billing documents with auto-generated invoice numbers, due dates, and line items.

## Invoice Lifecycle

| Status | Meaning |
|---|---|
| `IDLE` | Created but not yet published. Can be edited; items can be added/removed. |
| `ACTIVE` | Published and ready for payment. Editing is locked. |
| `PROCESSING` | A payment attempt is in progress. |
| `PAID` | Payment confirmed. Invoice is closed. |
| `CANCELED` | Canceled and no longer payable. |

## Create Invoice

```http
POST /v1/invoices/create
```

#### Request Body

| Field | Type | Required | Description |
|---|---|---|---|
| `counterparty_id` | integer | Yes | ID of the counterparty being invoiced |
| `currency` | string | Yes | ISO 4217 currency code (e.g. `USD`, `LRD`) |
| `note` | string | Yes | Description or note for this invoice |
| `fee_bearer` | enum | Yes | `PAYER` or `PAYEE` |
| `as_payment_link` | boolean | Yes | Whether the invoice can be shared as a payment link |
| `reference_id` | string \| null | No | Your internal reference ID |
| `due_date` | datetime \| null | No | ISO 8601 payment due date |

#### Code Examples

<CodeGroup>

```bash cURL
curl -X POST "https://api.heydollr.app/v1/invoices/create" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "counterparty_id": 7,
    "currency":        "USD",
    "note":            "Consulting services – June 2025",
    "fee_bearer":      "PAYER",
    "as_payment_link": true,
    "due_date":        "2025-06-30T23:59:00Z"
  }'
```

```python Python
import requests

BASE_URL = "https://api.heydollr.app"
headers  = {"Authorization": "Bearer YOUR_ACCESS_TOKEN", "Content-Type": "application/json"}

response = requests.post(
    f"{BASE_URL}/v1/invoices/create",
    headers=headers,
    json={
        "counterparty_id": 7,
        "currency":        "USD",
        "note":            "Consulting services – June 2025",
        "fee_bearer":      "PAYER",
        "as_payment_link": True,
        "due_date":        "2025-06-30T23:59:00Z",
    },
)
invoice = response.json()
print("Invoice ID:", invoice["id"])
print("Invoice Number:", invoice["invoice_number"])
```

```javascript Node.js
const BASE_URL = "https://api.heydollr.app";
const TOKEN    = "YOUR_ACCESS_TOKEN";

const response = await fetch(`${BASE_URL}/v1/invoices/create`, {
  method: "POST",
  headers: {
    Authorization:  `Bearer ${TOKEN}`,
    "Content-Type": "application/json",
  },
  body: JSON.stringify({
    counterparty_id: 7,
    currency:        "USD",
    note:            "Consulting services – June 2025",
    fee_bearer:      "PAYER",
    as_payment_link: true,
    due_date:        "2025-06-30T23:59:00Z",
  }),
});
const invoice = await response.json();
console.log("Invoice ID:", invoice.id);
console.log("Invoice Number:", invoice.invoice_number);
```

```php PHP
$ch = curl_init("https://api.heydollr.app/v1/invoices/create");
curl_setopt_array($ch, [
    CURLOPT_RETURNTRANSFER => true,
    CURLOPT_POST           => true,
    CURLOPT_HTTPHEADER     => [
        "Authorization: Bearer YOUR_ACCESS_TOKEN",
        "Content-Type: application/json",
    ],
    CURLOPT_POSTFIELDS => json_encode([
        "counterparty_id" => 7,
        "currency"        => "USD",
        "note"            => "Consulting services – June 2025",
        "fee_bearer"      => "PAYER",
        "as_payment_link" => true,
        "due_date"        => "2025-06-30T23:59:00Z",
    ]),
]);
$invoice = json_decode(curl_exec($ch), true);
curl_close($ch);
echo "Invoice Number: " . $invoice["invoice_number"];
```

```java Java
import java.net.URI;
import java.net.http.*;
import java.net.http.HttpRequest.BodyPublishers;

HttpClient client = HttpClient.newHttpClient();

String body = """
    {
      "counterparty_id": 7,
      "currency":        "USD",
      "note":            "Consulting services – June 2025",
      "fee_bearer":      "PAYER",
      "as_payment_link": true,
      "due_date":        "2025-06-30T23:59:00Z"
    }
    """;

HttpRequest request = HttpRequest.newBuilder()
    .uri(URI.create("https://api.heydollr.app/v1/invoices/create"))
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
        "currency":        "USD",
        "note":            "Consulting services – June 2025",
        "fee_bearer":      "PAYER",
        "as_payment_link": true,
        "due_date":        "2025-06-30T23:59:00Z",
    }
    body, _ := json.Marshal(payload)

    req, _ := http.NewRequest("POST",
        "https://api.heydollr.app/v1/invoices/create",
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

## Add Invoice Item

```http
POST /v1/invoices/{invoice_id}/items/add
```

Items can only be added while the invoice is in `IDLE` status.

| Field | Type | Required | Description |
|---|---|---|---|
| `name` | string | Yes | Name or description of the line item |
| `currency` | string | Yes | ISO 4217 currency code |
| `qty` | integer | Yes | Quantity (minimum 1) |
| `amount` | number | Yes | Unit price (min 0.01 for decimals, 1 for integers) |

#### Code Examples

<CodeGroup>

```bash cURL
curl -X POST "https://api.heydollr.app/v1/invoices/101/items/add" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "name":     "Strategy Session",
    "currency": "USD",
    "qty":      2,
    "amount":   150.00
  }'
```

```python Python
invoice_id = 101
response = requests.post(
    f"{BASE_URL}/v1/invoices/{invoice_id}/items/add",
    headers=headers,
    json={
        "name":     "Strategy Session",
        "currency": "USD",
        "qty":      2,
        "amount":   150.00,
    },
)
item = response.json()
print("Item ID:", item["id"])
```

```javascript Node.js
const invoiceId = 101;
const response = await fetch(`${BASE_URL}/v1/invoices/${invoiceId}/items/add`, {
  method: "POST",
  headers: {
    Authorization:  `Bearer ${TOKEN}`,
    "Content-Type": "application/json",
  },
  body: JSON.stringify({
    name:     "Strategy Session",
    currency: "USD",
    qty:      2,
    amount:   150.00,
  }),
});
const item = await response.json();
console.log("Item ID:", item.id);
```

```php PHP
$invoiceId = 101;
$ch = curl_init(
    "https://api.heydollr.app/v1/invoices/{$invoiceId}/items/add"
);
curl_setopt_array($ch, [
    CURLOPT_RETURNTRANSFER => true,
    CURLOPT_POST           => true,
    CURLOPT_HTTPHEADER     => [
        "Authorization: Bearer YOUR_ACCESS_TOKEN",
        "Content-Type: application/json",
    ],
    CURLOPT_POSTFIELDS => json_encode([
        "name"     => "Strategy Session",
        "currency" => "USD",
        "qty"      => 2,
        "amount"   => 150.00,
    ]),
]);
$item = json_decode(curl_exec($ch), true);
curl_close($ch);
echo "Item ID: " . $item["id"];
```

```java Java
int invoiceId = 101;
String body = """
    {
      "name":     "Strategy Session",
      "currency": "USD",
      "qty":      2,
      "amount":   150.00
    }
    """;

HttpRequest request = HttpRequest.newBuilder()
    .uri(URI.create(
        "https://api.heydollr.app/v1/invoices/"
        + invoiceId + "/items/add"
    ))
    .header("Authorization", "Bearer YOUR_ACCESS_TOKEN")
    .header("Content-Type", "application/json")
    .POST(BodyPublishers.ofString(body))
    .build();

HttpResponse<String> response = client.send(request, HttpResponse.BodyHandlers.ofString());
System.out.println(response.body());
```

```go Go
invoiceId := 101
payload := map[string]interface{}{
    "name":     "Strategy Session",
    "currency": "USD",
    "qty":      2,
    "amount":   150.00,
}
body, _ := json.Marshal(payload)

url := fmt.Sprintf(
    "https://api.heydollr.app/v1/invoices/%d/items/add",
    invoiceId,
)
req, _ := http.NewRequest("POST", url, bytes.NewBuffer(body))
req.Header.Set("Authorization", "Bearer YOUR_ACCESS_TOKEN")
req.Header.Set("Content-Type", "application/json")

client := &http.Client{}
resp, _ := client.Do(req)
defer resp.Body.Close()

data, _ := io.ReadAll(resp.Body)
fmt.Println(string(data))
```

</CodeGroup>

## Update Invoice Item

```http
PUT /v1/invoices/{invoice_id}/items/{id}/update
```

| Field | Type | Required | Description |
|---|---|---|---|
| `name` | string \| null | No | New item name |
| `qty` | integer \| null | No | New quantity |
| `amount` | number \| null | No | New unit price |

## Remove Invoice Item

```http
DELETE /v1/invoices/{invoice_id}/items/{id}/remove
```

Returns an empty object `{}` on success.

## Publish Invoice

```http
PUT /v1/invoices/publish/{id}
```

Transitions the invoice from `IDLE` to `ACTIVE`. No request body required.

#### Code Examples

<CodeGroup>

```bash cURL
curl -X PUT "https://api.heydollr.app/v1/invoices/publish/101" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
```

```python Python
invoice_id = 101
response = requests.put(
    f"{BASE_URL}/v1/invoices/publish/{invoice_id}",
    headers=headers,
)
print("Status:", response.json()["status"])  # ACTIVE
```

```javascript Node.js
const invoiceId = 101;
const response = await fetch(`${BASE_URL}/v1/invoices/publish/${invoiceId}`, {
  method: "PUT",
  headers: { Authorization: `Bearer ${TOKEN}` },
});
const invoice = await response.json();
console.log("Status:", invoice.status); // ACTIVE
```

```php PHP
$invoiceId = 101;
$ch = curl_init(
    "https://api.heydollr.app/v1/invoices/publish/{$invoiceId}"
);
curl_setopt_array($ch, [
    CURLOPT_RETURNTRANSFER => true,
    CURLOPT_CUSTOMREQUEST  => "PUT",
    CURLOPT_HTTPHEADER     => ["Authorization: Bearer YOUR_ACCESS_TOKEN"],
]);
$invoice = json_decode(curl_exec($ch), true);
curl_close($ch);
echo "Status: " . $invoice["status"]; // ACTIVE
```

```java Java
int invoiceId = 101;
HttpRequest request = HttpRequest.newBuilder()
    .uri(URI.create(
        "https://api.heydollr.app/v1/invoices/publish/" + invoiceId
    ))
    .header("Authorization", "Bearer YOUR_ACCESS_TOKEN")
    .PUT(BodyPublishers.noBody())
    .build();

HttpResponse<String> response = client.send(request, HttpResponse.BodyHandlers.ofString());
System.out.println(response.body());
```

```go Go
invoiceId := 101
url := fmt.Sprintf(
    "https://api.heydollr.app/v1/invoices/publish/%d",
    invoiceId,
)
req, _ := http.NewRequest("PUT", url, nil)
req.Header.Set("Authorization", "Bearer YOUR_ACCESS_TOKEN")

client := &http.Client{}
resp, _ := client.Do(req)
defer resp.Body.Close()

data, _ := io.ReadAll(resp.Body)
fmt.Println(string(data))
```

</CodeGroup>

## Update Invoice

```http
PUT /v1/invoices/update/{id}
```

Only available while the invoice is in `IDLE` status.

| Field | Type | Required | Description |
|---|---|---|---|
| `reference_id` | string \| null | No | Your internal reference |
| `note` | string \| null | No | Updated description |
| `fee_bearer` | string \| null | No | `PAYER` or `PAYEE` |
| `due_date` | datetime \| null | No | Updated due date |

## List Invoices

```http
GET /v1/invoices/list
```

| Query Param | Type | Required | Description |
|---|---|---|---|
| `currency` | string \| null | No | Filter by ISO 4217 currency code |
| `status` | string \| null | No | Filter by status: `IDLE`, `ACTIVE`, `PROCESSING`, `PAID`, `CANCELED` |

#### Code Examples

<CodeGroup>

```bash cURL
curl "https://api.heydollr.app/v1/invoices/list?status=ACTIVE" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
```

```python Python
response = requests.get(
    f"{BASE_URL}/v1/invoices/list",
    headers=headers,
    params={"status": "ACTIVE"},
)
for inv in response.json():
    print(inv["invoice_number"], inv["total_amount"])
```

```javascript Node.js
const response = await fetch(`${BASE_URL}/v1/invoices/list?status=ACTIVE`, {
  headers: { Authorization: `Bearer ${TOKEN}` },
});
const invoices = await response.json();
invoices.forEach(inv => console.log(inv.invoice_number, inv.total_amount));
```

```php PHP
$ch = curl_init(
    "https://api.heydollr.app/v1/invoices/list?status=ACTIVE"
);
curl_setopt_array($ch, [
    CURLOPT_RETURNTRANSFER => true,
    CURLOPT_HTTPHEADER     => ["Authorization: Bearer YOUR_ACCESS_TOKEN"],
]);
$invoices = json_decode(curl_exec($ch), true);
curl_close($ch);
foreach ($invoices as $inv) {
    echo $inv["invoice_number"] . "\n";
}
```

```java Java
HttpRequest request = HttpRequest.newBuilder()
    .uri(URI.create(
        "https://api.heydollr.app/v1/invoices/list?status=ACTIVE"
    ))
    .header("Authorization", "Bearer YOUR_ACCESS_TOKEN")
    .GET()
    .build();

HttpResponse<String> response = client.send(request, HttpResponse.BodyHandlers.ofString());
System.out.println(response.body());
```

```go Go
req, _ := http.NewRequest("GET",
    "https://api.heydollr.app/v1/invoices/list?status=ACTIVE",
    nil,
)
req.Header.Set("Authorization", "Bearer YOUR_ACCESS_TOKEN")

client := &http.Client{}
resp, _ := client.Do(req)
defer resp.Body.Close()

data, _ := io.ReadAll(resp.Body)
fmt.Println(string(data))
```

</CodeGroup>

## Retrieve Invoice

```http
GET /v1/invoices/retrieve/{id}
GET /v1/invoices/retrieve/number/{invoice_number}
```

Both return `InvoiceDetailResponse`, which includes line items and the linked counterparty.

## Retrieve Invoice Receipt

Receipts are available after an invoice has been paid. They include full payment details: amounts, fees, FX rate, provider, and line items.

```http
GET /v1/invoices/receipt/{id}
GET /v1/invoices/receipt/number/{invoice_number}
```

## Cancel Invoice

```http
DELETE /v1/invoices/cancel/{id}
```

A canceled invoice cannot be reactivated. No request body required.

---
