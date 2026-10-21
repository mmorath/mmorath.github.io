# Datenschutzerklärung — Frameworthy

**Gültig ab:** 2026-10-20
**Entwickler:** Matthias Morath

Frameworthy ist eine Mac-App, die die Videos verarbeitet, die du in ihr öffnest —
**vollständig auf deinem Mac**.

!!! note "Kurz gesagt"
    Kein Konto, kein Server, keine Analyse, keine Werbung, keine Nachverfolgung.
    Deine Videos, dein Ton und dein Text verlassen deinen Mac nicht. Die einzige
    eigene Netzwerkverbindung der App ist das einmalige Laden der Sprechermodelle
    von Hugging Face, und sie enthält keine Nutzerdaten.

## Was wir erheben

**Nichts.** Die App hat **kein Backend**, sendet Daten an **keinen Server** und enthält
**keine Analyse, Werbung oder Nachverfolgung**. Der Entwickler erhält keine Daten aus der App.

## Was die App auf deinem Mac verarbeitet

- **Videos, die du öffnest** — werden gelesen, konvertiert und in den von dir gewählten
  Ausgabeordner geschrieben (Standard: `Filme/Frameworthy`). Die App läuft in der
  App Sandbox von macOS: Sie kann nur Dateien und Ordner öffnen, die du auswählst, und
  merkt sich diese Erlaubnis, damit Aufträge in der Warteschlange nach einem Neustart
  weiterlaufen.
- **Gesprochener Text** — wird mit der Spracherkennung von Apple auf dem Gerät erkannt.
  Der Ton verlässt deinen Mac nie. macOS lädt eventuell einmal ein Sprachmodell für die
  gewählte Sprache; dieser Download enthält keine Nutzerdaten.
- **Korrekturen und Kapiteltitel** — entstehen auf dem Gerät mit Apple Intelligence.
  Kein Text geht an ein Cloud-Modell.
- **Übersetzungen** — auf dem Gerät mit dem Übersetzungs-Framework von Apple; macOS lädt
  Sprachpakete eventuell einmal, nachdem du zustimmst.
- **Sprecher** — werden auf dem Gerät unterschieden. Die Sprechermodelle werden einmal
  von Hugging Face geladen (`FluidInference/speaker-diarization-coreml`); dieser Download
  sendet keine Nutzerdaten. Es ist die einzige Netzwerkverbindung, die die App selbst aufbaut.
- **Transkripte, Untertitel und Kapitel** — werden neben deinen konvertierten Videos gespeichert.

## Was die App speichert

Alles bleibt im Container der App auf deinem Mac
(`~/Library/Containers/com.mmorath.frameworthy`): deine Einstellungen, die
Warteschlange und eine lokale Log-Datei mit Dateipfaden und Verarbeitungsdetails.
Nichts davon wird hochgeladen. Wenn du die App löschst, wird der Container entfernt.

## Weitergabe

Keine. Die App gibt keine Daten an den Entwickler oder Dritte weiter.

## Kinder

Die App erhebt von niemandem Daten, auch nicht von Kindern.

## Änderungen

Ändert sich der Umgang der App mit Daten, wird diese Seite aktualisiert und das Datum
„Gültig ab“ angepasst.

## Kontakt

Siehe [Support](../support/index.de.md).
