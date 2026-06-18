# Support — Hecate Admin

Help for **administrators** authoring and publishing Hecate profiles. (Using the
capture app or the Apple TV viewer instead? See
[Operator support](../operator/index.md).)

## Contact

!!! note "Contact address"
    **Email:** _to be confirmed before submission._

When reporting a problem, it helps to include:

- your **device** and **iOS version**,
- the **app version** (Settings → About),
- the broker you're publishing to (host / TLS, **never** the password),
- what you did and what you expected to happen.

## Common topics

### Connecting to the broker
The admin app connects to the **MQTT broker you configure**, over **TLS**
(`mqtts`), with admin credentials. The password is stored only in the device
**Keychain**.

### Authoring a profile
A profile declares the **steps**, **fields**, capture rules and a per-profile
accent colour. Each field can carry a validation pattern; the admin app checks a
profile before it is published so the capture app never receives one it would
reject.

### Publishing & versioning
Profiles are published as **retained** messages so devices that connect later
still receive them. Every meaningful change must publish a **strictly higher
version** — devices apply a profile only when its version is newer than the one
they hold. To "revert", republish the old content under a **new, higher**
version; never reuse or lower a number.

### Retiring a profile
To remove a profile from devices, **clear its retained message** (publish an
empty retained payload to its topic). Devices prune it on their next
reconciliation.

### Credentials & secrets
Profiles are broadly readable, so they **must not contain secrets**. The broker
password lives in the Keychain and is never written into a profile, a
provisioning QR, or a log.

---

See also the [Admin privacy policy](../../privacy/admin/index.md).
