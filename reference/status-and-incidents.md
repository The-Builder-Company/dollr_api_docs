---
title: "Status & Incidents"
description: "Monitor API health, transaction status, and how Dollr communicates incidents to developers."
keywords: ["API status", "incidents", "uptime", "Dollr monitoring"]

icon: "tower-broadcast"
---

# Status & Incidents

## Transaction-level status (your integration)

Dollr does not replace per-payment polling with a single global “API up” flag for your checkout flow. Use the **Status API** for each transaction:

| Operation | Poll execution status |
|---|---|
| Collection | `GET /v1/status/collection/{reference_id}` |
| Payout | `GET /v1/status/payout/{reference_id}` |
| Transfer | `GET /v1/status/transfer/{reference_id}` |
| Refund | `GET /v1/status/refund/{reference_id}` |
| Invoice / order document | `GET /v1/status/source` (source lifecycle) |

Guide: [Transaction Status](/api/status) · [API Reference](/api-reference/status/get-collection-status)

<Warning>
**Two status models** — Execution status (funds movement) and source status (`IDLE` → `PAID` on invoices/orders) are different. Do not treat `PROCESSING` on an execution as a failed invoice.
</Warning>

---

## Realtime updates (optional)

For active checkout sessions, generate a [Realtime Key](/api/realtime-keys) to subscribe to push events instead of polling. Keys are short-lived; refresh per session.

---

## Platform & API availability

| Channel | Use for |
|---|---|
| [Merchant Dashboard](https://merchant.heydollr.app) | Account alerts, maintenance notices, support tickets |
| [Help Center](https://dollr.tawk.help) | Known issues, integration FAQs, procedural updates |
| [dev@heydollr.app](mailto:dev@heydollr.app) | Confirmed outages, prolonged `5xx`, or data discrepancies |

If Dollr publishes a public status page for the API platform, it will be linked from the dashboard and Help Center. Subscribe there for incident start/resolution notifications.

---

## What to do during an incident

1. **Confirm scope** — Is the failure isolated to one `method`/market or all API calls?
2. **Check auth** — Rule out expired tokens (`401`) before assuming platform outage.
3. **Stop blind retries** — Use existing `reference_id` and status endpoints before re-executing.
4. **Capture evidence** — Timestamp (UTC), endpoint, `reference_id`, response bodies.
5. **Contact support** — Email [dev@heydollr.app](mailto:dev@heydollr.app) with the checklist in [Error catalog](/reference/error-catalog).

---

## Post-incident

After recovery, reconcile any payments left in `PROCESSING` by polling status with the original `reference_id`. Do not issue duplicate executions for the same customer charge without verifying the first attempt failed.

---

## Related

- [Error Handling](/guides/error-handling)
- [Support](/reference/support)
