---
hide:
  - toc
---

# Hecate for Apple TV

*A live wall display for your Hecate assets — read-only, on the big screen.*

!!! info "On the roadmap"

    The Apple TV viewer is **planned** and not yet available. This page
    describes the concept. Today, the live view ships as
    [Hecate Viewer for iPhone & iPad](../viewer-ios/index.md).

The Hecate Apple TV app turns any screen into a **live view of the objects your
team is capturing**. It connects to the same MQTT broker as the capture app,
**subscribes** to the asset stream, and shows records as they arrive — on a
shop-floor monitor, in an office, or at a site entrance.

It is a **pure viewer**. It captures nothing, edits nothing, and stores nothing
of its own.

## In one minute

- **Live, hands-off.** Assets appear and update as they're published; the screen
  keeps itself current with no interaction.
- **Read-only by design.** The viewer only *subscribes* — it never publishes to
  the broker and never writes a profile or an asset.
- **Same broker, same data.** Point it at your broker and it shows exactly what
  your credentials are allowed to read. No separate setup of the data itself.
- **Nothing collected.** No camera, no location, no accounts, no analytics — it
  is a display, not a sensor.
- **One product.** The same wire format and the same black-and-white visual
  language as the other Hecate apps; colour comes only from each object's
  profile accent.

## What it shows

The viewer renders the live asset stream from the broker — the objects, their
current state, and (where present) their location and profile accent. Because it
reads the same retained profiles and the same asset topics as the rest of the
system, what appears on screen is governed entirely by **your broker and its
permissions**, not by the app.

## Setup

Connect the app to your MQTT broker (host, port, TLS, credentials). Once
connected, the viewer subscribes and begins displaying — there is nothing to
configure about the data itself, because the data is defined by your profiles
and published by the capture app.

---

[:octicons-arrow-right-24: Privacy](../privacy/viewer/index.md) ·
[:octicons-arrow-right-24: Support](../support/operator/index.md) ·
[:octicons-arrow-right-24: The capture app](../capture/index.md)
