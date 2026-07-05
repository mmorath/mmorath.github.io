# Datenschutzerklärung — Hecate Viewer (iPhone & iPad)

**Gültig ab:** 05.07.2026
**Entwickler:** Matthias Morath

Hecate Viewer ist ein **rein lesender Monitor**. Er verbindet sich mit einem
von Ihnen konfigurierten MQTT-Broker und **zeigt** die dort veröffentlichten
Assets an. Er ist ein Abonnent, kein Sensor.

## Was wir erheben

**Nichts.** Der Viewer:

- betreibt **keine Analyse-, Werbe- oder Tracking-Dienste Dritter**;
- hat **keine Benutzerkonten** und fragt keine persönlichen Daten ab;
- nutzt die **Kamera nur**, wenn Sie in den Einstellungen einen
  Provisionierungs-QR-Code scannen — es werden keine Bilder gespeichert oder
  übertragen;
- nutzt Ihren **Standort nur** für den „Sie sind hier"-Punkt auf der
  Live-Karte, *und nur, wenn Sie die Berechtigung erteilen* — er wird weder
  gespeichert noch übertragen. Sie können sie jederzeit verweigern oder
  widerrufen; die Karte verliert dann lediglich den blauen Punkt.

Es gibt **kein vom Entwickler betriebenes Backend**. Der Entwickler erhält
keine Ihrer Daten.

## Was er anzeigt

Die App **abonniert** den Broker, auf den Sie sie richten, und zeigt die
empfangenen Asset-Daten — die Objekte, ihre erfassten Felder und die Standort-
oder Profilinformationen, die der Broker bereits hält. Diese Daten entstehen
anderswo (in der Erfassungs-App) und unterliegen vollständig **Ihrem** Broker
und seinen Berechtigungen. Empfangene Assets werden **nur im Arbeitsspeicher**
gehalten; beim Beenden der App sind sie weg. Zusätzlich können Sie eine
Anzeigedauer festlegen, nach der angezeigte Assets von selbst vom Bildschirm
verschwinden.

## Wohin die Daten gehen

Nirgendwohin Neues. Der Viewer **liest** nur von Ihrem Broker. Er
veröffentlicht nie, schreibt nie und überträgt keine Daten an den Entwickler
oder Dritte.

## Speicherung und Sicherheit

- Die App speichert nur die von Ihnen eingegebenen
  **Broker-Verbindungseinstellungen** (für die Wiederverbindung) sowie einen
  Cache der **Profil-Dokumente** des Brokers (Workflow-Beschreibungen ohne
  personenbezogene Daten).
- Passwörter liegen im **iOS-Schlüsselbund** — nie im Klartext, nie in
  Protokollen. Diagnoseprotokolle bleiben auf dem Gerät und erfassen von
  sensiblen Werten nur deren *Länge*, nie den Inhalt.
- Verbindungen zum Broker können **TLS** (`mqtts`) nutzen, sodass Daten
  während der Übertragung verschlüsselt sind.

## Ihre Wahlmöglichkeiten

- **Standort und Kamera** können jederzeit in den iOS-Einstellungen erteilt,
  verweigert oder widerrufen werden; beides ist optional.
- Broker-Konfigurationen (samt Schlüsselbund-Passwort) können jederzeit in
  den App-Einstellungen entfernt werden. Die angezeigten Asset-Daten
  unterliegen den Aufbewahrungs- und Zugriffsregeln *Ihres* Brokers.

## Kinder

Hecate ist ein professionelles Werkzeug und richtet sich nicht an Kinder.

## Änderungen dieser Erklärung

Ändert sich der Datenumgang der App, wird diese Seite aktualisiert.
