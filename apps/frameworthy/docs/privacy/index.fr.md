# Politique de confidentialité — Frameworthy

**Date d’effet :** 2026-10-20
**Développeur :** Matthias Morath

Frameworthy est une app pour Mac qui traite les vidéos que vous y ouvrez —
**entièrement sur votre Mac**.

!!! note "En bref"
    Pas de compte, pas de serveur, pas d’analyse, pas de publicité, pas de
    pistage. Vos vidéos, votre son et vos textes ne quittent jamais votre Mac. La
    seule connexion réseau propre à l’app est le téléchargement unique des
    modèles des intervenants depuis Hugging Face, et il ne contient aucune donnée
    d’utilisateur.

## Ce que nous collectons

**Rien.** L’app n’a **aucun backend**, n’envoie de données à **aucun serveur** et ne
contient **ni analyse, ni publicité, ni pistage**. Le développeur ne reçoit aucune
donnée de l’app.

## Ce que l’app traite, sur votre Mac

- **Les vidéos que vous ouvrez** — lues sur le disque, converties et écrites dans le
  dossier de sortie que vous choisissez (par défaut : `~/Movies/Frameworthy`). L’app
  s’exécute dans l’App Sandbox de macOS : elle ne peut ouvrir que les fichiers et
  dossiers que vous choisissez, et elle mémorise cette autorisation pour que les
  vidéos en file d’attente continuent après un redémarrage.
- **Le texte parlé** — reconnu avec la reconnaissance vocale d’Apple sur l’appareil.
  Le son ne quitte jamais votre Mac. macOS peut télécharger une fois un modèle vocal
  pour la langue choisie ; ce téléchargement ne contient aucune donnée d’utilisateur.
- **Les corrections et les titres de chapitres** — produits sur l’appareil par Apple
  Intelligence. Aucun texte n’est envoyé à un modèle dans le cloud.
- **Les traductions** — sur l’appareil avec le framework Translation d’Apple ; macOS
  peut télécharger une fois des packs de langue, après votre confirmation.
- **Les intervenants** — distingués sur l’appareil. Les modèles des intervenants sont
  téléchargés une fois depuis Hugging Face (`FluidInference/speaker-diarization-coreml`) ;
  ce téléchargement n’envoie aucune donnée d’utilisateur. C’est la seule connexion
  réseau que l’app établit elle-même.
- **Les transcriptions, sous-titres et chapitres** — enregistrés à côté de vos vidéos
  converties.

## Ce que l’app conserve

Tout reste dans le conteneur de l’app sur votre Mac
(`~/Library/Containers/com.mmorath.frameworthy`) : vos réglages, la file d’attente et
un fichier journal local contenant des chemins de fichiers et des détails de
traitement. Rien de tout cela n’est téléversé. Supprimer l’app supprime le conteneur.

## Partage

Aucun. L’app ne partage aucune donnée avec le développeur ni avec des tiers.

## Enfants

L’app ne collecte de données auprès de personne, y compris des enfants.

## Modifications

Si le traitement des données par l’app change, cette page est mise à jour et la date
d’effet change.

## Contact

Voir [Assistance](../support/index.fr.md).
