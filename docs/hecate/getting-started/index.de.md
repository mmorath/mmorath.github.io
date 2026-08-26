# Erste Schritte

*Vom leeren Broker zum ersten erfassten Asset — in etwa zwanzig Minuten.*

Hecate betreibt **kein Backend**. Es gibt kein Konto anzulegen und keinen Server
von uns zwischen Ihren Geräten und Ihren Daten — was zugleich bedeutet: Es gibt
keinen vorgegebenen Ort, an den Ihre Erfassungen gehen. Der **MQTT-Broker ist
die fehlende Mitte, und er gehört Ihnen**. Diese Seite richtet ihn ein und führt
einen Ablauf einmal von Anfang bis Ende durch.

!!! tip "Was Sie brauchen"

    1. **Einen erreichbaren MQTT-Broker** — Ihren eigenen oder eine kostenlose Testinstanz.
    2. **[Hecate Admin](../admin/index.md)** auf iPhone oder iPad, um den Ablauf zu erstellen und zu publizieren.
    3. **[Hecate Capture](../capture/index.md)** auf dem Gerät, das scannen soll.

    Der [Viewer](../viewer-ios/index.md) ist für einen ersten Test optional — und in jedem Fall kostenlos.

## 1 · Broker wählen

Hecate spricht Standard-MQTT und ist an keinen bestimmten Broker gebunden.

**Wenn Sie bereits MQTT betreiben**, nutzen Sie ihn. Was Hecate voraussetzt:

| Voraussetzung | Wozu |
| --- | --- |
| MQTT 3.1.1 oder 5 | das Protokoll, das die Apps sprechen |
| **Retained Messages** | so erreicht ein publizierter Ablauf ein Gerät, das beim Publizieren offline war |
| TLS | die Apps nutzen standardmäßig `mqtts` auf Port `8883` mit Zertifikatsprüfung |
| Zugangsdaten je Client | damit jedes Gerät eine eigene Identität hat und einzeln entzogen werden kann |
| Rechte je Topic | damit der Viewer tatsächlich nur liest und nicht bloß der Absicht nach |

**Wenn nicht**, ist eine gehostete Testinstanz in Minuten eingerichtet und im
Testumfang kostenlos. HiveMQ Cloud und EMQX Serverless haben beide einen
kostenlosen Tarif; ein Mosquitto-Container auf dem Notebook genügt für einen
ersten Test in einem Netz.

!!! warning "Ein Broker ohne Retained Messages sieht aus, als funktioniere er"

    Geräte empfangen dann schlicht keinen Ablauf, auf den sie nicht genau im
    Moment des Publizierens schon gelauscht haben. Prüfen Sie diese eine
    Fähigkeit, bevor Sie irgendetwas anderes suchen.

## 2 · Admin-App verbinden

<div class="shots">
  <figure><img src="/assets/screens/de/gs-broker-connection.png" alt="Broker-Verbindungseinstellungen — Host, Port, Protokoll und TLS"><figcaption>Verbindung: Host, Port, TLS</figcaption></figure>
  <figure><img src="/assets/screens/de/gs-broker-auth.png" alt="Broker-Authentifizierung — Benutzername und Passwort"><figcaption>Authentifizierung</figcaption></figure>
</div>

Die Voreinstellungen sind die sicheren, und es soll Mühe kosten, sie
abzuschwächen:

| Einstellung | Voreinstellung |
| --- | --- |
| Protokoll | `mqtts` — einfaches `mqtt` ist möglich und wird gewarnt |
| Port | `8883` |
| TLS | ein |
| Zertifikat prüfen | ein — nur für einen Entwicklungs-Broker mit selbstsigniertem Zertifikat abschalten |

Zugangsdaten gehen direkt in den **Schlüsselbund** des Geräts, verschlüsselt
gespeichert. Sie werden nie in einen Ablauf geschrieben, nie an den Broker
publiziert und nie im Provisionierungs-QR mitgeführt.

Wenn der Verbindungstest gelingt, **publizieren Sie einen Ablauf**. Halten Sie
ihn für den ersten Durchgang trivial — ein einzelner Scan-Schritt und ein
Textfeld beweisen die ganze Kette. Ein schlecht modellierter echter Prozess
beweist gar nichts.

## 3 · Feldgeräte provisionieren

Ein zwanzigstelliges Passwort, zwanzigmal in ein Pistolengriff-Handgerät
getippt — so stirbt ein Pilot, bevor er beginnt. Hecate provisioniert
stattdessen per QR-Code.

<div class="shots">
  <figure><img src="/assets/screens/de/gs-broker-share-qr.png" alt="Die Broker-Konfiguration als QR-Code teilen"><figcaption>Konfiguration teilen</figcaption></figure>
  <figure><img src="/assets/screens/de/gs-provisioning.png" alt="Das Gerät bestätigt die empfangenen Broker-Koordinaten"><figcaption>Das Gerät bestätigt</figcaption></figure>
</div>

Der Code trägt die **Koordinaten**: Host, Port, TLS-Einstellungen, Topic-Präfixe
und die optionalen Unified-Namespace-Ebenen. Er trägt **nicht** das Passwort —
ein QR-Code an einer Lagerwand ist ein Zugangsdatum, das jeder Vorbeigehende
bekommt. Jedes Gerät erhält einmalig eigenen Benutzernamen und eigenes Passwort,
und beide gehen in den Schlüsselbund.

Wo ein MDM die Geräte verwaltet, lassen sich dieselben Koordinaten als Managed
App Configuration ausrollen — und dort *dürfen* die Zugangsdaten mitreisen: Ein
MDM-Payload ist ein Verwaltungskanal, kein Aushang. Dieser Kanal ist unter
Android umgesetzt und im Feld verifiziert; unter iOS ist er spezifiziert und
noch nicht gebaut.

## 4 · Erfassen — und selbst nachprüfen

Der Ablauf erscheint von allein auf dem Feldgerät. Kein Download-Schritt, kein
App-Update — das ist die Retained Message bei der Arbeit.

<div class="shots">
  <figure><img src="/assets/screens/de/capture-sent.png" alt="Übermittelte Assets, vom Broker bestätigt"><figcaption>Gesendet — die Erfassung hat den Broker erreicht</figcaption></figure>
</div>

Scannen, ausfüllen, speichern. Die Validierung passiert **auf dem Gerät**, gegen
die Regeln des Autors — schlechte Daten verlassen es nie. Kein Netz? Trotzdem
erfassen: Fertige Erfassungen warten in einer Outbox und laufen ab, sobald die
Verbindung zurück ist. Ein sinkender Outbox-Zähler ist das ehrliche Zeichen,
dass der Broker Ihre Nachrichten annimmt.

**Sehen Sie sich den Broker jetzt mit etwas an, das nicht von uns ist.**
Verbinden Sie [MQTT Explorer](http://mqtt-explorer.com/) mit beliebigen
Zugangsdaten, die abonnieren dürfen: Der retained Ablauf liegt unter dem
Config-Präfix, und Ihre Erfassung erscheint binnen einer Sekunde nach dem
Speichern unter dem Asset-Präfix.

Dieser letzte Schritt wiegt schwerer, als er aussieht. Er beweist, dass die
Daten in *Ihrer* Infrastruktur liegen, in einem Format, das Sie lesen können,
erreichbar für Systeme, die von Hecate nie gehört haben. Keine Hecate-App hängt
vom MQTT Explorer ab — er ist ein Diagnosewerkzeug und muss eines bleiben.

## Was wo auf dem Broker liegt

Zwei Bäume, die Segment für Segment zueinander passen:

```text
hecate/config/profiles/<profileId>        der Ablauf     — RETAINED
hecate/assets/<profileId>/<assetUuid>     eine Erfassung — nicht retained
```

- **Abläufe sind retained.** Ein Gerät, das eine Woche aus war, erhält den
  aktuellen Stand beim Verbinden. Einen Ablauf zurückziehen heißt: einen leeren
  retained Payload publizieren — er verschwindet dann von jedem Gerät.
- **Erfassungen sind Ereignisse** und nicht retained. So bleibt beim Umbenennen
  eines Ablaufs nichts Veraltetes an einer alten Adresse liegen.
- **Die Ablauf-ID ist eine eigene Topic-Ebene.** Genau das macht
  `hecate/assets/<profileId>/#` zu einem brauchbaren Filter statt zu einem
  flachen Haufen von UUIDs.

Beide Präfixe sind konfigurierbar und reisen im Provisionierungs-QR mit.
Betreiben Sie einen Unified Namespace, schalten Sie die Hierarchie ein, und der
Asset-Baum fügt sich ein:

```text
<enterprise>/<site>/<area>/<line>/assets/<profileId>/<assetUuid>
acme/plant1/line3/assets/goods-in/1E935809-BF49-4716-B1D6-40F572FECE5B
```

Erfassungen kommen als selbstbeschreibender `{ header, data }`-Umschlag an. Jedes
nachgelagerte System — Historian, Dashboard, ERP-Brücke — kann ihn abonnieren
und lesen, ohne uns zu fragen.

## Rechte

Geben Sie jeder Capture-Installation **einen eigenen Broker-Benutzer** —
`capture-001`, `capture-002`. Das kostet bei der Einrichtung Minuten und bringt
Nachvollziehbarkeit, Entzug je Gerät, isolierte Passwortwechsel und eine
Auditantwort, die aus einem Topic-Log besteht statt aus einem Schulterzucken.

| App | Abläufe: abonnieren | Abläufe: publizieren | Erfassungen: abonnieren | Erfassungen: publizieren |
| --- | :---: | :---: | :---: | :---: |
| **Admin** | ja | **ja** | ja | nein |
| **Capture** | ja | nein | nein | **ja** |
| **Viewer** | ja | nein | ja | nein |

Als Broker-Regeln:

```text
capture-001   SUBSCRIBE  hecate/config/profiles/#
              PUBLISH    hecate/assets/#

viewer-lobby  SUBSCRIBE  hecate/config/profiles/#
              SUBSCRIBE  hecate/assets/#

admin-anna    SUBSCRIBE  hecate/config/profiles/#
              PUBLISH    hecate/config/profiles/#
              SUBSCRIBE  hecate/assets/#
```

!!! note "Den Nur-Lese-Viewer erzwingen, nicht ihm vertrauen"

    Der Viewer publiziert nichts; so ist er gebaut. Geben Sie ihm trotzdem ein
    Konto, das nur abonnieren darf. Ein Recht, das der Broker durchsetzt,
    übersteht eine Fehlkonfiguration, eine künftige Version und ein Gerät, das
    jemand anderes installiert.

## Wenn es nicht geht

| Symptom | Übliche Ursache | Prüfen |
| --- | --- | --- |
| Broker nicht erreichbar | DNS, Firewall, falscher Port | Host aus demselben Netz auf demselben Port erreichen |
| Verbindung abgelehnt | falscher Endpunkt, Broker aus | Endpunkt zeichenweise mit der Broker-Konsole vergleichen |
| Authentifizierung fehlgeschlagen | Benutzername oder Passwort | am Gerät neu eingeben; der Schlüsselbund hält bis dahin das alte |
| Autorisierung fehlgeschlagen | Topic-Rechte | die Zugangsdaten verbinden sich, dürfen das Topic aber nicht |
| TLS-Handshake fehlgeschlagen | Zertifikat oder Vertrauen | eine private CA braucht ihr Wurzelzertifikat auf dem Gerät |
| Kein Ablauf erscheint | Retained Message, Präfix oder Abo-Recht | im Explorer unter dem Config-Präfix nachsehen |
| Erfassung kommt nicht an | Publish-Recht oder offline | eine Outbox, die nie leer wird, heißt: Publish verweigert |
| Viewer bleibt leer | Abo-Recht auf dem Asset-Baum | er braucht das Asset-Präfix, nicht nur den Ablauf-Baum |

Die Unterscheidung, die man verinnerlicht haben sollte: **Authentifizierung**
ist, wer Sie sind; **Autorisierung** ist, was diese Identität anfassen darf. Ein
Gerät, das sich anstandslos verbindet und nichts publiziert, hat das Erste
bestanden und am Zweiten verloren — und die Lösung liegt in den Broker-Regeln,
nicht in der App.

## Nach der Evaluierung

Pilot- und Produktivaufbau unterscheiden sich in der Identitätsverwaltung, nicht
in der Architektur. Nichts aus dem Test ist verloren.

- **Zertifikate statt Passwörter.** Mutual TLS (mTLS) gibt jedem Gerät ein
  Client-Zertifikat und damit einen echten Lebenszyklus: ausstellen, erneuern,
  entziehen. Teilen Sie **nicht** ein Zertifikat über alle Geräte — das stellt
  das Problem des geteilten Passworts mit mehr Aufwand wieder her.
- **Rollen statt Regeln je Gerät.** Das fünfzigste Handgerät hinzuzufügen sollte
  eine Rollenzuweisung sein, nicht fünf ACL-Zeilen.
- **Jetzt in Ihren Namensraum einfügen**, nicht später migrieren. Das Topic
  ändert sich, der Payload nicht.
- **Das Nachgelagerte anhängen.** Der Viewer ist ein Live-Fenster, kein
  Datenlager — er hält Erfassungen im Speicher und filtert clientseitig. Für
  Historie und Auswertung abonnieren Sie ein System, das Sie ohnehin haben.
  Diese Grenze ist Absicht.

---

Irgendwo hängen geblieben? [Admin-Support](../support/admin/index.md) ·
[Bediener-Support](../support/operator/index.md)
