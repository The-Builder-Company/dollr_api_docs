# Counterparties

A Counterparty links an existing Party to your merchant account with a defined relationship type. Counterparties are required before creating invoices or orders.

## Relationship Types

`CUSTOMER` `FRIEND` `DONOR` `DONEE` `FAMILY` `EMPLOYEE` `SUPPLIER` `CONTACT` `SERVICE_PROVIDER` `PARTNER` `BENEFICIARY`

## Create Counterparty

```http
POST /v1/counterparties/create
```

#### Request Body

| Field | Type | Required | Description |
|---|---|---|---|
| `relationship_type` | enum | Yes | One of the relationship type values above |
| `party_id` | integer \| null | No | ID of an existing Party to link |

#### Example Response

```json
{
  "id": 15,
  "relationship_type": "CUSTOMER",
  "party_id": 42,
  "created_at": "2025-06-01T10:05:00Z",
  "updated_at": "2025-06-01T10:05:00Z"
}
```

#### Code Examples

=== "cURL"

    ```bash
    curl -X POST "https://api.heydollr.app/v1/counterparties/create" \
      -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
      -H "Content-Type: application/json" \
      -d '{
        "relationship_type": "CUSTOMER",
        "party_id": 42
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
        f"{BASE_URL}/v1/counterparties/create",
        headers=headers,
        json={
            "relationship_type": "CUSTOMER",
            "party_id":          42,
        },
    )
    counterparty = response.json()
    print("Counterparty ID:", counterparty["id"])
    ```

=== "Node.js"

    ```javascript
    const BASE_URL = "https://api.heydollr.app";
    const TOKEN    = "YOUR_ACCESS_TOKEN";

    const response = await fetch(`${BASE_URL}/v1/counterparties/create`, {
      method: "POST",
      headers: {
        Authorization:  `Bearer ${TOKEN}`,
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        relationship_type: "CUSTOMER",
        party_id:          42,
      }),
    });
    const counterparty = await response.json();
    console.log("Counterparty ID:", counterparty.id);
    ```

=== "PHP"

    ```php
    $ch = curl_init("https://api.heydollr.app/v1/counterparties/create");
    curl_setopt_array($ch, [
        CURLOPT_RETURNTRANSFER => true,
        CURLOPT_POST           => true,
        CURLOPT_HTTPHEADER     => [
            "Authorization: Bearer YOUR_ACCESS_TOKEN",
            "Content-Type: application/json",
        ],
        CURLOPT_POSTFIELDS => json_encode([
            "relationship_type" => "CUSTOMER",
            "party_id"          => 42,
        ]),
    ]);
    $counterparty = json_decode(curl_exec($ch), true);
    curl_close($ch);
    echo "Counterparty ID: " . $counterparty["id"];
    ```

=== "Java"

    ```java
    import java.net.URI;
    import java.net.http.*;
    import java.net.http.HttpRequest.BodyPublishers;

    HttpClient client = HttpClient.newHttpClient();

    String body = """
        {
          "relationship_type": "CUSTOMER",
          "party_id": 42
        }
        """;

    HttpRequest request = HttpRequest.newBuilder()
        .uri(URI.create("https://api.heydollr.app/v1/counterparties/create"))
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
            "relationship_type": "CUSTOMER",
            "party_id":          42,
        }
        body, _ := json.Marshal(payload)

        req, _ := http.NewRequest("POST",
            "https://api.heydollr.app/v1/counterparties/create",
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

## List Counterparties

```http
GET /v1/counterparties/list
```

| Query Param | Type | Required | Description |
|---|---|---|---|
| `fullname` | string \| null | No | Filter by linked party's full name |
| `relationship_type` | enum \| null | No | Filter by relationship type |

## Retrieve Counterparty

```http
GET /v1/counterparties/retrieve/{id}
```

Returns a `CounterPartyWithPartyResponse` — includes the linked `PartyResponse`.

## Update Counterparty

```http
PUT /v1/counterparties/update/{id}
```

| Field | Type | Required | Description |
|---|---|---|---|
| `relationship_type` | enum \| null | No | New relationship type |
| `party_id` | integer \| null | No | Link to a different existing Party |

---
