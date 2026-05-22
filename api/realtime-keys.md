---
title: "Realtime Keys"
description: "Short-lived tokens for live payment status on a checkout session."

icon: "tower-broadcast"


keywords: ["Dollr realtime API", "Dollr API", "Dollr live payment status"]
---

# Realtime Keys

Short-lived tokens for subscribing to live payment events — alternative to polling [status](/api/status).

<Note>
**Try in API Reference:** [Collection realtime key](/api-reference/realtime-keys/get-collection-realtime-key)
</Note>

## When to use

Live checkout UI, POS displays, or dashboards that need immediate updates when MoMo or card payments complete.

## Minimal example

```bash
curl -X POST "https://api.heydollr.app/v1/realtime-keys/collection" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "session_id": 55,
    "source_type": "INVOICE",
    "reference_id": "550e8400-e29b-41d4-a716-446655440000"
  }'
```

## Related

- [Realtime status guide](/guides/realtime-status)
- [Sessions & executions](/concepts/sessions-and-executions)
