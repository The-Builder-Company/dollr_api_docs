---
title: "Merchants"
description: "Retrieve merchant profile and configuration from the API."

icon: "building"


keywords: ["Dollr merchant API", "Dollr API"]
---

Read merchant metadata associated with your API credentials — useful for multi-tenant dashboards and environment checks.

**Try in API Reference:** [Merchant info](/api-reference/merchants/get-merchant-info)

## Query parameters

| Parameter | Required | Description |
|-----------|----------|-------------|
| `merchant_id` | Yes | Merchant entity ID (integer) |
| `merchant_type` | Yes | `MICRO_ORGANIZATION` or `ORGANIZATION` |

## Minimal example

```bash
curl "https://api.heydollr.app/v1/merchants/merchant-info?merchant_id=42&merchant_type=ORGANIZATION" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
```

**Response fields:** `id`, `name`, `type`, `email`, `phone`.

## Where to find `merchant_id`

1. Log in to [merchant.heydollr.app](https://merchant.heydollr.app)
2. Open **Settings → Business** or **Organization profile**
3. Copy your merchant / organization ID

`merchant_type` is `ORGANIZATION` for registered businesses or `MICRO_ORGANIZATION` for sole proprietors — match your account type.

## Related

- [Authentication](/authentication)
- [Merchant Dashboard](https://merchant.heydollr.app)
