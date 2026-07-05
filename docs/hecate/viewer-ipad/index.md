---
hide:
  - toc
---

# Hecate Viewer for iPad

*The live map, wall to wall — with the feed always at its side.*

Hecate Viewer for iPad is the **read-only companion** to the capture app,
laid out for the big screen. It connects to the same MQTT broker,
**subscribes** to the asset stream, and shows everything at once: the live
feed as a **sidebar**, the **map** filling the rest — no tabs, both panes
always in view, in portrait and landscape alike.

It is a **pure viewer**. It captures nothing, edits nothing, and publishes
nothing; everything on screen came from your broker and lives only in memory.

## In one minute

- **Sidebar and map, together.** Every incoming asset appears as a feed row
  *and* as a pin the moment it is published. Fresh arrivals pulse teal; as
  they age they settle to grey.
- **Tap a row, fly to its pin.** The sidebar is the map's index: tapping a
  row zooms the map to that asset and rings it — tap again (or tap empty
  map) to release. The row's info button, or the pin itself, opens the full
  detail.
- **Assets fade out on a timer.** Choose how long a received asset stays
  visible (minutes, or forever). Pins visibly shrink and fade as their time
  runs out, then leave sidebar and map together — so the screen only ever
  shows what is current.
- **Filter by profile.** One tap on a profile chip narrows both panes to
  that workflow, in its accent colour; one more tap brings everything back.
- **Read-only by design.** The viewer only *subscribes* — it never publishes
  to the broker and never writes a profile or an asset.
- **One product.** The same wire format and the same black-and-white visual
  language as the other Hecate apps; colour comes only from each object's
  profile accent.

## Screenshots

<div class="shots">
  <figure class="wide"><img src="/assets/screens/viewer-ipad-karte.png" alt="Hecate Viewer for iPad — the split layout: live feed sidebar beside the full-bleed map with incoming assets as pins"><figcaption>The split layout — sidebar feed and live map</figcaption></figure>
</div>

## What it shows

The viewer renders the live asset stream from the broker — each object's
captured fields, its profile colour and name, and its position on the map.
The broker's **retained backlog** fills the screen the moment you connect, so
you never open onto an empty map while there is history to show; everything
after that arrives live. What appears is governed entirely by **your broker
and its permissions**, not by the app.

## Setup

Connect the app to your MQTT broker — scan a provisioning QR from your
administrator or enter host, port, TLS and credentials by hand (the password
goes straight into the device keychain). Pull the profiles once, pick how long
assets should stay on screen, and watch. There is nothing to configure about
the data itself, because the data is defined by your profiles and published by
the capture app.

On iPhone, the same live view ships as
[Hecate Viewer for iPhone](../viewer-ios/index.md) with a Karte/Feed tab
layout — the iPad app falls back to those tabs when it shares the screen in
Split View.

---

[:octicons-arrow-right-24: Privacy](../privacy/viewer-ipad/index.md) ·
[:octicons-arrow-right-24: Support](../support/operator/index.md) ·
[:octicons-arrow-right-24: The iPhone viewer](../viewer-ios/index.md)
