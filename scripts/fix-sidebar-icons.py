#!/usr/bin/env python3
"""Normalize page frontmatter icons to Font Awesome names that render in Mintlify sidebar."""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

# path -> (icon, iconType or None)
PAGE_ICONS: dict[str, tuple[str, str | None]] = {
    "index.mdx": ("house", None),
    "quickstart.md": ("rocket", None),
    "authentication.mdx": ("key", None),
    "api-conventions.mdx": ("file-lines", None),
    "guides/choose-integration.mdx": ("route", None),
    "guides/collect-via-checkout.mdx": ("cart-shopping", None),
    "guides/payout-with-nodejs.mdx": ("arrow-up-right", None),
    "guides/integration.md": ("map", None),
    "guides/realtime-status.mdx": ("tower-broadcast", None),
    "guides/error-handling.md": ("triangle-exclamation", None),
    "guides/collect-with-nodejs.mdx": ("node", "brands"),
    "guides/collect-with-python.mdx": ("python", "brands"),
    "guides/collect-with-django.mdx": ("python", "brands"),
    "guides/collect-with-ruby.mdx": ("gem", None),
    "guides/collect-with-php.mdx": ("php", "brands"),
    "guides/collect-with-java.mdx": ("java", "brands"),
    "guides/collect-with-go.mdx": ("golang", "brands"),
    "guides/collect-with-rust.mdx": ("circle-info", None),
    "guides/collect-with-dotnet.mdx": ("microsoft", "brands"),
    "guides/collect-with-nextjs.mdx": ("react", "brands"),
    "guides/collect-with-laravel.mdx": ("laravel", "brands"),
    "concepts/parties-and-counterparties.mdx": ("users", None),
    "concepts/sessions-and-executions.mdx": ("bolt", None),
    "api/invoices.md": ("file-invoice", None),
    "api/orders.md": ("box", None),
    "api/checkouts.md": ("bag-shopping", None),
    "api/sessions.md": ("link", None),
    "api/executions.md": ("play", None),
    "api/status.md": ("chart-line", None),
    "api/payment-accounts.md": ("wallet", None),
    "api/links.md": ("link", None),
    "api/predictions.md": ("chart-line", None),
    "api/fees.md": ("percent", None),
    "api/merchants.md": ("building", None),
    "api/realtime-keys.md": ("tower-broadcast", None),
    "api/parties.md": ("user", None),
    "api/counterparties.md": ("users", None),
    "knowledge-base/index.mdx": ("circle-question", None),
    "knowledge-base/invalid-credentials-401.mdx": ("key", None),
    "knowledge-base/forbidden-403-unverified.mdx": ("shield", None),
    "knowledge-base/validation-422.mdx": ("list-check", None),
    "knowledge-base/duplicate-reference-id.mdx": ("clone", None),
    "knowledge-base/session-expired-or-invalid.mdx": ("clock", None),
    "knowledge-base/payment-processing-status.mdx": ("spinner", None),
    "knowledge-base/rate-limit-429.mdx": ("gauge-high", None),
    "knowledge-base/server-error-5xx.mdx": ("server", None),
    "reference/payments-by-market.md": ("globe", None),
    "reference/status-and-incidents.md": ("tower-broadcast", None),
    "reference/examples.mdx": ("flask", None),
    "reference/ai-context.mdx": ("robot", None),
    "reference/sdks.md": ("boxes-stacked", None),
    "reference/glossary.md": ("book", None),
    "reference/support.md": ("life-ring", None),
    "reference/error-catalog.md": ("triangle-exclamation", None),
    "agentic-development/index.mdx": ("wand-magic-sparkles", None),
    "agentic-development/start-here.mdx": ("compass", None),
    "agentic-development/prompt-library.mdx": ("comments", None),
}


def patch_frontmatter(text: str, icon: str, icon_type: str | None) -> str:
    if not text.startswith("---"):
        return text
    end = text.find("---", 3)
    if end == -1:
        return text
    body = text[end + 3 :]
    front = text[3:end]
    lines = [ln for ln in front.split("\n") if not re.match(r"^icon(Type)?:", ln)]
    lines.append(f'icon: "{icon}"')
    if icon_type:
        lines.append(f'iconType: "{icon_type}"')
    else:
        # drop iconType if switching to solid-only page
        pass
    new_front = "\n".join(lines).strip("\n") + "\n"
    return "---\n" + new_front + "---" + body


def main() -> None:
    for rel, (icon, icon_type) in PAGE_ICONS.items():
        path = ROOT / rel
        if not path.exists():
            print("skip missing", rel)
            continue
        original = path.read_text()
        updated = patch_frontmatter(original, icon, icon_type)
        if updated != original:
            path.write_text(updated)
            print("updated", rel, icon, icon_type or "solid")


if __name__ == "__main__":
    main()
