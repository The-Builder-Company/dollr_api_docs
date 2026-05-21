---
title: "Executions"
description: "Submit an active session to trigger the movement of funds."
icon: "play"
---

# Executions

An **execution** submits a session and moves funds. All execution endpoints return an `ExecutionResponse`.

<Note>
**Try in API Reference:** [Collect](/api-reference/executions/collect) · [Payout](/api-reference/executions/payout) · [Transfer](/api-reference/executions/transfer) · [Refund](/api-reference/executions/refund)
</Note>

<Warning>
Generate a UUID v4 `reference_id` **before** the HTTP call and store it. If the response is lost, [poll status](/api/status) with that same ID — do not mint a new one until you confirm the attempt did not land.
</Warning>

## Collect (minimal)

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

## Execution status

`PENDING` → `PROCESSING` → `COMPLETED` | `FAILED`. Mobile money may remain `PROCESSING` for several minutes.

## Related

- [Payment accounts](/api/payment-accounts) · [Status](/api/status)
- [Duplicate reference_id](/knowledge-base/duplicate-reference-id)
- [Quick Start](/quickstart)
