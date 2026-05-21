---
title: "Error Catalog"
description: "Common Dollr API error messages, causes, and recommended actions beyond HTTP status codes."
keywords: ["API errors", "422 validation", "idempotency", "reference_id", "Dollr troubleshooting"]
---

# Error Catalog

HTTP status codes tell you *what class* of problem occurred. This catalog covers frequent **`detail`** messages and field validation patterns so you can fix requests without opening a support ticket.

For retry logic and idempotency rules, see [Error Handling](/guides/error-handling).

---

## Authentication & authorization

| Symptom | Typical HTTP | What it means | What to do |
|---|---|---|---|
| `Could not validate credentials` | `401` | Missing, malformed, or expired Bearer token | `POST /v1/jwt/client/obtain/token` — refresh before `expires_in` elapses |
| Token works on one endpoint but `403` on another | `403` | Account not verified or feature gated | Complete KYB in [Merchant Dashboard](https://merchant.heydollr.app); check overview restrictions |
| `Not authenticated` | `401` | No `Authorization` header | Send `Authorization: Bearer <access_token>` on every call |

---

## Validation (HTTP 422)

Inspect the `detail` array. Each item has `loc`, `msg`, and `type`.

| Field / pattern | Example `msg` | Cause | Fix |
|---|---|---|---|
| `body.currency` | `field required` | Currency omitted | ISO 4217 uppercase, e.g. `USD` |
| `body.phone` | `invalid phone` / length errors | Not E.164 without `+` | Use digits only, e.g. `231771234567` |
| `body.reference_id` | `invalid uuid` | Not UUID v4 | Generate with `uuid4()` once per execution attempt |
| `body.reference_id` | duplicate / already exists | Reused idempotency key for a *different* payment | Query status with the same `reference_id` first |
| `body.amount` | less than minimum | Below `0.01` or integer rules | Increase amount or use predictions endpoint |
| `body.session_id` | session not found / expired | Session timed out or wrong ID | Create a new session; do not reuse stale IDs |
| `body.payment_account_id` | not found | Account not registered for party | `POST /v1/payment-accounts/create?operation_type=COLLECTION` |
| `body.method` / `body.provider` | invalid combination | Mismatched MoMo operator | Call [MMO provider prediction](/api-reference/predictions/predict-mmo-provider-info) |
| `body.source_type` / `body.source_kind` | invalid enum | Wrong document type constant | Use `INVOICE` or `ORDER` for checkout sources (see [Checkouts](/api/checkouts)) |
| `body.counterparty_id` | required | Invoice/order without counterparty | Create [Counterparty](/api/counterparties) first in document-first flows |

---

## Resource state errors

| Symptom | HTTP | Cause | Fix |
|---|---|---|---|
| Invoice not publishable | `422` / `404` | Still `IDLE` or wrong ID | `PUT /v1/invoices/publish/{id}` when ready |
| Execution rejected — session | `422` | Session not `ACTIVE` or wrong operation type | Match session type to execution (`checkout` → `collection`) |
| Source `CANCELED` | `422` | Invoice/order canceled | Create a new source; do not execute against canceled IDs |
| Party / counterparty mismatch | `422` | IDs from another merchant | Use IDs returned under your authenticated merchant |

---

## Execution & status

| Symptom | HTTP | Cause | Fix |
|---|---|---|---|
| Status stays `PROCESSING` | `200` on status poll | MoMo carrier delay (normal) | Poll `GET /v1/status/collection/{reference_id}`; **do not** retry with a new `reference_id` |
| Status `FAILED` | `200` | Payer declined, insufficient funds, or operator error | Show failure to user; optional new session + new `reference_id` for a *new* attempt |
| Lost HTTP response after execute | — | Network timeout | Poll status with **stored** `reference_id` before retrying execute |
| `429 Too Many Requests` | `429` | Rate limit | Honor `Retry-After`; exponential backoff |

---

## Server errors (5xx)

| Symptom | Action |
|---|---|
| `500` / `502` / `503` | Retry with backoff; if persistent, contact support with `reference_id` and timestamp |
| Intermittent timeouts on execute | Treat as ambiguous: **status poll first**, then retry only if status shows no `COMPLETED`/`PROCESSING` |

---

## Support payload checklist

When escalating to [Support](/reference/support) or [dev@heydollr.app](mailto:dev@heydollr.app), include:

1. `reference_id` (if execution-related)
2. Request URL, method, and redacted body
3. Full response status + JSON body
4. Merchant ID / environment (test vs live)
5. Payment `method`, `provider`, and market

---

## Related

- [Error Handling](/guides/error-handling) — retries, backoff, rules
- [Transaction Status](/api/status) — polling execution vs source status
- [Try in API Reference: collection status](/api-reference/status/get-collection-status)
