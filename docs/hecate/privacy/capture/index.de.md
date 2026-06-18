# Datenschutzerklärung — Hecate

**Gültig ab:** 11.06.2026
**Entwickler:** Matthias Morath

Hecate ist ein Feldwerkzeug zur Geo-Referenzierung physischer Objekte. Es erfasst
nur, was zur Identifizierung und Lokalisierung der von Ihnen erfassten Assets
erforderlich ist. Es gibt **kein vom Entwickler betriebenes Backend** und **keine
Analyse- oder Tracking-Dienste Dritter**.

## Was wir erfassen

Was die App erfasst, wird **ausschließlich durch das Profil** bestimmt, das die
Administratorin oder der Administrator Ihrer Organisation einrichtet — ein Profil
ist ein anpassbares Formular, das die Felder und Scans für einen Anwendungsfall
beschreibt. **Wir als Entwickler erstellen diese Profile nicht und sehen weder
die von Ihnen verwendeten Profile noch die damit erfassten Daten.** Was eine
konkrete Installation erfasst, entscheidet daher *Ihr* Administrator, nicht wir.

Bei einem typischen Profil verarbeitet die App:

- **Asset-Daten**, die Sie eingeben oder scannen (z. B. Serien-, Auftragsnummer,
  Typ).
- **Ein optionales Foto** des Assets, sofern Sie eines aufnehmen.
- **Den genauen GPS-Standort** zum Zeitpunkt der Erfassung — *nur, wenn Sie die
  Standortberechtigung erteilen*. Sie können diese jederzeit in den
  iOS-Einstellungen verweigern oder widerrufen; die App funktioniert auch ohne.

## Wohin die Daten gehen

Asset-Daten werden **ausschließlich an den von Ihnen konfigurierten MQTT-Broker**
gesendet. Diesen Broker wählen und kontrollieren Sie selbst. Der Entwickler
betreibt keinen Server, erhält keine Ihrer Daten und sieht weder die von Ihnen
verwendeten Profile noch die damit erfassten Assets. Es gibt keine Werbung, kein
Profiling und kein App- oder Website-übergreifendes Tracking.

## Speicherung und Sicherheit

- Assets werden **auf Ihrem Gerät gespeichert**, bis Sie sie löschen.
- Das Broker-**Passwort wird im iOS-Schlüsselbund** gespeichert — niemals im
  Klartext und niemals in Protokollen.
- Verbindungen zum Broker können **TLS** (`mqtts`) nutzen, sodass Daten während
  der Übertragung verschlüsselt sind.

## Weitergabe von Daten

Wir **verkaufen, vermieten oder teilen Ihre Daten nicht** mit Dritten. Die
einzige Übertragung ist die Veröffentlichung an **Ihren eigenen** MQTT-Broker,
die in Ihrem Auftrag und auf Ihre Veranlassung erfolgt.

## Ihre Wahlmöglichkeiten

- **Standort:** jederzeit in iOS-Einstellungen → Datenschutz erteilen,
  verweigern oder widerrufen.
- **Fotos:** vollständig optional, je Asset.
- **Löschung:** Sie können jedes Asset jederzeit auf dem Gerät löschen. Bereits
  an Ihren Broker gesendete Daten unterliegen der Aufbewahrung *Ihres* Brokers.

## Kinder

Hecate ist ein professionelles Feld-Werkzeug und richtet sich nicht an Kinder.

## Änderungen dieser Erklärung

Ändert sich der Datenumgang der App, werden diese Seite und der In-App-Bildschirm
**Einstellungen → Datenschutz** gemeinsam aktualisiert.
