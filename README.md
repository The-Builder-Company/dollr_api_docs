# Dollr Developer Docs

Official documentation for the [Dollr Open API](https://api.heydollr.app), published on **[docs.heydollr.app](https://docs.heydollr.app)** via [Mintlify](https://mintlify.com).

## Edit content

- Prose pages: `docs/**/*.md`
- Site config & navigation: `docs.json`
- AI context: `llms.txt`, `ASSISTANT.md`

## Local preview

Mintlify CLI requires Node.js LTS (20 or 22):

```bash
npx mintlify@latest dev
```

Optional MkDocs preview (not deployed to production):

```bash
pip install mkdocs-material
mkdocs serve
```

## Deploy

Production deploys are handled by **Mintlify** when changes merge to `main` on the connected GitHub repository. This repo does not publish to GitHub Pages.

After deploy, the [Docs health check](.github/workflows/docs-health.yml) workflow verifies critical URLs and sitemap entries.

## Structure

| Tab | Content |
|-----|---------|
| Documentation | Guides, API concepts, resources |
| API Reference | OpenAPI-generated endpoints (`/api-reference/...`) |

API Guide pages link to matching API Reference paths for interactive testing.
