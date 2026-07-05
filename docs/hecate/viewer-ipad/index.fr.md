---
hide:
  - toc
---

# Hecate Viewer pour iPad

*La carte en direct, bord à bord — avec le fil toujours à ses côtés.*

Hecate Viewer pour iPad est le **compagnon en lecture seule** de l'application
de saisie, conçu pour le grand écran. Il se connecte au même broker MQTT,
**s'abonne** au flux d'actifs et montre tout à la fois : le fil en direct en
**barre latérale**, la **carte** occupant le reste — pas d'onglets, les deux
volets toujours visibles, en portrait comme en paysage.

C'est un **pur visualiseur**. Il ne saisit rien, ne modifie rien et ne publie
rien ; tout ce qui est à l'écran vient de votre broker et ne vit qu'en
mémoire.

## En une minute

- **Barre latérale et carte, ensemble.** Chaque actif entrant apparaît comme
  une ligne du fil *et* comme une épingle dès sa publication. Les arrivées
  fraîches pulsent en sarcelle ; en vieillissant elles passent au gris.
- **Touchez une ligne, volez vers son épingle.** La barre latérale est
  l'index de la carte : toucher une ligne zoome la carte sur cet actif et
  l'entoure d'un anneau — touchez de nouveau (ou touchez la carte vide) pour
  le libérer. Le bouton info de la ligne, ou l'épingle elle-même, ouvre le
  détail complet.
- **Les actifs s'estompent sur minuterie.** Choisissez combien de temps un
  actif reçu reste visible (des minutes, ou pour toujours). Les épingles
  rétrécissent et s'estompent visiblement quand leur temps s'écoule, puis
  quittent barre latérale et carte ensemble — l'écran ne montre que ce qui
  est actuel.
- **Filtrer par profil.** Un toucher sur une puce de profil restreint les
  deux volets à ce flux de travail, dans sa couleur d'accent ; un toucher de
  plus ramène tout.
- **Lecture seule par conception.** Le visualiseur ne fait que *s'abonner* —
  il ne publie jamais vers le broker et n'écrit ni profil ni actif.
- **Un seul produit.** Le même format de transport et le même langage visuel
  noir et blanc que les autres applications Hecate ; la couleur ne vient que
  de l'accent de profil de chaque objet.

## Captures d'écran

<div class="shots">
  <figure class="wide"><img src="/assets/screens/viewer-ipad-karte.png" alt="Hecate Viewer pour iPad — la disposition scindée : barre latérale du fil en direct à côté de la carte pleine page avec les actifs entrants en épingles"><figcaption>La disposition scindée — fil latéral et carte en direct</figcaption></figure>
</div>

## Ce qu'il montre

Le visualiseur rend le flux d'actifs en direct du broker — les champs saisis
de chaque objet, sa couleur et son nom de profil, et sa position sur la
carte. Le **backlog retenu** du broker remplit l'écran dès la connexion, si
bien que vous n'ouvrez jamais sur une carte vide tant qu'il y a de
l'historique à montrer ; tout ce qui suit arrive en direct. Ce qui apparaît
est régi entièrement par **votre broker et ses permissions**, pas par
l'application.

## Mise en route

Connectez l'application à votre broker MQTT — scannez un QR de
provisionnement fourni par votre administrateur ou saisissez hôte, port, TLS
et identifiants à la main (le mot de passe va directement dans le trousseau
de l'appareil). Récupérez les profils une fois, choisissez combien de temps
les actifs restent à l'écran, et regardez. Il n'y a rien à configurer sur les
données elles-mêmes, car les données sont définies par vos profils et
publiées par l'application de saisie.

Sur iPhone, la même vue en direct existe sous la forme de
[Hecate Viewer pour iPhone](../viewer-ios/index.md) avec une disposition à
onglets Karte/Fil — l'application iPad revient à ces onglets quand elle
partage l'écran en Split View.

---

[:octicons-arrow-right-24: Confidentialité](../privacy/viewer-ipad/index.md) ·
[:octicons-arrow-right-24: Assistance](../support/operator/index.md) ·
[:octicons-arrow-right-24: Le visualiseur iPhone](../viewer-ios/index.md)
