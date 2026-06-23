---
title: "Realtime Keys"
description: "Short-lived tokens for live payment status on a checkout session."

icon: "tower-broadcast"


keywords: ["Dollr realtime API", "Dollr API", "Dollr live payment status"]
---

Short-lived tokens for subscribing to live payment events via **Supabase Realtime** — alternative to polling [status](/api/status).

**Try in API Reference:** [Collection realtime key](/api-reference/realtime-keys/get-collection-realtime-key)

## When to use

Live checkout UI while the customer approves MoMo or completes card 3DS. Not a replacement for server-side fulfillment verification — see [Payment status patterns](/guides/payment-status-patterns).

## Request

| Field | Type | Description |
|-------|------|-------------|
| `session_id` | integer | Checkout session ID |
| `source_type` | string | `INVOICE` or `ORDER` |
| `reference_id` | string | UUID v4 |

## Response

| Field | Description |
|-------|-------------|
| `access_token` | JWT for Supabase Realtime (`expires_in` is **seconds**) |

## After obtaining the token

Connect with Supabase client, channel `payment-intent:{session_id}:{reference_id}`, table `checkout_payment_intent_public_status`. Full walkthrough: [Realtime status](/guides/realtime-status).

## Related

- [Environments](/reference/environments) — Supabase URL and anon key
- [Sessions & executions](/concepts/sessions-and-executions)
