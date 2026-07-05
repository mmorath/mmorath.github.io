---
hide:
  - toc
---

# Datenschutz

Jede Hecate-App hat ihre **eigene** Datenschutzerklärung, weil jede anders mit
Daten umgeht. Wählen Sie die App, die Sie verwenden:

<div class="grid cards" markdown>

-   :material-cellphone: __Erfassungs-App__

    ---

    Erfasst Assets, einschließlich **Standort** und einer Geräteidentität —
    personenbezogene Daten im Sinne der DSGVO.

    [:octicons-arrow-right-24: Datenschutz Erfassung](capture/index.md)

-   :material-map-marker-radius: __Hecate Viewer__ · iPhone & iPad

    ---

    Ein reiner Abonnent mit Live-Karte. Standort nur für den „Sie sind
    hier"-Punkt; **nichts wird gespeichert, nichts übertragen**.

    [:octicons-arrow-right-24: Datenschutz Viewer](viewer-ios/index.md)

-   :material-television: __Apple-TV-Viewer__ · *geplant*

    ---

    Ein reiner Abonnent. **Erhebt nichts** — keine Kamera, kein Standort,
    keine Konten.

    [:octicons-arrow-right-24: Datenschutz Viewer](viewer/index.md)

-   :material-tune-variant: __Admin-App__

    ---

    Verfasst Profile und hält Broker-Zugangsdaten. **Keine Telemetrie.**

    [:octicons-arrow-right-24: Datenschutz Admin](admin/index.md)

</div>

Über alle Hecate-Apps hinweg gilt: **kein Entwickler-Backend**, **keine
Analyse-Dienste Dritter**, **kein Tracking**. Das einzige Netzwerkziel ist der
MQTT-Broker, den *Sie* konfigurieren und kontrollieren.
