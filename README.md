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

A `Makefile` wraps the MkDocs commands (run `make` for the full list):

```bash
make install   # install the toolchain (mkdocs-material) via pip
make serve     # live preview at http://127.0.0.1:8000
make build     # build the static site into ./site
make deploy    # build + publish to the gh-pages branch (republishes the live site)
make clean     # remove ./site
```

© 2023-2026 Matthias Morath · All rights reserved
