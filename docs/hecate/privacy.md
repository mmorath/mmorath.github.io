# Privacy Policy — Hecate

*Deutsche Fassung [unten](#datenschutzerklarung-hecate).*

**Effective date:** 2026-06-11
**Developer:** Matthias Morath

Hecate is a field tool for geo-referencing physical objects. It collects only
what is needed to identify and locate the assets you record. There is **no
hosted backend operated by the developer**, and **no third-party analytics or
tracking** of any kind.

## What we collect

What the app captures is **defined entirely by the profile** your organisation's
administrator configures — a profile is a customizable form describing the fields
and scans for one use case. **We, as the developer, neither create these profiles
nor ever see them or the data you capture against them.** What any given
deployment collects is therefore decided by *your* administrator, not by us.

For a typical profile the app handles:

- **Asset details** you enter or scan (e.g. serial number, order number, type).
- **An optional photo** of the asset, if you choose to take one.
- **Precise location (GPS)** at the moment of capture — *only if you grant the
  location permission*. You can decline or revoke it in iOS Settings at any
  time; the app still works without it.

## Where it goes

Asset data is published **only to the MQTT broker you configure**. You choose
and control that broker. The developer operates no server, receives none of your
data, and never sees the profiles you use or the assets you capture against them.
There is no advertising, no profiling, and no cross-app or cross-website
tracking.

## Storage and security

- Assets are stored **on your device** until you delete them.
- The broker **password is held in the iOS Keychain** — never in plain text and
  never written to logs.
- Connections to the broker can use **TLS** (`mqtts`) so data in transit is
  encrypted.

## Data sharing

We do **not** sell, rent, or share your data with third parties. The only
transmission is the publish to **your own** MQTT broker, performed on your
behalf at your direction.

## Your choices

- **Location:** grant, decline, or revoke at any time in iOS Settings → Privacy.
- **Photos:** entirely optional, per asset.
- **Deletion:** delete any asset on-device at any time. Data already published
  to your broker is governed by *your* broker's retention.

## Children

Hecate is a professional/field utility and is not directed at children.

## Changes to this policy

If the app's data handling changes, this page and the in-app
**Settings → Privacy** screen will be updated together.

---

# Datenschutzerklärung — Hecate

**Gültig ab:** 11.06.2026
**Entwickler:** Matthias Morath

Hecate ist ein Feldwerkzeug zur Geo-Referenzierung physischer Objekte. Es erfasst
nur, was zur Identifizierung und Lokalisierung der von Ihnen erfassten Assets
erforderlich ist. Es gibt **kein vom Entwickler betriebenes Backend** und **keine
Analyse- oder Tracking-Dienste Dritter**.

## Was wir erfassen

Was die App erfasst, wird **ausschließlich durch das Profil** bestimmt, das die
Administratorin oder der Administrator Ihrer Organisation einrichtet — ein Profil
ist ein anpassbares Formular, das die Felder und Scans für einen Anwendungsfall
beschreibt. **Wir als Entwickler erstellen diese Profile nicht und sehen weder
die von Ihnen verwendeten Profile noch die damit erfassten Daten.** Was eine
konkrete Installation erfasst, entscheidet daher *Ihr* Administrator, nicht wir.

Bei einem typischen Profil verarbeitet die App:

- **Asset-Daten**, die Sie eingeben oder scannen (z. B. Serien-, Auftragsnummer,
  Typ).
- **Ein optionales Foto** des Assets, sofern Sie eines aufnehmen.
- **Den genauen GPS-Standort** zum Zeitpunkt der Erfassung — *nur, wenn Sie die
  Standortberechtigung erteilen*. Sie können diese jederzeit in den
  iOS-Einstellungen verweigern oder widerrufen; die App funktioniert auch ohne.

## Wohin die Daten gehen

Asset-Daten werden **ausschließlich an den von Ihnen konfigurierten MQTT-Broker**
gesendet. Diesen Broker wählen und kontrollieren Sie selbst. Der Entwickler
betreibt keinen Server, erhält keine Ihrer Daten und sieht weder die von Ihnen
verwendeten Profile noch die damit erfassten Assets. Es gibt keine Werbung, kein
Profiling und kein App- oder Website-übergreifendes Tracking.

## Speicherung und Sicherheit

- Assets werden **auf Ihrem Gerät gespeichert**, bis Sie sie löschen.
- Das Broker-**Passwort wird im iOS-Schlüsselbund** gespeichert — niemals im
  Klartext und niemals in Protokollen.
- Verbindungen zum Broker können **TLS** (`mqtts`) nutzen, sodass Daten während
  der Übertragung verschlüsselt sind.

## Weitergabe von Daten

Wir **verkaufen, vermieten oder teilen Ihre Daten nicht** mit Dritten. Die
einzige Übertragung ist die Veröffentlichung an **Ihren eigenen** MQTT-Broker,
die in Ihrem Auftrag und auf Ihre Veranlassung erfolgt.

## Ihre Wahlmöglichkeiten

- **Standort:** jederzeit in iOS-Einstellungen → Datenschutz erteilen,
  verweigern oder widerrufen.
- **Fotos:** vollständig optional, je Asset.
- **Löschung:** Sie können jedes Asset jederzeit auf dem Gerät löschen. Bereits
  an Ihren Broker gesendete Daten unterliegen der Aufbewahrung *Ihres* Brokers.

## Kinder

Hecate ist ein professionelles Feld-Werkzeug und richtet sich nicht an Kinder.

## Änderungen dieser Erklärung

Ändert sich der Datenumgang der App, werden diese Seite und der In-App-Bildschirm
**Einstellungen → Datenschutz** gemeinsam aktualisiert.
