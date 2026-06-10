# mmorath.github.io

Public site for apps by **Matthias Morath**, built with
[MkDocs Material](https://squidfunk.github.io/mkdocs-material/) and served via
GitHub Pages at <https://mmorath.github.io/>.

Each app lives in its own section under `docs/<app>/`:

| App | Pages |
| --- | --- |
| **Hecate** | [Overview](https://mmorath.github.io/hecate/) · [Privacy](https://mmorath.github.io/hecate/privacy/) · [Support](https://mmorath.github.io/hecate/support/) |

The application source code lives in separate, private repositories. This repo
holds only the public website.

## Build locally

```bash
pip install mkdocs-material
mkdocs serve          # live preview at http://127.0.0.1:8000
mkdocs gh-deploy      # build + publish to the gh-pages branch
```

© 2026 Matthias Morath
