# Checkouts

The Checkout API is a single-call shortcut that creates a counterparty, a payment source (invoice or order), and a hosted checkout session in one request. Use it when you want Dollr to manage the checkout flow without manually wiring together parties, counterparties, invoices/orders, and sessions.

## Create Checkout Source

```http
POST /v1/checkouts/create
```

#### Request Body

| Field | Type | Required | Description |
|---|---|---|---|
| `mode` | string | Yes | Checkout mode (e.g. `HOSTED`, `DIRECT`) |
| `source_kind` | string | Yes | Type of payment source to create (`INVOICE` or `ORDER`) |
| `party_name` | string | Yes | Full name of the paying party |
| `party_phone` | string | Yes | Phone in E.164 digits only, without `+` (e.g. `231771234567`) |
| `party_email` | string \| null | No | Email address of the paying party |
| `party_relationship` | enum \| null | No | Relationship type — see [Relationship Types](counterparties.md#relationship-types) |
| `currency` | string | Yes | ISO 4217 currency code (e.g. `USD`, `LRD`) |
| `items` | array | Yes | Line items for the payment source — see [Item Fields](#item-fields) below |
| `reference_id` | string \| null | No | Your internal reference ID |
| `note` | string \| null | No | A note or description for the payment source |
| `due_date` | datetime \| null | No | ISO 8601 payment due date |
| `success_url` | string \| null | No | URL to redirect to after successful payment |
| `cancel_url` | string \| null | No | URL to redirect to if the payment is cancelled |
| `expires_at` | datetime \| null | No | ISO 8601 session expiry time |

#### Item Fields

Each object in the `items` array must include:

| Field | Type | Required | Description |
|---|---|---|---|
| `name` | string | Yes | Line item name |
| `currency` | string | Yes | ISO 4217 currency code |
| `amount` | number | Yes | Item amount (minimum `0.01`) |

#### Response — `CreateCheckoutSourceResponse`

| Field | Type | Description |
|---|---|---|
| `id` | integer | Checkout record ID |
| `mode` | string | Checkout mode used |
| `source_type` | string | Type of payment source created |
| `source_id` | integer | ID of the created invoice or order |
| `source_number` | string | Auto-generated invoice or order number |
| `source_status` | string | Current status of the payment source |
| `counterparty_id` | integer | ID of the created or matched counterparty |
| `party_id` | integer | ID of the created or matched party |
| `source_checkout_config_id` | integer | Internal checkout config ID |
| `currency` | string | Currency of the payment source |
| `total_amount` | number | Total amount across all items |
| `reference_id` | string \| null | Your supplied reference ID |
| `hosted_path_or_token` | string \| null | Hosted checkout URL path or session token (HOSTED mode) |
| `due_date` | datetime \| null | Due date, if set |
| `expires_at` | datetime \| null | Session expiry time, if set |
| `success_url` | string \| null | Success redirect URL, if set |
| `cancel_url` | string \| null | Cancel redirect URL, if set |

#### Code Examples

=== "cURL"

    ```bash
    curl -X POST "https://api.heydollr.app/v1/checkouts/create" \
      -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
      -H "Content-Type: application/json" \
      -d '{
        "mode":               "HOSTED",
        "source_kind":        "INVOICE",
        "party_name":         "Amara Koroma",
        "party_phone":        "231771234567",
        "party_email":        "amara@example.com",
        "party_relationship": "CUSTOMER",
        "currency":           "USD",
        "items": [
          { "name": "Consulting – June 2025", "currency": "USD", "amount": 150.00 }
        ],
        "success_url": "https://yourapp.com/payment/success",
        "cancel_url":  "https://yourapp.com/payment/cancel"
      }'
    ```

=== "Python"

    ```python
    import requests

    BASE_URL = "https://api.heydollr.app"
    headers  = {
        "Authorization": "Bearer YOUR_ACCESS_TOKEN",
        "Content-Type":  "application/json",
    }

    response = requests.post(
        f"{BASE_URL}/v1/checkouts/create",
        headers=headers,
        json={
            "mode":               "HOSTED",
            "source_kind":        "INVOICE",
            "party_name":         "Amara Koroma",
            "party_phone":        "231771234567",
            "party_email":        "amara@example.com",
            "party_relationship": "CUSTOMER",
            "currency":           "USD",
            "items": [
                {"name": "Consulting – June 2025", "currency": "USD", "amount": 150.00},
            ],
            "success_url": "https://yourapp.com/payment/success",
            "cancel_url":  "https://yourapp.com/payment/cancel",
        },
    )
    checkout = response.json()
    print("Source ID:", checkout["source_id"])
    print("Hosted URL:", checkout["hosted_path_or_token"])
    ```

=== "Node.js"

    ```javascript
    const BASE_URL = "https://api.heydollr.app";
    const TOKEN    = "YOUR_ACCESS_TOKEN";

    const response = await fetch(`${BASE_URL}/v1/checkouts/create`, {
      method: "POST",
      headers: {
        Authorization:  `Bearer ${TOKEN}`,
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        mode:               "HOSTED",
        source_kind:        "INVOICE",
        party_name:         "Amara Koroma",
        party_phone:        "231771234567",
        party_email:        "amara@example.com",
        party_relationship: "CUSTOMER",
        currency:           "USD",
        items: [
          { name: "Consulting – June 2025", currency: "USD", amount: 150.00 },
        ],
        success_url: "https://yourapp.com/payment/success",
        cancel_url:  "https://yourapp.com/payment/cancel",
      }),
    });
    const checkout = await response.json();
    console.log("Source ID:", checkout.source_id);
    console.log("Hosted URL:", checkout.hosted_path_or_token);
    ```

=== "PHP"

    ```php
    $ch = curl_init("https://api.heydollr.app/v1/checkouts/create");
    curl_setopt_array($ch, [
        CURLOPT_RETURNTRANSFER => true,
        CURLOPT_POST           => true,
        CURLOPT_HTTPHEADER     => [
            "Authorization: Bearer YOUR_ACCESS_TOKEN",
            "Content-Type: application/json",
        ],
        CURLOPT_POSTFIELDS => json_encode([
            "mode"               => "HOSTED",
            "source_kind"        => "INVOICE",
            "party_name"         => "Amara Koroma",
            "party_phone"        => "231771234567",
            "party_relationship" => "CUSTOMER",
            "currency"           => "USD",
            "items"              => [
                ["name" => "Consulting – June 2025", "currency" => "USD", "amount" => 150.00],
            ],
            "success_url" => "https://yourapp.com/payment/success",
            "cancel_url"  => "https://yourapp.com/payment/cancel",
        ]),
    ]);
    $checkout = json_decode(curl_exec($ch), true);
    curl_close($ch);
    echo "Source ID: " . $checkout["source_id"];
    ```

=== "Java"

    ```java
    import java.net.URI;
    import java.net.http.*;
    import java.net.http.HttpRequest.BodyPublishers;

    HttpClient client = HttpClient.newHttpClient();

    String body = """
        {
          "mode":               "HOSTED",
          "source_kind":        "INVOICE",
          "party_name":         "Amara Koroma",
          "party_phone":        "231771234567",
          "party_relationship": "CUSTOMER",
          "currency":           "USD",
          "items": [
            { "name": "Consulting – June 2025", "currency": "USD", "amount": 150.00 }
          ],
          "success_url": "https://yourapp.com/payment/success",
          "cancel_url":  "https://yourapp.com/payment/cancel"
        }
        """;

    HttpRequest request = HttpRequest.newBuilder()
        .uri(URI.create("https://api.heydollr.app/v1/checkouts/create"))
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
        type Item struct {
            Name     string  `json:"name"`
            Currency string  `json:"currency"`
            Amount   float64 `json:"amount"`
        }
        payload := map[string]interface{}{
            "mode":               "HOSTED",
            "source_kind":        "INVOICE",
            "party_name":         "Amara Koroma",
            "party_phone":        "231771234567",
            "party_relationship": "CUSTOMER",
            "currency":           "USD",
            "items":              []Item{{Name: "Consulting – June 2025", Currency: "USD", Amount: 150.00}},
            "success_url":        "https://yourapp.com/payment/success",
            "cancel_url":         "https://yourapp.com/payment/cancel",
        }
        body, _ := json.Marshal(payload)

        req, _ := http.NewRequest("POST",
            "https://api.heydollr.app/v1/checkouts/create",
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
