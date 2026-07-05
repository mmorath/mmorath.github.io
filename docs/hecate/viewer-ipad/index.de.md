---
hide:
  - toc
---

# Hecate Viewer für iPad

*Die Live-Karte in voller Breite — mit dem Feed stets an ihrer Seite.*

Hecate Viewer für iPad ist der **rein lesende Begleiter** der Erfassungs-App,
gestaltet für den großen Bildschirm. Er verbindet sich mit demselben
MQTT-Broker, **abonniert** den Asset-Strom und zeigt alles auf einmal: den
Live-Feed als **Seitenleiste**, die **Karte** füllt den Rest — keine Tabs,
beide Bereiche immer im Blick, im Hoch- wie im Querformat.

Er ist ein **reiner Viewer**. Er erfasst nichts, bearbeitet nichts und
veröffentlicht nichts; alles auf dem Bildschirm kam von Ihrem Broker und lebt
nur im Arbeitsspeicher.

## In einer Minute

- **Seitenleiste und Karte, gemeinsam.** Jedes eintreffende Asset erscheint
  als Feed-Zeile *und* als Pin, sobald es veröffentlicht wird. Frische
  Ankünfte pulsieren türkis; mit dem Alter werden sie grau.
- **Zeile antippen, zum Pin fliegen.** Die Seitenleiste ist das Register der
  Karte: Ein Tipp auf eine Zeile zoomt die Karte zu diesem Asset und
  markiert es mit einem Ring — erneut tippen (oder auf freie Karte tippen)
  löst ihn wieder. Der Info-Knopf der Zeile oder der Pin selbst öffnet die
  vollständigen Details.
- **Assets verblassen auf Zeit.** Wählen Sie, wie lange ein empfangenes
  Asset sichtbar bleibt (Minuten oder für immer). Pins schrumpfen und
  verblassen sichtbar, wenn ihre Zeit abläuft, und verlassen dann
  Seitenleiste und Karte gemeinsam — der Bildschirm zeigt nur, was aktuell
  ist.
- **Nach Profil filtern.** Ein Tipp auf einen Profil-Chip verengt beide
  Bereiche auf diesen Arbeitsablauf, in seiner Akzentfarbe; ein weiterer
  Tipp bringt alles zurück.
- **Nur-Lesen als Prinzip.** Der Viewer *abonniert* ausschließlich — er
  veröffentlicht nie zum Broker und schreibt weder Profil noch Asset.
- **Ein Produkt.** Dasselbe Leitungsformat und dieselbe schwarz-weiße
  Bildsprache wie die anderen Hecate-Apps; Farbe kommt allein aus dem
  Profil-Akzent jedes Objekts.

## Bildschirmfotos

<div class="shots">
  <figure class="wide"><img src="/assets/screens/viewer-ipad-karte.png" alt="Hecate Viewer für iPad — das geteilte Layout: Live-Feed-Seitenleiste neben der vollflächigen Karte mit eintreffenden Assets als Pins"><figcaption>Das geteilte Layout — Feed-Seitenleiste und Live-Karte</figcaption></figure>
</div>

## Was er zeigt

Der Viewer stellt den Live-Asset-Strom des Brokers dar — die erfassten Felder
jedes Objekts, seine Profilfarbe und seinen Namen sowie seine Position auf der
Karte. Der **zurückbehaltene Bestand** des Brokers füllt den Bildschirm im
Moment der Verbindung, sodass Sie nie auf eine leere Karte blicken, solange es
Geschichte zu zeigen gibt; alles danach trifft live ein. Was erscheint,
bestimmt allein **Ihr Broker und seine Berechtigungen**, nicht die App.

## Einrichtung

Verbinden Sie die App mit Ihrem MQTT-Broker — scannen Sie einen
Provisionierungs-QR Ihres Administrators oder geben Sie Host, Port, TLS und
Zugangsdaten von Hand ein (das Passwort wandert direkt in den Schlüsselbund
des Geräts). Laden Sie die Profile einmal, wählen Sie, wie lange Assets auf
dem Bildschirm bleiben, und schauen Sie zu. An den Daten selbst gibt es nichts
zu konfigurieren, denn die Daten definieren Ihre Profile — veröffentlicht von
der Erfassungs-App.

Auf dem iPhone gibt es dieselbe Live-Ansicht als
[Hecate Viewer für iPhone](../viewer-ios/index.md) mit einem
Karte/Feed-Tab-Layout — die iPad-App fällt auf diese Tabs zurück, wenn sie
sich den Bildschirm im Split View teilt.

---

[:octicons-arrow-right-24: Datenschutz](../privacy/viewer-ipad/index.md) ·
[:octicons-arrow-right-24: Support](../support/operator/index.md) ·
[:octicons-arrow-right-24: Der iPhone-Viewer](../viewer-ios/index.md)
