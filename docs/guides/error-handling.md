# Error Handling

## Rules

!!! danger "Store reference_id before executing"
    Always persist your `reference_id` before calling any execution endpoint. If the HTTP response is lost due to a network error, query the transaction status using this ID before retrying. Never generate a new `reference_id` unless you have confirmed the original did not result in a transaction.

!!! tip "HTTP 422 is a developer error"
    Treat `422 Unprocessable Entity` as a signal to fix your request payload. Inspect the `detail` array for field-level validation messages.

!!! warning "PROCESSING is not a failure"
    Mobile money transactions may remain in `PROCESSING` for several minutes while the carrier confirms the payment. Do not cancel or retry during this window.

!!! note "Refresh your Bearer token proactively"
    Implement a background refresh that obtains a new token when the remaining validity drops below 5 minutes. Expired tokens return `HTTP 401`.

!!! tip "Use prediction endpoints first"
    Call `/v1/predictions/amount-and-fees` before executing to validate fee calculations and detect FX rate changes before funds move.

---

## Error Response Format

### Validation Error (HTTP 422)

```json
{
  "detail": [
    {
      "loc": ["body", "currency"],
      "msg": "field required",
      "type": "value_error.missing"
    }
  ]
}
```

The `loc` array shows the exact field path that failed. `loc[0]` is always `"body"` for request body fields.

### Authentication Error (HTTP 401)

```json
{
  "detail": "Could not validate credentials"
}
```

Obtain a new token via `POST /v1/jwt/client/obtain/token` and retry.

---

## Retry with Exponential Backoff

For network errors and `5xx` responses, implement exponential backoff before retrying.

=== "Python"

    ```python
    import time
    import uuid
    import requests

    BASE_URL = "https://api.heydollr.app"

    def execute_with_retry(session_id, payment_account_id, currency, headers, max_retries=3):
        reference_id = str(uuid.uuid4())  # generate ONCE, reuse on retry
        delay = 1

        for attempt in range(max_retries):
            try:
                response = requests.post(
                    f"{BASE_URL}/v1/executions/collection",
                    headers=headers,
                    json={
                        "session_id":         session_id,
                        "payment_account_id": payment_account_id,
                        "currency":           currency,
                        "reference_id":       reference_id,
                    },
                    timeout=30,
                )
                if response.status_code < 500:
                    return response.json()
            except requests.RequestException:
                pass

            # Before retrying, check if the transaction already landed
            status = requests.get(
                f"{BASE_URL}/v1/status/collection/{reference_id}",
                headers=headers,
            )
            if status.ok and status.json().get("status") in ("COMPLETED", "PROCESSING"):
                return status.json()

            time.sleep(delay)
            delay *= 2  # exponential backoff

        raise Exception(f"Execution failed after {max_retries} attempts")
    ```

=== "Node.js"

    ```javascript
    import { randomUUID } from "crypto";

    const BASE_URL = "https://api.heydollr.app";

    async function executeWithRetry(sessionId, paymentAccountId, currency, token, maxRetries = 3) {
      const referenceId = randomUUID(); // generate ONCE, reuse on retry
      let delay = 1000;

      for (let attempt = 0; attempt < maxRetries; attempt++) {
        try {
          const res = await fetch(`${BASE_URL}/v1/executions/collection`, {
            method: "POST",
            headers: { Authorization: `Bearer ${token}`, "Content-Type": "application/json" },
            body: JSON.stringify({
              session_id:         sessionId,
              payment_account_id: paymentAccountId,
              currency,
              reference_id:       referenceId,
            }),
          });
          if (res.status < 500) return res.json();
        } catch (_) {}

        // Before retrying, check if the transaction already landed
        const status = await fetch(`${BASE_URL}/v1/status/collection/${referenceId}`, {
          headers: { Authorization: `Bearer ${token}` },
        }).then(r => r.json()).catch(() => null);

        if (status?.status === "COMPLETED" || status?.status === "PROCESSING") {
          return status;
        }

        await new Promise(r => setTimeout(r, delay));
        delay *= 2; // exponential backoff
      }

      throw new Error(`Execution failed after ${maxRetries} attempts`);
    }
    ```

---

## HTTP Status Code Reference

| Code | Status | Action |
|---|---|---|
| `200` | OK | Success — process the response |
| `401` | Unauthorized | Refresh your Bearer token and retry |
| `403` | Forbidden | Check your account permissions |
| `404` | Not Found | Verify the resource ID is correct |
| `422` | Unprocessable Entity | Fix your request payload — inspect `detail` array |
| `429` | Too Many Requests | Back off and retry after the `Retry-After` header value |
| `500` | Internal Server Error | Retry with backoff; contact support if it persists |

---

## Support & Resources

| Resource | URL / Contact |
|---|---|
| Merchant Portal | [merchant.heydollr.app](https://merchant.heydollr.app) |
| Help Center | [dollr.tawk.help](https://dollr.tawk.help) |
| Open API Spec (JSON) | [api.heydollr.app/openapi.json](https://api.heydollr.app/openapi.json) |
| Support Email | support@heydollr.app |

When contacting support about a specific transaction, always include your `reference_id`, the full request body, and the HTTP response body.
