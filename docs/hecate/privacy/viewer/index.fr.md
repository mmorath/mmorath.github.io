# Politique de confidentialité — Hecate pour Apple TV

**Date d'effet :** 18/06/2026
**Développeur :** Matthias Morath

L'application Hecate pour Apple TV est un **viewer en lecture seule**. Elle se
connecte à un broker MQTT que vous configurez et **affiche** les actifs qui y
sont publiés. C'est un abonné, pas un capteur.

## Ce que nous collectons

**Rien.** Le viewer :

- n'a **pas de caméra** et ne capture aucune image ;
- ne demande **aucune position** et n'enregistre aucune donnée GPS ;
- n'a **pas de comptes utilisateurs** et ne demande aucune donnée
  personnelle ;
- n'exécute **aucune analyse, publicité ou suivi de tiers**.

Il n'existe **aucun backend hébergé par le développeur**. Le développeur ne
reçoit aucune de vos données.

## Ce qu'il affiche

L'application **s'abonne** au broker que vous lui indiquez et montre les
données d'actifs reçues — les objets, leur état et les informations de
position ou de profil que le broker détient déjà. Ces données sont créées
ailleurs (par l'application de saisie) et gouvernées entièrement par **votre**
broker et ses permissions. Le viewer ne les crée pas et ne les stocke pas
durablement ; il affiche le flux en direct pendant qu'il tourne.

## Où vont les données

Nulle part ailleurs. Le viewer ne fait que **lire** votre broker. Il ne publie
jamais, n'écrit jamais et ne transmet aucune donnée au développeur ni à un
tiers.

## Stockage et sécurité

- L'application ne conserve que les **réglages de connexion au broker** que
  vous saisissez sur l'appareil, pour pouvoir se reconnecter. Tout mot de
  passe est conservé dans le trousseau de la plateforme — jamais en clair,
  jamais dans les journaux.
- Les connexions au broker peuvent utiliser **TLS** (`mqtts`) pour chiffrer
  les données en transit.

## Vos choix

Comme le viewer ne collecte rien, il n'y a rien à refuser, exporter ou
supprimer — hormis les réglages de connexion au broker, que vous pouvez
modifier ou retirer de l'appareil à tout moment. Les données affichées
relèvent des règles de rétention et d'accès de *votre* broker.

## Enfants

Hecate est un utilitaire professionnel et ne s'adresse pas aux enfants.

## Modifications de cette politique

Si le traitement des données de l'application change, cette page sera mise à
jour.
