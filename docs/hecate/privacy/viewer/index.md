# Privacy Policy — Hecate for Apple TV

**Effective date:** 2026-06-18
**Developer:** Matthias Morath

The Hecate Apple TV app is a **read-only viewer**. It connects to an MQTT broker
you configure and **displays** the assets published to it. It is a subscriber,
not a sensor.

## What we collect

**Nothing.** The viewer:

- has **no camera** and captures no images;
- requests **no location** and records no GPS data;
- has **no user accounts** and asks for no personal information;
- runs **no third-party analytics, advertising, or tracking** of any kind.

There is **no hosted backend operated by the developer**. The developer receives
none of your data.

## What it displays

The app **subscribes** to the broker you point it at and shows the asset data it
receives — the objects, their state, and any location or profile information
that the broker already holds. That data is created elsewhere (by the capture
app) and governed entirely by **your** broker and its permissions. The viewer
neither creates nor stores it persistently; it renders the live stream while
running.

## Where data goes

Nowhere new. The viewer only **reads** from your broker. It never publishes,
never writes, and never transmits data to the developer or any third party.

## Storage and security

- The app keeps only the **broker connection settings** you enter on the device
  so it can reconnect. Any password is held in the platform keychain, never in
  plain text and never written to logs.
- Connections to the broker can use **TLS** (`mqtts`) so data in transit is
  encrypted.

## Your choices

Because the viewer collects nothing, there is nothing to opt out of, export, or
delete beyond the broker connection settings, which you can change or remove on
the device at any time. The asset data shown is governed by *your* broker's
retention and access rules.

## Children

Hecate is a professional/field utility and is not directed at children.

## Changes to this policy

If the app's data handling changes, this page will be updated.
