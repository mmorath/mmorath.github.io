# Privacy Policy — Hecate Viewer (iPhone & iPad)

**Effective date:** 2026-07-05
**Developer:** Matthias Morath

Hecate Viewer is a **read-only monitor**. It connects to an MQTT broker you
configure and **displays** the assets published to it. It is a subscriber, not
a sensor.

## What we collect

**Nothing.** The viewer:

- runs **no third-party analytics, advertising, or tracking** of any kind;
- has **no user accounts** and asks for no personal information;
- uses the **camera only** when you choose to scan a broker-provisioning QR
  code in Settings — no images are stored or transmitted;
- uses your **location only** to show the "you are here" dot on the live map,
  *and only if you grant the permission* — it is never stored and never
  transmitted. Decline or revoke it at any time; the map simply loses the
  blue dot.

There is **no hosted backend operated by the developer**. The developer
receives none of your data.

## What it displays

The app **subscribes** to the broker you point it at and shows the asset data
it receives — the objects, their captured fields, and any location or profile
information the broker already holds. That data is created elsewhere (by the
capture app) and governed entirely by **your** broker and its permissions.
Received assets are held **in memory only**; quitting the app discards them.
You can also set a display time limit, after which shown assets fade from the
screen on their own.

## Where data goes

Nowhere new. The viewer only **reads** from your broker. It never publishes,
never writes, and never transmits data to the developer or any third party.

## Storage and security

- The app keeps only the **broker connection settings** you enter, so it can
  reconnect, plus a cache of the broker's **profile documents** (workflow
  descriptions that carry no personal data).
- Any password is held in the **iOS Keychain**, never in plain text and never
  written to logs. Diagnostic logs stay on the device and record only the
  *length* of sensitive values, never their content.
- Connections to the broker can use **TLS** (`mqtts`) so data in transit is
  encrypted.

## Your choices

- **Location and camera** can be granted, declined, or revoked at any time in
  iOS Settings; both are optional.
- Remove a broker configuration (and its Keychain password) at any time in
  the app's Settings. The asset data shown is governed by *your* broker's
  retention and access rules.

## Children

Hecate is a professional/field utility and is not directed at children.

## Changes to this policy

If the app's data handling changes, this page will be updated.
