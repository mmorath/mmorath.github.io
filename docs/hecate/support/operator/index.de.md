# Support — Bediener (Capture & Viewer)

Hilfe für **Bediener** im Feld: die **Erfassungs-App** auf iPhone/iPad und der
**Viewer** auf Apple TV. (Profile erstellen oder den Broker einrichten? Siehe
[Admin-Support](../admin/index.md).) Fehler gefunden oder einen Wunsch? So
nehmen Sie Kontakt auf.

## Kontakt

!!! note "Kontaktadresse"
    **E-Mail:** [info@hecateapps.com](mailto:info@hecateapps.com)

Wenn Sie ein Problem melden, hilft es, Folgendes anzugeben:

- Ihre **iOS-Version** und Ihr **Gerät** (z. B. iPhone 15 Pro, iOS 18.5),
- die **App-Version** (Einstellungen → Über),
- was Sie getan haben und was Sie erwartet hatten.

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
