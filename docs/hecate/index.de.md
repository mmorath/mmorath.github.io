---
hide:
  - toc
---

# Hecate

*Ein profilgesteuertes System zur Geo-Referenzierung physischer Objekte — eine App-Familie, ein Broker, kein Backend.*

Hecate erfasst physische Objekte anhand eines **Profils** — eines
konfigurierbaren Ablaufs aus Scans, Feldern und Fotos —, verortet sie auf der
Karte und streamt sie über **MQTT** an einen Broker Ihrer Wahl. Nichts an der
Fachdomäne ist fest einprogrammiert: Ändern Sie das Profil, und dasselbe
System erfasst Gabelstapler, Feuerlöscher, Netzwerkdosen oder archäologische
Funde — **ohne neuen Build, ohne neue App**.

!!! tip "Das Einzige, was Sie brauchen, ist ein MQTT-Broker"

    Hecate benötigt **kein Backend-System**. Die eine und einzige
    Netzwerkabhängigkeit ist der **MQTT-Broker, den Sie ohnehin betreiben** —
    on-premise oder in der Cloud. Es gibt keinen Entwickler-Server, keine
    Konten, keine Analyse, kein Tracking — und Ihre Daten berühren zu keinem
    Zeitpunkt fremde Infrastruktur.

Und Hecate ist **keine Silo-Anwendung**: *Sie* entscheiden, welche Profile Sie
anlegen und welche Rolle die erfassten Assets in Ihrem Unternehmen und Ihrem
Betrieb spielen. Weil alles in einem einheitlichen, selbstbeschreibenden
Umschlag an Ihrem Broker ankommt, kann jedes nachgelagerte System Ihrer Wahl —
ein Dashboard, ein Historian, eine ERP-Übergabe, ein Unified Namespace — die
Daten abonnieren und nutzen. Die Apps enden am Broker; die Bedeutung gehört
Ihnen.

## Das Problem, das es löst

Unternehmen betreiben einen **Wildwuchs an Einzweck-Erfassungsapps** — ein
Werkzeug pro Anwendungsfall, jedes isoliert gebaut. Die Folge: uneinheitliche
Datenqualität (jede App validiert anders), Erfassung am Schreibtisch statt
dort, wo die Arbeit ist, Datensätze, die nie sagen, **wo** das Objekt
eigentlich steht — und pro Werkzeug ein Backend samt Gerätemanagement.

Hecate ersetzt den Wildwuchs durch **ein konfigurierbares System**: Profile
definieren, *was* erfasst wird, validiert wird im Moment der Erfassung, jeder
Datensatz trägt seine GPS-Position, und alles fließt über den einen Broker,
den Sie bereits kontrollieren.

[:octicons-arrow-right-24: Das Problem im Detail](capture/problem.md) ·
[:octicons-arrow-right-24: Wie Hecate jeden dieser Schmerzen beseitigt](capture/solution.md)

## Die Apps

<div class="grid cards" markdown>

-   :material-cellphone: __Hecate__ · die Erfassungs-App · iPhone & iPad

    ---

    Das Feldwerkzeug. Scannt, validiert und geo-referenziert jedes Objekt
    anhand des aktiven Profils und veröffentlicht es an Ihren Broker.
    Arbeitet offline mit einer robusten Outbox, die sich beim Wiederverbinden
    leert.

    [:octicons-arrow-right-24: Überblick Erfassung](capture/index.md)

-   :material-map-marker-radius: __Hecate Viewer__ · iPhone

    ---

    Die Live-Karte für die Hosentasche. Ein reiner Abonnent, der Assets im
    Moment der Veröffentlichung auf der Karte verortet und nach einer von
    Ihnen gewählten Zeit ausblendet — er erfasst nichts und veröffentlicht
    nichts.

    [:octicons-arrow-right-24: Überblick iPhone-Viewer](viewer-ios/index.md)

-   :material-tablet: __Hecate Viewer__ · iPad

    ---

    Die Live-Karte in voller Breite. Der Feed sitzt als Seitenleiste neben
    der vollflächigen Karte — ein Tipp auf eine Zeile fliegt zur Position
    des Assets. Derselbe Abonnent, gestaltet für den großen Bildschirm.

    [:octicons-arrow-right-24: Überblick iPad-Viewer](viewer-ipad/index.md)

-   :material-tune-variant: __Hecate Admin__ · iPhone & iPad · *in Entwicklung*

    ---

    Die Autoritäts-App fürs Authoring. Erstellt, validiert, versioniert,
    veröffentlicht und zieht die Profile zurück, die die Erfassungs-App
    konsumiert — derzeit in aktiver Entwicklung.

    [:octicons-arrow-right-24: Überblick Admin](admin/index.md)

</div>

## Screenshots

<div class="shots">
  <figure><img src="/assets/screens/assets.png" alt="Hecate Erfassungs-App — die Outbox mit erfassten Objekten, die auf Zustellung warten"><figcaption>Hecate — Erfassung &amp; Outbox</figcaption></figure>
  <figure><img src="/assets/screens/detail.png" alt="Hecate Erfassungs-App — die Detailansicht eines Assets mit seinen erfassten Feldern"><figcaption>Hecate — Asset-Detail</figcaption></figure>
  <figure><img src="/assets/screens/viewer-ios-karte.png" alt="Hecate Viewer — die Live-Karte mit eintreffenden Assets als Pins"><figcaption>Viewer — die Live-Karte</figcaption></figure>
  <figure><img src="/assets/screens/viewer-ios-feed.png" alt="Hecate Viewer — der Live-Feed, neueste zuerst, mit Frische-Markierungen"><figcaption>Viewer — der Live-Feed</figcaption></figure>
  <figure class="wide"><img src="/assets/screens/viewer-ipad-karte.png" alt="Hecate Viewer für iPad — das geteilte Layout: Feed-Seitenleiste neben der vollflächigen Live-Karte"><figcaption>Viewer für iPad — das geteilte Layout</figcaption></figure>
</div>

## Auf der Roadmap

- :material-television: **Apple-TV-Viewer** — dieselbe Live-Ansicht als
  wartungsfreie Wandanzeige für Hallen, Büros und Werkstore.
  [Eine Vorschau des Konzepts](viewer/index.md) ist bereits beschrieben.

## Wie alles zusammenspielt

```
Admin-App  ──autorisiert & publiziert (retained)──▶  MQTT-Broker  ◀──liest Profile──  Erfassungs-App
                                                          ▲                                  │
                                                          └────── veröffentlicht Assets ─────┘
                                                          │
                                              abonniert & zeigt an
                                                          ▼
                                  Hecate Viewer (iPhone · iPad) · Apple TV (geplant)
```

Die **Admin-App** ist die Autorität für *Profile*; die **Erfassungs-App**
liest Profile nur und ist die Autorität für *Assets*; die **Viewer** lesen
alles nur. Alle Apps teilen einen Kern, ein Wire-Format und eine
schwarz-weiße Bildsprache — Farbe kommt ausschließlich vom Profil-Akzent des
jeweiligen Objekts.

## Der Name & das Zeichen

**Hecate** ist die griechische Göttin der Wegkreuzungen, Schwellen und
Schlüssel — sie, die an der Grenze steht und hält, was sie öffnet. Das Zeichen
ist der **Strophalos** („Hekates Rad") — ein Labyrinth gewundener Pfade um
eine einzige Nabe: die Wege durchs Feld und die Nachrichten, die beim Broker
in der Mitte zusammenlaufen.

## Für jede App

| | Datenschutz | Support |
| --- | --- | --- |
| **Hecate (Erfassung)** | [Datenschutz](privacy/capture/index.md) | [Support](support/operator/index.md) |
| **Hecate Viewer (iPhone)** | [Datenschutz](privacy/viewer-ios/index.md) | [Support](support/operator/index.md) |
| **Hecate Viewer (iPad)** | [Datenschutz](privacy/viewer-ipad/index.md) | [Support](support/operator/index.md) |
| **Hecate Admin** | [Datenschutz](privacy/admin/index.md) | [Support](support/admin/index.md) |
| **Apple-TV-Viewer** *(geplant)* | [Datenschutz](privacy/viewer/index.md) | [Support](support/operator/index.md) |
