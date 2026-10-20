# Datenschutz — Leaf Relief

**Stand:** 2026-10-21
**Entwickler:** Matthias Morath

Leaf Relief ist eine Mac-App für ein papierloses Archiv. Sie verarbeitet deine Dokumente
**ausschließlich auf deinem Mac**.

## Was wir erheben

**Nichts.** Die App hat kein Backend, kein Konto, keine Analyse, keine Werbung und kein
Tracking. Der Entwickler erhält keine Daten aus der App.

## Was die App auf deinem Mac verarbeitet

- **Dokumente** in dem Archivordner und dem Eingangsordner, die du wählst. Die App läuft
  in der macOS-Sandbox: Sie kann nur die Ordner öffnen, die du ausgewählt hast, und merkt
  sich diese Erlaubnis.
- **Scans** von einem Scanner, den du auswählst (USB oder im lokalen Netz über AirScan).
  Die Seitenbilder bleiben 14 Tage im Cache der App, damit ein Fehler nachgebessert
  werden kann.
- **Texterkennung** mit Apples Vision, auf dem Mac.
- **Vorschläge** (Art, Absender, Datum, Betrag, Frist …) mit Apple Intelligence, auf dem
  Mac. Kein Text geht an ein Cloud-Modell.
- **Suche** mit einem Index im Container der App.
- **Spotlight:** Titel, Absender, Arten, Schlagwörter und Text stehen im Spotlight-Index
  dieses Macs.
- **Erinnerungen** für Fristen legt die App nur an, wenn du „Erinnerung anlegen“ klickst;
  macOS fragt dabei einmal um Erlaubnis.
- **Nachweis:** Änderungen an Dokumenten werden mit einem Schlüssel aus der Secure Enclave
  dieses Macs signiert und im Index und an der Datei vermerkt.

## Netzwerk

- **Scanner im lokalen Netz** (AirScan) werden über Bonjour gefunden; macOS fragt dafür
  nach der Erlaubnis für das lokale Netz.
- **Zeitstempel (optional, standardmäßig aus):** Schaltest du sie ein, geht für jeden
  Nachweis-Eintrag nur ein Prüfwert (SHA-256) an den Zeitstempeldienst freetsa.org — nie
  der Inhalt eines Dokuments.

Sonst baut die App keine Verbindung auf.

## Weitergabe

Ein Dokument oder das Protokoll verlässt den Mac nur, wenn du es selbst über „Teilen“
oder „Per E-Mail senden“ weitergibst. Die Kopie trägt dann keine Schlagwörter und Arten.
Das Protokoll enthält Abläufe und Dateinamen, keine Dokumentinhalte; Benutzerordner,
E-Mail-Adressen und Schlüssel werden beim Export ersetzt.

## Löschen

Löschst du die App, entfernt macOS ihren Container (Index, Einstellungen, Cache). Deine
Dokumente im Archivordner bleiben, wo sie sind.

## Kontakt

Fragen: `kubisch-gemacht3p@icloud.com`
