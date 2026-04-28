# Payment Links

Generate shareable URLs for payment checkout or receipt pages. These links can be sent directly to customers.

## Generate Payment Link

```http
GET /v1/links/pay
```

#### Query Parameters

| Param | Type | Required | Description |
|---|---|---|---|
| `source_type` | enum | Yes | `INVOICE` or `ORDER` |
| `source_number` | string | Yes | The invoice or order number (e.g. `INV-2025-00042`). If subscriptions are supported publicly in the future, subscription numbering semantics will be documented here. |

#### Response — `LinkResponse`

| Field | Type | Description |
|---|---|---|
| `url` | string | Shareable payment checkout URL |

#### Code Examples

=== "cURL"

    ```bash
    curl "https://api.heydollr.app/v1/links/pay?source_type=INVOICE&source_number=INV-2025-00042" \
      -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
    ```

=== "Python"

    ```python
    import requests

    BASE_URL = "https://api.heydollr.app"
    headers  = {"Authorization": "Bearer YOUR_ACCESS_TOKEN"}

    response = requests.get(
        f"{BASE_URL}/v1/links/pay",
        headers=headers,
        params={
            "source_type":   "INVOICE",
            "source_number": "INV-2025-00042",
        },
    )
    link = response.json()
    print("Payment URL:", link["url"])
    ```

=== "Node.js"

    ```javascript
    const BASE_URL = "https://api.heydollr.app";
    const TOKEN    = "YOUR_ACCESS_TOKEN";

    const params = new URLSearchParams({
      source_type:   "INVOICE",
      source_number: "INV-2025-00042",
    });

    const response = await fetch(`${BASE_URL}/v1/links/pay?${params}`, {
      headers: { Authorization: `Bearer ${TOKEN}` },
    });
    const link = await response.json();
    console.log("Payment URL:", link.url);
    ```

=== "PHP"

    ```php
    $params = http_build_query([
        "source_type"   => "INVOICE",
        "source_number" => "INV-2025-00042",
    ]);
    $ch = curl_init("https://api.heydollr.app/v1/links/pay?{$params}");
    curl_setopt_array($ch, [
        CURLOPT_RETURNTRANSFER => true,
        CURLOPT_HTTPHEADER     => ["Authorization: Bearer YOUR_ACCESS_TOKEN"],
    ]);
    $link = json_decode(curl_exec($ch), true);
    curl_close($ch);
    echo "Payment URL: " . $link["url"];
    ```

=== "Java"

    ```java
    import java.net.URI;
    import java.net.http.*;

    HttpClient client = HttpClient.newHttpClient();
    HttpRequest request = HttpRequest.newBuilder()
        .uri(URI.create(
            "https://api.heydollr.app/v1/links/pay?source_type=INVOICE&source_number=INV-2025-00042"
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
            "https://api.heydollr.app/v1/links/pay",
            nil,
        )
        q := req.URL.Query()
        q.Add("source_type",   "INVOICE")
        q.Add("source_number", "INV-2025-00042")
        req.URL.RawQuery = q.Encode()
        req.Header.Set("Authorization", "Bearer YOUR_ACCESS_TOKEN")

        client := &http.Client{}
        resp, _ := client.Do(req)
        defer resp.Body.Close()

        data, _ := io.ReadAll(resp.Body)
        fmt.Println(string(data))
    }
    ```

    Note: Use these endpoints to generate the public URL for a link-enabled invoice or order (for example, when an invoice was created with `as_payment_link: true`).

---

## Generate Receipt Link

```http
GET /v1/links/receipt
```

#### Query Parameters

| Param | Type | Required | Description |
|---|---|---|---|
| `source_type` | enum | Yes | `INVOICE`, `ORDER`, or `SUBSCRIPTION` |
| `source_number` | string | Yes | The invoice/order number |

#### Response — `LinkResponse`

| Field | Type | Description |
|---|---|---|
| `url` | string | Shareable receipt URL |

#### Code Examples

=== "cURL"

    ```bash
    curl "https://api.heydollr.app/v1/links/receipt?source_type=INVOICE&source_number=INV-2025-00042" \
      -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
    ```

=== "Python"

    ```python
    response = requests.get(
        f"{BASE_URL}/v1/links/receipt",
        headers=headers,
        params={
            "source_type":   "INVOICE",
            "source_number": "INV-2025-00042",
        },
    )
    link = response.json()
    print("Receipt URL:", link["url"])
    ```

=== "Node.js"

    ```javascript
    const params = new URLSearchParams({
      source_type:   "INVOICE",
      source_number: "INV-2025-00042",
    });

    const response = await fetch(`${BASE_URL}/v1/links/receipt?${params}`, {
      headers: { Authorization: `Bearer ${TOKEN}` },
    });
    const link = await response.json();
    console.log("Receipt URL:", link.url);
    ```

=== "PHP"

    ```php
    $params = http_build_query([
        "source_type"   => "INVOICE",
        "source_number" => "INV-2025-00042",
    ]);
    $ch = curl_init("https://api.heydollr.app/v1/links/receipt?{$params}");
    curl_setopt_array($ch, [
        CURLOPT_RETURNTRANSFER => true,
        CURLOPT_HTTPHEADER     => ["Authorization: Bearer YOUR_ACCESS_TOKEN"],
    ]);
    $link = json_decode(curl_exec($ch), true);
    curl_close($ch);
    echo "Receipt URL: " . $link["url"];
    ```

=== "Java"

    ```java
    HttpRequest request = HttpRequest.newBuilder()
        .uri(URI.create(
            "https://api.heydollr.app/v1/links/receipt?source_type=INVOICE&source_number=INV-2025-00042"
        ))
        .header("Authorization", "Bearer YOUR_ACCESS_TOKEN")
        .GET()
        .build();

    HttpResponse<String> response = client.send(request, HttpResponse.BodyHandlers.ofString());
    System.out.println(response.body());
    ```

=== "Go"

    ```go
    req, _ := http.NewRequest("GET",
        "https://api.heydollr.app/v1/links/receipt",
        nil,
    )
    q := req.URL.Query()
    q.Add("source_type",   "INVOICE")
    q.Add("source_number", "INV-2025-00042")
    req.URL.RawQuery = q.Encode()
    req.Header.Set("Authorization", "Bearer YOUR_ACCESS_TOKEN")

    client := &http.Client{}
    resp, _ := client.Do(req)
    defer resp.Body.Close()

    data, _ := io.ReadAll(resp.Body)
    fmt.Println(string(data))
    ```

---
