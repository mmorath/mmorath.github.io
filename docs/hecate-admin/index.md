---
hide:
  - toc
---

# Hecate Admin

*The authoring authority for Hecate profiles*

Hecate Admin is the universal iOS companion to the [Hecate](../hecate/index.md) capture
app. Where the capture app is strictly **read-only** on a profile — it follows
whatever workflow a profile describes — the admin app is the **authority** that
**authors, validates, versions, publishes and retires** those profiles.

A *profile* is the configurable workflow of scans, fields and photos that tells
the capture app what an object is and how to record it. Hecate Admin is where
that profile is written and governed.

## In one minute

- **Authoring counterpart, same core.** Built on the same shared Swift core
  (`HecateKit`) and the same Hecate Architecture & Protocol Specification as the
  capture app — one product, two roles.
- **Broker-only — there is no backend.** Profiles reach devices as **retained
  MQTT messages**; deletion is a zero-length retained payload to the same topic.
  The admin app introduces no server and no second network dependency.
- **Validated before publish.** A profile is checked against its declared schema
  and versioning contract before it is ever published to the broker.
- **Credentials never travel.** The admin broker credential lives in the
  platform Keychain and is never written to a profile, a manifest, a
  provisioning QR, a log, or the repository.
- **Universal iOS.** One adaptive app for iPhone and iPad.

## Design identity

Hecate Admin shares the capture app's visual language. App chrome is **strict
black-and-white** — there is **no global brand colour** ("the mark carries no
colour of its own"). The only colour in the product is the **per-profile
accent**, which follows a profile through its row, swatch and detail card.
Active versus inactive is shown by **fill and a checkmark, never by colour**. An
absent or invalid accent degrades to a built-in palette and never breaks a
screen.

The mark is the shared **Strophalos** ("Hecate's Wheel") — the same labyrinth of
winding paths around a single hub that the capture app carries.

## Status

Hecate Admin is built in phases. It currently ships as a **branded shell**
(Phase 0): a buildable, on-brand, navigable app that demonstrates the
per-profile accent convention with a display-only demo profile set. Authoring,
validation, versioning, publishing and the broker connection arrive in later
phases. The point of Phase 0 is that the app already *looks like Hecate* before
it *does* anything.

## Read on

<div class="grid cards" markdown>

-   :material-cellphone: __The capture app__

    ---

    Hecate is the field-first app that captures objects against these profiles
    and streams them to your broker.

    [:octicons-arrow-right-24: Hecate overview](../hecate/index.md)

</div>

The application source lives in a separate, private repository.
