---
hide:
  - toc
---

# Hecate für Apple TV

*Eine Live-Wandanzeige für Ihre Hecate-Assets — rein lesend, auf dem großen Bildschirm.*

!!! info "Auf der Roadmap"

    Der Apple-TV-Viewer ist **geplant** und noch nicht verfügbar. Diese Seite
    beschreibt das Konzept. Heute gibt es die Live-Ansicht als
    [Hecate Viewer für iPhone](../viewer-ios/index.md) und
    [für iPad](../viewer-ipad/index.md).

Die Hecate-App für Apple TV macht aus jedem Bildschirm eine **Live-Ansicht der
Objekte, die Ihr Team gerade erfasst**. Sie verbindet sich mit demselben
MQTT-Broker wie die Erfassungs-App, **abonniert** den Asset-Strom und zeigt
Datensätze, sobald sie eintreffen — auf einem Hallenmonitor, im Büro oder am
Werkstor.

Sie ist ein **reiner Viewer**. Sie erfasst nichts, bearbeitet nichts und
speichert nichts Eigenes.

## In einer Minute

- **Live und wartungsfrei.** Assets erscheinen und aktualisieren sich, wie sie
  veröffentlicht werden; der Bildschirm hält sich ohne jede Interaktion
  aktuell.
- **Rein lesend, per Konstruktion.** Der Viewer *abonniert* nur — er
  veröffentlicht nie an den Broker und schreibt weder Profil noch Asset.
- **Gleicher Broker, gleiche Daten.** Richten Sie ihn auf Ihren Broker, und er
  zeigt genau das, was Ihre Zugangsdaten lesen dürfen. Keine separate
  Einrichtung der Daten selbst.
- **Nichts wird erhoben.** Keine Kamera, kein Standort, keine Konten, keine
  Analyse — er ist eine Anzeige, kein Sensor.
- **Ein Produkt.** Dasselbe Wire-Format und dieselbe schwarz-weiße
  Bildsprache wie die anderen Hecate-Apps; Farbe kommt ausschließlich vom
  Profil-Akzent des jeweiligen Objekts.

## Was er zeigt

Der Viewer rendert den Live-Asset-Strom vom Broker — die Objekte, ihren
aktuellen Zustand und (wo vorhanden) ihren Standort und Profil-Akzent. Weil er
dieselben Retained-Profile und dieselben Asset-Topics liest wie der Rest des
Systems, bestimmen allein **Ihr Broker und seine Berechtigungen**, was auf dem
Bildschirm erscheint — nicht die App.

## Einrichtung

Verbinden Sie die App mit Ihrem MQTT-Broker (Host, Port, TLS, Zugangsdaten).
Einmal verbunden, abonniert der Viewer und beginnt anzuzeigen — an den Daten
selbst gibt es nichts zu konfigurieren, denn die Daten definieren Ihre
Profile, veröffentlicht von der Erfassungs-App.

---

[:octicons-arrow-right-24: Datenschutz](../privacy/viewer/index.md) ·
[:octicons-arrow-right-24: Support](../support/operator/index.md) ·
[:octicons-arrow-right-24: Die Erfassungs-App](../capture/index.md)
