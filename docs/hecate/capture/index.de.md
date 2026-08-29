---
hide:
  - toc
---

# Hecate Capture

*Universelle, profilgesteuerte Geo-Referenzierung von Objekten*

Hecate Capture ist eine feldtaugliche iOS-App zur **Geo-Referenzierung physischer
Objekte**. Jedes Objekt wird anhand eines **Profils** erfasst — eines
konfigurierbaren Ablaufs aus Scans und Feldern — und anschließend mit
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
  <figure><img src="/assets/screens/de/capture-assets.png" alt="Die Asset-Outbox — erfasste Objekte, die auf die Übermittlung warten"><figcaption>Assets &amp; Outbox</figcaption></figure>
  <figure><img src="/assets/screens/de/capture-detail.png" alt="Die Detailansicht eines Assets mit seinen erfassten Feldern"><figcaption>Asset-Detail</figcaption></figure>
  <figure><img src="/assets/screens/de/capture-sent.png" alt="Übermittlungsverlauf gesendeter Assets"><figcaption>Übermittlungsverlauf</figcaption></figure>
  <figure><img src="/assets/screens/de/capture-settings.png" alt="Der Einstellungs-Hub"><figcaption>Einstellungen</figcaption></figure>
</div>

*Die Aufnahmen stammen aus Entwicklungsversionen. Einzelne Bildschirme können Funktionen zeigen, die ein Abo voraussetzen oder erst in einer späteren Version kommen — was die kostenlose Stufe heute enthält, steht unter [Free & Pro](../plans/index.de.md).*


## Das Problem

Unternehmen betreiben einen **Wildwuchs aus Einzweck-Apps**, um Daten entlang
ihrer Prozessschritte zu erfassen — ein Werkzeug je Anwendungsfall, jedes für
sich entwickelt. Daraus folgen drei Schwachstellen.

### Inkonsistente Qualität

Jede App validiert ihre Eingaben anders (oder gar nicht), sodass die Daten, die
in nachgelagerten Systemen ankommen, uneinheitlich und schwer vertrauenswürdig
sind.

### Nicht mobil nutzbar

Ein Großteil dieser Erfassung findet noch am Schreibtisch statt — nicht dort, wo
die Arbeit tatsächlich passiert.

### Kein Ortsbezug

Kaum etwas davon ist geo-referenziert, sodass ein Datensatz selten sagt, **wo**
sich das beschriebene Objekt tatsächlich befindet.

---

### Kurz gesagt

| Schmerzpunkt im Unternehmen | |
| --- | --- |
| Viele Einzweck-Erfassungs-Apps | ein neuer Build je Anwendungsfall |
| Inkonsistente Datenqualität | jede App validiert anders |
| Nicht mobil nutzbar | Erfassung passiert am Schreibtisch |
| Kein Ortsbezug | Datensätze sagen nicht, *wo* |
| Hoher Infrastruktur-/IT-Aufwand | ein Backend und Geräteverwaltung je Werkzeug |
| Ungeregelter Zugriff | keine einheitliche Regel, wer was erfassen darf |

[:octicons-arrow-right-24: Wie Hecate jeden dieser Punkte beseitigt](#was-hecate-capture-leistet)

## Was Hecate Capture leistet

Hecate fasst diesen Wildwuchs zu **einer** konfigurierbaren App zusammen — und
korrigiert die Daten dort, wo sie entstehen, statt im Nachhinein.

### Eine App, definiert durch Profile

Der Eingabedialog für jeden Anwendungsfall ist **nicht programmiert** — er ist
ein **Profil**: ein kleines Dokument, das die Schritte, die Felder und die
zulässigen Eingabemethoden deklariert und über ein MQTT-Topic an die Geräte
verteilt wird. Ändern Sie das Profil, und dieselbe App bedient einen neuen
Anwendungsfall — ohne neuen Build.

### An der Quelle validiert

Jedes Feld wird **im Moment der Erfassung** gegen sein deklariertes Format
geprüft, sodass fehlerhafte Daten dort gestoppt werden, wo sie entstehen, statt
nachgelagert bereinigt zu werden.

### Die richtige Eingabe für jeden Schritt

Die Schritte eines Profils entscheiden, **was** erfasst wird; jeder Schritt
wählt die Eingabemethode, die zur Aufgabe passt:

- **Manuelle Eingabe.** Tippen Sie den Wert direkt in das Feld.
- **Kamera-Scan.** Richten Sie die Gerätekamera aus und lassen Sie die
  On-Device-Scan-Frameworks **QR-Codes, 2D-Data-Matrix-Codes und 1D-Barcodes**
  lesen — ohne Netzwerk-Roundtrip und ohne Drittanbieterdienst.

Welche Methode ein Schritt auch nutzt: Der Wert durchläuft **dieselbe
Validierungs- und Erfassungs-Pipeline**, sodass sich ein Profil unabhängig von
der Eingabeart identisch verhält.

### Die Bausteine

| Baustein | Eingabe | Erzeugtes Feld |
|---|---|---|
| QR-Code scannen | QR-Code per Kamera | Text, optional mit Muster geprüft |
| Barcode scannen | 1D-Barcode (EAN, Code 128, …) | Text, optional mit Muster geprüft |
| 2D-Matrix-Code scannen | DataMatrix per Kamera | Text, optional mit Muster geprüft |
| Menge erfassen | Zahleneingabe | Zahl |
| Status-Checkliste abhaken | Checkboxen — mehrere dürfen zutreffen | Mehrfachauswahl |
| Einen Grund wählen | Radio-Buttons — genau einer trifft zu | Auswahl (genau eine) |
| Text eingeben | Freitext, eine Zeile | Text |
| Kommentar hinterlassen | Freitext, mehrzeilig | Text, mehrzeilig |

### Immer geo-referenziert

Jeder Datensatz trägt einen **GPS-Fix** und wird in einem einheitlichen,
selbstbeschreibenden Umschlag an den Broker gestreamt.

### Governance mit nahezu keiner Infrastruktur

Erforderlich sind nur ein **MQTT-Broker und die App** — kein zu betreibendes
Backend, keine Geräteverwaltungs-Einbindung. Die Autorität liegt in den
Berechtigungen des Brokers: Eine Administratorin oder ein Administrator
veröffentlicht beibehaltene (retained) Profile; eine Nutzerin oder ein Nutzer
sieht nur die Profile, die ihre bzw. seine Zugangsdaten lesen dürfen, und erfasst
anhand dieser.

Weil alle, die an einem Anwendungsfall arbeiten, dasselbe **validierte Profil**
ausfüllen, kommen die Daten konsistent, vergleichbar und einsatzbereit an — by
design, nicht durch nachträgliche Bereinigung.

---

### Wie es jeden Schmerzpunkt beseitigt

| Schmerzpunkt im Unternehmen | Wie Hecate ihn beseitigt |
| --- | --- |
| Viele Einzweck-Erfassungs-Apps | Eine App; jeder Anwendungsfall ist ein Profil, kein neuer Build |
| Inkonsistente Datenqualität | Feldweise Formatvalidierung, bei der Erfassung blockiert |
| Nicht mobil nutzbar | Eine feldtaugliche iOS-App, dort genutzt, wo die Arbeit passiert |
| Kein Ortsbezug | Jeder Datensatz trägt einen GPS-Fix |
| Hoher Infrastruktur-/IT-Aufwand | Nur Broker + App; Profile als beibehaltene MQTT-Nachrichten geliefert |
| Ungeregelter Zugriff | Broker-Berechtigungen entscheiden, wer welche Profile lesen darf |

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
