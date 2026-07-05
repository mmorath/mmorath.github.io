---
hide:
  - toc
---

# Hecate

*One profile-driven system for geo-referencing physical objects — a family of apps, one broker, no backend.*

Hecate captures physical objects against a **profile** — a configurable
workflow of scans, fields and photos — places them on the map, and streams
them over **MQTT** to a broker of your choice. Nothing about the domain is
hard-coded: change the profile and the same system serves forklifts, fire
extinguishers, network sockets or archaeological finds — **no new build, no
new app**.

!!! tip "The only thing you need is an MQTT broker"

    Hecate requires **no backend system**. The one and only network dependency
    is the **MQTT broker you already control** — on-premise or cloud. There is
    no developer server, no accounts, no analytics, no tracking, and your data
    never touches anyone else's infrastructure.

And Hecate is **not a silo application**: *you* decide what profiles you
create and what role the captured assets play in your enterprise and your
operation. Because everything arrives at your broker in one uniform,
self-describing envelope, any downstream system you choose — a dashboard, a
historian, an ERP hand-off, a Unified Namespace — can subscribe and use the
data. The apps end at the broker; the meaning is yours.

## The problem it solves

Enterprises run a **sprawl of single-purpose capture apps** — one tool per use
case, each built in isolation. The result: inconsistent data quality (every
app validates differently), capture that still happens at a desk instead of
where the work is, records that never say **where** the thing actually is, and
a backend plus device management to run **per tool**.

Hecate replaces the sprawl with **one configurable system**: profiles define
*what* to capture, validation happens at the moment of capture, every record
carries its GPS position, and everything flows through the one broker you
already control.

[:octicons-arrow-right-24: The problem in detail](capture/problem.md) ·
[:octicons-arrow-right-24: How Hecate removes each pain](capture/solution.md)

## The apps

<div class="grid cards" markdown>

-   :material-cellphone: __Hecate__ · the capture app · iPhone & iPad

    ---

    The field tool. Scans, validates and geo-references each object against
    the active profile, then publishes it to your broker. Works offline with
    a durable outbox that drains on reconnect.

    [:octicons-arrow-right-24: Capture overview](capture/index.md)

-   :material-map-marker-radius: __Hecate Viewer__ · iPhone

    ---

    The live map in your pocket. A pure subscriber that plots assets the
    moment they are published and fades them out on a timer you choose —
    it captures nothing and publishes nothing.

    [:octicons-arrow-right-24: iPhone viewer overview](viewer-ios/index.md)

-   :material-tablet: __Hecate Viewer__ · iPad

    ---

    The live map wall to wall. The feed sits in a sidebar beside a
    full-bleed map — tap a row and the map flies to that asset's pin.
    Same subscriber, laid out for the big screen.

    [:octicons-arrow-right-24: iPad viewer overview](viewer-ipad/index.md)

-   :material-tune-variant: __Hecate Admin__ · iPhone & iPad · *under development*

    ---

    The authoring authority. Creates, validates, versions, publishes and
    retires the profiles the capture app consumes, and sets up the broker —
    currently in active development.

    [:octicons-arrow-right-24: Admin overview](admin/index.md)

</div>

## Screenshots

<div class="shots">
  <figure><img src="/assets/screens/assets.png" alt="Hecate capture app — the assets outbox with captured objects awaiting delivery"><figcaption>Hecate — capture &amp; outbox</figcaption></figure>
  <figure><img src="/assets/screens/detail.png" alt="Hecate capture app — an asset's detail view with its captured fields"><figcaption>Hecate — asset detail</figcaption></figure>
  <figure><img src="/assets/screens/viewer-ios-karte.png" alt="Hecate Viewer — the live map with incoming assets as pins"><figcaption>Viewer — the live map</figcaption></figure>
  <figure><img src="/assets/screens/viewer-ios-feed.png" alt="Hecate Viewer — the live feed, newest first with freshness tags"><figcaption>Viewer — the live feed</figcaption></figure>
  <figure class="wide"><img src="/assets/screens/viewer-ipad-karte.png" alt="Hecate Viewer for iPad — the split layout: feed sidebar beside the full-bleed live map"><figcaption>Viewer for iPad — the split layout</figcaption></figure>
</div>

## On the roadmap

- :material-television: **Apple TV viewer** — the same live view as a
  hands-off wall display for shop floors, offices and site entrances.
  [A preview of the concept](viewer/index.md) is already described.

## How they fit together

```
Admin app  ──authors & publishes (retained)──▶  MQTT broker  ◀──reads profiles──  Capture app
                                                     ▲                                  │
                                                     └──────── publishes assets ────────┘
                                                     │
                                          subscribes & displays
                                                     ▼
                              Hecate Viewer (iPhone · iPad) · Apple TV (planned)
```

The **admin** app is the authority for *profiles*; the **capture** app is
read-only on profiles and the authority for *assets*; the **viewers** are
read-only on everything. All apps share one core, one wire format and one
black-and-white visual language — colour comes only from each object's
profile accent.

## The name & the mark

**Hecate** is the Greek goddess of crossroads, thresholds and keys — she who
stands at the boundary and holds what unlocks it. The mark is the **Strophalos**
("Hecate's Wheel") — a labyrinth of winding paths around a single hub: the
routes through the field, and the messages converging on the broker at the
centre.

## For each app

| | Privacy | Support |
| --- | --- | --- |
| **Hecate (capture)** | [Privacy](privacy/capture/index.md) | [Support](support/operator/index.md) |
| **Hecate Viewer (iPhone)** | [Privacy](privacy/viewer-ios/index.md) | [Support](support/operator/index.md) |
| **Hecate Viewer (iPad)** | [Privacy](privacy/viewer-ipad/index.md) | [Support](support/operator/index.md) |
| **Hecate Admin** | [Privacy](privacy/admin/index.md) | [Support](support/admin/index.md) |
| **Apple TV viewer** *(planned)* | [Privacy](privacy/viewer/index.md) | [Support](support/operator/index.md) |
