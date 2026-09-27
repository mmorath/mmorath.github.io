# Support — Bediener (Capture & Viewer)

Hilfe für **Bediener** im Feld: die **Erfassungs-App** auf iPhone/iPad und der
**Viewer** auf Apple TV. (Profile erstellen oder den Broker einrichten? Siehe
[Admin-Support](../admin/index.md).) Fehler gefunden oder einen Wunsch? So
nehmen Sie Kontakt auf.

## Kontakt

!!! note "Kontaktadresse"
    **E-Mail:** [info@hecateapps.com](mailto:info@hecateapps.com)

Am schnellsten geht eine Problemmeldung, wenn Sie uns **das Ereignisprotokoll
schicken** (siehe unten): Gerät, iOS-Version und App-Version stehen schon darin.
Ein Satz dazu, was Sie getan und was Sie erwartet hatten, macht sie vollständig.

## Das Ereignisprotokoll schicken

Seit **Version 2.0.0** führen die Erfassungs-App und Hecate Viewer auf iPhone
und iPad ein **Ereignisprotokoll**: Verbindungsversuche, Antworten des Brokers,
Profil-Updates, Zustellungen, Fehler. Das ist meist alles, was wir brauchen, um
ein Problem zu verstehen. Sie finden es unter **Einstellungen → Diagnose →
Ereignisprotokoll**.

<div class="shots">
  <figure><img src="/assets/screens/de/support-settings-row.png" alt="Die Einstellungsliste mit der Zeile Ereignisprotokoll in der Gruppe Diagnose"><figcaption>Einstellungen → Ereignisprotokoll</figcaption></figure>
  <figure><img src="/assets/screens/de/support-event-log.png" alt="Das Ereignisprotokoll: Einträge mit Uhrzeit, neueste zuerst, oben die Knöpfe Aktualisieren, Teilen und An Hecate senden"><figcaption>Das Ereignisprotokoll</figcaption></figure>
  <figure><img src="/assets/screens/de/support-send-dialog.png" alt="Der Dialog Protokoll an Hecate senden? mit den Knöpfen Ja und Abbrechen"><figcaption>An Hecate senden → Ja</figcaption></figure>
  <figure><img src="/assets/screens/de/support-share-sheet.png" alt="Das Teilen-Blatt des Systems mit dem Ereignisprotokoll als Textdatei"><figcaption>Teilen … als Textdatei</figcaption></figure>
</div>

Neben *Aktualisieren* oben rechts bringen es zwei Knöpfe auf den Weg:

- :material-send-outline: **An Hecate senden** öffnet einen fertigen
  **E-Mail-Entwurf** an [info@hecateapps.com](mailto:info@hecateapps.com). Sie
  sehen alles, was darin steht, ergänzen bei Bedarf eine Zeile und schicken ihn
  selbst aus Ihrer eigenen Mail-App ab. (Der Knopf erscheint nur, wenn auf dem
  Gerät ein E-Mail-Konto eingerichtet ist.)
- :material-export-variant: **Ereignisprotokoll teilen** öffnet das Teilen-Blatt
  des Systems mit dem Bericht als Textdatei — für AirDrop, Nachrichten, Dateien
  oder Ihre eigene IT.

Nichts verlässt das Gerät von selbst. Passwörter und Zugangsdaten werden ersetzt,
bevor der Bericht entsteht; Fotos und Standorte sind nie darin enthalten. Die
Bilder oben stammen aus der Erfassungs-App, der Senden-Dialog aus Hecate Admin
— der Bildschirm ist in allen Hecate-Apps derselbe. Der
Viewer auf Apple TV hat kein Ereignisprotokoll.

## Häufige Themen

### Verbindung zu einem Broker
Hecate veröffentlicht an den **von Ihnen konfigurierten MQTT-Broker** unter
*Einstellungen → Broker*. Nutzen Sie dort **Verbindung testen** — es nennt
Ablehnungsgründe (falscher Host, TLS, Zugangsdaten) in verständlicher Sprache.

### Standort
Hecate funktioniert auch ohne Standort, dann tragen die Datensätze jedoch keinen
GPS-Fix. Erteilen oder widerrufen Sie die Berechtigung jederzeit unter
**iOS-Einstellungen → Datenschutz → Ortungsdienste → Hecate**.

### Profile
Erfassungs-Abläufe werden als **Profile** über MQTT geliefert. Erscheint kein
Profil, prüfen Sie, ob Ihr Broker die beibehaltenen Profildokumente vorhält und
ob Ihre Zugangsdaten sie lesen dürfen.

### Apple-TV-Viewer
Der Viewer ist eine **rein lesende** Anzeige: Richten Sie ihn auf denselben
Broker, zeigt er den Live-Asset-Strom, den Ihre Zugangsdaten lesen dürfen.
Erscheint nichts, prüfen Sie die Broker-Verbindung (Host, TLS, Zugangsdaten)
und ob überhaupt Assets veröffentlicht werden. Der Viewer erfasst nichts und
braucht keine Einrichtung der Daten selbst.

---

Siehe auch die Datenschutzerklärungen der
[Erfassungs-App](../../privacy/capture/index.md) und des
[Apple-TV-Viewers](../../privacy/viewer/index.md).
