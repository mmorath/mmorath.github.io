# Was Hecate leistet

Hecate fasst diesen Wildwuchs zu **einer** konfigurierbaren App zusammen — und
korrigiert die Daten dort, wo sie entstehen, statt im Nachhinein.

## Eine App, definiert durch Profile

Der Eingabedialog für jeden Anwendungsfall ist **nicht programmiert** — er ist
ein **Profil**: ein kleines Dokument, das die Schritte, die Felder und die
zulässigen Eingabemethoden deklariert und über ein MQTT-Topic an die Geräte
verteilt wird. Ändern Sie das Profil, und dieselbe App bedient einen neuen
Anwendungsfall — ohne neuen Build.

## An der Quelle validiert

Jedes Feld wird **im Moment der Erfassung** gegen sein deklariertes Format
geprüft, sodass fehlerhafte Daten dort gestoppt werden, wo sie entstehen, statt
nachgelagert bereinigt zu werden.

## Die richtige Eingabe für jeden Schritt

Die Schritte eines Profils entscheiden, **was** erfasst wird; jeder Schritt
wählt die Eingabemethode, die zur Aufgabe passt:

- **Manuelle Eingabe.** Tippen Sie den Wert direkt in das Feld.
- **Kamera-Scan.** Richten Sie die Gerätekamera aus und lassen Sie die
  On-Device-Scan-Frameworks **QR-Codes, 2D-Data-Matrix-Codes, 1D-Barcodes und
  gedruckten Text** lesen — ohne Netzwerk-Roundtrip und ohne Drittanbieterdienst.

Welche Methode ein Schritt auch nutzt: Der Wert durchläuft **dieselbe
Validierungs- und Erfassungs-Pipeline**, sodass sich ein Profil unabhängig von
der Eingabeart identisch verhält.

## Immer geo-referenziert

Jeder Datensatz trägt einen **GPS-Fix** und wird in einem einheitlichen,
selbstbeschreibenden Umschlag an den Broker gestreamt.

## Governance mit nahezu keiner Infrastruktur

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

## Wie es jeden Schmerzpunkt beseitigt

| Schmerzpunkt im Unternehmen | Wie Hecate ihn beseitigt |
| --- | --- |
| Viele Einzweck-Erfassungs-Apps | Eine App; jeder Anwendungsfall ist ein Profil, kein neuer Build |
| Inkonsistente Datenqualität | Feldweise Formatvalidierung, bei der Erfassung blockiert |
| Nicht mobil nutzbar | Eine feldtaugliche iOS-App, dort genutzt, wo die Arbeit passiert |
| Kein Ortsbezug | Jeder Datensatz trägt einen GPS-Fix |
| Hoher Infrastruktur-/IT-Aufwand | Nur Broker + App; Profile als beibehaltene MQTT-Nachrichten geliefert |
| Ungeregelter Zugriff | Broker-Berechtigungen entscheiden, wer welche Profile lesen darf |
