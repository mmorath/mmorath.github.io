# Politique de confidentialité — Leaf Relief

**Date d’effet :** 2026-10-21
**Développeur :** Matthias Morath

Leaf Relief est une app Mac pour une archive sans papier. Elle traite vos documents
**entièrement sur votre Mac**.

## Ce que nous collectons

**Rien.** L’app n’a **aucun backend**, **aucun compte**, et ne contient **aucun outil
d’analyse, aucune publicité ni aucun pistage**. Le développeur ne reçoit aucune donnée
de l’app. Les informations de confidentialité de l’app sur l’App Store indiquent donc
**« Données non collectées »**.

## Ce que l’app traite, sur votre Mac

- **Les documents** du dossier d’archive et du dossier d’entrée que vous choisissez.
  L’app s’exécute dans le bac à sable (App Sandbox) de macOS : elle ne peut ouvrir que
  les dossiers que vous avez choisis, et elle mémorise cette autorisation (sous forme
  de signet).
- **Les numérisations** d’un scanner que vous choisissez (USB, ou AirScan sur votre
  réseau local). Les images des pages restent 14 jours dans le cache de l’app, afin
  qu’une étape qui a échoué puisse être répétée.
- **La reconnaissance de texte** avec le framework Vision d’Apple, sur votre Mac.
- **Les suggestions** (type, expéditeur, date, montant, échéance …) avec Apple
  Intelligence, sur l’appareil. Aucun texte n’est envoyé à un modèle dans le cloud.
- **La recherche**, avec un index dans le conteneur de l’app (SQLite, avec le
  plongement de phrases d’Apple pour la recherche par le sens).
- **Spotlight :** titres, expéditeurs, types, mots-clés et texte figurent dans l’index
  Spotlight de ce Mac.
- **Les rappels** pour les échéances ne sont créés que lorsque vous cliquez sur
  « Créer un rappel » ; macOS demande l’autorisation une seule fois.
- **Le journal des modifications :** les modifications des documents sont signées avec
  une clé de la Secure Enclave de ce Mac et consignées dans l’index et sur le fichier.

## Réseau

- **Les scanners de votre réseau local** (AirScan) sont trouvés via Bonjour ; macOS
  demande l’autorisation d’accès au réseau local.
- **Horodatages (facultatifs, désactivés par défaut) :** si vous les activez, seule une
  empreinte (SHA-256) de chaque entrée du journal des modifications est envoyée au
  service d’horodatage freetsa.org — jamais le contenu d’un document.

L’app n’établit aucune autre connexion.

## Partage

Un document ou le journal ne quitte votre Mac que si vous le partagez vous-même
(« Partager », « Envoyer par e-mail »). La copie ne porte ni mots-clés ni types. Le
journal contient des étapes et des noms de fichier, aucun contenu de document ; votre
dossier personnel, vos adresses e-mail et vos clés sont remplacés lors de l’export.

## Suppression

Lorsque vous supprimez l’app, macOS supprime son conteneur (index, réglages, cache).
Vos documents dans le dossier d’archive restent où ils sont.

## Contact

Questions : `kubisch-gemacht3p@icloud.com`

---

[Leaf Relief](../index.md) · [Assistance](../support/index.md)
