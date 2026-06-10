---
hide:
  - toc
---

<div class="hero" markdown>
![Hecate logo](../assets/hecate-logo.png){ width="96" }
# Hecate
Universal, profile-driven geo-referencing of objects
</div>

---

Hecate turns a sprawl of single-purpose capture apps into **one** configurable
tool. The input form for each use case isn't coded — it's a **profile**: a small
document that declares the steps, fields and allowed input methods, delivered to
devices over MQTT. Change the profile and the same app captures forklifts, fire
extinguishers, network sockets or archaeological finds — with no new build.

## What it does

- **Profile-driven** — every use case is a profile, not a new app.
- **Validated at the source** — each field is checked against its declared
  format the moment it is captured, so bad data never reaches your systems.
- **The right input for each step** — QR codes, 1D/2D barcodes, or manual entry.
- **Always geo-referenced** — every record carries a GPS fix and lands on the map.
- **Streamed over MQTT** — published to your own broker in a uniform,
  self-describing envelope. No developer backend, no analytics, no tracking.
- **Works offline** — a durable outbox holds records out of range and drains
  automatically on reconnect.

## Built on modern iOS

SwiftUI · SwiftData · VisionKit scanning · CoreLocation · TLS MQTT.

---

[Privacy Policy](privacy.md){ .md-button } &nbsp; [Support](support.md){ .md-button }
