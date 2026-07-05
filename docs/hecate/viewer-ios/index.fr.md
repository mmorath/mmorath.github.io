---
hide:
  - toc
---

# Hecate Viewer pour iPhone & iPad

*Regardez vos actifs arriver — en direct, sur la carte, dans votre poche.*

Hecate Viewer est le **compagnon en lecture seule** de l'application de
saisie. Il se connecte au même broker MQTT, **s'abonne** au flux d'actifs et
place chaque objet entrant sur une carte en direct à l'instant de sa
publication — avec, à côté, un flux chronologique pour suivre le fil des
événements.

C'est un **pur viewer** : il ne saisit rien, ne modifie rien et ne publie
rien ; tout ce qui est à l'écran vient de votre broker et ne vit qu'en
mémoire.

## En une minute

- **Une carte en direct, d'abord.** Une épingle par actif entrant, à l'endroit
  de sa saisie. Les arrivées récentes pulsent en turquoise ; en vieillissant,
  elles passent au gris. Un onglet Flux montre le même courant, du plus récent
  au plus ancien.
- **Les actifs s'estompent sur minuterie.** Choisissez la durée d'affichage
  d'un actif reçu (quelques minutes, ou toujours). Les épingles rétrécissent
  et s'estompent visiblement quand leur temps s'épuise, puis quittent la carte
  et le flux ensemble — la carte ne montre ainsi que l'actuel.
- **Filtrer par profil.** Un appui sur une pastille de profil restreint carte
  et flux à ce flux de travail, dans sa couleur d'accent ; un second appui
  ramène tout.
- **Lecture seule, par conception.** Le viewer ne fait que *s'abonner* — il ne
  publie jamais vers le broker et n'écrit ni profil ni actif.
- **Même broker, mêmes données.** Pointez-le vers votre broker (ou scannez un
  QR de configuration) et il montre exactement ce que vos identifiants ont le
  droit de lire.
- **Un seul produit.** Le même format de messages et le même langage visuel
  noir et blanc que les autres applications Hecate ; la couleur vient
  uniquement de l'accent de profil de chaque objet.

## Captures d'écran

<div class="shots">
  <figure><img src="/assets/screens/viewer-ios-karte.png" alt="La carte en direct — les actifs entrants en épingles, pastilles broker et profil au-dessus"><figcaption>La carte en direct</figcaption></figure>
  <figure><img src="/assets/screens/viewer-ios-feed.png" alt="Le flux en direct — du plus récent au plus ancien, avec indicateurs de fraîcheur"><figcaption>Le flux en direct</figcaption></figure>
</div>

## Ce qu'il montre

Le viewer affiche le flux d'actifs en direct du broker — les champs saisis de
chaque objet, la couleur et le nom de son profil, et sa position sur la carte.
Le **backlog retenu** du broker remplit l'écran dès la connexion, si bien que
vous n'ouvrez jamais sur une carte vide tant qu'il y a de l'historique à
montrer ; tout le reste arrive en direct. Ce qui apparaît est entièrement
gouverné par **votre broker et ses permissions**, pas par l'application.

## Mise en route

Connectez l'application à votre broker MQTT — scannez un QR de configuration
fourni par votre administrateur, ou saisissez hôte, port, TLS et identifiants
à la main (le mot de passe va directement dans le trousseau de l'appareil).
Chargez les profils une fois, choisissez la durée d'affichage des actifs, et
regardez. Il n'y a rien à configurer sur les données elles-mêmes : elles sont
définies par vos profils et publiées par l'application de saisie.

---

[:octicons-arrow-right-24: Confidentialité](../privacy/viewer-ios/index.md) ·
[:octicons-arrow-right-24: Assistance](../support/operator/index.md) ·
[:octicons-arrow-right-24: L'application de saisie](../capture/index.md)
