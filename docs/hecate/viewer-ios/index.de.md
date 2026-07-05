---
hide:
  - toc
---

# Hecate Viewer für iPhone & iPad

*Sehen Sie Ihre Assets eintreffen — live, auf der Karte, in Ihrer Tasche.*

Hecate Viewer ist der **rein lesende Begleiter** der Erfassungs-App. Er
verbindet sich mit demselben MQTT-Broker, **abonniert** den Asset-Strom und
setzt jedes eintreffende Objekt im Moment seiner Veröffentlichung auf eine
Live-Karte — mit einem chronologischen Feed daneben für den Spielverlauf.

Er ist ein **reiner Viewer**: Er erfasst nichts, bearbeitet nichts und
veröffentlicht nichts; alles auf dem Bildschirm kam von Ihrem Broker und lebt
nur im Arbeitsspeicher.

## In einer Minute

- **Zuerst eine Live-Karte.** Ein Pin pro eintreffendem Asset, dort, wo es
  erfasst wurde. Frische Ankünfte pulsieren türkis; mit dem Alter werden sie
  grau. Ein Feed-Tab zeigt denselben Strom, neueste zuerst.
- **Assets blenden sich per Timer aus.** Wählen Sie, wie lange ein empfangenes
  Asset sichtbar bleibt (Minuten oder unbegrenzt). Pins schrumpfen und
  verblassen sichtbar, wenn ihre Zeit abläuft, und verlassen Karte und Feed
  gemeinsam — die Karte zeigt so immer nur Aktuelles.
- **Nach Profil filtern.** Ein Tipp auf einen Profil-Chip verengt Karte und
  Feed auf diesen Workflow, in seiner Akzentfarbe; ein weiterer Tipp bringt
  alles zurück.
- **Rein lesend, per Konstruktion.** Der Viewer *abonniert* nur — er
  veröffentlicht nie an den Broker und schreibt weder Profil noch Asset.
- **Gleicher Broker, gleiche Daten.** Richten Sie ihn auf Ihren Broker (oder
  scannen Sie einen Provisionierungs-QR), und er zeigt genau das, was Ihre
  Zugangsdaten lesen dürfen.
- **Ein Produkt.** Dasselbe Wire-Format und dieselbe schwarz-weiße
  Bildsprache wie die anderen Hecate-Apps; Farbe kommt ausschließlich vom
  Profil-Akzent des jeweiligen Objekts.

## Screenshots

<div class="shots">
  <figure><img src="/assets/screens/viewer-ios-karte.png" alt="Die Live-Karte — eintreffende Assets als Pins, Broker- und Profil-Chips darüber"><figcaption>Die Live-Karte</figcaption></figure>
  <figure><img src="/assets/screens/viewer-ios-feed.png" alt="Der Live-Feed — neueste zuerst, mit Frische-Markierungen und Profilfarben"><figcaption>Der Live-Feed</figcaption></figure>
</div>

## Was er zeigt

Der Viewer rendert den Live-Asset-Strom vom Broker — die erfassten Felder
jedes Objekts, seine Profilfarbe und seinen Profilnamen sowie seine Position
auf der Karte. Der **Retained-Bestand** des Brokers füllt den Bildschirm im
Moment der Verbindung, sodass Sie nie auf eine leere Karte blicken, solange es
Historie zu zeigen gibt; alles danach trifft live ein. Was erscheint, bestimmen
allein **Ihr Broker und seine Berechtigungen**, nicht die App.

## Einrichtung

Verbinden Sie die App mit Ihrem MQTT-Broker — scannen Sie einen
Provisionierungs-QR Ihres Administrators oder geben Sie Host, Port, TLS und
Zugangsdaten von Hand ein (das Passwort wandert direkt in den Schlüsselbund
des Geräts). Laden Sie einmal die Profile, wählen Sie, wie lange Assets auf
dem Bildschirm bleiben sollen, und schauen Sie zu. An den Daten selbst gibt es
nichts zu konfigurieren, denn die Daten definieren Ihre Profile — und
veröffentlicht werden sie von der Erfassungs-App.

---

[:octicons-arrow-right-24: Datenschutz](../privacy/viewer-ios/index.md) ·
[:octicons-arrow-right-24: Support](../support/operator/index.md) ·
[:octicons-arrow-right-24: Die Erfassungs-App](../capture/index.md)
