# Privacy Policy — Hecate Admin

**Effective date:** 2026-06-18
**Developer:** Matthias Morath

Hecate Admin is an **authoring tool**. It is used to create and publish the
**profiles** that configure the capture app, and to set up the connection to
your MQTT broker. It is not a data-collection app.

## What we collect

**No telemetry and no personal data.** The admin app:

- requests **no location** and has **no camera**;
- runs **no third-party analytics, advertising, or tracking**;
- sends **nothing** to the developer — there is **no hosted backend**.

## What it handles

- **Profiles you author.** A profile describes the fields and steps of a capture
  workflow. Profiles are **configuration, not personal data**, and **must not
  contain secrets** — they are broadly readable by the devices that subscribe to
  them.
- **Broker credentials.** To publish profiles, the app connects to **your** MQTT
  broker with admin credentials. The password is held in the platform
  **Keychain** — never in plain text, never written to a profile, a provisioning
  QR, or a log, and never transmitted anywhere except to authenticate to your
  broker.

## Where data goes

The only network destination is the **MQTT broker you configure**. The admin app
publishes profiles there (as retained messages) at your direction. It transmits
nothing to the developer or any third party, and there is no advertising,
profiling, or cross-app tracking.

## Storage and security

- Profiles and connection settings are stored **on your device**.
- The broker **password is held in the Keychain**.
- Connections to the broker can use **TLS** (`mqtts`) so data in transit is
  encrypted.

## Your choices

- **Credentials:** stored only on the device; remove them at any time.
- **Profiles:** you author, publish and retire them; retiring a profile clears
  its retained message on your broker.

## Children

Hecate is a professional utility and is not directed at children.

## Changes to this policy

If the app's data handling changes, this page and the in-app privacy screen will
be updated together.
