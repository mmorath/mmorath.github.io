---
hide:
  - toc
---

# Hecate Viewer TV

*Le mur en direct — lisible d'un bout à l'autre de la pièce, et personne n'a
besoin d'y toucher.*

Hecate Viewer TV transforme un Apple TV en **mur d'actifs en direct** pour votre
installation Hecate. L'app se connecte au même broker MQTT que l'app de capture,
**s'abonne** au flux d'actifs et affiche chaque objet entrant sur une carte en
direct plein écran, avec un fil chronologique à côté — sur un écran d'atelier,
dans un bureau ou à l'entrée d'un site.

C'est un **pur visualiseur**. Il ne capture rien, ne modifie rien et ne publie
rien ; tout ce qui est à l'écran vient de votre broker et ne vit qu'en mémoire.

## En une minute

- **Configuration depuis l'iPhone, pas depuis la télécommande.** Le téléviseur
  affiche un code QR ; vous le scannez dans Hecate Viewer sur votre iPhone ou
  iPad et envoyez la configuration du broker — identifiants inclus — chiffrée sur
  votre réseau local. Le mur se remplit en quelques secondes. Aucune saisie à la
  télécommande, jamais.
- **Une carte pensée pour la pièce.** Un point par actif entrant, placé là où il
  a été capturé. Les arrivées récentes pulsent en turquoise ; en vieillissant
  elles passent au gris. Le fil latéral liste le même flux, le plus récent
  d'abord, avec les couleurs de profil et des étiquettes de fraîcheur.
- **La télécommande est facultative.** Ciblez une ligne du fil pour mettre son
  point en évidence, cliquez pour y zoomer, cliquez à nouveau pour voir tous les
  champs capturés. Laissé seul, le mur compose lui-même son image et se tient à
  jour.
- **Honnête sur son propre état.** Quand le flux se tait, le mur le dit — d'abord
  une teinte de repos, puis un voile de données périmées, puis un état de
  reconnexion clair qui se rétablit de lui-même. Un écran qui prétend être en
  direct est pire qu'un écran qui admet être hors ligne.
- **Conçu pour rester allumé.** Une protection anti-marquage décale la mise en
  page sur un écran non surveillé, et le mur garde l'écran éveillé pour qu'un
  affichage 24/7 ne s'endorme pas en pleine journée de travail.
- **Filtrer par profil et par zone.** Restreignez le mur à un profil de capture ou
  à une zone du site depuis l'overlay Lecture/Pause ; les actifs masqués restent
  comptés, donc les totaux ne mentent jamais.
- **Un seul produit.** Le même format de données et le même langage visuel noir et
  blanc que les autres apps Hecate ; la couleur ne vient que de l'accent de
  profil de chaque objet.

## Captures d'écran

<div class="shots">
  <figure class="wide"><img src="/assets/screens/fr/tv-wall.png" alt="Hecate Viewer TV — le mur en direct : fil latéral à côté de la carte plein écran avec les actifs entrants en points"><figcaption>Le mur — fil latéral et carte en direct</figcaption></figure>
</div>

*Les captures proviennent de versions de développement. Certaines peuvent montrer des fonctions nécessitant un abonnement ou prévues pour une version ultérieure — ce que l'offre gratuite contient aujourd'hui est indiqué sous [Free & Pro](../plans/index.fr.md).*

## Ce qu'il affiche

Le mur restitue le flux d'actifs en direct du broker — les champs capturés de
chaque objet, sa couleur et son nom de profil, et sa position sur la carte.
L'**historique conservé** du broker remplit l'écran dès la connexion, de sorte que
le mur ne démarre jamais vide s'il y a un historique à montrer ; tout le reste
arrive en direct. Ce qui apparaît est régi entièrement par **votre broker et ses
autorisations**, pas par l'app.

## Mise en route

Installez l'app : elle affiche un code de jumelage. Ouvrez
[Hecate Viewer pour iPhone](../viewer-ios/index.md) ou
[pour iPad](../viewer-ipad/index.md), choisissez votre broker et envoyez-le à
l'Apple TV — la configuration traverse votre réseau local chiffrée et le mot de
passe va directement dans le trousseau de l'appareil. Le mur se connecte et
démarre tout seul, et reste jumelé d'un redémarrage à l'autre.

Il n'y a rien à configurer sur les données elles-mêmes, car elles sont définies
par vos profils et publiées par l'app de capture.

!!! note "Il vous faut l'un des visualiseurs téléphone pour la configuration"

    Le jumelage est le seul mode de configuration — à dessein, car saisir un nom
    d'hôte de broker et un mot de passe avec une télécommande est un supplice.
    Installez d'abord Hecate Viewer sur un iPhone ou un iPad du même réseau.

---

[:octicons-arrow-right-24: Confidentialité](../privacy/viewer-tvos/index.md) ·
[:octicons-arrow-right-24: Assistance](../support/operator/index.md) ·
[:octicons-arrow-right-24: Le visualiseur iPhone](../viewer-ios/index.md)
