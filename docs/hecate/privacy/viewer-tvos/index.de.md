# Datenschutzerklärung — Hecate Viewer TV

**Gültig ab:** 24.08.2026
**Entwickler:** Matthias Morath

Hecate Viewer TV ist eine **Anzeige**. Die App läuft auf einem Apple TV,
verbindet sich mit einem von Ihnen konfigurierten MQTT-Broker und **zeigt** die
dort veröffentlichten Assets auf einer Live-Wand. Sie ist ein Abonnent, kein
Sensor.

## Was wir erheben

**Nichts.** Die App:

- hat **keine Kamera** und erfasst keine Bilder;
- hat **keinen Zugriff auf die Fotobibliothek** und liest keine Ihrer Medien;
- fordert **keinen Standort** an und speichert keine GPS-Daten — ein Apple TV
  bewegt sich nicht, also zeigt die Wand die Positionen, die Ihre
  *Erfassungs-App* aufgezeichnet hat, und fragt den Fernseher nach nichts;
- hat **keine Benutzerkonten** und fragt keine persönlichen Daten ab;
- betreibt **keine Analyse-, Werbe- oder Tracking-Dienste Dritter**;
- enthält **kein Crash-Reporting-SDK**.

Es gibt **kein vom Entwickler betriebenes Backend**. Der Entwickler erhält keine
Ihrer Daten.

## Die zwei Dinge, mit denen sie spricht

Das ist die gesamte Netzwerkaktivität der App:

1. **Ihr lokales Netzwerk, einmal, zur Einrichtung.** Tippen mit der
   Fernbedienung ist eine Qual, deshalb tippt der Fernseher nie. Stattdessen
   zeigt er einen QR-Code und wartet in Ihrem lokalen Netzwerk darauf, dass
   **Hecate Viewer auf Ihrem iPhone oder iPad** ihm die Broker-Konfiguration
   übergibt. tvOS fragt beim ersten Mal Ihre Erlaubnis für den Zugriff auf das
   lokale Netzwerk; die Übergabe ist verschlüsselt, läuft ausschließlich zwischen
   Ihren beiden Geräten und erreicht keinen unserer Server. Die Konfiguration —
   samt Broker-Zugangsdaten — wandert direkt in den Schlüsselbund des Geräts.
2. **Ihr MQTT-Broker, zum Abonnieren.** Danach **liest** die App von dem Broker,
   auf den Sie sie gerichtet haben, und von nichts anderem.

## Was sie anzeigt

Die App **abonniert** Ihren Broker und zeigt die empfangenen Asset-Daten — die
Objekte, ihre erfassten Felder und die Standort- oder Profilinformationen, die
der Broker bereits hält. Diese Daten entstehen anderswo (in der Erfassungs-App)
und unterliegen vollständig **Ihrem** Broker und seinen Berechtigungen.
Empfangene Assets werden **nur im Arbeitsspeicher** gehalten; beim Beenden der
App sind sie weg.

## Wohin die Daten gehen

Nirgendwohin Neues. Die App **liest** nur von Ihrem Broker. Sie veröffentlicht
nie, schreibt nie und übermittelt keine Daten an den Entwickler oder Dritte.

## Speicherung und Sicherheit

- Die App speichert nur die **Broker-Verbindungseinstellungen**, mit denen sie
  gekoppelt wurde, damit sie sich nach einem Stromausfall ohne erneute Kopplung
  wieder verbinden kann, sowie einen Zwischenspeicher der **Profildokumente**
  des Brokers (Workflow-Beschreibungen und ihre Farben, die keine
  personenbezogenen Daten enthalten).
- Das Broker-Passwort liegt im **Schlüsselbund des Geräts**, nie im Klartext und
  nie in Protokollen. Diagnoseprotokolle bleiben auf dem Gerät und halten von
  sensiblen Werten nur die *Länge* fest, nie den Inhalt.
- Verbindungen zum Broker können **TLS** (`mqtts`) nutzen, sodass Daten während
  der Übertragung verschlüsselt sind.
- Der einzige weitere gespeicherte Zustand ist eine Anzeigeeinstellung — auf
  welches Profil oder welche Zone die Wand eingegrenzt ist — in den
  app-eigenen Einstellungen.

## Ihre Wahl

- Der **Zugriff auf das lokale Netzwerk** kann in den tvOS-Einstellungen
  jederzeit verweigert oder widerrufen werden. Beachten Sie: Die Kopplung ist
  der einzige Einrichtungsweg der App — wird sie verweigert, hat die Wand nichts
  zu zeigen.
- Koppeln Sie den Apple TV jederzeit neu, um ihn auf einen anderen Broker zu
  richten. Die angezeigten Asset-Daten unterliegen den Aufbewahrungs- und
  Zugriffsregeln **Ihres** Brokers.

## Kinder

Hecate ist ein professionelles Arbeitswerkzeug und richtet sich nicht an Kinder.

## Änderungen dieser Erklärung

Ändert sich der Datenumgang der App, wird diese Seite aktualisiert.

---

[:octicons-arrow-right-24: Die Apple-TV-App](../../viewer-tvos/index.md) ·
[:octicons-arrow-right-24: Support](../../support/operator/index.md)
