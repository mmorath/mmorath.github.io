# Politique de confidentialité — Hecate Viewer pour iPad

**Date d'effet :** 05/07/2026
**Développeur :** Matthias Morath

Hecate Viewer est un **moniteur en lecture seule**. Il se connecte à un broker
MQTT que vous configurez et **affiche** les actifs qui y sont publiés. C'est
un abonné, pas un capteur.

## Ce que nous collectons

**Rien.** Le viewer :

- n'exécute **aucune analyse, publicité ou suivi de tiers** ;
- n'a **pas de comptes utilisateurs** et ne demande aucune donnée
  personnelle ;
- n'utilise la **caméra que** lorsque vous choisissez de scanner un QR de
  configuration dans les réglages — aucune image n'est stockée ni transmise ;
- n'utilise votre **position que** pour le point « vous êtes ici » sur la
  carte en direct, *et seulement si vous accordez l'autorisation* — elle
  n'est ni stockée ni transmise. Refusez-la ou révoquez-la à tout moment ; la
  carte perd simplement le point bleu.

Il n'existe **aucun backend hébergé par le développeur**. Le développeur ne
reçoit aucune de vos données.

## Ce qu'il affiche

L'application **s'abonne** au broker que vous lui indiquez et montre les
données d'actifs reçues — les objets, leurs champs saisis et les informations
de position ou de profil que le broker détient déjà. Ces données sont créées
ailleurs (par l'application de saisie) et gouvernées entièrement par **votre**
broker et ses permissions. Les actifs reçus ne sont conservés qu'**en
mémoire** ; quitter l'application les efface. Vous pouvez aussi définir une
durée d'affichage au-delà de laquelle les actifs disparaissent d'eux-mêmes de
l'écran.

## Où vont les données

Nulle part ailleurs. Le viewer ne fait que **lire** votre broker. Il ne publie
jamais, n'écrit jamais et ne transmet aucune donnée au développeur ni à un
tiers.

## Stockage et sécurité

- L'application ne conserve que les **réglages de connexion au broker** que
  vous saisissez (pour se reconnecter), plus un cache des **documents de
  profil** du broker (descriptions de flux de travail, sans données
  personnelles).
- Tout mot de passe est conservé dans le **trousseau iOS** — jamais en clair,
  jamais dans les journaux. Les journaux de diagnostic restent sur l'appareil
  et n'enregistrent des valeurs sensibles que la *longueur*, jamais le
  contenu.
- Les connexions au broker peuvent utiliser **TLS** (`mqtts`) pour chiffrer
  les données en transit.

## Vos choix

- **Position et caméra** peuvent être accordées, refusées ou révoquées à tout
  moment dans les réglages iOS ; les deux sont optionnelles.
- Supprimez une configuration de broker (et son mot de passe du trousseau) à
  tout moment dans les réglages de l'application. Les données affichées
  relèvent des règles de rétention et d'accès de *votre* broker.

## Enfants

Hecate est un utilitaire professionnel et ne s'adresse pas aux enfants.

## Modifications de cette politique

Si le traitement des données de l'application change, cette page sera mise à
jour.
