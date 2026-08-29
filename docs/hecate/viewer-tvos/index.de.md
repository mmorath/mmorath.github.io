---
hide:
  - toc
---

# Hecate Viewer TV

*Die Live-Wand — quer durch den Raum ablesbar, und niemand muss sie anfassen.*

Hecate Viewer TV macht aus einem Apple TV eine **Live-Asset-Wand** für Ihre
Hecate-Installation. Die App verbindet sich mit demselben MQTT-Broker wie die
Erfassungs-App, **abonniert** den Asset-Strom und zeigt jedes eintreffende
Objekt auf einer bildschirmfüllenden Live-Karte mit chronologischem Feed
daneben — auf einem Monitor in der Halle, im Büro oder an der Werkseinfahrt.

Ein **reiner Viewer**: Die App erfasst nichts, ändert nichts und veröffentlicht
nichts. Alles auf dem Bildschirm stammt von Ihrem Broker und existiert nur im
Arbeitsspeicher.

## In einer Minute

- **Einrichtung vom iPhone, nicht von der Fernbedienung.** Der Fernseher zeigt
  einen QR-Code; Sie scannen ihn im Hecate Viewer auf iPhone oder iPad und
  senden die Broker-Konfiguration — samt Zugangsdaten — verschlüsselt über Ihr
  lokales Netzwerk. Die Wand füllt sich in Sekunden. Kein Tippen auf der
  Fernbedienung, nie.
- **Eine Karte für den Raum.** Ein Pin pro eintreffendem Asset, dort platziert,
  wo es erfasst wurde. Neue Einträge pulsieren türkis; mit dem Alter werden sie
  grau. Der Feed in der Seitenleiste zeigt denselben Strom, neueste zuerst, mit
  Profilfarben und Frische-Kennzeichen.
- **Die Fernbedienung ist optional.** Eine Feed-Zeile fokussieren, um ihren Pin
  hervorzuheben; klicken zum Zoomen; erneut klicken für alle erfassten Felder.
  Bleibt sie unberührt, komponiert die Wand ihr Bild selbst und hält sich aktuell.
- **Ehrlich zur eigenen Gesundheit.** Verstummt der Datenstrom, sagt die Wand es
  — erst eine Ruhe-Tönung, dann ein Stale-Schleier, dann ein klarer
  Reconnect-Zustand, der sich selbst erholt. Ein Bildschirm, der Aktualität
  vortäuscht, ist schlimmer als einer, der zugibt, offline zu sein.
- **Für den Dauerbetrieb gebaut.** Ein Einbrennschutz verschiebt das Layout auf
  unbeaufsichtigten Panels, und die Wand hält den Bildschirm wach, damit eine
  24/7-Anzeige nicht mitten in der Schicht einschläft.
- **Nach Profil und Zone filtern.** Begrenzen Sie die Wand über das
  Play/Pause-Overlay auf ein Erfassungsprofil oder eine Standortzone;
  ausgeblendete Assets werden weiter mitgezählt — die Summen lügen nie.
- **Ein Produkt.** Dasselbe Wire-Format und dieselbe schwarz-weiße Bildsprache
  wie die übrigen Hecate-Apps; Farbe kommt allein vom Profil-Akzent des Objekts.

## Screenshots

<div class="shots">
  <figure class="wide"><img src="/assets/screens/de/tv-wall.png" alt="Hecate Viewer TV — die Live-Wand: Feed-Seitenleiste neben der bildschirmfüllenden Karte mit eintreffenden Assets als Pins"><figcaption>Die Wand — Feed-Seitenleiste und Live-Karte</figcaption></figure>
</div>

*Die Aufnahmen stammen aus Entwicklungsversionen. Einzelne Bildschirme können Funktionen zeigen, die ein Abo voraussetzen oder erst in einer späteren Version kommen — was die kostenlose Stufe heute enthält, steht unter [Free & Pro](../plans/index.de.md).*

## Was sie zeigt

Die Wand rendert den Live-Asset-Strom des Brokers — die erfassten Felder jedes
Objekts, seine Profilfarbe und seinen Namen sowie seine Position auf der Karte.
Der **aufbewahrte Verlauf** des Brokers füllt den Bildschirm im Moment der
Verbindung, sodass die Wand nie leer startet, solange es Historie zu zeigen gibt;
alles danach kommt live. Was erscheint, unterliegt vollständig **Ihrem Broker und
seinen Berechtigungen**, nicht der App.

## Einrichtung

App installieren — sie zeigt einen Kopplungscode. Öffnen Sie
[Hecate Viewer für iPhone](../viewer-ios/index.md) oder
[für iPad](../viewer-ipad/index.md), wählen Sie Ihren Broker und senden Sie ihn
an den Apple TV: Die Konfiguration überquert Ihr lokales Netzwerk verschlüsselt,
das Passwort wandert direkt in den Schlüsselbund des Geräts. Die Wand verbindet
sich und startet von selbst — und bleibt über Neustarts hinweg gekoppelt.

An den Daten selbst ist nichts zu konfigurieren, denn die Daten werden von Ihren
Profilen definiert und von der Erfassungs-App veröffentlicht.

!!! note "Für die Einrichtung brauchen Sie einen der Telefon-Viewer"

    Die Kopplung ist der einzige Einrichtungsweg — mit Absicht, denn
    Broker-Hostname und Passwort mit einer Fernbedienung einzugeben ist eine
    Zumutung. Installieren Sie Hecate Viewer zuerst auf einem iPhone oder iPad im
    selben Netzwerk.

---

[:octicons-arrow-right-24: Datenschutz](../privacy/viewer-tvos/index.md) ·
[:octicons-arrow-right-24: Support](../support/operator/index.md) ·
[:octicons-arrow-right-24: Der iPhone-Viewer](../viewer-ios/index.md)
