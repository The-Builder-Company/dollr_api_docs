#!/usr/bin/env python3
"""Set or merge keywords frontmatter; every keyword starts with Dollr."""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

# path -> keywords list (all must start with Dollr)
KEYWORDS: dict[str, list[str]] = {
    "index.mdx": [
        "Dollr API",
        "Dollr developer documentation",
        "Dollr payment API Africa",
        "Dollr mobile money API",
    ],
    "quickstart.md": [
        "Dollr API quickstart",
        "Dollr invoice API",
        "Dollr collect payment",
        "Dollr API tutorial",
    ],
    "authentication.mdx": [
        "Dollr API authentication",
        "Dollr OAuth",
        "Dollr API keys",
        "Dollr Bearer token",
    ],
    "api-conventions.mdx": [
        "Dollr API conventions",
        "Dollr API reference",
        "Dollr REST API",
    ],
    "changelog.mdx": [
        "Dollr API changelog",
        "Dollr release notes",
        "Dollr API updates",
    ],
    "guides/choose-integration.mdx": [
        "Dollr API integration",
        "Dollr checkout",
        "Dollr invoice API",
        "Dollr payout API",
    ],
    "guides/collect-via-checkout.mdx": [
        "Dollr checkout API",
        "Dollr collect payment",
        "Dollr API",
    ],
    "guides/payout-with-nodejs.mdx": [
        "Dollr payout API",
        "Dollr API Node.js",
        "Dollr mobile money payout",
    ],
    "guides/integration.md": [
        "Dollr API integration guide",
        "Dollr collect API",
        "Dollr payout API",
    ],
    "guides/realtime-status.mdx": [
        "Dollr API webhooks",
        "Dollr payment status",
        "Dollr realtime API",
    ],
    "guides/error-handling.md": [
        "Dollr API errors",
        "Dollr error handling",
        "Dollr API troubleshooting",
    ],
    "guides/collect-with-nodejs.mdx": [
        "Dollr API Node.js",
        "Dollr invoice API",
        "Dollr collect payment",
    ],
    "guides/collect-with-python.mdx": [
        "Dollr API Python",
        "Dollr invoice API",
        "Dollr collect payment",
    ],
    "guides/collect-with-django.mdx": [
        "Dollr API Django",
        "Dollr API Python",
        "Dollr invoice API",
    ],
    "guides/collect-with-ruby.mdx": [
        "Dollr API Ruby",
        "Dollr invoice API",
        "Dollr collect payment",
    ],
    "guides/collect-with-php.mdx": [
        "Dollr API PHP",
        "Dollr invoice API",
        "Dollr collect payment",
    ],
    "guides/collect-with-java.mdx": [
        "Dollr API Java",
        "Dollr invoice API",
        "Dollr collect payment",
    ],
    "guides/collect-with-go.mdx": [
        "Dollr API Go",
        "Dollr invoice API",
        "Dollr collect payment",
    ],
    "guides/collect-with-rust.mdx": [
        "Dollr API Rust",
        "Dollr invoice API",
        "Dollr collect payment",
    ],
    "guides/collect-with-dotnet.mdx": [
        "Dollr API .NET",
        "Dollr invoice API",
        "Dollr C# integration",
    ],
    "guides/collect-with-nextjs.mdx": [
        "Dollr API Next.js",
        "Dollr invoice API",
        "Dollr React integration",
    ],
    "guides/collect-with-laravel.mdx": [
        "Dollr API Laravel",
        "Dollr PHP integration",
        "Dollr invoice API",
    ],
    "concepts/parties-and-counterparties.mdx": [
        "Dollr party API",
        "Dollr counterparty API",
        "Dollr API",
    ],
    "concepts/sessions-and-executions.mdx": [
        "Dollr checkout session",
        "Dollr payment execution",
        "Dollr API",
    ],
    "api/invoices.md": [
        "Dollr invoice API",
        "Dollr payment link",
        "Dollr API",
        "Dollr billing API",
    ],
    "api/orders.md": [
        "Dollr order API",
        "Dollr checkout",
        "Dollr API",
        "Dollr e-commerce payments",
    ],
    "api/checkouts.md": [
        "Dollr checkout API",
        "Dollr collect payment",
        "Dollr API",
    ],
    "api/sessions.md": [
        "Dollr checkout session",
        "Dollr API",
        "Dollr payment session",
    ],
    "api/executions.md": [
        "Dollr payment execution",
        "Dollr collect API",
        "Dollr API",
    ],
    "api/status.md": [
        "Dollr payment status",
        "Dollr API",
        "Dollr collection status",
    ],
    "api/payment-accounts.md": [
        "Dollr payment account",
        "Dollr wallet API",
        "Dollr API",
    ],
    "api/links.md": [
        "Dollr payment link",
        "Dollr API",
        "Dollr hosted checkout",
    ],
    "api/predictions.md": [
        "Dollr API",
        "Dollr mobile money detection",
        "Dollr fees preview",
    ],
    "api/fees.md": [
        "Dollr API fees",
        "Dollr pricing",
        "Dollr API",
    ],
    "api/merchants.md": [
        "Dollr merchant API",
        "Dollr API",
    ],
    "api/realtime-keys.md": [
        "Dollr realtime API",
        "Dollr API",
        "Dollr live payment status",
    ],
    "api/parties.md": [
        "Dollr party API",
        "Dollr API",
        "Dollr customer record",
    ],
    "api/counterparties.md": [
        "Dollr counterparty API",
        "Dollr API",
    ],
    "knowledge-base/index.mdx": [
        "Dollr API troubleshooting",
        "Dollr knowledge base",
        "Dollr API errors",
    ],
    "knowledge-base/invalid-credentials-401.mdx": [
        "Dollr API 401",
        "Dollr authentication error",
        "Dollr API",
    ],
    "knowledge-base/forbidden-403-unverified.mdx": [
        "Dollr API 403",
        "Dollr merchant verification",
        "Dollr API",
    ],
    "knowledge-base/validation-422.mdx": [
        "Dollr API 422",
        "Dollr validation error",
        "Dollr API",
    ],
    "knowledge-base/duplicate-reference-id.mdx": [
        "Dollr reference_id",
        "Dollr API idempotency",
        "Dollr API",
    ],
    "knowledge-base/session-expired-or-invalid.mdx": [
        "Dollr checkout session",
        "Dollr API session error",
        "Dollr API",
    ],
    "knowledge-base/payment-processing-status.mdx": [
        "Dollr PROCESSING status",
        "Dollr mobile money API",
        "Dollr API",
    ],
    "knowledge-base/rate-limit-429.mdx": [
        "Dollr API rate limit",
        "Dollr API 429",
        "Dollr API",
    ],
    "knowledge-base/server-error-5xx.mdx": [
        "Dollr API 500",
        "Dollr API server error",
        "Dollr API",
    ],
    "reference/payments-by-market.md": [
        "Dollr payment methods",
        "Dollr mobile money Liberia",
        "Dollr API Rwanda",
    ],
    "reference/status-and-incidents.md": [
        "Dollr API status",
        "Dollr API incidents",
        "Dollr API uptime",
    ],
    "reference/examples.mdx": [
        "Dollr API examples",
        "Dollr OpenAPI",
        "Dollr Postman",
    ],
    "reference/ai-context.mdx": [
        "Dollr API documentation AI",
        "Dollr llms.txt",
        "Dollr MCP",
    ],
    "reference/sdks.md": [
        "Dollr API SDK",
        "Dollr API client libraries",
    ],
    "reference/glossary.md": [
        "Dollr API glossary",
        "Dollr API terms",
    ],
    "reference/support.md": [
        "Dollr API support",
        "Dollr developer help",
    ],
    "reference/error-catalog.md": [
        "Dollr API error catalog",
        "Dollr API errors",
        "Dollr troubleshooting",
    ],
    "vibe-coding/index.mdx": [
        "Dollr API AI integration",
        "Dollr vibe coding",
        "Dollr developer docs",
    ],
    "vibe-coding/start-here.mdx": [
        "Dollr API Cursor",
        "Dollr llms.txt setup",
        "Dollr MCP",
    ],
    "vibe-coding/prompt-library.mdx": [
        "Dollr API prompts",
        "Dollr integration prompts",
        "Dollr AI coding",
    ],
}


def format_keywords(words: list[str]) -> str:
    inner = ", ".join(f'"{w}"' for w in words)
    return f"keywords: [{inner}]"


def patch_file(path: Path, words: list[str]) -> bool:
    text = path.read_text()
    if not text.startswith("---"):
        return False
    end = text.find("---", 3)
    if end == -1:
        return False
    front = text[3:end]
    body = text[end + 3 :]
    lines = [ln for ln in front.split("\n") if not ln.startswith("keywords:")]
    lines.append(format_keywords(words))
    new_front = "\n".join(lines).strip("\n") + "\n"
    new_text = "---\n" + new_front + "---" + body
    if new_text != text:
        path.write_text(new_text)
        return True
    return False


def main() -> None:
    for rel, words in KEYWORDS.items():
        path = ROOT / rel
        if not path.exists():
            print("missing", rel)
            continue
        if patch_file(path, words):
            print("updated", rel)


if __name__ == "__main__":
    main()
