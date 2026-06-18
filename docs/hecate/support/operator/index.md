# Support — Operators (Capture & Viewer)

Help for **operators** in the field: the iPhone/iPad **capture app** and the
Apple TV **viewer**. (Authoring profiles or setting up the broker? See
[Admin support](../admin/index.md).) Found a bug or have a request? Here's how to
get in touch.

## Contact

!!! note "Contact address"
    **Email:** _to be confirmed before submission._

When reporting a problem, it helps to include:

- your **iOS version** and **device** (e.g. iPhone 15 Pro, iOS 18.5),
- the **app version** (Settings → About),
- what you did and what you expected to happen.

## Common topics

### Connecting to a broker
Hecate publishes to the **MQTT broker you configure** under
*Settings → Broker*. Use **Test Connection** there — it reports rejection
reasons (bad host, TLS, credentials) in plain language.

### Location
Hecate works without location, but records then carry no GPS fix. Grant or
revoke the permission any time in **iOS Settings → Privacy → Location Services →
Hecate**.

### Profiles
Capture workflows are delivered as **profiles** over MQTT. If no profile
appears, check that your broker has the retained profile documents and that
your credentials are allowed to read them.

### Apple TV viewer
The viewer is a **read-only** display: point it at the same broker and it shows
the live asset stream your credentials can read. If nothing appears, check the
broker connection (host, TLS, credentials) and that assets are being published.
The viewer captures nothing and needs no setup of the data itself.

---

See also the privacy policies for the
[capture app](../../privacy/capture/index.md) and the
[Apple TV viewer](../../privacy/viewer/index.md).
