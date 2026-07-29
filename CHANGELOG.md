# Changelog

Notable changes to **mmorath.github.io** — the public site, including the
`/hecate/` umbrella pages and the per-app privacy policies.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).
The site is not versioned, so entries are grouped by date.

**Why this file exists, and why it starts here.** This repo publishes the privacy
policies that App Store Connect links to. When the apps change what they do, the site
becomes wrong *silently* — nothing builds, nothing fails, the pages simply keep making a
claim that is no longer true. That happened on 2026-07-29 and is the first entry below.
Everything before that date is in `git log` only; this file starts at the point where a
trail became worth keeping.

Convention: for privacy-relevant edits, record **all three language variants** and the
**reason the claim changed**, not just the wording.

---

## 2026-07-29

### Fixed — the site claimed a photo capture that no longer exists

- **15 places across EN / DE / FR corrected.** Removing the photo step from HecateKit,
  Capture, Admin and the three Viewers left the site as the last place still promising it.
  Touched: the Hecate landing pages, the Capture pages, the Admin pages, and the Capture
  privacy policies in all three languages.

- **The privacy pages needed more than a deletion.** `docs/hecate/privacy/capture/` said
  *"Photos: entirely optional"* — a sentence whose whole point was that the user was in
  control. Replacing it with *"Photos: none"* alone would have read like a shrug, so each
  now states the **structural** reason: Hecate publishes a `{header, data}` JSON envelope
  over MQTT and runs no image backend, so there is no path by which a photo could leave
  the device. A capability that cannot exist is a stronger guarantee than one that is
  merely switched off, and that is what the pages now say.

- **Elsewhere the fix was narrower:** *"scans, fields and photos"* → *"scans and fields"*
  on the landing, Capture and Admin pages.

#### Design decisions

- **The site is checked against the apps, not the other way round.** Nothing in the build
  can detect this class of error: MkDocs renders a false claim exactly as happily as a
  true one, and no test reads prose. Until something does, a change to what the apps
  collect has to include this repo in its blast radius — the removal was found only
  because the family was swept deliberately, not because anything flagged it.

- **All three languages in one commit, never staggered.** A German page that still
  promises photos while the English one does not is not a translation lag — it is two
  different privacy claims for the same app, both published, both linked from the store.
