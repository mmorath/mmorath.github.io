# Support — Hecate Admin

Hilfe für **Administratoren**, die Hecate-Profile verfassen und
veröffentlichen. (Sie nutzen stattdessen die Erfassungs-App oder einen Viewer?
Siehe [Bediener-Support](../operator/index.md).)

## Kontakt

!!! note "Kontaktadresse"
    **E-Mail:** _wird vor der Einreichung bestätigt._

Bei einer Problemmeldung hilft es, Folgendes anzugeben:

- Ihr **Gerät** und Ihre **iOS-Version**,
- die **App-Version** (Einstellungen → Über),
- den Broker, an den Sie veröffentlichen (Host / TLS, **niemals** das
  Passwort),
- was Sie getan haben und was Sie erwartet hätten.

## Häufige Themen

### Verbindung zum Broker
Die Admin-App verbindet sich mit dem **von Ihnen konfigurierten MQTT-Broker**,
über **TLS** (`mqtts`), mit Admin-Zugangsdaten. Das Passwort liegt
ausschließlich im **Schlüsselbund** des Geräts.

### Ein Profil verfassen
Ein Profil deklariert die **Schritte**, **Felder**, Erfassungsregeln und eine
profil-eigene Akzentfarbe. Jedes Feld kann ein Validierungsmuster tragen; die
Admin-App prüft ein Profil vor der Veröffentlichung, damit die Erfassungs-App
nie eines erhält, das sie ablehnen würde.

### Veröffentlichen & Versionieren
Profile werden als **Retained**-Nachrichten veröffentlicht, damit auch später
verbindende Geräte sie erhalten. Jede inhaltliche Änderung muss unter einer
**strikt höheren Version** veröffentlicht werden — Geräte übernehmen ein
Profil nur, wenn seine Version neuer ist als die vorhandene. Zum
„Zurückdrehen" veröffentlichen Sie den alten Inhalt unter einer **neuen,
höheren** Version; Nummern werden nie wiederverwendet oder gesenkt.

### Ein Profil zurückziehen
Um ein Profil von den Geräten zu entfernen, **löschen Sie seine
Retained-Nachricht** (eine leere Retained-Nachricht auf sein Topic
veröffentlichen). Die Geräte entfernen es bei ihrer nächsten Abstimmung.

### Zugangsdaten & Geheimnisse
Profile sind breit lesbar und **dürfen daher keine Geheimnisse enthalten**.
Das Broker-Passwort lebt im Schlüsselbund und wird nie in ein Profil, einen
Provisionierungs-QR oder ein Protokoll geschrieben.

---

Siehe auch die [Datenschutzerklärung der Admin-App](../../privacy/admin/index.md).
