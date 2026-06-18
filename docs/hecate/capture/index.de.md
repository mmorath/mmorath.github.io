---
hide:
  - toc
---

# Hecate

*Universelle, profilgesteuerte Geo-Referenzierung von Objekten*

Hecate ist eine feldtaugliche iOS-App zur **Geo-Referenzierung physischer
Objekte**. Jedes Objekt wird anhand eines **Profils** erfasst — eines
konfigurierbaren Ablaufs aus Scans, Feldern und Fotos — und anschließend mit
einem GPS-Fix auf der Karte verortet sowie über **MQTT** an einen Broker Ihrer
Wahl gestreamt.

Nichts an der Fachdomäne ist fest einprogrammiert. Ändern Sie das Profil, und
dieselbe App erfasst Gabelstapler, Feuerlöscher, Netzwerkdosen oder
archäologische Funde — ohne neuen Build.

## In einer Minute

- **Eine App, viele Anwendungsfälle.** Jeder Anwendungsfall ist ein *Profil*,
  keine separate App.
- **An der Quelle validiert.** Jedes Feld wird im Moment der Erfassung gegen sein
  deklariertes Format geprüft.
- **Immer verortet.** Jeder Datensatz trägt einen GPS-Fix und landet auf der
  Karte.
- **Über MQTT gestreamt.** Veröffentlicht an *Ihren eigenen* Broker in einem
  einheitlichen, selbstbeschreibenden Umschlag — kein Entwickler-Backend, keine
  Analyse, kein Tracking.
- **Funktioniert offline.** Eine dauerhafte Outbox hält Datensätze außerhalb der
  Reichweite zurück und sendet sie bei erneuter Verbindung.

## Screenshots

<div class="shots">
  <figure><img src="/assets/screens/assets.png" alt="Die Asset-Outbox — erfasste Objekte, die auf die Übermittlung warten"><figcaption>Assets &amp; Outbox</figcaption></figure>
  <figure><img src="/assets/screens/detail.png" alt="Die Detailansicht eines Assets mit seinen erfassten Feldern"><figcaption>Asset-Detail</figcaption></figure>
  <figure><img src="/assets/screens/sent.png" alt="Übermittlungsverlauf gesendeter Assets"><figcaption>Übermittlungsverlauf</figcaption></figure>
  <figure><img src="/assets/screens/settings.png" alt="Der Einstellungs-Hub"><figcaption>Einstellungen</figcaption></figure>
</div>

## Weiterlesen

<div class="grid cards" markdown>

-   :material-alert-circle-outline: __Das Problem__

    ---

    Warum ein Wildwuchs aus Einzweck-Erfassungs-Apps die Daten inkonsistent,
    schreibtischgebunden und ortsblind macht.

    [:octicons-arrow-right-24: Das Problem](problem.md)

-   :material-checkbox-marked-circle-outline: __Was Hecate leistet__

    ---

    Wie eine profilgesteuerte App diesen Wildwuchs auflöst und die Daten an der
    Quelle korrigiert.

    [:octicons-arrow-right-24: Was Hecate leistet](solution.md)

</div>

## Der Name & das Zeichen

Der Name **Hecate** geht auf die griechische Göttin **Hekate** zurück — Göttin
der Wegkreuzungen, Schwellen und Schlüssel, die an der Grenze steht und hält,
was sie öffnet. Ein Feldwerkzeug lebt genau an dieser Kante: zwischen dem
physischen Objekt vor Ihnen und den digitalen Systemen, die davon erfahren
müssen. Hecate **verortet** es, **führt** durch die Erfassung, **trägt** es
weiter zum Broker und **hält die Schlüssel**, die den Weg öffnen.

Das Zeichen ist der **Strophalos** („Hekates Rad") — ein Labyrinth gewundener
Pfade um eine einzige Nabe: die Wege durch das Feld und die Nachrichten, die in
der Mitte beim Broker zusammenlaufen.
