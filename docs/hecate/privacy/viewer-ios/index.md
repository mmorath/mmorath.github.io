# Privacy Policy — Hecate Viewer (iPhone)

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

## Diagnostic reports you send us

There is exactly one exception to everything above, and it is your decision
every time: under **Settings → Event log** you can **send** us a report if you
would like help. It never happens by itself.

- You see the **whole** report before it leaves the device — nothing is added
  after that screen.
- You decide **each single time**.
- You send it from **your own mail app**. The app sends nothing in the
  background; there is no server of ours it could send anything to.
- It contains: device and system version, app and core version, your plan
  (free/pro) and log lines. **Never** photos, location fixes, passwords, tokens
  or broker credentials — matching patterns are replaced before sending.
- A **comment** and a **reply address** are optional. We use the address solely
  to answer that one report.

If you would rather keep the report or hand it to your own IT: "Share …" on the
same screen gives you the same information as a text file, without us seeing
any of it.

## Children

Hecate is a professional/field utility and is not directed at children.

## Changes to this policy

If the app's data handling changes, this page will be updated.
