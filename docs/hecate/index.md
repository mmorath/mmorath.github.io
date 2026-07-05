---
hide:
  - toc
---

# Hecate

*One profile-driven system for geo-referencing physical objects — three apps, one broker, no backend.*

Hecate captures physical objects against a **profile** — a configurable workflow
of scans, fields and photos — places them on the map, and streams them over
**MQTT** to a broker of your choice. Nothing about the domain is hard-coded:
change the profile and the same system serves forklifts, fire extinguishers,
network sockets or archaeological finds.

It is **broker-only**: the only network dependency is the MQTT broker you
control. There is no developer backend, no analytics, and no tracking.

## The apps

<div class="grid cards" markdown>

-   :material-cellphone: __Capture app__ · iPhone & iPad

    ---

    The field tool. Scans, validates and locates each object, then publishes it
    to your broker. Works offline with a durable outbox.

    [:octicons-arrow-right-24: Capture overview](capture/index.md)

-   :material-television: __Apple TV viewer__

    ---

    A live wall display. A pure subscriber that shows assets as they arrive —
    it captures nothing and stores nothing.

    [:octicons-arrow-right-24: Viewer overview](viewer/index.md)

-   :material-map-marker-radius: __Hecate Viewer__ · iPhone & iPad

    ---

    The live map in your pocket. A pure subscriber that plots assets as they
    arrive and fades them out on a timer you choose.

    [:octicons-arrow-right-24: iPhone viewer overview](viewer-ios/index.md)

-   :material-tune-variant: __Admin app__ · iPhone & iPad

    ---

    The authoring authority. Creates, validates, versions, publishes and retires
    the profiles the capture app consumes, and sets up the broker.

    [:octicons-arrow-right-24: Admin overview](admin/index.md)

</div>

## How they fit together

```
Admin app  ──authors & publishes (retained)──▶  MQTT broker  ◀──reads profiles──  Capture app
                                                     ▲                                  │
                                                     └──────── publishes assets ────────┘
                                                     │
                                          subscribes & displays
                                                     ▼
                                  Apple TV viewer · Hecate Viewer (iPhone)
```

The **admin** app is the authority for *profiles*; the **capture** app is
read-only on profiles and the authority for *assets*; the **viewer** is read-only
on everything. All three are governed by the **Hecate Architecture & Protocol
Specification v1.1** and built on the shared
[`HecateKit`](https://github.com/mmorath/HecateKit) core.

## The name & the mark

**Hecate** is the Greek goddess of crossroads, thresholds and keys — she who
stands at the boundary and holds what unlocks it. The mark is the **Strophalos**
("Hecate's Wheel") — a labyrinth of winding paths around a single hub: the
routes through the field, and the messages converging on the broker at the
centre. The mark carries no colour of its own; the only colour in each app is
the per-profile accent.

## For each app

| | Privacy | Support |
| --- | --- | --- |
| **Capture** | [Privacy](privacy/capture/index.md) | [Support](support/operator/index.md) |
| **Apple TV viewer** | [Privacy](privacy/viewer/index.md) | [Support](support/operator/index.md) |
| **Hecate Viewer (iPhone)** | [Privacy](privacy/viewer-ios/index.md) | [Support](support/operator/index.md) |
| **Admin** | [Privacy](privacy/admin/index.md) | [Support](support/admin/index.md) |
