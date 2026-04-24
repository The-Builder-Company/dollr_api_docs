# Payment Accounts

Payment Accounts represent the specific account numbers (mobile wallets, card accounts, etc.) associated with a Party.

## Create Payment Account

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
| `provider` | enum | Yes | `MTN_MOMO_LBR`, `ORANGE_MONEY_LBR`, `PAWAPAY`, `STRIPE`, or `PLATFORM` |
| `method` | enum | Yes | `MTN_MOMO_LBR`, `ORANGE_MONEY_LBR`, `AIRTEL_RWA`, `MTN_MOMO_RWA`, `ORANGE_MONEY_RWA`, `CREDIT_CARD`, or `WALLET` |
| `party_id` | integer | Yes | ID of the Party this account belongs to |
| `country_code` | string \| null | No | ISO 3166-1 alpha-2 country code |
| `insensitive_account_number` | string \| null | No | Account number (e.g., mobile number) for display |

#### Code Examples

=== "cURL"

    ```bash
    curl -X POST "https://api.heydollr.app/v1/payment-accounts/create?operation_type=COLLECTION" \
      -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
      -H "Content-Type: application/json" \
      -d '{
        "account_name":               "Amara MTN Wallet",
        "provider":                   "MTN_MOMO_LBR",
        "method":                     "MTN_MOMO_LBR",
        "party_id":                   42,
        "country_code":               "LR",
        "insensitive_account_number": "231771234567"
      }'
    ```

=== "Python"

    ```python
    import requests

    BASE_URL = "https://api.heydollr.app"
    headers  = {"Authorization": "Bearer YOUR_ACCESS_TOKEN", "Content-Type": "application/json"}

    response = requests.post(
        f"{BASE_URL}/v1/payment-accounts/create",
        headers=headers,
        params={"operation_type": "COLLECTION"},
        json={
            "account_name":               "Amara MTN Wallet",
            "provider":                   "MTN_MOMO_LBR",
            "method":                     "MTN_MOMO_LBR",
            "party_id":                   42,
            "country_code":               "LR",
            "insensitive_account_number": "231771234567",
        },
    )
    account = response.json()
    print("Payment Account ID:", account["id"])
    ```

=== "Node.js"

    ```javascript
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

=== "PHP"

    ```php
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

=== "Java"

    ```java
    import java.net.URI;
    import java.net.http.*;
    import java.net.http.HttpRequest.BodyPublishers;

    HttpClient client = HttpClient.newHttpClient();

    String body = """
        {
          "account_name":               "Amara MTN Wallet",
          "provider":                   "MTN_MOMO_LBR",
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
            "account_name":               "Amara MTN Wallet",
            "provider":                   "MTN_MOMO_LBR",
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

---
