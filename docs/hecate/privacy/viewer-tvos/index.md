# Privacy Policy — Hecate Viewer TV

**Effective date:** 2026-08-24
**Developer:** Matthias Morath

Hecate Viewer TV is a **display**. It runs on an Apple TV, connects to an MQTT
broker you configure, and **shows** the assets published to it on a live wall.
It is a subscriber, not a sensor.

## What we collect

**Nothing.** The app:

- has **no camera** and captures no images;
- has **no photo library access** and reads none of your media;
- requests **no location** and records no GPS data — an Apple TV does not move,
  so the wall plots the positions your *capture* app recorded, and asks the
  television for nothing;
- has **no user accounts** and asks for no personal information;
- runs **no third-party analytics, advertising, or tracking** of any kind;
- contains **no crash-reporting SDK**.

There is **no hosted backend operated by the developer**. The developer receives
none of your data.

## The two things it talks to

This is the whole of the app's network activity:

1. **Your local network, once, to be set up.** Typing on a remote is painful, so
   the TV never types. Instead it shows a QR code and waits on your local
   network for **Hecate Viewer on your iPhone or iPad** to hand it the broker
   configuration. tvOS asks your permission for local-network access the first
   time this happens; the handoff is encrypted, travels only between your two
   devices, and reaches no server of ours. The configuration — including the
   broker credential — goes straight into the device keychain.
2. **Your MQTT broker, to subscribe.** After that the app **reads** from the
   broker you pointed it at, and nothing else.

## What it displays

The app **subscribes** to your broker and shows the asset data it receives — the
objects, their captured fields, and any location or profile information the
broker already holds. That data is created elsewhere (by the capture app) and
governed entirely by **your** broker and its permissions. Received assets are
held **in memory only**; quitting the app discards them.

## Where data goes

Nowhere new. The app only **reads** from your broker. It never publishes, never
writes, and never transmits data to the developer or any third party.

## Storage and security

- The app keeps only the **broker connection settings** it was paired with, so
  it can reconnect after a power cut without being paired again, plus a cache of
  the broker's **profile documents** (workflow descriptions and their colours,
  which carry no personal data).
- The broker password is held in the **device keychain**, never in plain text
  and never written to logs. Diagnostic logs stay on the device and record only
  the *length* of sensitive values, never their content.
- Connections to the broker can use **TLS** (`mqtts`) so data in transit is
  encrypted.
- The app's only other stored state is display preference — which profile or
  zone the wall is scoped to — kept in the app's own preferences.

## Your choices

- **Local-network access** can be declined or revoked at any time in tvOS
  Settings. Note that pairing is the app's only setup path, so declining it
  leaves the wall with nothing to show.
- Re-pair the Apple TV at any time to point it at a different broker. The asset
  data shown is governed by *your* broker's retention and access rules.

## Children

Hecate is a professional/field utility and is not directed at children.

## Changes to this policy

If the app's data handling changes, this page will be updated.

---

[:octicons-arrow-right-24: The Apple TV app](../../viewer-tvos/index.md) ·
[:octicons-arrow-right-24: Support](../../support/operator/index.md)
