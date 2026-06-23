---
title: "Transaction Status"
description: "Poll execution and payment source status by reference_id or source ID."

icon: "chart-line"


keywords: ["Dollr payment status", "Dollr API", "Dollr collection status"]
---

Query execution progress with the `reference_id` you stored at execute time. Query payment **source** status (invoice/order) separately when building receipts or UI.

`source_type` values: `INVOICE`, `ORDER`. `SUBSCRIPTION` appears in the API schema but is **not publicly supported** yet.

**Try in API Reference:** [Collection](/api-reference/status/get-collection-status) · [Payout](/api-reference/status/get-payout-status) · [Source status](/api-reference/status/get-payment-source-status)

## Execution status endpoints


| Operation  | Endpoint                                  |
| ---------- | ----------------------------------------- |
| Collection | `GET /v1/status/collection/:reference_id` |
| Payout     | `GET /v1/status/payout/:reference_id`     |
| Transfer   | `GET /v1/status/transfer/:reference_id`   |
| Refund     | `GET /v1/status/refund/:reference_id`     |


## Minimal example

```bash
curl "https://api.heydollr.app/v1/status/collection/550e8400-e29b-41d4-a716-446655440000" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
```

Prefer [Realtime status](/guides/realtime-status) for live checkout UIs instead of aggressive polling.

## Related

- [Status & incidents](/reference/status-and-incidents)
- [Payment stuck in PROCESSING](/knowledge-base/payment-processing-status)

