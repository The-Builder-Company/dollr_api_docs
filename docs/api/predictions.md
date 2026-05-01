---
title: "Predictions"
description: "Preview fees, FX rates, and detect mobile money providers before executing."
---

# Predictions

Prediction endpoints let you preview amounts and fees before committing to a transaction.

## Predict Amount and Fees

```http
GET /v1/predictions/amount-and-fees
```

#### Query Parameters

| Param | Type | Required | Description |
|---|---|---|---|
| `base_amount` | number | Yes | The starting amount to calculate against |
| `base_currency` | string | Yes | ISO 4217 currency code of the base amount |
| `target_currency` | string | Yes | ISO 4217 currency code the payee will receive |
| `payment_method` | enum | Yes | `MTN_MOMO_LBR`, `ORANGE_MONEY_LBR`, `AIRTEL_RWA`, `MTN_MOMO_RWA`, `ORANGE_MONEY_RWA`, `CREDIT_CARD`, or `WALLET` |
| `operation_type` | enum | Yes | `COLLECTION`, `PAYOUT`, `TRANSFER`, or `REFUND` |
| `provider` | enum | Yes | `PAWAPAY`, `STRIPE`, or `PLATFORM` |
| `fee_bearer` | enum | Yes | `PAYER` or `PAYEE` |
| `owner_type` | enum \| null | No | `USER`, `MICRO_ORGANIZATION`, or `ORGANIZATION` |
| `owner_id` | integer \| null | No | ID of the owner entity |

#### Response — `AmountAndFeePredictionResponse`

| Field | Type | Description |
|---|---|---|
| `payer_amount` | string | Total amount the payer will be charged |
| `payer_currency` | string | Currency the payer pays in |
| `payee_amount` | string | Amount the payee receives after all fees |
| `payee_currency` | string | Currency the payee receives |
| `platform_fee` | string | Dollr platform fee |
| `platform_currency` | string | Currency of the platform fee |
| `fx_fee` | string \| null | FX conversion fee, if applicable |
| `gateway_fee` | string \| null | Payment gateway fee, if applicable |
| `gateway_currency` | string \| null | Currency of the gateway fee |

#### Code Examples

<CodeGroup>

```bash cURL
curl "https://api.heydollr.app/v1/predictions/amount-and-fees?base_amount=100&base_currency=USD&target_currency=USD&payment_method=MTN_MOMO_LBR&operation_type=COLLECTION&provider=PAWAPAY&fee_bearer=PAYER" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
```

```python Python
import requests

BASE_URL = "https://api.heydollr.app"
headers  = {"Authorization": "Bearer YOUR_ACCESS_TOKEN"}

response = requests.get(
    f"{BASE_URL}/v1/predictions/amount-and-fees",
    headers=headers,
    params={
        "base_amount":     100,
        "base_currency":   "USD",
        "target_currency": "USD",
        "payment_method":  "MTN_MOMO_LBR",
        "operation_type":  "COLLECTION",
        "provider":        "PAWAPAY",
        "fee_bearer":      "PAYER",
    },
)
p = response.json()
print(f"Payer pays: {p['payer_amount']} {p['payer_currency']}")
print(f"Payee gets: {p['payee_amount']} {p['payee_currency']}")
print(f"Platform fee: {p['platform_fee']}")
```

```javascript Node.js
const BASE_URL = "https://api.heydollr.app";
const TOKEN    = "YOUR_ACCESS_TOKEN";

const params = new URLSearchParams({
  base_amount:     "100",
  base_currency:   "USD",
  target_currency: "USD",
  payment_method:  "MTN_MOMO_LBR",
  operation_type:  "COLLECTION",
  provider:        "PAWAPAY",
  fee_bearer:      "PAYER",
});

const response = await fetch(`${BASE_URL}/v1/predictions/amount-and-fees?${params}`, {
  headers: { Authorization: `Bearer ${TOKEN}` },
});
const p = await response.json();
console.log(`Payer pays: ${p.payer_amount} ${p.payer_currency}`);
console.log(`Payee gets: ${p.payee_amount} ${p.payee_currency}`);
```

```php PHP
$params = http_build_query([
    "base_amount"     => 100,
    "base_currency"   => "USD",
    "target_currency" => "USD",
    "payment_method"  => "MTN_MOMO_LBR",
    "operation_type"  => "COLLECTION",
    "provider"        => "PAWAPAY",
    "fee_bearer"      => "PAYER",
]);

$ch = curl_init("https://api.heydollr.app/v1/predictions/amount-and-fees?{$params}");
curl_setopt_array($ch, [
    CURLOPT_RETURNTRANSFER => true,
    CURLOPT_HTTPHEADER     => ["Authorization: Bearer YOUR_ACCESS_TOKEN"],
]);
$p = json_decode(curl_exec($ch), true);
curl_close($ch);
echo "Payer pays: " . $p["payer_amount"] . " " . $p["payer_currency"];
```

```java Java
import java.net.URI;
import java.net.http.*;

String url = "https://api.heydollr.app/v1/predictions/amount-and-fees"
    + "?base_amount=100&base_currency=USD&target_currency=USD"
    + "&payment_method=MTN_MOMO_LBR&operation_type=COLLECTION"
    + "&provider=PAWAPAY&fee_bearer=PAYER";

HttpClient client = HttpClient.newHttpClient();
HttpRequest request = HttpRequest.newBuilder()
    .uri(URI.create(url))
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
        "https://api.heydollr.app/v1/predictions/amount-and-fees",
        nil,
    )
    q := req.URL.Query()
    q.Add("base_amount",     "100")
    q.Add("base_currency",   "USD")
    q.Add("target_currency", "USD")
    q.Add("payment_method",  "MTN_MOMO_LBR")
    q.Add("operation_type",  "COLLECTION")
    q.Add("provider",        "PAWAPAY")
    q.Add("fee_bearer",      "PAYER")
    req.URL.RawQuery = q.Encode()
    req.Header.Set("Authorization", "Bearer YOUR_ACCESS_TOKEN")

    client := &http.Client{}
    resp, _ := client.Do(req)
    defer resp.Body.Close()

    data, _ := io.ReadAll(resp.Body)
    fmt.Println(string(data))
}
```

</CodeGroup>

## Predict Payment Source Amount and Fees

```http
GET /v1/predictions/payment-source/amount-and-fees
```

| Param | Type | Required | Description |
|---|---|---|---|
| `target_currency` | string | Yes | ISO 4217 currency code the payee will receive |
| `payment_method` | enum | Yes | `MTN_MOMO_LBR`, `ORANGE_MONEY_LBR`, `AIRTEL_RWA`, `MTN_MOMO_RWA`, `ORANGE_MONEY_RWA`, `CREDIT_CARD`, or `WALLET` |
| `provider` | enum | Yes | `PAWAPAY`, `STRIPE`, or `PLATFORM` |
| `source_type` | enum | Yes | `INVOICE` or `ORDER` |
| `source_id` | integer | Yes | ID of the invoice or order |

## Predict MMO Provider Info

```http
GET /v1/predictions/mmo-provider-info
```

| Param | Type | Required | Description |
|---|---|---|---|
| `phone` | string | Yes | E.164 phone number without `+` (e.g. `231771234567`) |
| `operation_type` | string | Yes | `COLLECTION`, `PAYOUT`, `TRANSFER`, or `REFUND` |

#### Response — `PredictPhonePaymentInfoResponse`

| Field | Type | Description |
|---|---|---|
| `carrier` | string | Mobile network operator name |
| `country` | string | Country associated with the phone number |
| `currencies` | string[] | Supported ISO 4217 currency codes for this carrier |
| `phone` | string | The queried phone number |
| `payment_method` | string | Recommended payment method identifier |
| `gateway_provider` | string | Recommended gateway provider — the routing network or gateway that will process the payment (for example `PAWAPAY`, `STRIPE`, or `PLATFORM`). |
| `operation_type` | string | The operation type used in the query |

#### Code Examples

<CodeGroup>

```bash cURL
curl "https://api.heydollr.app/v1/predictions/mmo-provider-info?phone=231771234567&operation_type=COLLECTION" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
```

```python Python
response = requests.get(
    f"{BASE_URL}/v1/predictions/mmo-provider-info",
    headers=headers,
    params={
        "phone":          "231771234567",
        "operation_type": "COLLECTION",
    },
)
info = response.json()
print("Carrier:", info["carrier"])
print("Method:", info["payment_method"])
print("Provider:", info["gateway_provider"])
```

```javascript Node.js
const params = new URLSearchParams({
  phone:          "231771234567",
  operation_type: "COLLECTION",
});
const response = await fetch(`${BASE_URL}/v1/predictions/mmo-provider-info?${params}`, {
  headers: { Authorization: `Bearer ${TOKEN}` },
});
const info = await response.json();
console.log("Carrier:", info.carrier);
console.log("Method:", info.payment_method);
```

```php PHP
$params = http_build_query([
    "phone"          => "231771234567",
    "operation_type" => "COLLECTION",
]);
$ch = curl_init("https://api.heydollr.app/v1/predictions/mmo-provider-info?{$params}");
curl_setopt_array($ch, [
    CURLOPT_RETURNTRANSFER => true,
    CURLOPT_HTTPHEADER     => ["Authorization: Bearer YOUR_ACCESS_TOKEN"],
]);
$info = json_decode(curl_exec($ch), true);
curl_close($ch);
echo "Carrier: " . $info["carrier"] . ", Method: " . $info["payment_method"];
```

```java Java
HttpRequest request = HttpRequest.newBuilder()
    .uri(URI.create(
        "https://api.heydollr.app/v1/predictions/mmo-provider-info"
        + "?phone=231771234567&operation_type=COLLECTION"
    ))
    .header("Authorization", "Bearer YOUR_ACCESS_TOKEN")
    .GET()
    .build();

HttpResponse<String> response = client.send(request, HttpResponse.BodyHandlers.ofString());
System.out.println(response.body());
```

```go Go
req, _ := http.NewRequest("GET",
    "https://api.heydollr.app/v1/predictions/mmo-provider-info",
    nil,
)
q := req.URL.Query()
q.Add("phone",          "231771234567")
q.Add("operation_type", "COLLECTION")
req.URL.RawQuery = q.Encode()
req.Header.Set("Authorization", "Bearer YOUR_ACCESS_TOKEN")

client := &http.Client{}
resp, _ := client.Do(req)
defer resp.Body.Close()

data, _ := io.ReadAll(resp.Body)
fmt.Println(string(data))
```

</CodeGroup>

---
