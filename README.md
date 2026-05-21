# Dollr Developer Docs

Official documentation for the [Dollr Open API](https://api.heydollr.app), published on **[docs.heydollr.app](https://docs.heydollr.app)**

## Edit content


| Path                                                                    | Purpose                                                                                               |
| ----------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- |
| `index.mdx`, `quickstart.md`                                            | Introduction hub and tutorial                                                                         |
| `authentication.mdx`, `api-conventions.mdx`                             | Auth and request conventions                                                                          |
| `guides/*.mdx`                                                          | Task-based guides; **Integrate by stack** (Node, Python, PHP, Java, Go, Rust, .NET, Next.js, Laravel) |
| `concepts/*.mdx`                                                        | Core API concepts                                                                                     |
| `api/*.md`                                                              | Short concept pages (link to API Reference)                                                           |
| `reference/*.md`                                                        | Market matrix, errors, support                                                                        |
| `docs.json`                                                             | Navigation, redirects, theme                                                                          |
| `llms.txt`, `llms-full.txt`, `reference/ai-context.mdx`, `ASSISTANT.md` | AI / MCP context                                                                                      |


Use `**.mdx`** for pages with Mintlify components (`Card`, `Steps`, `CodeGroup`, etc.).

## Local preview

Node.js LTS (20 or 22):

```bash
npx mintlify@latest dev
```

Open the URL printed in the terminal (default port 3000).

## Deploy

Production deploys run through **Mintlify** when changes merge to `main` on the connected GitHub repository.

After deploy, [.github/workflows/docs-health.yml](.github/workflows/docs-health.yml) verifies critical URLs.

## Structure


| Tab               | Content                                        |
| ----------------- | ---------------------------------------------- |
| **Documentation** | Introduction, guides, concepts, knowledge base |
| **API Reference** | OpenAPI-generated interactive endpoints        |


Guides explain *how* to integrate; API Reference is the source of truth for request/response fields.

## Legacy

`mkdocs.yml.deprecated` is kept for reference only — it is not deployed to production.