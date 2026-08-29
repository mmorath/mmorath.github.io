---
hide:
  - toc
---

# Hecate Capture

*Géoréférencement universel d'objets, piloté par profils*

Hecate Capture est une application iOS pensée pour le terrain, dédiée au
**géoréférencement d'objets physiques**. Chaque objet est saisi à partir d'un
**profil** — un déroulé configurable de scans et de champs — puis
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
  <figure><img src="/assets/screens/fr/capture-assets.png" alt="La file d'attente des assets — objets saisis en attente d'envoi"><figcaption>Assets &amp; file d'attente</figcaption></figure>
  <figure><img src="/assets/screens/fr/capture-detail.png" alt="La vue détaillée d'un asset avec ses champs saisis"><figcaption>Détail d'un asset</figcaption></figure>
  <figure><img src="/assets/screens/fr/capture-sent.png" alt="Historique d'envoi des assets transmis"><figcaption>Historique d'envoi</figcaption></figure>
  <figure><img src="/assets/screens/fr/capture-settings.png" alt="Le hub des réglages"><figcaption>Réglages</figcaption></figure>
</div>

*Les captures proviennent de versions de développement. Certaines peuvent montrer des fonctions nécessitant un abonnement ou prévues pour une version ultérieure — ce que l'offre gratuite contient aujourd'hui est indiqué sous [Free & Pro](../plans/index.fr.md).*


## Le problème

Les entreprises font tourner une **multitude d'applications à usage unique**
pour enregistrer des données tout au long de leurs étapes de processus — un
outil par cas d'usage, chacun conçu isolément. Trois défaillances en découlent.

### Qualité incohérente

Chaque application valide ses entrées différemment (ou pas du tout), si bien que
les données qui parviennent aux systèmes en aval sont hétérogènes et difficiles
à exploiter en confiance.

### Pas adapté à la mobilité

Une grande partie de cette saisie se fait encore au bureau — pas là où le
travail a réellement lieu.

### Aucun contexte de localisation

Presque rien n'est géoréférencé : un enregistrement indique rarement **où** se
trouve réellement l'objet qu'il décrit.

---

### En bref

| Difficulté en entreprise | |
| --- | --- |
| Multiples applications de saisie à usage unique | une nouvelle compilation par cas d'usage |
| Qualité de données incohérente | chaque application valide différemment |
| Pas adapté à la mobilité | la saisie se fait au bureau |
| Aucun contexte de localisation | les enregistrements n'indiquent pas *où* |
| Infrastructure / charge informatique lourde | un backend et une gestion de parc par outil |
| Accès non encadré | aucune règle cohérente sur qui peut saisir quoi |

[:octicons-arrow-right-24: Comment Hecate supprime chacun de ces points](#ce-que-fait-hecate-capture)

## Ce que fait Hecate Capture

Hecate résorbe cette dispersion en **une seule** application configurable — et
corrige les données là où elles naissent, au lieu de le faire après coup.

### Une application, définie par des profils

Le dialogue de saisie de chaque cas d'usage n'est **pas programmé** — c'est un
**profil** : un petit document qui déclare les étapes, les champs et les modes
de saisie autorisés, distribué aux appareils via un topic MQTT. Changez de
profil et la même application sert un nouveau cas d'usage, sans nouvelle
compilation.

### Validé à la source

Chaque champ est vérifié par rapport au format déclaré **au moment de la
saisie**, de sorte que les données erronées sont arrêtées là où elles naissent
plutôt que nettoyées en aval.

### La bonne saisie pour chaque étape

Les étapes d'un profil décident **ce qui** est saisi ; chaque étape choisit le
mode de saisie adapté à la tâche :

- **Saisie manuelle.** Tapez la valeur directement dans le champ.
- **Scan par caméra.** Pointez la caméra de l'appareil et laissez les
  frameworks de scan embarqués lire **les QR codes, les codes Data Matrix 2D
  et les codes-barres 1D** — sans aller-retour réseau ni service tiers.

Quel que soit le mode utilisé par une étape, la valeur passe par la **même
chaîne de validation et de saisie**, de sorte qu'un profil se comporte de façon
identique quelle que soit la provenance des données.

### Les briques

| Brique | Saisie | Champ produit |
|---|---|---|
| Scanner un code QR | Code QR par caméra | Texte, motif vérifiable en option |
| Scanner un code-barres | Code-barres 1D (EAN, Code 128, …) | Texte, motif vérifiable en option |
| Scanner un code 2D matriciel | Data Matrix par caméra | Texte, motif vérifiable en option |
| Saisir une quantité | Saisie numérique | Nombre |
| Cocher une liste d'état | Cases à cocher — plusieurs possibles | Sélection multiple |
| Choisir un motif | Boutons radio — exactement un | Choix (exactement un) |
| Saisir du texte | Texte libre, une ligne | Texte |
| Laisser un commentaire | Texte libre, multiligne | Texte, multiligne |

### Toujours géoréférencé

Chaque enregistrement porte un **point GPS** et est transmis au broker dans une
enveloppe uniforme et auto-descriptive.

### Une gouvernance avec quasiment aucune infrastructure

Il ne faut qu'un **broker MQTT et l'application** — aucun backend à exploiter,
aucune inscription à une gestion de parc. L'autorité réside dans les permissions
du broker : un administrateur publie des profils conservés (retained) ; un
utilisateur ne voit que les profils que ses identifiants l'autorisent à lire, et
saisit à partir de ceux-ci.

Parce que toutes les personnes travaillant sur un cas d'usage remplissent le
**même profil validé**, les données arrivent cohérentes, comparables et prêtes à
l'emploi — par conception, et non par nettoyage a posteriori.

---

### Comment elle supprime chaque difficulté

| Difficulté en entreprise | Comment Hecate la supprime |
| --- | --- |
| Multiples applications de saisie à usage unique | Une application ; chaque cas d'usage est un profil, pas une nouvelle compilation |
| Qualité de données incohérente | Validation de format champ par champ, bloquée à la saisie |
| Pas adapté à la mobilité | Une application iOS de terrain, utilisée là où le travail a lieu |
| Aucun contexte de localisation | Chaque enregistrement porte un point GPS |
| Infrastructure / charge informatique lourde | Broker + application uniquement ; profils livrés en messages MQTT conservés |
| Accès non encadré | Les permissions du broker décident qui peut lire quels profils |

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
