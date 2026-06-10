# Support — Hecate

Need help, found a bug, or have a feature request? Here's how to get in touch.

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

---

See also the [Privacy Policy](privacy.md).
