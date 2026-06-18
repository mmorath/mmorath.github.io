# What Hecate does

Hecate collapses that sprawl into **one** configurable app — and fixes the data
where it's created, not after the fact.

## One app, defined by profiles

The input dialog for each use case is **not coded** — it is a **profile**: a
small document that declares the steps, the fields, and the allowed input
methods, distributed to devices over an MQTT topic. Change the profile and the
same app serves a new use case, with no new build.

## Validated at the source

Every field is checked against its declared format **at the moment of capture**,
so bad data is stopped where it's created rather than cleaned up downstream.

## The right input for each step

A profile's steps decide **what** is captured; each step picks the input method
that fits the job:

- **Manual entry.** Type the value straight into the field.
- **Camera scan.** Point the device camera and let the on-device scanning
  frameworks read **QR codes, 2D Data Matrix codes, 1D barcodes, and printed
  text** — no network round-trip and no third-party service.

Whichever method a step uses, the value flows through the **same validation and
capture pipeline**, so a profile behaves identically no matter how the data
arrives.

## Always geo-referenced

Every record carries a **GPS fix** and is streamed in a uniform,
self-describing envelope to the broker.

## Governance with almost no infrastructure

The only things required are an **MQTT broker and the app** — no backend to
operate, no device-management enrolment. Authority lives in the broker's
permissions: an admin publishes retained profiles; a user sees only the profiles
their credential is allowed to read, and captures against them.

Because everyone working a use case fills in the **same validated profile**, the
data arrives consistent, comparable, and ready to use — by construction, not by
after-the-fact cleanup.

---

## How it removes each pain point

| Enterprise pain | How Hecate removes it |
| --- | --- |
| Many single-purpose capture apps | One app; each use case is a profile, not a new build |
| Inconsistent data quality | Per-field format validation, blocked at capture |
| Not enabled for mobile | A field-first iOS app, used where the work happens |
| No location context | Every record carries a GPS fix |
| Heavy infrastructure / IT lift | Broker + app only; profiles delivered as retained MQTT messages |
| Ungoverned access | Broker permissions decide who may read which profiles |
