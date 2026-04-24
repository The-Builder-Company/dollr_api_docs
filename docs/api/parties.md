# Parties

Parties are contact records representing the people and entities your business transacts with.

## Create Party

```http
POST /v1/parties/create
```

#### Request Body

| Field | Type | Required | Description |
|---|---|---|---|
| `fullname` | string | Yes | Full name of the party |
| `phone` | string | Yes | E.164 phone number without `+` (e.g. `231771234567`). Min 8, max 15 digits. |
| `email` | string \| null | No | Email address |
| `country_code` | string \| null | No | ISO 3166-1 alpha-2 country code (e.g. `LR`) |

#### Response — `PartyResponse`

| Field | Type | Description |
|---|---|---|
| `id` | integer | Unique system-generated party ID |
| `fullname` | string | Full name as provided |
| `phone` | string | Phone number in E.164 format |
| `email` | string \| null | Email address |
| `country_code` | string \| null | Country code |
| `created_at` | datetime | ISO 8601 creation timestamp |
| `updated_at` | datetime | ISO 8601 last update timestamp |

#### Example Response

```json
{
  "id": 42,
  "fullname": "Amara Kamara",
  "phone": "231771234567",
  "email": "amara@example.com",
  "country_code": "LR",
  "created_at": "2025-06-01T10:00:00Z",
  "updated_at": "2025-06-01T10:00:00Z"
}
```

#### Code Examples

=== "cURL"

    ```bash
    curl -X POST "https://api.heydollr.app/v1/parties/create" \
      -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
      -H "Content-Type: application/json" \
      -d '{
        "fullname":     "Amara Kamara",
        "phone":        "231771234567",
        "email":        "amara@example.com",
        "country_code": "LR"
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
        f"{BASE_URL}/v1/parties/create",
        headers=headers,
        json={
            "fullname":     "Amara Kamara",
            "phone":        "231771234567",
            "email":        "amara@example.com",
            "country_code": "LR",
        },
    )
    party = response.json()
    print("Party ID:", party["id"])
    ```

=== "Node.js"

    ```javascript
    const BASE_URL = "https://api.heydollr.app";
    const TOKEN    = "YOUR_ACCESS_TOKEN";

    const response = await fetch(`${BASE_URL}/v1/parties/create`, {
      method: "POST",
      headers: {
        Authorization:  `Bearer ${TOKEN}`,
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        fullname:     "Amara Kamara",
        phone:        "231771234567",
        email:        "amara@example.com",
        country_code: "LR",
      }),
    });
    const party = await response.json();
    console.log("Party ID:", party.id);
    ```

=== "PHP"

    ```php
    $ch = curl_init("https://api.heydollr.app/v1/parties/create");
    curl_setopt_array($ch, [
        CURLOPT_RETURNTRANSFER => true,
        CURLOPT_POST           => true,
        CURLOPT_HTTPHEADER     => [
            "Authorization: Bearer YOUR_ACCESS_TOKEN",
            "Content-Type: application/json",
        ],
        CURLOPT_POSTFIELDS => json_encode([
            "fullname"     => "Amara Kamara",
            "phone"        => "231771234567",
            "email"        => "amara@example.com",
            "country_code" => "LR",
        ]),
    ]);
    $party = json_decode(curl_exec($ch), true);
    curl_close($ch);
    echo "Party ID: " . $party["id"];
    ```

=== "Java"

    ```java
    import java.net.URI;
    import java.net.http.*;
    import java.net.http.HttpRequest.BodyPublishers;

    HttpClient client = HttpClient.newHttpClient();

    String body = """
        {
          "fullname":     "Amara Kamara",
          "phone":        "231771234567",
          "email":        "amara@example.com",
          "country_code": "LR"
        }
        """;

    HttpRequest request = HttpRequest.newBuilder()
        .uri(URI.create("https://api.heydollr.app/v1/parties/create"))
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
        payload := map[string]string{
            "fullname":     "Amara Kamara",
            "phone":        "231771234567",
            "email":        "amara@example.com",
            "country_code": "LR",
        }
        body, _ := json.Marshal(payload)

        req, _ := http.NewRequest("POST",
            "https://api.heydollr.app/v1/parties/create",
            bytes.NewBuffer(body),
        )
        req.Header.Set("Authorization", "Bearer YOUR_ACCESS_TOKEN")
        req.Header.Set("Content-Type", "application/json")

        client := &http.Client{}
        resp, _ := client.Do(req)
        defer resp.Body.Close()

        var result map[string]interface{}
        data, _ := io.ReadAll(resp.Body)
        json.Unmarshal(data, &result)
        fmt.Println("Party ID:", result["id"])
    }
    ```

## List Parties

```http
GET /v1/parties/list
```

| Query Param | Type | Required | Description |
|---|---|---|---|
| `fullname` | string \| null | No | Filter by full name (partial match) |

## Retrieve Party

```http
GET /v1/parties/retrieve/{id}
```

Returns a `PartyResponse` for the specified party ID.

---
