
## Authorship (binding, family-wide — 2026-09-03)

Every commit in this repository is authored and committed by its human
maintainer. AI assistants (e.g. Claude) are tools, not contributors — for
legal reasons (authorship and rights attribution must rest with a natural
person):

- **no** AI name as commit author or committer,
- **no** `Co-Authored-By` trailers naming an AI,
- this applies to sub-agents, automation and CI alike.

The `commit-msg` hook (where `core.hooksPath = .githooks` is active)
rejects such commits; the rule holds with or without the hook.
