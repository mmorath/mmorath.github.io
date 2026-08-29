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

## 2026-08-29

### Added — a Free & Pro comparison page, in four languages

The site said what Hecate does and what we stand for, but never what the
free tier actually gives you. That gap sat badly next to the fairness value
we had just sharpened: you cannot invite comparison and then publish
nothing to compare. `hecate/plans/` now carries three tables — Capture,
Admin, Viewer — with the free limits stated in numbers (10 captures a day,
5 steps per profile, 1 broker configuration, 1 active profile) and a plain
explanation of what each limit really counts.

Two decisions worth recording. **The page says outright that Pro is not on
sale**: the shipping apps carry the free tier only, so a price column would
promise a purchase that does not exist — instead the page commits to
stating the price here, in full, the moment it does. And **features that
are built but switched off are marked *planned*, never as something
withheld**: no feature visible today will ever grow a lock, and the page
says so.

### Changed — fairness now promises a *comparable* offer, in all four languages

The fairness value already said "no buy-in" and "cancel any time". What it
did not say is the part that makes those two verifiable: the price is
stated openly, there is no minimum term, and the offer is meant to be
**compared**. That is the sharper promise — anyone who wants to do the
maths should be able to, and we would rather be compared than make
comparing hard. Reworded in en/de/fr/es (each written in its own idiom,
not translated word for word) and in the reference PDF
(`hecate-business/latex/vision-mission.tex`, v1.1), whose product check now
names the App Store's monthly cancellation as the mechanism.

### Changed — the landing entry is "Home", so "Hecate" is said once

The sidebar opened with **Hecate** twice in a row: Material puts the
`site_name` above the menu as its header (with the logo), and the first nav
entry carried the same word. One is the brand, the other is a page — and
nothing on screen said which. The entry is now **Home** (Start / Accueil /
Inicio), which names what it actually is: the head of the site.
"Overview" was the obvious alternative and was rejected — every app group
already uses that word one level down.

### Changed — the sidebar stopped shouting: six entries instead of thirty

A first-time visitor met roughly thirty sidebar entries at once, and the
Vision & Mission page — added the same day, second from the top — was hard
to find in the noise. Three causes, all removed:

- **`navigation.sections`** rendered every top-level group as an
  always-open section. Without it, Material's default applies: groups
  collapse and open only along the active path. The landing page now shows
  **six** entries — Hecate, Getting started, Vision & Mission, The apps,
  Support, Privacy — with three collapsed groups.
- **Support and Privacy appeared twice per app** (five groups × two links)
  *plus* once as hubs: ten of the thirty entries were the same two pages
  over and over. They now live once each, as a collapsed group whose first
  child is the hub itself (`navigation.indexes`). **No page moved** — the
  per-app privacy URLs that App Store Connect links to are untouched;
  navigation placement never changes a URL.
- **`toc.integrate`** folded each page's own headings into the left
  sidebar, so the landing page alone contributed seven more lines to the
  list we were trying to shorten. The table of contents is on the right
  again, where it belongs to the page rather than to the site.

The three viewers are one product on three screens and now read that way:
one **Hecate Viewer** entry with iPhone / iPad / Apple TV beneath it,
instead of three separate top-level groups.

### Fixed — the privacy hub's Apple TV card pointed at the legacy page

It still linked `privacy/viewer/`, the pre-rename path. The card now points
at `privacy/viewer-tvos/`, which is what the navigation lists. The legacy
page stays in place and keeps answering: the shipped iPhone Viewer links to
that URL from inside the app.

## 2026-08-29

### Added — Vision & Mission, in four languages

New page `hecate/vision/` (EN base plus `.de/.fr/.es` twins), linked right
after Getting started: the vision (traceability replaces conflict — and it
traces the process, never the person), the mission, and the five values,
each backed by what the product actually does. The wording is the reference
text from `hecate-business/positioning/vision-mission.md` — site and
business repo deliberately share one source, so the story cannot fork.

## 2026-08-26

### Added — a "Getting started" entry, in all four languages

`docs/hecate/getting-started/` in English, German, French and Spanish (4 files),
plus a top-level **Getting started** nav entry with `nav_translations` for the
other three locales (Erste Schritte / Premiers pas / Primeros pasos).

**Why it sits second, ahead of the per-app groups.** The site explained every
app well and never explained the one step that precedes all of them: Hecate has
no backend, so nothing works until the visitor has an MQTT broker and the apps
point at it. A prospect who has decided to try Hecate needs that before any
single app's overview is useful to them, and until now the only place it existed
was a support page they would reach after already being stuck.

The page walks one evaluation end to end — choose a broker, connect Admin,
provision the field devices by QR, capture, then **verify the message with an
MQTT client that is not ours** — and closes with the topic tree, a permission
matrix with broker rules, a troubleshooting table and what changes for
production (mTLS, roles, Unified Namespace, downstream consumers).

Three things it deliberately does *not* do:

- **No invented facts.** Topics, ports and defaults are taken from HecateKit
  (`AssetTopic.swift`, `FeaturesModel.swift`) and the provisioning spec, not
  from prose. Where the MDM channel is specified but unbuilt on iOS, the page
  says so rather than implying it works.
- **No HiveMQ partnership claim.** HiveMQ Cloud is named alongside EMQX
  Serverless and Mosquitto as an evaluation option, with no free-tier limits
  quoted — those change, and a number here would go stale silently.
- **No password in the QR story.** The provisioning code carries coordinates
  only; the page explains why, because that is the question every evaluator
  asks second.

### Changed — the screenshot sync learned four broker screens

`tools/sync_screenshots.py` gained `gs-broker-connection`, `gs-broker-auth`,
`gs-broker-share-qr` and `gs-provisioning` (16 images: 4 screens x 4 languages).

They come from **Capture** rather than Admin on purpose. The broker screens are
HecateKit's and look the same in both apps, but Admin's doc set has them in
English only — a German page showing an English screenshot is worse than one
showing Capture's. If Admin's German, French and Spanish sets ever include them,
those four mappings are the ones to switch.

## 2026-08-24

### Added — the Apple TV app finally has pages of its own, in all four languages

`docs/hecate/viewer-tvos/` and `docs/hecate/privacy/viewer-tvos/`, each in
English, German, Spanish and French (8 files). The tvOS app's App Store metadata
has been pointing at `hecate/privacy/viewer-tvos/`, `hecate/viewer-tvos/` and
`hecate/support/operator/` for a while; the first two existed in **no** language,
so a pre-release audit measured all three tvOS store URLs as **404** while the
five iOS/iPadOS equivalents returned 200. A 404 privacy URL is an automatic App
Store rejection, so this blocked the submission outright.

The pages are modelled on `viewer-ipad` and corrected for the television, which
is a genuinely different privacy story rather than a reworded one:

- **no camera, no photo library, no location.** An Apple TV does not move, so the
  wall plots the positions the *capture* app recorded and asks the television for
  nothing. The iPad page's camera-and-location paragraphs have no counterpart
  here and are gone rather than softened.
- **the local-network pairing handoff is named as network activity**, because it
  is the app's only setup path: the TV shows a QR code and waits for the phone's
  Viewer to hand it the broker configuration, since typing a hostname and
  password on a remote is miserable. tvOS raises a local-network permission
  prompt for this, so the policy has to explain it.
- **the only two things it talks to** are that handoff and the MQTT subscription
  to the reader's own broker. Stated as a closed list, not as examples.

Checked against the shipped manifest rather than written from memory:
`tvOS-Hecate-Viewer/Hecate/PrivacyInfo.xcprivacy` declares "Data Not Collected"
(empty `NSPrivacyCollectedDataTypes`, `NSPrivacyTracking` false, and
`UserDefaults`/`CA92.1` as its one accessed-API reason), and these pages claim
exactly that and nothing more.

### Changed — the TV nav entry and the hub links point at the new slug

`mkdocs.yml`'s "Hecate Viewer (Apple TV)" group and the Apple-TV links in
`docs/hecate/index*.md` (all four languages, both the card link and the
privacy/support table) now use `viewer-tvos`. All three viewers therefore read
alike — `viewer-ios`, `viewer-ipad`, `viewer-tvos` — and the tvOS store metadata
gets a URL shaped like its siblings'.

### Not done, deliberately — the old `hecate/viewer/` pair stays exactly where it is

Those two pages (`hecate/viewer/`, `hecate/privacy/viewer/`) are the *previous*
Apple TV pages, dated 2026-06-18, and the obvious tidy-up would be to delete them
or redirect them here. Both would break a shipped app: the **iPhone** Viewer links
to `/hecate/privacy/viewer/` from inside its About screen
(`iOS-Hecate-Viewer` → `StartButtonView.swift`), so that URL has to keep
answering, and redirecting it *here* would hand iPhone users the television's
policy. So the files stay, unlisted — mkdocs now reports them under "exist in the
docs directory, but are not included in the nav", which is expected and is the
same state the root `index.md` and `hecate-admin/` redirect stubs are in.

The real fix belongs in the app: once `iOS-Hecate-Viewer` points at
`hecate/privacy/viewer-ios/` (which has existed for a while), this pair can become
redirect stubs to `viewer-tvos` and the duplicate-policy problem goes away.

**Note that none of this is live until someone runs `make deploy`.** The three
tvOS URLs keep returning 404 to App Store Connect until then; a local `site/`
build proves the pages compile, not that they are published.

### Fixed — the Viewer screenshots ignored the language switcher too

`docs/hecate/viewer-ios/` and `docs/hecate/viewer-ipad/` embedded the flat,
language-neutral `/assets/screens/viewer-*.png` on every language page — the
same three English images for German, French and Spanish readers. They now read
from `/assets/screens/<lang>/`, like the landing and capture pages. The flat
copies are deleted; nothing referenced them any more.

The Spanish hub page's Apple-TV figure now uses the Spanish `tv-wall.png`,
which existed all along but was referenced as `en/`.

### Fixed — the last Spanish fallback: `viewer-ios-feed` captured for real

The iOS Viewer's screenshot suite still looked for a *tab bar* to reach the
Feed, but the app switched to a segmented control long ago — the capture was
silently skipped in every language run, and the Spanish set never had one. The
test now drives the segmented control (fixed in iOS-Hecate-Viewer), the es-ES
run was recaptured, and `es/viewer-ios-feed.png` replaces the English fallback
on both Spanish pages. iPad `tapzoom` stays English-only by design: no page
references a Spanish one (the Spanish hub shows the iPad feed figure instead),
and no UI test produces it.

## 2026-08-19

### Added — `make screens`, so the app screenshots stop arriving by hand

`tools/sync_screenshots.py` pulls the images the site embeds straight out of the
app repos' per-language screenshot sets and downscales them to the 720 px height
the pages actually render:

```sh
make screens                    # all four languages
make screens SCREEN_LANG=de     # one
make screens-check              # which site images are older than the app repos'
```

Sources default to sibling clones (`../iOS-Hecate-Capture`,
`../iOS-Hecate-Admin`); `HECATE_CAPTURE_REPO` / `HECATE_ADMIN_REPO` override.
Only the names in the script's `SCREENS` table are touched — the Viewer and tvOS
images in the same directories come from other repos and other runs.

### Fixed — the capture pages showed one un-localized set in all four languages

`docs/hecate/capture/index{,.de,.fr,.es}.md` all pointed at
`/assets/screens/assets.png`, `detail.png`, `sent.png` and `settings.png`: four
English screenshots from 2026-07-05, served to German, French and Spanish
readers alike. They now read from their own language directory
(`/assets/screens/<lang>/capture-*.png`), like the landing page already did.

### Removed — the four un-localized Capture images

`docs/assets/screens/{assets,detail,sent,settings}.png` (2026-07-05, 1.0 MB
together). The capture pages were their only readers and now read per-language
files instead. The Viewer images at the same level stay: four pages still embed
them.

### Changed — every Capture and Admin screenshot is current again

Both apps changed visibly since the last set was taken (the Capture home lost its
map segment, screen titles replaced the app name in the nav bar, actions moved
into floating buttons within thumb reach). All four languages were recaptured
from the apps' UI-test suites and re-synced.

### Design decisions

- **Downscale on the way in, not in CSS.** A 6.9" device PNG is 1320x2868 and
  ~900 KB; the page renders it 331 px wide. Serving the full-size file would cost
  the visitor almost a megabyte per thumbnail for pixels the browser throws away.
  `sips` resamples to 720 px high, which is what the existing images already were
  — this only writes down how they got that way.
- **A table of names, not a directory sweep.** The sync copies the six images the
  pages embed, listed explicitly. A sweep would quietly add whatever the app
  repos captured next, and a page that embeds an image the table does not list
  fails loudly under `make screens-check` instead of silently keeping an old one.

## 2026-08-18

A long day on the site: three languages became four, the pages stopped
claiming things that were no longer true, and every app got its own name back.

### Added — Spanish, the fourth language

The apps have shipped in four languages all along (en/de/fr/es); the site
stopped at three. All nineteen pages now exist as `.es.md` siblings —
landing, capture overview with problem/solution, admin, the three viewers,
six privacy pages, three support pages and both redirect stubs (targets moved
to `/es/`). Formal *usted* register throughout; product names, MQTT vocabulary
and the contact address untouched; the privacy assurances translated
word-faithfully, nothing softened. `mkdocs.yml` registers the locale.

### Added — the gallery shows all five apps, in the reader's language, and opens on click

The screenshots section grew from five shots to ten (capture
outbox/detail/delivered, admin profiles/detail, viewer map/feed, iPad
split/feed, TV wall), and each language page shows its **own** localized set
generated from the fastlane store screenshots. Clicking a screenshot now opens
it enlarged (mkdocs-glightbox, also added to `make install`). Eight of ten
Spanish shots are real es-ES captures; the iPhone feed motif and the TV wall
still borrow the English images, which the paths show honestly.

### Changed — three apps, three names

The capture app was called plain "Hecate" wherever the site named it — card,
H1, privacy heading, and the sentence defining what it is — while "Hecate" is
also the family and the site. The store metadata had said "Hecate Capture" all
along, so the site was the odd one out. Now aligned in four languages, and the
navigation carries the product names (Hecate Capture, Hecate Viewer for
iPhone/iPad/Apple TV, Hecate Admin), which retired fifteen nav_translations —
a product name needs no translation.

### Changed — the pages tell the truth about what shipped

Hecate Admin was still described as "under development" and the Apple TV
viewer as "planned", though both were released in the 2026-08-16 family cut.
The admin card lost its status suffix, the TV viewer moved from the roadmap
into the app grid as a real card, and both concept admonitions went. The
per-app table stopped calling the capture app three different things.

### Changed — the building blocks are back, corrected

The capture solution page carries the block table again — eight blocks
including the quantity block the old cached version never had, and without the
two the product no longer has: photo capture (removed in HecateKit 0.17.0, ADR
004) and serial-number scanning (iPhone-only camera text recognition, so
profiles built on it would not run on the Android fleet). The camera bullet
stopped promising printed-text reading for the same reason. No test-code
examples: the table suffices.

### Added — Android and the CT47 are on the record

The landing pages now say what was only true in private: Hecate Capture is
finished for Android, arrives in the Google Play Store at the end of 2026, and
drives the built-in scan engine of industrial scanners such as the Honeywell
CT47 (manufacturer link, verified).

### Changed — the letterbox is real

All nine support pages carried a placeholder ("to be confirmed before
submission") where the contact address belongs. The family has had an official
address since 2026-08-17, receipt verified by test mail, so the pages now say
`info@hecateapps.com` as a mailto link.

### Fixed — two translations were behind their English base

The **German** and, later the same day, the **French** operator support pages
were missing the operator/admin split in the intro and the entire Apple TV
viewer section — a silent drift of exactly the kind this file exists to catch.
Both rewritten in full; all four languages now carry the same structure.

### Removed — a header script that could no longer match anything

`assets/section-title.js` rewrote the header to "Hecate · Admin" for paths
under `/hecate-admin/`, which has been a redirect stub since the admin pages
moved to `/hecate/admin/`. It went, along with its `extra_javascript` entry.

### Added — defensive `.env` hygiene

Rescued from a stale sibling clone before its deletion (it was the only work
that existed nowhere else): if a `.env` ever appears in this repo it must not
be committable. Templates (`*.example`) stay tracked.

## 2026-08-01

### Added — a way to back the project

- **"Back the project" on the Support page** (EN / DE / FR): a short, honest
  pitch — one developer, no backend, no accounts, no tracking — plus a
  *Buy me a coffee* button and a scannable QR, both linking to
  `buymeacoffee.com/hecateHQ`. The QR lives at
  `docs/assets/hecate-bmac-qr.png`; the button uses the Material `md-button`
  style already in the theme, so it matches the rest of the site.

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
