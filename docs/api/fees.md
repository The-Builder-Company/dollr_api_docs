# Fees

The Fees endpoints give programmatic access to Dollr's fee structures.

## Get Gateway Fees

```http
GET /v1/fees/gateway
```

| Param | Type | Required | Description |
|---|---|---|---|
| `payment_method` | string | Yes | Payment method identifier |
| `operation_type` | string | Yes | `COLLECTION`, `PAYOUT`, `TRANSFER`, or `REFUND` |

## Get Platform Fees

```http
GET /v1/fees/platform
```

| Param | Type | Required | Description |
|---|---|---|---|
| `operation_type` | string | Yes | `COLLECTION`, `PAYOUT`, `TRANSFER`, or `REFUND` |
| `fee_tier_name` | string | Yes | Fee tier name (obtain from List Fee Tiers) |

## Get Merchant Fee Tier

```http
GET /v1/fees/merchant-tier
```

| Param | Type | Required | Description |
|---|---|---|---|
| `owner_type` | string | Yes | `USER`, `MICRO_ORGANIZATION`, or `ORGANIZATION` |
| `owner_id` | integer | Yes | Your merchant entity ID |

## List Fee Tiers

```http
GET /v1/fees/tiers
```

Returns an array of `FeeTierResponse` objects. Use the `name` field when querying platform fees.

#### Code Examples

=== "cURL"

    ```bash
    # Gateway fees
    curl "https://api.heydollr.app/v1/fees/gateway?payment_method=MTN_MOMO_LBR&operation_type=COLLECTION" \
      -H "Authorization: Bearer YOUR_ACCESS_TOKEN"

    # List all fee tiers
    curl "https://api.heydollr.app/v1/fees/tiers" \
      -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
    ```

=== "Python"

    ```python
    import requests

    BASE_URL = "https://api.heydollr.app"
    headers  = {"Authorization": "Bearer YOUR_ACCESS_TOKEN"}

    # Gateway fees
    response = requests.get(
        f"{BASE_URL}/v1/fees/gateway",
        headers=headers,
        params={"payment_method": "MTN_MOMO_LBR", "operation_type": "COLLECTION"},
    )
    print(response.json())

    # List all fee tiers
    tiers = requests.get(f"{BASE_URL}/v1/fees/tiers", headers=headers).json()
    for tier in tiers:
        print(tier["name"], "— default:", tier["is_default"])
    ```

=== "Node.js"

    ```javascript
    const BASE_URL = "https://api.heydollr.app";
    const TOKEN    = "YOUR_ACCESS_TOKEN";

    // Gateway fees
    const fees = await fetch(
      `${BASE_URL}/v1/fees/gateway?payment_method=MTN_MOMO_LBR&operation_type=COLLECTION`,
      { headers: { Authorization: `Bearer ${TOKEN}` } }
    ).then(r => r.json());
    console.log(fees);

    // List all tiers
    const tiers = await fetch(`${BASE_URL}/v1/fees/tiers`, {
      headers: { Authorization: `Bearer ${TOKEN}` },
    }).then(r => r.json());
    tiers.forEach(t => console.log(t.name, "| default:", t.is_default));
    ```

=== "PHP"

    ```php
    // Gateway fees
    $ch = curl_init(
        "https://api.heydollr.app/v1/fees/gateway?payment_method=MTN_MOMO_LBR&operation_type=COLLECTION"
    );
    curl_setopt_array($ch, [
        CURLOPT_RETURNTRANSFER => true,
        CURLOPT_HTTPHEADER     => ["Authorization: Bearer YOUR_ACCESS_TOKEN"],
    ]);
    $fees = json_decode(curl_exec($ch), true);
    curl_close($ch);
    print_r($fees);
    ```

=== "Java"

    ```java
    import java.net.URI;
    import java.net.http.*;

    HttpClient client = HttpClient.newHttpClient();

    HttpRequest request = HttpRequest.newBuilder()
        .uri(URI.create(
            "https://api.heydollr.app/v1/fees/gateway"
            + "?payment_method=MTN_MOMO_LBR&operation_type=COLLECTION"
        ))
        .header("Authorization", "Bearer YOUR_ACCESS_TOKEN")
        .GET()
        .build();

    HttpResponse<String> response = client.send(request, HttpResponse.BodyHandlers.ofString());
    System.out.println(response.body());
    ```

=== "Go"

    ```go
    package main

    import (
        "fmt"
        "io"
        "net/http"
    )

    func main() {
        req, _ := http.NewRequest("GET",
            "https://api.heydollr.app/v1/fees/gateway?payment_method=MTN_MOMO_LBR&operation_type=COLLECTION",
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

---
