---
hide:
  - toc
---

# Hecate

*Géoréférencement universel d'objets, piloté par profils*

Hecate est une application iOS pensée pour le terrain, dédiée au
**géoréférencement d'objets physiques**. Chaque objet est saisi à partir d'un
**profil** — un déroulé configurable de scans, de champs et de photos — puis
placé sur la carte avec un point GPS et transmis en **MQTT** vers le broker de
votre choix.

Rien du domaine métier n'est figé dans le code. Changez de profil et la même
application saisit des chariots élévateurs, des extincteurs, des prises réseau
ou des découvertes archéologiques — sans nouvelle compilation.

## En une minute

- **Une application, de multiples cas d'usage.** Chaque cas d'usage est un
  *profil*, pas une application distincte.
- **Validé à la source.** Chaque champ est vérifié par rapport au format
  déclaré au moment même de la saisie.
- **Toujours localisé.** Chaque enregistrement porte un point GPS et apparaît
  sur la carte.
- **Transmis en MQTT.** Publié vers *votre propre* broker dans une enveloppe
  uniforme et auto-descriptive — sans backend du développeur, sans analytique,
  sans suivi.
- **Fonctionne hors ligne.** Une file d'attente durable (outbox) conserve les
  enregistrements hors de portée et les envoie à la reconnexion.

## Captures d'écran

<div class="shots">
  <figure><img src="/assets/screens/assets.png" alt="La file d'attente des assets — objets saisis en attente d'envoi"><figcaption>Assets &amp; file d'attente</figcaption></figure>
  <figure><img src="/assets/screens/detail.png" alt="La vue détaillée d'un asset avec ses champs saisis"><figcaption>Détail d'un asset</figcaption></figure>
  <figure><img src="/assets/screens/sent.png" alt="Historique d'envoi des assets transmis"><figcaption>Historique d'envoi</figcaption></figure>
  <figure><img src="/assets/screens/settings.png" alt="Le hub des réglages"><figcaption>Réglages</figcaption></figure>
</div>

## Pour aller plus loin

<div class="grid cards" markdown>

-   :material-alert-circle-outline: __Le problème__

    ---

    Pourquoi une multitude d'applications de saisie à usage unique rend les
    données incohérentes, sédentaires et aveugles à la localisation.

    [:octicons-arrow-right-24: Le problème](problem.md)

-   :material-checkbox-marked-circle-outline: __Ce que fait Hecate__

    ---

    Comment une application pilotée par profils résorbe cette dispersion et
    corrige les données à la source.

    [:octicons-arrow-right-24: Ce que fait Hecate](solution.md)

</div>

## Le nom & le symbole

Le nom **Hecate** vient de la déesse grecque **Hécate** — déesse des
carrefours, des seuils et des clés, celle qui se tient à la frontière et
détient ce qui l'ouvre. Un outil de terrain vit précisément à cette limite :
entre l'objet physique devant vous et les systèmes numériques qui doivent en
prendre connaissance. Hecate le **localise**, **guide** la saisie, le
**transporte** jusqu'au broker et **détient les clés** qui ouvrent le chemin.

Le symbole est le **Strophalos** (« roue d'Hécate ») — un labyrinthe de
chemins sinueux autour d'un moyeu unique : les itinéraires sur le terrain et
les messages qui convergent vers le broker, au centre.
