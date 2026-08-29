---
hide:
  - toc
---

# Hecate Admin

*Die Autoritäts-App für Hecate-Profile — iPhone & iPad.*

Hecate Admin ist der Begleiter der [Erfassungs-App](../capture/index.md). Wo
die Erfassungs-App einem Profil *folgt*, ist die Admin-App die **Autorität**,
die diese Profile **erstellt, validiert, versioniert, veröffentlicht und
zurückzieht** — und die Broker-Verbindung einrichtet, über die sie laufen.

Ein *Profil* ist der konfigurierbare Ablauf aus Scans und Feldern, der
der Erfassungs-App sagt, was ein Objekt ist und wie es zu erfassen ist. In
Hecate Admin wird dieses Profil geschrieben, geprüft und verwaltet.

## In einer Minute

- **Profile verfassen.** Definieren Sie Schritte, Felder, Erfassungsregeln und
  den Profil-Akzent, die einen Erfassungs-Workflow formen — ohne Code, ohne
  neuen App-Build.
- **Validiert vor dem Publizieren.** Ein Profil wird gegen sein Schema und den
  Versionierungs-Vertrag geprüft, damit die Erfassungs-App nie eines erhält,
  das sie stillschweigend verwerfen würde.
- **Sichere Versionierung.** Versionen bleiben monoton; ein „Zurückdrehen" ist
  ein Republish unter höherer Version, nie ein Rollback — Geräte können nicht
  herabgestuft werden.
- **Broker-only.** Profile werden als **Retained**-MQTT-Nachrichten
  veröffentlicht; zum Zurückziehen wird die Retained-Nachricht gelöscht. Kein
  Server, keine zweite Netzwerkabhängigkeit.
- **Zugangsdaten bleiben, wo sie hingehören.** Das Admin-Broker-Credential
  liegt im **Schlüsselbund** des Geräts und wird nie in ein Profil, einen
  Provisionierungs-QR, ein Log oder sonst irgendwohin geschrieben, wo es
  auslaufen könnte.
- **Keine Telemetrie.** Die Admin-App erhebt keinen Standort, keine
  Nutzungsanalysen und kein Tracking irgendeiner Art.

## Screenshots

Zwei Bildschirme tragen diese App: die **Profil-Übersicht**, die zeigt, was
publiziert ist und woran gerade gearbeitet wird, und der **Assistent**, in
dem ein Ablauf aus Bausteinen entsteht. Die Schritte stehen in der
Reihenfolge, in der die Anwender sie durchlaufen, und nichts wird
publiziert, bevor es geprüft wurde.

<div class="shots">
  <figure><img src="/assets/screens/de/admin-profiles.png" alt="Die Profil-Übersicht mit den erstellten Profilen"><figcaption>Profil-Übersicht</figcaption></figure>
  <figure><img src="/assets/screens/de/admin-wizard.png" alt="Die Bausteinauswahl des Assistenten — was ein Schritt erfassen soll"><figcaption>Der Assistent: Baustein wählen</figcaption></figure>
  <figure><img src="/assets/screens/de/admin-steps.png" alt="Die Schritte des Ablaufs in der Reihenfolge, in der sie durchlaufen werden"><figcaption>Die Schritte, der Reihe nach</figcaption></figure>
  <figure><img src="/assets/screens/de/admin-review.png" alt="Die vollständige Prüfung eines Profils, bevor es angelegt wird"><figcaption>Prüfen vor dem Publizieren</figcaption></figure>
  <figure><img src="/assets/screens/de/admin-detail.png" alt="Der Profil-Editor"><figcaption>Profil-Editor</figcaption></figure>
  <figure><img src="/assets/screens/de/admin-broker.png" alt="Die Broker-Konfigurationen, in die publiziert wird"><figcaption>Broker-Konfigurationen</figcaption></figure>
</div>

*Die Aufnahmen stammen aus Entwicklungsversionen. Einzelne Bildschirme können Funktionen zeigen, die ein Abo voraussetzen oder erst in einer späteren Version kommen — was die kostenlose Stufe heute enthält, steht unter [Free & Pro](../plans/index.de.md).*

## Wie Profile auf die Geräte kommen

Die Admin-App veröffentlicht jedes Profil als **Retained**-Nachricht unter
`<configPrefix>/profiles/<id>` (Standard `hecate/config`). Das Retained-Flag
sorgt dafür, dass auch ein Gerät, das sich *später* verbindet, das aktuelle
Profil erhält; die Erfassungs-App übernimmt es nur, wenn seine Version strikt
neuer ist als die vorhandene. Zum **Zurückziehen** löscht die Admin-App die
Retained-Nachricht, und die Geräte entfernen das Profil bei ihrer nächsten
Abstimmung.

## Gestaltungsidentität

Hecate Admin teilt die Bildsprache der Erfassungs-App: **strikt
schwarz-weißes** Chrome **ohne globale Markenfarbe** — die einzige Farbe ist
der Akzent des jeweiligen Profils, der ihm durch Zeile, Farbfeld und
Detailkarte folgt. Das Zeichen ist der gemeinsame Strophalos.

---

[:octicons-arrow-right-24: Datenschutz](../privacy/admin/index.md) ·
[:octicons-arrow-right-24: Support](../support/admin/index.md) ·
[:octicons-arrow-right-24: Die Erfassungs-App](../capture/index.md)
