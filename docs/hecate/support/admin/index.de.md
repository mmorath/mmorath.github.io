# Support — Hecate Admin

Hilfe für **Administratoren**, die Hecate-Profile verfassen und
veröffentlichen. (Sie nutzen stattdessen die Erfassungs-App oder einen Viewer?
Siehe [Bediener-Support](../operator/index.md).)

## Kontakt

!!! note "Kontaktadresse"
    **E-Mail:** [info@hecateapps.com](mailto:info@hecateapps.com)

Bei einer Problemmeldung hilft es, Folgendes anzugeben:

- Ihr **Gerät** und Ihre **iOS-Version**,
- die **App-Version** (Einstellungen → Über),
- den Broker, an den Sie veröffentlichen (Host / TLS, **niemals** das
  Passwort),
- was Sie getan haben und was Sie erwartet hätten.

## Das Ereignisprotokoll schicken

Seit **Version 2.0.0** führt Hecate Admin ein **Ereignisprotokoll** —
Broker-Verbindungen, Ergebnisse beim Veröffentlichen, Prüffehler — unter
**Einstellungen → Diagnose → Ereignisprotokoll**. Gerät, iOS- und App-Version
stehen schon darin; damit erübrigt sich der Großteil der Liste oben.

<div class="shots">
  <figure><img src="/assets/screens/de/support-admin-settings-row.png" alt="Die Einstellungen von Hecate Admin mit der Zeile Ereignisprotokoll in der Gruppe Diagnose"><figcaption>Einstellungen → Ereignisprotokoll</figcaption></figure>
  <figure><img src="/assets/screens/de/support-admin-event-log.png" alt="Das Ereignisprotokoll in Hecate Admin: Einträge mit Uhrzeit, oben die Knöpfe Aktualisieren, Teilen und An Hecate senden"><figcaption>Das Ereignisprotokoll</figcaption></figure>
  <figure><img src="/assets/screens/de/support-send-dialog.png" alt="Der Dialog Protokoll an Hecate senden? mit den Knöpfen Ja und Abbrechen"><figcaption>An Hecate senden → Ja</figcaption></figure>
  <figure><img src="/assets/screens/de/support-share-sheet.png" alt="Das Teilen-Blatt des Systems mit dem Ereignisprotokoll als Textdatei"><figcaption>Teilen … als Textdatei</figcaption></figure>
</div>

- :material-send-outline: **An Hecate senden** öffnet einen E-Mail-Entwurf an
  [info@hecateapps.com](mailto:info@hecateapps.com) — Sie sehen alles, was
  darin steht, und schicken ihn selbst ab (nur sichtbar, wenn ein E-Mail-Konto
  eingerichtet ist).
- :material-export-variant: **Ereignisprotokoll teilen** gibt den Bericht als
  Textdatei an das Teilen-Blatt — für AirDrop, Dateien oder Ihre eigene IT.

Passwörter und Zugangsdaten werden ersetzt, bevor der Bericht entsteht. Die
ersten drei Bilder stammen aus Hecate Admin, das Teilen-Blatt
aus der Erfassungs-App. Die ausführliche Anleitung steht im
[Bediener-Support](../operator/index.md#das-ereignisprotokoll-schicken).

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
