---
title: "SDKs"
description: "Official and community-built SDKs for integrating Dollr into your application."
---

# SDKs

## Official Dollr SDKs

<Warning>
Official Dollr SDKs are currently in active development. They are not yet available for production use. Use the REST API directly in the meantime — see the [Quick Start](/docs/quickstart) for a step-by-step guide.
</Warning>

The following SDKs are being built and maintained by the Dollr team. They will wrap the REST API with idiomatic, language-native interfaces, handle token refresh automatically, and include typed request/response models.

<CardGroup cols={2}>
  <Card title="Node.js / TypeScript" icon="node-js" iconType="brands">
    **Status:** In development

    A TypeScript-first SDK for Node.js and browser environments with full type safety.
  </Card>
  <Card title="Python" icon="python" iconType="brands">
    **Status:** In development

    A Python SDK with async support, Pydantic models, and auto token refresh built in.
  </Card>
  <Card title="PHP" icon="php" iconType="brands">
    **Status:** Planned

    A PHP SDK compatible with Laravel and other popular frameworks.
  </Card>
  <Card title="Go" icon="golang" iconType="brands">
    **Status:** Planned

    A Go SDK with idiomatic interfaces and context-aware requests.
  </Card>
</CardGroup>

Official SDKs will be published on each language's package registry (npm, PyPI, Packagist, pkg.go.dev) and linked here when available.

---

## Community SDKs

<Note>
Community SDKs are built and maintained by third-party developers. Dollr does not officially support or guarantee these packages. Always review the code and test thoroughly before using in production.
</Note>

No community SDKs have been submitted yet.

**Built a wrapper or SDK for Dollr?** Email [dev@heydollr.app](mailto:dev@heydollr.app) with a link to your repository and a short description and we'll add it here.

---

## Build Your Own

Until official SDKs are available, you can build your integration directly against the REST API.

<CardGroup cols={2}>
  <Card title="Quick Start" icon="rocket" href="/docs/quickstart">
    Get from zero to a working payment collection in under 10 minutes.
  </Card>
  <Card title="OpenAPI Spec" icon="braces" href="https://api.heydollr.app/openapi.json">
    Import the spec into Postman, Insomnia, or any code generator.
  </Card>
  <Card title="Integration Guide" icon="map" href="/docs/guides/integration">
    Full end-to-end walkthrough of every flow type.
  </Card>
  <Card title="Error Handling" icon="triangle-exclamation" href="/docs/guides/error-handling">
    Retry logic, idempotency, and error response patterns.
  </Card>
</CardGroup>
