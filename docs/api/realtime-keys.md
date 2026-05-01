---
title: "Realtime Keys"
description: "Generate short-lived keys for subscribing to real-time transaction events."
---

# Realtime Keys

Realtime Keys are short-lived tokens for subscribing to live payment status updates on a checkout session. Use these to update your UI immediately upon payment confirmation, without polling.

Realtime Keys are the recommended alternative to frequent polling — use them when you want push-style updates instead of repeatedly calling `GET /v1/status/*`.

## Get Collection Realtime Key

```http
POST /v1/realtime-keys/collection
```

#### Request Body

| Field | Type | Required | Description |
|---|---|---|---|
| `session_id` | integer | Yes | ID of the checkout session to subscribe to |
| `source_type` | string | Yes | `INVOICE` or `ORDER` |
| `reference_id` | string | Yes | Your UUID v4 reference for this subscription |

#### Response — `RealtimeTokenResponse`

| Field | Type | Description |
|---|---|---|
| `access_token` | string | Short-lived token for the Dollr realtime push service |
| `expires_in` | integer | Token validity in **seconds** |

#### Code Examples

<CodeGroup>

```bash cURL
curl -X POST "https://api.heydollr.app/v1/realtime-keys/collection" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "session_id":   55,
    "source_type":  "INVOICE",
    "reference_id": "550e8400-e29b-41d4-a716-446655440000"
  }'
```

```python Python
import uuid
import requests

BASE_URL = "https://api.heydollr.app"
headers  = {"Authorization": "Bearer YOUR_ACCESS_TOKEN", "Content-Type": "application/json"}

response = requests.post(
    f"{BASE_URL}/v1/realtime-keys/collection",
    headers=headers,
    json={
        "session_id":   55,
        "source_type":  "INVOICE",
        "reference_id": str(uuid.uuid4()),
    },
)
rt = response.json()
print("Realtime token:", rt["access_token"])
print("Expires in (seconds):", rt["expires_in"])
```

```javascript Node.js
import { randomUUID } from "crypto";

const BASE_URL = "https://api.heydollr.app";
const TOKEN    = "YOUR_ACCESS_TOKEN";

const response = await fetch(`${BASE_URL}/v1/realtime-keys/collection`, {
  method: "POST",
  headers: {
    Authorization:  `Bearer ${TOKEN}`,
    "Content-Type": "application/json",
  },
  body: JSON.stringify({
    session_id:   55,
    source_type:  "INVOICE",
    reference_id: randomUUID(),
  }),
});
const rt = await response.json();
console.log("Realtime token:", rt.access_token);
console.log("Expires in (seconds):", rt.expires_in);
```

```php PHP
$ch = curl_init("https://api.heydollr.app/v1/realtime-keys/collection");
curl_setopt_array($ch, [
    CURLOPT_RETURNTRANSFER => true,
    CURLOPT_POST           => true,
    CURLOPT_HTTPHEADER     => [
        "Authorization: Bearer YOUR_ACCESS_TOKEN",
        "Content-Type: application/json",
    ],
    CURLOPT_POSTFIELDS => json_encode([
        "session_id"   => 55,
        "source_type"  => "INVOICE",
        "reference_id" => $referenceId,
    ]),
]);
$rt = json_decode(curl_exec($ch), true);
curl_close($ch);
echo "Realtime token: " . $rt["access_token"];
```

```java Java
import java.util.UUID;
import java.net.URI;
import java.net.http.*;
import java.net.http.HttpRequest.BodyPublishers;

String body = String.format("""
    {
      "session_id":   55,
      "source_type":  "INVOICE",
      "reference_id": "%s"
    }
    """, UUID.randomUUID().toString());

HttpClient client = HttpClient.newHttpClient();
HttpRequest request = HttpRequest.newBuilder()
    .uri(URI.create("https://api.heydollr.app/v1/realtime-keys/collection"))
    .header("Authorization", "Bearer YOUR_ACCESS_TOKEN")
    .header("Content-Type", "application/json")
    .POST(BodyPublishers.ofString(body))
    .build();

HttpResponse<String> response = client.send(request, HttpResponse.BodyHandlers.ofString());
System.out.println(response.body());
```

```go Go
// go get github.com/google/uuid
package main

import (
    "bytes"
    "encoding/json"
    "fmt"
    "io"
    "net/http"

    "github.com/google/uuid"
)

func main() {
    payload := map[string]interface{}{
        "session_id":   55,
        "source_type":  "INVOICE",
        "reference_id": uuid.New().String(),
    }
    body, _ := json.Marshal(payload)

    req, _ := http.NewRequest("POST",
        "https://api.heydollr.app/v1/realtime-keys/collection",
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
