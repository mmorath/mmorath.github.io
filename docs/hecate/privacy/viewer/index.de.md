# Datenschutzerklärung — Hecate für Apple TV

**Gültig ab:** 18.06.2026
**Entwickler:** Matthias Morath

Die Hecate-App für Apple TV ist ein **rein lesender Viewer**. Sie verbindet
sich mit einem von Ihnen konfigurierten MQTT-Broker und **zeigt** die dort
veröffentlichten Assets an. Sie ist ein Abonnent, kein Sensor.

## Was wir erheben

**Nichts.** Der Viewer:

- hat **keine Kamera** und nimmt keine Bilder auf;
- fragt **keinen Standort** ab und speichert keine GPS-Daten;
- hat **keine Benutzerkonten** und fragt keine persönlichen Daten ab;
- betreibt **keine Analyse-, Werbe- oder Tracking-Dienste Dritter**.

Es gibt **kein vom Entwickler betriebenes Backend**. Der Entwickler erhält
keine Ihrer Daten.

## Was er anzeigt

Die App **abonniert** den Broker, auf den Sie sie richten, und zeigt die
empfangenen Asset-Daten — die Objekte, ihren Zustand und die Standort- oder
Profilinformationen, die der Broker bereits hält. Diese Daten entstehen
anderswo (in der Erfassungs-App) und unterliegen vollständig **Ihrem** Broker
und seinen Berechtigungen. Der Viewer erzeugt sie weder noch speichert er sie
dauerhaft; er rendert den Live-Strom, solange er läuft.

## Wohin die Daten gehen

Nirgendwohin Neues. Der Viewer **liest** nur von Ihrem Broker. Er
veröffentlicht nie, schreibt nie und überträgt keine Daten an den Entwickler
oder Dritte.

## Speicherung und Sicherheit

- Die App behält nur die **Broker-Verbindungseinstellungen**, die Sie auf dem
  Gerät eingeben, um sich wieder verbinden zu können. Passwörter liegen im
  Schlüsselbund der Plattform — nie im Klartext, nie in Protokollen.
- Verbindungen zum Broker können **TLS** (`mqtts`) nutzen, sodass Daten
  während der Übertragung verschlüsselt sind.

## Ihre Wahlmöglichkeiten

Weil der Viewer nichts erhebt, gibt es nichts abzubestellen, zu exportieren
oder zu löschen — außer den Broker-Verbindungseinstellungen, die Sie jederzeit
auf dem Gerät ändern oder entfernen können. Die angezeigten Asset-Daten
unterliegen den Aufbewahrungs- und Zugriffsregeln *Ihres* Brokers.

## Kinder

Hecate ist ein professionelles Werkzeug und richtet sich nicht an Kinder.

## Änderungen dieser Erklärung

Ändert sich der Datenumgang der App, wird diese Seite aktualisiert.
