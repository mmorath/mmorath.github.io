# Datenschutzerklärung — Hecate Admin

**Gültig ab:** 18.06.2026
**Entwickler:** Matthias Morath

Hecate Admin ist ein **Authoring-Werkzeug**. Mit ihm werden die **Profile**
erstellt und veröffentlicht, die die Erfassungs-App konfigurieren, und die
Verbindung zu Ihrem MQTT-Broker eingerichtet. Es ist keine App zur
Datenerhebung.

## Was wir erheben

**Keine Telemetrie und keine personenbezogenen Daten.** Die Admin-App:

- fragt **keinen Standort** ab und hat **keine Kamera**;
- betreibt **keine Analyse-, Werbe- oder Tracking-Dienste Dritter**;
- sendet **nichts** an den Entwickler — es gibt **kein gehostetes Backend**.

## Womit sie umgeht

- **Profile, die Sie verfassen.** Ein Profil beschreibt die Felder und
  Schritte eines Erfassungs-Workflows. Profile sind **Konfiguration, keine
  personenbezogenen Daten**, und **dürfen keine Geheimnisse enthalten** — sie
  sind für die abonnierenden Geräte breit lesbar.
- **Broker-Zugangsdaten.** Zum Veröffentlichen von Profilen verbindet sich die
  App mit **Ihrem** MQTT-Broker mit Admin-Zugangsdaten. Das Passwort liegt im
  **Schlüsselbund** der Plattform — nie im Klartext, nie in einem Profil,
  einem Provisionierungs-QR oder einem Protokoll, und es wird nirgendwohin
  übertragen außer zur Authentifizierung an Ihrem Broker.

## Wohin die Daten gehen

Das einzige Netzwerkziel ist der **von Ihnen konfigurierte MQTT-Broker**. Die
Admin-App veröffentlicht dort auf Ihre Veranlassung Profile (als
Retained-Nachrichten). Sie überträgt nichts an den Entwickler oder Dritte; es
gibt keine Werbung, kein Profiling und kein App-übergreifendes Tracking.

## Speicherung und Sicherheit

- Profile und Verbindungseinstellungen werden **auf Ihrem Gerät** gespeichert.
- Das Broker-**Passwort liegt im Schlüsselbund**.
- Verbindungen zum Broker können **TLS** (`mqtts`) nutzen, sodass Daten
  während der Übertragung verschlüsselt sind.

## Ihre Wahlmöglichkeiten

- **Zugangsdaten:** liegen nur auf dem Gerät; jederzeit entfernbar.
- **Profile:** Sie verfassen, veröffentlichen und ziehen sie zurück; das
  Zurückziehen löscht die Retained-Nachricht auf Ihrem Broker.

## Kinder

Hecate ist ein professionelles Werkzeug und richtet sich nicht an Kinder.

## Änderungen dieser Erklärung

Ändert sich der Datenumgang der App, werden diese Seite und der
In-App-Datenschutzbildschirm gemeinsam aktualisiert.
