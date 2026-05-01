---
title: "Payment Accounts"
description: "Register and manage mobile money or card accounts for a party."
---

# Payment Accounts

Payment Accounts represent the specific account numbers (mobile wallets, card accounts, etc.) associated with a Party.

## Create Payment Account

Note: `provider` identifies the routing network or gateway (e.g. `PAWAPAY`, `STRIPE`, `PLATFORM`). `method` identifies the payment instrument or method identifier (e.g. `MTN_MOMO_LBR`, `ORANGE_MONEY_RWA`, `CREDIT_CARD`, `WALLET`). Keep these concepts distinct when selecting values for requests and examples.

```http
POST /v1/payment-accounts/create?operation_type={type}
```

#### Query Parameters

| Param | Type | Required | Description |
|---|---|---|---|
| `operation_type` | enum | Yes | `COLLECTION`, `PAYOUT`, `TRANSFER`, or `REFUND` |

#### Request Body

| Field | Type | Required | Description |
|---|---|---|---|
| `account_name` | string | Yes | Display name for this payment account |
| `provider` | enum | Yes | `PAWAPAY`, `STRIPE`, or `PLATFORM` |
| `method` | enum | Yes | `MTN_MOMO_LBR`, `ORANGE_MONEY_LBR`, `AIRTEL_RWA`, `MTN_MOMO_RWA`, `ORANGE_MONEY_RWA`, `CREDIT_CARD`, or `WALLET` |
| `party_id` | integer | Yes | ID of the Party this account belongs to |
| `country_code` | string \| null | No | ISO 3166-1 alpha-2 country code |
| `insensitive_account_number` | string \| null | No | Account number (e.g., mobile number) for display |

#### Code Examples

<CodeGroup>

```text cURL
    ```bash
    curl -X POST "https://api.heydollr.app/v1/payment-accounts/create?operation_type=COLLECTION" \
        -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
        -H "Content-Type: application/json" \
        -d '{
            "account_name":               "Amara MTN Wallet",
            "provider":                   "PAWAPAY",
            "method":                     "MTN_MOMO_LBR",
            "party_id":                   42,
            "country_code":               "LR",
            "insensitive_account_number": "231771234567"
        }'
    ```
```

```python Python
import requests

BASE_URL = "https://api.heydollr.app"
headers  = {"Authorization": "Bearer YOUR_ACCESS_TOKEN", "Content-Type": "application/json"}

response = requests.post(
    f"{BASE_URL}/v1/payment-accounts/create",
    headers=headers,
    params={"operation_type": "COLLECTION"},
    json={
        "account_name":               "Amara MTN Wallet",
        "provider":                   "PAWAPAY",
        "method":                     "MTN_MOMO_LBR",
        "party_id":                   42,
        "country_code":               "LR",
        "insensitive_account_number": "231771234567",
    },
)
account = response.json()
print("Payment Account ID:", account["id"])
```

```javascript Node.js
const BASE_URL = "https://api.heydollr.app";
const TOKEN    = "YOUR_ACCESS_TOKEN";

const response = await fetch(
  `${BASE_URL}/v1/payment-accounts/create?operation_type=COLLECTION`,
  {
    method: "POST",
    headers: {
      Authorization:  `Bearer ${TOKEN}`,
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      account_name:               "Amara MTN Wallet",
      provider:                   "MTN_MOMO_LBR",
      method:                     "MTN_MOMO_LBR",
      party_id:                   42,
      country_code:               "LR",
      insensitive_account_number: "231771234567",
    }),
  }
);
const account = await response.json();
console.log("Payment Account ID:", account.id);
```

```php PHP
$ch = curl_init(
    "https://api.heydollr.app/v1/payment-accounts/create?operation_type=COLLECTION"
);
curl_setopt_array($ch, [
    CURLOPT_RETURNTRANSFER => true,
    CURLOPT_POST           => true,
    CURLOPT_HTTPHEADER     => [
        "Authorization: Bearer YOUR_ACCESS_TOKEN",
        "Content-Type: application/json",
    ],
    CURLOPT_POSTFIELDS => json_encode([
        "account_name"               => "Amara MTN Wallet",
        "provider"                   => "MTN_MOMO_LBR",
        "method"                     => "MTN_MOMO_LBR",
        "party_id"                   => 42,
        "country_code"               => "LR",
        "insensitive_account_number" => "231771234567",
    ]),
]);
$account = json_decode(curl_exec($ch), true);
curl_close($ch);
echo "Payment Account ID: " . $account["id"];
```

```java Java
import java.net.URI;
import java.net.http.*;
import java.net.http.HttpRequest.BodyPublishers;

HttpClient client = HttpClient.newHttpClient();

String body = """
    {
      "account_name":               "Amara MTN Wallet",
      "provider":                   "PAWAPAY",
      "method":                     "MTN_MOMO_LBR",
      "party_id":                   42,
      "country_code":               "LR",
      "insensitive_account_number": "231771234567"
    }
    """;

HttpRequest request = HttpRequest.newBuilder()
    .uri(URI.create(
        "https://api.heydollr.app/v1/payment-accounts/create?operation_type=COLLECTION"
    ))
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
        "account_name":               "Amara MTN Wallet",
        "provider":                   "PAWAPAY",
        "method":                     "MTN_MOMO_LBR",
        "party_id":                   42,
        "country_code":               "LR",
        "insensitive_account_number": "231771234567",
    }
    body, _ := json.Marshal(payload)

    req, _ := http.NewRequest("POST",
        "https://api.heydollr.app/v1/payment-accounts/create?operation_type=COLLECTION",
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

---
