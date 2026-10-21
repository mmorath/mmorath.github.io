---
hide:
  - toc
---

# Leaf Relief

*Une archive sans papier pour votre Mac*

**Bientôt sur le Mac App Store.**

Leaf Relief transforme le papier en archive consultable – sans compte, sans cloud,
**entièrement sur votre Mac**. Numérisez vos papiers ou déposez des fichiers dans
un dossier d’entrée : l’app reconnaît le texte, classe chaque document sous le nom
que vous choisissez, propose titre, type, expéditeur, date, montant et mots-clés,
et retrouve tout – en texte intégral, en langage naturel ou par le sens.

## En une minute

- **Numériser ou importer.** Les scanners AirScan du réseau et les scanners USB
  dotés d’un pilote macOS numérisent directement dans l’app ; tout autre scanner,
  téléchargement ou photo passe par le dossier d’entrée.
- **Des PDF consultables.** Les pages sont redressées, le texte est reconnu et
  ajouté au PDF comme couche consultable.
- **Classé à votre façon.** Des fichiers PDF ordinaires dans votre propre dossier,
  rangés selon les sous-dossiers et noms de fichier que vous définissez ; mots-clés
  et types comme tags du Finder.
- **Suggestions sur l’appareil.** Apple Intelligence propose type, expéditeur,
  titre, date, montant, échéance, IBAN et mots-clés – sur votre Mac. Rien n’est
  repris tant que vous ne cliquez pas.
- **Retrouvé.** Texte intégral, langage naturel (« factures de l’an dernier de plus
  de 100 € »), recherche par le sens, Spotlight et Raccourcis.
- **Preuve.** Chaque classement et chaque modification de page est journalisé et
  signé avec une clé de la Secure Enclave.
- **Ni compte, ni cloud, ni pistage.** Le développeur ne reçoit aucune donnée de
  l’app.

## Captures d’écran

<div class="shots">
  <figure class="wide"><img src="/leafrelief/assets/screens/en/light.png" alt="Leaf Relief en mode clair : barre latérale avec boîte d’entrée, types et mots-clés, liste des documents de démonstration, aperçu d’une facture aux champs surlignés et suggestions de type, d’expéditeur et de mots-clés"><figcaption>Clair</figcaption></figure>
  <figure class="wide"><img src="/leafrelief/assets/screens/en/dark.png" alt="Leaf Relief en mode sombre : l’archive avec des documents de démonstration, l’aperçu et des suggestions de type, d’expéditeur et de mots-clés"><figcaption>Sombre</figcaption></figure>
</div>

*Les captures montrent une archive de démonstration aux documents fictifs, avec
l’interface en anglais.*

## Le problème

Chaque semaine arrive du papier – factures, contrats, fiches de paie, courriers des
impôts –, et la plupart doit être conservée pendant des années.

### Des piles de papier

Classeurs et cartons se remplissent. Retrouver le courrier de l’assurance de l’an
dernier, c’est tous les feuilleter.

### Des PDF dispersés

Ce qui est déjà numérique traîne dans Téléchargements, sur le bureau et dans les
pièces jointes, sous des noms comme `scan0042.pdf`.

### Aucune recherche

Une page numérisée n’est qu’une image. Sans couche de texte, ni le Finder ni
Spotlight n’y trouvent un seul mot.

### Des services cloud qui lisent vos documents

Beaucoup de services d’archivage règlent cela en téléversant vos documents et en
les analysant sur leurs serveurs – relevés bancaires, courriers médicaux et
contrats compris.

---

### En bref

| Problème | |
| --- | --- |
| Piles de papier | retrouver un courrier, c’est fouiller chaque classeur |
| PDF dispersés | des fichiers partout, aux noms sans signification |
| Aucune recherche | les pages numérisées sont des images sans texte |
| Classement à la main | chaque document demande un nom, un dossier et des mots-clés |
| Services cloud | vos documents les plus privés finissent sur le serveur d’un autre |

[:octicons-arrow-right-24: Comment Leaf Relief résout chacun de ces points](#ce-que-fait-leaf-relief)

## Ce que fait Leaf Relief

Leaf Relief couvre tout le chemin du papier à l’archive consultable dans une seule
app Mac – et garde chaque étape sur votre Mac.

### Numériser ou importer

- **Numériser** avec les scanners AirScan du réseau et les scanners USB dotés d’un
  pilote macOS – ceux que macOS connaît lui-même. Le chargeur avant la vitre,
  recto verso si le chargeur le permet, 300 dpi, mode couleur *Automatique* : les
  pages sans couleur notable sont enregistrées en niveaux de gris.
- **Suivre chaque étape** : Numérisation → Texte → Classement → Index, avec le
  nombre de pages. Vous pouvez annuler à tout moment.
- **Importer** depuis le dossier d’entrée : tout autre scanner, téléchargement ou
  photo – déposez-le, Leaf Relief le classe. PDF, JPEG, PNG, HEIC et TIFF sont
  acceptés ; les PDF qui contiennent déjà du texte sont repris tels quels, les
  images et les PDF uniquement image reçoivent une couche de texte.
- **La reconnaissance de texte** utilise le framework Vision d’Apple, en français,
  anglais, allemand et espagnol. Les pages sont d’abord redressées ; la couche de
  texte invisible se superpose exactement à l’image, si bien que sélectionner et
  copier dans Aperçu tombe sur le bon mot.

### Classer à votre façon

- **Sous-dossiers** par année, par année et mois, par type, ou par année et type –
  ou aucun.
- **Noms de fichier** à partir de la date, du type, d’un suffixe et du nombre de
  pages ; un nom qui existe déjà reçoit `-2`, `-3` …
- **Des fichiers PDF ordinaires** dans votre propre dossier. Mots-clés et types sont
  des tags du Finder, les champs voyagent avec le fichier. L’index de l’app n’est
  qu’un index – la source, c’est le PDF.
- **Vos propres types** avec nom, couleur et symbole, à côté de ceux fournis.

### Suggestions sur l’appareil

- **Apple Intelligence** lit le document et propose type, expéditeur, titre, date,
  montant, échéance, référence de dossier, IBAN, un résumé et des mots-clés – sur
  votre Mac, dans la langue du document. Aucun texte n’est envoyé à un modèle
  dans le cloud.
- **Sans Apple Intelligence**, des règles simples proposent ce qu’elles peuvent :
  dates, montants, IBAN avec clé de contrôle, numéros de client, de facture et de
  contrat, et formes juridiques comme GmbH, Ltd ou Inc. Ces règles comprennent les
  documents en allemand et en anglais.
- **Vous décidez.** Les suggestions sont enregistrées, jamais reprises d’elles-mêmes.
  Les champs reconnus sont surlignés dans l’aperçu ; un clic suffit pour les
  reprendre.

### Retrouver

- **Texte intégral** dans toute l’archive.
- **Langage naturel** – une phrase comme « factures de l’an dernier de plus de
  100 € » devient des filtres de type, d’expéditeur, de période et de montant.
- **Recherche par le sens**, quand vous savez de quoi parlait un document mais plus
  ses mots. La recherche par le sens comprend le français, l’espagnol,
  l’allemand et l’anglais ; la recherche en langage naturel, l’allemand et l’anglais.
- **Spotlight** trouve aussi vos documents ; un résultat ouvre le document dans
  l’app.
- **Raccourcis et Siri** : « Numériser un document », « Rechercher un document »,
  « Ouvrir le dernier scan ».
- **Les fichiers présents uniquement dans iCloud** ne sont pas téléchargés ; ils
  sont indexés d’après leur nom, leurs champs et leurs mots-clés.

### Preuve : un journal des modifications signé

- **Chaque classement, import et modification de page** – y compris les
  modifications faites hors de l’app, par exemple dans Aperçu – est enregistré
  comme maillon d’une chaîne de hachage et signé avec une clé de la Secure Enclave
  de ce Mac.
- **Un sceau** sur chaque document indique ce qui est établi : *Inchangé depuis la
  numérisation*, *Modifié (n×), chaîne valide* ou *Échec de la vérification* avec
  la raison.
- **Exportez** un rapport de vérification et la clé publique.
- **Horodatages (facultatifs, désactivés par défaut)** : une fois activés, seule
  une empreinte (SHA-256) de chaque entrée part vers un service d’horodatage –
  jamais le document.

### Modifier les pages

- **Faire pivoter, déplacer et supprimer des pages** – avec annulation.
- **L’original est conservé.** Chaque modification est reconstruite à partir de
  l’original, si bien que les pages supprimées peuvent revenir.
- **Corriger l’orientation automatiquement** redresse les pages de travers avec la
  même reconnaissance que lors de la numérisation.

### Échéances et partage

- **Échéances comme rappels** – créés uniquement quand vous cliquez sur « Créer un
  rappel ».
- **Partager et envoyer par e-mail** une copie nommée d’après le titre, sans vos
  mots-clés ni vos types privés.
- **Une icône dans la barre des menus** affiche la numérisation, la progression et
  le nombre de documents en entrée.

---

### Comment Leaf Relief résout chaque point

| Problème | Comment Leaf Relief le résout |
| --- | --- |
| Piles de papier | Numérisation avec le scanner que macOS connaît déjà, directement dans l’archive |
| PDF dispersés | Un dossier d’entrée pour tout le reste ; classement automatique |
| Aucune recherche | Une couche de texte dans chaque PDF ; texte intégral, langage naturel et sens |
| Classement à la main | Dossiers et noms selon votre modèle ; suggestions de type, d’expéditeur et de mots-clés |
| Services cloud | Reconnaissance, suggestions et recherche sur votre Mac ; ni compte, ni serveur |

## Confidentialité

Leaf Relief n’a **ni backend, ni compte, ni outil d’analyse, ni publicité, ni
pistage**. Vos documents restent dans les dossiers que vous choisissez ; ils ne
quittent votre Mac que si vous les partagez vous-même. Détails dans la
[politique de confidentialité](privacy/index.md).

## Configuration requise

- macOS 26 ou version ultérieure sur un Mac avec puce Apple.
- Pour les suggestions d’Apple Intelligence : Apple Intelligence activé. Sans elle,
  des règles simples font des suggestions.
- Un scanner est facultatif : AirScan sur le réseau ou USB avec pilote macOS ; tout
  autre scanner passe par le dossier d’entrée.
- En français, anglais, allemand et espagnol. Les règles simples et la recherche en
  langage naturel comprennent les documents en allemand et en anglais.
- Leaf Relief produit des PDF standard avec une couche de texte consultable – pas
  de PDF/A.
- Achat unique, sans achats intégrés. Bientôt sur le Mac App Store.

---

[Politique de confidentialité](privacy/index.md) · [Assistance](support/index.md)
