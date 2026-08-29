---
hide:
  - toc
---

# Hecate Capture

*Universal, profile-driven geo-referencing of objects*

Hecate Capture is a field-first iOS app for **geo-referencing physical objects**. Each
object is captured against a **profile** — a configurable workflow of scans,
fields — then placed on the map with a GPS fix and streamed over
**MQTT** to a broker of your choice.

Nothing about the domain is hard-coded. Change the profile and the same app
captures forklifts, fire extinguishers, network sockets or archaeological
finds — with no new build.

## In one minute

- **One app, many use cases.** Each use case is a *profile*, not a separate app.
- **Validated at the source.** Every field is checked against its declared
  format the moment it's captured.
- **Always located.** Every record carries a GPS fix and lands on the map.
- **Streamed over MQTT.** Published to *your own* broker in a uniform,
  self-describing envelope — no developer backend, no analytics, no tracking.
- **Works offline.** A durable outbox holds records out of range and drains on
  reconnect.

## Screenshots

<div class="shots">
  <figure><img src="/assets/screens/en/capture-assets.png" alt="The assets outbox — captured objects awaiting delivery"><figcaption>Assets &amp; outbox</figcaption></figure>
  <figure><img src="/assets/screens/en/capture-detail.png" alt="An asset's detail view with its captured fields"><figcaption>Asset detail</figcaption></figure>
  <figure><img src="/assets/screens/en/capture-sent.png" alt="Delivery history of sent assets"><figcaption>Delivery history</figcaption></figure>
  <figure><img src="/assets/screens/en/capture-settings.png" alt="The settings hub"><figcaption>Settings</figcaption></figure>
</div>

*Screens come from development builds. Some may show features that require a subscription or arrive in a later release — what the free tier includes today is listed under [Free & Pro](../plans/index.md).*


## The problem

Enterprises run a **sprawl of single-purpose apps** to record data along their
process steps — one tool per use case, each built in isolation. Three failures
follow.

### Inconsistent quality

Every app validates (or fails to validate) its inputs differently, so the data
that reaches downstream systems is uneven and hard to trust.

### Not enabled for mobile

Much of this capture still happens at a desk — not where the work actually is.

### No location context

Almost none of it is geo-referenced, so a record rarely says **where** the thing
it describes actually is.

---

### In short

| Enterprise pain | |
| --- | --- |
| Many single-purpose capture apps | one new build per use case |
| Inconsistent data quality | every app validates differently |
| Not enabled for mobile | capture happens at a desk |
| No location context | records don't say *where* |
| Heavy infrastructure / IT lift | a backend and device management per tool |
| Ungoverned access | no consistent rule for who may capture what |

[:octicons-arrow-right-24: How Hecate removes each of these](#what-hecate-capture-does)

## What Hecate Capture does

Hecate collapses that sprawl into **one** configurable app — and fixes the data
where it's created, not after the fact.

### One app, defined by profiles

The input dialog for each use case is **not coded** — it is a **profile**: a
small document that declares the steps, the fields, and the allowed input
methods, distributed to devices over an MQTT topic. Change the profile and the
same app serves a new use case, with no new build.

### Validated at the source

Every field is checked against its declared format **at the moment of capture**,
so bad data is stopped where it's created rather than cleaned up downstream.

### The right input for each step

A profile's steps decide **what** is captured; each step picks the input method
that fits the job:

- **Manual entry.** Type the value straight into the field.
- **Camera scan.** Point the device camera and let the on-device scanning
  frameworks read **QR codes, 2D Data Matrix codes and 1D barcodes** — no
  network round-trip and no third-party service.

Whichever method a step uses, the value flows through the **same validation and
capture pipeline**, so a profile behaves identically no matter how the data
arrives.

### The building blocks

| Block | Input | Resulting field |
|---|---|---|
| Scan a QR code | QR code via camera | Text, optionally pattern-checked |
| Scan a barcode | 1D barcode (EAN, Code 128, …) | Text, optionally pattern-checked |
| Scan a 2D matrix code | Data Matrix via camera | Text, optionally pattern-checked |
| Capture a quantity | Number entry | Number |
| Tick a status checklist | Checkboxes — several may apply | Multi-select |
| Pick a reason | Radio buttons — exactly one applies | Choice (exactly one) |
| Enter text | Free text, one line | Text |
| Leave a comment | Free text, multi-line | Text, multi-line |

### Always geo-referenced

Every record carries a **GPS fix** and is streamed in a uniform,
self-describing envelope to the broker.

### Governance with almost no infrastructure

The only things required are an **MQTT broker and the app** — no backend to
operate, no device-management enrolment. Authority lives in the broker's
permissions: an admin publishes retained profiles; a user sees only the profiles
their credential is allowed to read, and captures against them.

Because everyone working a use case fills in the **same validated profile**, the
data arrives consistent, comparable, and ready to use — by construction, not by
after-the-fact cleanup.

---

### How it removes each pain point

| Enterprise pain | How Hecate removes it |
| --- | --- |
| Many single-purpose capture apps | One app; each use case is a profile, not a new build |
| Inconsistent data quality | Per-field format validation, blocked at capture |
| Not enabled for mobile | A field-first iOS app, used where the work happens |
| No location context | Every record carries a GPS fix |
| Heavy infrastructure / IT lift | Broker + app only; profiles delivered as retained MQTT messages |
| Ungoverned access | Broker permissions decide who may read which profiles |

## The name & the mark

**Hecate** is the Greek goddess of crossroads, thresholds and keys — she who
stands at the boundary and holds what unlocks it. A field tool lives at exactly
that edge: between the physical object in front of you and the digital systems
that must learn about it. Hecate **locates** it, **guides** the capture,
**carries** it onward to the broker, and **holds the keys** that unlock the path.

The mark is the **Strophalos** ("Hecate's Wheel") — a labyrinth of winding paths
around a single hub: the routes through the field, and the messages converging
on the broker at the centre.
