# Politique de confidentialité — Hecate Viewer TV

**Date d'entrée en vigueur :** 24/08/2026
**Développeur :** Matthias Morath

Hecate Viewer TV est un **affichage**. L'app fonctionne sur un Apple TV, se
connecte à un broker MQTT que vous configurez et **affiche** sur un mur en direct
les actifs qui y sont publiés. C'est un abonné, pas un capteur.

## Ce que nous collectons

**Rien.** L'app :

- n'a **pas d'appareil photo** et ne capture aucune image ;
- n'a **aucun accès à la photothèque** et ne lit aucun de vos médias ;
- ne demande **aucune position** et n'enregistre aucune donnée GPS — un Apple TV
  ne se déplace pas, donc le mur affiche les positions enregistrées par votre app
  de *capture* et ne demande rien au téléviseur ;
- n'a **aucun compte utilisateur** et ne demande aucune information personnelle ;
- n'utilise **aucun service tiers d'analyse, de publicité ou de suivi** ;
- ne contient **aucun SDK de rapport de plantage**.

Il n'existe **aucun backend exploité par le développeur**. Le développeur ne
reçoit aucune de vos données.

## Les deux choses avec lesquelles elle communique

Voici la totalité de l'activité réseau de l'app :

1. **Votre réseau local, une fois, pour la configuration.** Saisir du texte avec
   une télécommande est pénible : le téléviseur ne saisit donc jamais rien. Il
   affiche un code QR et attend sur votre réseau local que **Hecate Viewer sur
   votre iPhone ou iPad** lui transmette la configuration du broker. tvOS vous
   demande l'autorisation d'accès au réseau local la première fois ; le transfert
   est chiffré, circule uniquement entre vos deux appareils et n'atteint aucun de
   nos serveurs. La configuration — identifiants du broker inclus — va
   directement dans le trousseau de l'appareil.
2. **Votre broker MQTT, pour s'abonner.** Ensuite l'app **lit** depuis le broker
   que vous lui avez indiqué, et rien d'autre.

## Ce qu'elle affiche

L'app **s'abonne** à votre broker et affiche les données d'actifs qu'elle reçoit
— les objets, leurs champs capturés et les informations de position ou de profil
que le broker détient déjà. Ces données sont créées ailleurs (par l'app de
capture) et régies entièrement par **votre** broker et ses autorisations. Les
actifs reçus sont conservés **en mémoire uniquement** ; quitter l'app les efface.

## Où vont les données

Nulle part de nouveau. L'app se contente de **lire** depuis votre broker. Elle ne
publie jamais, n'écrit jamais et ne transmet aucune donnée au développeur ni à un
tiers.

## Stockage et sécurité

- L'app ne conserve que les **paramètres de connexion au broker** avec lesquels
  elle a été jumelée, afin de se reconnecter après une coupure de courant sans
  être jumelée à nouveau, plus un cache des **documents de profil** du broker
  (descriptions de workflow et leurs couleurs, sans donnée personnelle).
- Le mot de passe du broker est conservé dans le **trousseau de l'appareil**,
  jamais en clair et jamais dans les journaux. Les journaux de diagnostic restent
  sur l'appareil et ne notent que la *longueur* des valeurs sensibles, jamais leur
  contenu.
- Les connexions au broker peuvent utiliser **TLS** (`mqtts`), de sorte que les
  données en transit sont chiffrées.
- Le seul autre état stocké est une préférence d'affichage — le profil ou la zone
  auquel le mur est restreint — dans les réglages propres à l'app.

## Vos choix

- L'**accès au réseau local** peut être refusé ou révoqué à tout moment dans les
  réglages tvOS. À noter : le jumelage est le seul mode de configuration de
  l'app ; le refuser laisse le mur sans rien à afficher.
- Jumelez à nouveau l'Apple TV à tout moment pour le diriger vers un autre
  broker. Les données d'actifs affichées sont régies par les règles de
  conservation et d'accès de **votre** broker.

## Enfants

Hecate est un utilitaire professionnel/de terrain et ne s'adresse pas aux
enfants.

## Modifications de cette politique

Si le traitement des données de l'app change, cette page sera mise à jour.

---

[:octicons-arrow-right-24: L'app Apple TV](../../viewer-tvos/index.md) ·
[:octicons-arrow-right-24: Assistance](../../support/operator/index.md)
