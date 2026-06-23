---
title: "Executions"
description: "Submit an active session to trigger the movement of funds."

icon: "play"


keywords: ["Dollr payment execution", "Dollr collect API", "Dollr API"]
---

An **execution** submits a session and moves funds. All execution endpoints return an `ExecutionResponse`.

<Note>
**Try in API Reference:** [Collect](/api-reference/executions/collect) · [Payout](/api-reference/executions/payout)
</Note>

<Info>
**Hosted checkout** does not require server-side execution — Dollr executes payment on the hosted page. See [Hosted checkout](/guides/hosted-checkout).
</Info>

<Warning>
Generate a UUID v4 `reference_id` **before** the HTTP call and store it. If the response is lost, [poll status](/api/status) with that same ID — do not mint a new one until you confirm the attempt did not land.
</Warning>

## Collect

```bash
curl -X POST "https://api.heydollr.app/v1/executions/collection" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "session_id": "55",
    "payment_account_id": "18",
    "currency": "USD",
    "reference_id": "550e8400-e29b-41d4-a716-446655440000"
  }'
```

## Payout

Requires `session_id`, `payout_account_id`, `reference_id`, and `passcode` (merchant verification). See [Payout with Node.js](/guides/payout-with-nodejs).

## Execution response

| Field | Description |
|-------|-------------|
| `status` | `PENDING` → `PROCESSING` → `COMPLETED` \| `FAILED` |
| `reference_id` | Your idempotency key |
| `payer_amount` / `payee_amount` | Settled amounts |
| `requires_action` | `true` when card 3DS is needed |
| `client_secret` | Stripe secret for 3DS confirmation (card only) |
| `gateway_message` | Provider status message |

For card payments, when `requires_action` is `true`, complete authentication with `client_secret` before polling status. See [Collect with card](/guides/collect-with-card).

## Execution status

Mobile money may remain `PROCESSING` for several minutes. Do not re-execute during this window.

## Related

- [Hosted checkout](/guides/hosted-checkout) · [Payment accounts](/api/payment-accounts) · [Status](/api/status)
- [Duplicate reference_id](/knowledge-base/duplicate-reference-id)
- [Quick Start](/quickstart)
