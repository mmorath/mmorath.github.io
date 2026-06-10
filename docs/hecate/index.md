---
hide:
  - toc
---

# Hecate

*Universal, profile-driven geo-referencing of objects*

Hecate is a field-first iOS app for **geo-referencing physical objects**. Each
object is captured against a **profile** — a configurable workflow of scans,
fields and photos — then placed on the map with a GPS fix and streamed over
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

## Read on

<div class="grid cards" markdown>

-   :material-alert-circle-outline: __The problem__

    ---

    Why a sprawl of single-purpose capture apps leaves data inconsistent,
    desk-bound and location-blind.

    [:octicons-arrow-right-24: The problem](problem.md)

-   :material-checkbox-marked-circle-outline: __What Hecate does__

    ---

    How one profile-driven app collapses that sprawl and fixes the data at the
    source.

    [:octicons-arrow-right-24: What Hecate does](solution.md)

</div>

## The name & the mark

**Hecate** is the Greek goddess of crossroads, thresholds and keys — she who
stands at the boundary and holds what unlocks it. A field tool lives at exactly
that edge: between the physical object in front of you and the digital systems
that must learn about it. Hecate **locates** it, **guides** the capture,
**carries** it onward to the broker, and **holds the keys** that unlock the path.

The mark is the **Strophalos** ("Hecate's Wheel") — a labyrinth of winding paths
around a single hub: the routes through the field, and the messages converging
on the broker at the centre.
