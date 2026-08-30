# Nutzungsbedingungen

*Hecate ist ein Produkt von MMM Software & Consulting. Diese Seite sagt in
klaren Worten, was für die Nutzung der Hecate-Apps gilt — und welcher Text
rechtlich gilt.*

## Was Hecate ist

Hecate ist eine Familie von Apps für iPhone, iPad und Apple TV, die physische
Objekte anhand eines konfigurierbaren **Profils** erfasst, sie verortet und
über **MQTT** an einen Broker Ihrer Wahl streamt.

Es gibt dafür kein Backend, kein Konto und keinen Dienst von uns: Die Apps
sprechen ausschließlich mit dem Broker, den Sie selbst eintragen.

## Welche Lizenz gilt

Für die Nutzung der Hecate-Apps gilt **Apples Standard-Lizenzvereinbarung für
Endnutzer**:

[Apple — Standard-Lizenzvereinbarung für Endnutzer (Licensed Application End
User License Agreement)](https://www.apple.com/legal/internet-services/itunes/dev/stdeula/)

Wir schreiben **absichtlich keine eigene Lizenz**. Eine selbst verfasste würde
Apples nicht ergänzen, sondern mit ihr konkurrieren — und müsste juristisch
geprüft werden, bevor sie irgendetwas verbessert. Das Feld für eine eigene EULA
in App Store Connect bleibt deshalb leer; genau dann greift Apples
Standardvereinbarung. **Diese Seite erklärt, sie ersetzt nichts.**

## Die kostenlose Stufe

Die kostenlose Stufe ist **ein echtes Produkt, kein Test**: Sie läuft nie ab,
und nichts von dem, was Sie erfasst haben, wird Ihnen vorenthalten. Begrenzt
ist die *Menge* — 10 Erfassungen je Kalendertag, ein gespeichertes Profil, ein
gleichzeitig publiziertes Profil, eine Broker-Konfiguration, Profile bis fünf
Bausteine.

Was diese Grenzen genau zählen und was die kostenlose Stufe sonst enthält,
steht vollständig unter [Free & Pro](../plans/index.de.md) — dort und nur
dort, damit dieselbe Angabe nicht an zwei Stellen auseinanderläuft.

## Das Abo

!!! info "Das Abo ist noch nicht käuflich"

    Die Apps, die heute ausgeliefert werden, enthalten **ausschließlich die
    kostenlose Stufe**. Es gibt in ihnen keinen Kauf und keinen Preis zu
    zahlen. Was hier steht, gilt, sobald ein Abo angeboten wird.

Das Abo wird **monatlich oder jährlich** angeboten, über Ihren Apple-Account
abgerechnet und **verlängert sich automatisch**, bis Sie es kündigen. Die
Kündigung erfolgt in der Apple-Abo-Verwaltung; die Bindung beträgt nie mehr als
eine Abrechnungsperiode.

**Einen Preis nennen wir hier noch nicht.** Die Produkte sind nicht angelegt,
und ein Preis, der sich bis zur Freigabe noch ändert, stünde falsch im Netz.
Sobald es so weit ist, steht er auf [Free & Pro](../plans/index.de.md), offen
und vollständig — genau dort, wo wir es zugesagt haben.

Läuft ein Abo aus, verlieren Sie nichts. Bereits erfasste Daten liegen auf
Ihrem Broker und auf Ihrem Gerät und bleiben dort. Die App fällt auf den
kostenlosen Umfang zurück — sie löscht nichts und sperrt nichts, was Sie
bereits angelegt haben.

## Wo der Vertrag zustande kommt

Die Hecate-Apps werden ausschließlich über den **App Store** vertrieben.
Ein Kauf oder ein Abonnement kommt dort mit **Apple** zustande, nicht mit uns.
Abrechnung, Rechnung, Widerruf und Kündigung laufen deshalb über Ihren
Apple-Account. Fragen zum Produkt selbst beantworten wir gerne unter der unten
genannten Adresse.

## Kündigen

Ein Abo kündigen Sie in der Abo-Verwaltung Ihres Apple-Accounts:

[apps.apple.com/account/subscriptions](https://apps.apple.com/account/subscriptions)

Die Kündigung wirkt zum Ende der laufenden Abrechnungsperiode; bis dahin bleibt
das Abo aktiv. Wir können ein Abo weder einsehen noch für Sie kündigen.

## Rückerstattung

Käufe laufen vollständig über Apple. Erstattungen können deshalb nur von Apple
vorgenommen werden — über den üblichen Weg:

[reportaproblem.apple.com](https://reportaproblem.apple.com)

**Über eine Erstattung entscheidet Apple, nicht wir.** Wir haben weder Ihre
Zahlungsdaten noch die Möglichkeit, eine Zahlung zurückzuholen. Schreiben Sie
uns trotzdem, wenn etwas nicht stimmt: Wir können den Fehler beheben, auch wenn
wir das Geld nicht bewegen können.

## Falls dieses Projekt endet

Hecate ist ein kleines Projekt, und das verschweigen wir nicht. Sollte die
Weiterentwicklung enden, kündigen wir das an, verkaufen keine neuen Abos mehr
und lassen laufende auslaufen.

Sie behalten alles. Ihre Daten liegen bereits auf Ihrem eigenen Broker, das
Profil-Format ist offenes, dokumentiertes JSON, und Profile lassen sich auch
ohne diese App veröffentlichen. Es gibt nichts zu exportieren und nichts zu
migrieren — genau deshalb ist das Monatsabo das Hauptprodukt: Ihre Bindung
beträgt nie mehr als dreißig Tage.

## Was wir betreiben — und was nicht

Hecate betreibt keine Server. Es gibt kein Backend, kein Konto und keinen
Dienst, der zwischen Ihnen und Ihren Daten steht. Die App spricht
ausschließlich mit dem MQTT-Broker, den Sie selbst eintragen.

Damit liegt der Betrieb bei Ihnen: der Broker, das Netz, die Zertifikate, die
Geräte. Ist der Broker nicht erreichbar, ein Zertifikat abgelaufen oder eine
Verwaltungsrichtlinie falsch gesetzt, kann die App das weder erkennen noch
beheben — sie zeigt es an und speichert Ihre Erfassung so lange auf dem Gerät.

Prüfen Sie wichtige Daten am Ziel. Diese App ist ein Werkzeug zur Erfassung,
kein Nachweis über den Verbleib einer Nachricht.

Was in Profilen und Erfassungen steht, bestimmen Sie. Die App prüft die
Struktur eines Profils, nicht seinen Inhalt — ob ein Feld sinnvoll, zulässig
oder rechtmäßig ist, kann nur der Betreiber beurteilen. Dasselbe gilt für den
Einsatz der Apps insgesamt: Sie sind Werkzeuge zur Erfassung im eigenen
Betrieb; ein Einsatz gegen geltende Regeln oder Rechte Dritter ist Missbrauch,
nicht Bestimmung.

Und: Diese Apps laufen auf Plattformen, die uns nicht gehören. Schränkt Apple,
Google oder ein Gerätehersteller mit einem Update eine Schnittstelle ein —
Kamera, Bluetooth, Druckdienste, Hintergrundbetrieb —, kann eine Funktion
eingeschränkt werden oder wegfallen, ohne dass wir das verhindern können. Wir
ziehen nach, wo es geht; ein Anspruch darauf, dass jede Funktion unter jeder
künftigen Betriebssystemversion fortbesteht, entsteht dadurch nicht.

## Kontakt

**MMM Software & Consulting**, Inhaber: Matthias Morath<br>
E-Mail: [info@hecateapps.com](mailto:info@hecateapps.com)

Die vollständigen Anbieterangaben stehen im
[Impressum](../impressum/index.de.md); was die Apps mit Daten tun, steht im
[Datenschutz](../privacy/index.de.md).
