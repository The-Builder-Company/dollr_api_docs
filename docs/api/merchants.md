# Merchants

## Get Merchant Info

```http
GET /v1/merchants/merchant-info
```

| Param | Type | Required | Description |
|---|---|---|---|
| `merchant_id` | integer | Yes | Your merchant entity ID |
| `merchant_type` | string | Yes | `MICRO_ORGANIZATION` (sole proprietorship) or `ORGANIZATION` (registered business) |

#### Response — `MerchantInfoResponse`

| Field | Type | Description |
|---|---|---|
| `id` | integer | Merchant entity ID |
| `name` | string | Merchant business name |
| `type` | string | `MICRO_ORGANIZATION` or `ORGANIZATION` |
| `email` | string \| null | Business email address |
| `phone` | string \| null | Business phone number |

#### Code Examples

=== "cURL"

    ```bash
    curl "https://api.heydollr.app/v1/merchants/merchant-info?merchant_id=5&merchant_type=MICRO_ORGANIZATION" \
      -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
    ```

=== "Python"

    ```python
    import requests

    BASE_URL = "https://api.heydollr.app"
    headers  = {"Authorization": "Bearer YOUR_ACCESS_TOKEN"}

    response = requests.get(
        f"{BASE_URL}/v1/merchants/merchant-info",
        headers=headers,
        params={"merchant_id": 5, "merchant_type": "MICRO_ORGANIZATION"},
    )
    merchant = response.json()
    print(merchant["name"], merchant["type"])
    ```

=== "Node.js"

    ```javascript
    const BASE_URL = "https://api.heydollr.app";
    const TOKEN    = "YOUR_ACCESS_TOKEN";

    const params = new URLSearchParams({ merchant_id: "5", merchant_type: "MICRO_ORGANIZATION" });
    const response = await fetch(`${BASE_URL}/v1/merchants/merchant-info?${params}`, {
      headers: { Authorization: `Bearer ${TOKEN}` },
    });
    const merchant = await response.json();
    console.log(merchant.name, merchant.type);
    ```

=== "PHP"

    ```php
    $params = http_build_query(["merchant_id" => 5, "merchant_type" => "MICRO_ORGANIZATION"]);
    $ch = curl_init("https://api.heydollr.app/v1/merchants/merchant-info?{$params}");
    curl_setopt_array($ch, [
        CURLOPT_RETURNTRANSFER => true,
        CURLOPT_HTTPHEADER     => ["Authorization: Bearer YOUR_ACCESS_TOKEN"],
    ]);
    $merchant = json_decode(curl_exec($ch), true);
    curl_close($ch);
    echo $merchant["name"] . " — " . $merchant["type"];
    ```

=== "Java"

    ```java
    import java.net.URI;
    import java.net.http.*;

    HttpClient client = HttpClient.newHttpClient();
    HttpRequest request = HttpRequest.newBuilder()
        .uri(URI.create(
            "https://api.heydollr.app/v1/merchants/merchant-info"
            + "?merchant_id=5&merchant_type=MICRO_ORGANIZATION"
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
            "https://api.heydollr.app/v1/merchants/merchant-info?merchant_id=5&merchant_type=MICRO_ORGANIZATION",
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
