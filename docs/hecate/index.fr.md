---
hide:
  - toc
---

# Hecate

*Un système piloté par profils pour géo-référencer des objets physiques — une famille d'applications, un broker, pas de backend.*

Hecate saisit des objets physiques selon un **profil** — un flux configurable
de scans, de champs et de photos —, les place sur la carte et les diffuse en
**MQTT** vers le broker de votre choix. Rien du domaine métier n'est codé en
dur : changez le profil et le même système sert pour des chariots élévateurs,
des extincteurs, des prises réseau ou des découvertes archéologiques — **sans
nouveau build, sans nouvelle application**.

!!! tip "La seule chose requise : un broker MQTT"

    Hecate n'exige **aucun système backend**. La seule et unique dépendance
    réseau est le **broker MQTT que vous contrôlez déjà** — sur site ou dans
    le cloud. Pas de serveur de l'éditeur, pas de comptes, pas d'analyses,
    pas de suivi — et vos données ne touchent jamais l'infrastructure de
    quelqu'un d'autre.

Et Hecate n'est **pas une application silo** : c'est *vous* qui décidez quels
profils créer et quel rôle les actifs saisis jouent dans votre entreprise et
votre exploitation. Comme tout arrive sur votre broker dans une enveloppe
uniforme et auto-descriptive, n'importe quel système en aval de votre choix —
un tableau de bord, un historian, une passerelle ERP, un Unified Namespace —
peut s'abonner et exploiter les données. Les applications s'arrêtent au
broker ; le sens vous appartient.

## Le problème résolu

Les entreprises font tourner une **prolifération d'applications de saisie
mono-usage** — un outil par cas d'usage, chacun construit isolément. Résultat :
une qualité de données inégale (chaque application valide différemment), une
saisie qui se fait encore au bureau plutôt que sur le terrain, des
enregistrements qui ne disent jamais **où** se trouve l'objet — et, par outil,
un backend et une gestion de flotte à opérer.

Hecate remplace cette prolifération par **un système configurable** : les
profils définissent *quoi* saisir, la validation a lieu au moment de la
saisie, chaque enregistrement porte sa position GPS, et tout transite par le
seul broker que vous contrôlez déjà.

[:octicons-arrow-right-24: Le problème en détail](capture/problem.md) ·
[:octicons-arrow-right-24: Comment Hecate supprime chaque irritant](capture/solution.md)

## Les applications

<div class="grid cards" markdown>

-   :material-cellphone: __Hecate__ · l'application de saisie · iPhone & iPad

    ---

    L'outil de terrain. Scanne, valide et géo-référence chaque objet selon le
    profil actif, puis le publie vers votre broker. Fonctionne hors ligne avec
    une file d'attente durable qui se vide à la reconnexion.

    [:octicons-arrow-right-24: Présentation de la saisie](capture/index.md)

-   :material-map-marker-radius: __Hecate Viewer__ · iPhone

    ---

    La carte en direct, dans la poche. Un pur abonné qui place les actifs sur
    la carte à l'instant de leur publication et les estompe après la durée de
    votre choix — il ne saisit rien et ne publie rien.

    [:octicons-arrow-right-24: Présentation du viewer iPhone](viewer-ios/index.md)

-   :material-tablet: __Hecate Viewer__ · iPad

    ---

    La carte en direct, bord à bord. Le fil occupe une barre latérale à côté
    de la carte pleine page — touchez une ligne et la carte vole vers
    l'épingle de cet actif. Le même abonné, conçu pour le grand écran.

    [:octicons-arrow-right-24: Présentation du viewer iPad](viewer-ipad/index.md)

-   :material-tune-variant: __Hecate Admin__ · iPhone & iPad · *en développement*

    ---

    L'autorité d'édition. Crée, valide, versionne, publie et retire les
    profils que l'application de saisie consomme — actuellement en
    développement actif.

    [:octicons-arrow-right-24: Présentation de l'admin](admin/index.md)

</div>

## Captures d'écran

<div class="shots">
  <figure><img src="/assets/screens/assets.png" alt="Application de saisie Hecate — la file d'attente des objets saisis en attente d'envoi"><figcaption>Hecate — saisie &amp; file d'attente</figcaption></figure>
  <figure><img src="/assets/screens/detail.png" alt="Application de saisie Hecate — la vue détaillée d'un actif avec ses champs saisis"><figcaption>Hecate — détail d'un actif</figcaption></figure>
  <figure><img src="/assets/screens/viewer-ios-karte.png" alt="Hecate Viewer — la carte en direct avec les actifs entrants en épingles"><figcaption>Viewer — la carte en direct</figcaption></figure>
  <figure><img src="/assets/screens/viewer-ios-feed.png" alt="Hecate Viewer — le flux en direct, du plus récent au plus ancien"><figcaption>Viewer — le flux en direct</figcaption></figure>
  <figure class="wide"><img src="/assets/screens/viewer-ipad-karte.png" alt="Hecate Viewer pour iPad — la disposition scindée : barre latérale du fil à côté de la carte en direct pleine page"><figcaption>Viewer pour iPad — la disposition scindée</figcaption></figure>
</div>

## Sur la feuille de route

- :material-television: **Viewer Apple TV** — la même vue en direct comme
  affichage mural autonome pour les ateliers, bureaux et entrées de site.
  [Un aperçu du concept](viewer/index.md) est déjà décrit.

## Comment tout s'articule

```
App admin  ──édite & publie (retained)──▶  Broker MQTT  ◀──lit les profils──  App de saisie
                                                ▲                                  │
                                                └──────── publie les actifs ───────┘
                                                │
                                      s'abonne & affiche
                                                ▼
                         Hecate Viewer (iPhone · iPad) · Apple TV (prévu)
```

L'application **admin** fait autorité sur les *profils* ; l'application de
**saisie** est en lecture seule sur les profils et fait autorité sur les
*actifs* ; les **viewers** sont en lecture seule sur tout. Toutes les
applications partagent un même cœur, un même format de messages et un même
langage visuel noir et blanc — la couleur vient uniquement de l'accent de
profil de chaque objet.

## Le nom & le symbole

**Hécate** est la déesse grecque des carrefours, des seuils et des clés —
celle qui se tient à la frontière et détient ce qui l'ouvre. Le symbole est le
**Strophalos** (« la roue d'Hécate ») — un labyrinthe de chemins sinueux
autour d'un moyeu unique : les itinéraires sur le terrain, et les messages qui
convergent vers le broker au centre.

## Pour chaque application

| | Confidentialité | Assistance |
| --- | --- | --- |
| **Hecate (saisie)** | [Confidentialité](privacy/capture/index.md) | [Assistance](support/operator/index.md) |
| **Hecate Viewer (iPhone)** | [Confidentialité](privacy/viewer-ios/index.md) | [Assistance](support/operator/index.md) |
| **Hecate Viewer (iPad)** | [Confidentialité](privacy/viewer-ipad/index.md) | [Assistance](support/operator/index.md) |
| **Hecate Admin** | [Confidentialité](privacy/admin/index.md) | [Assistance](support/admin/index.md) |
| **Viewer Apple TV** *(prévu)* | [Confidentialité](privacy/viewer/index.md) | [Assistance](support/operator/index.md) |
