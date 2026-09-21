# Politique de confidentialité — Hecate Admin

**Date d'effet :** 18/06/2026
**Développeur :** Matthias Morath

Hecate Admin est un **outil d'édition**. Il sert à créer et publier les
**profils** qui configurent l'application de saisie, et à établir la connexion
à votre broker MQTT. Ce n'est pas une application de collecte de données.

## Ce que nous collectons

**Aucune télémétrie et aucune donnée personnelle.** L'application admin :

- ne demande **aucune position** et n'a **pas de caméra** ;
- n'exécute **aucune analyse, publicité ou suivi de tiers** ;
- n'envoie **rien** au développeur — il n'existe **aucun backend hébergé**.

## Ce qu'elle manipule

- **Les profils que vous rédigez.** Un profil décrit les champs et les étapes
  d'un flux de saisie. Les profils sont de la **configuration, pas des
  données personnelles**, et **ne doivent contenir aucun secret** — ils sont
  largement lisibles par les appareils qui s'y abonnent.
- **Les identifiants du broker.** Pour publier des profils, l'application se
  connecte à **votre** broker MQTT avec des identifiants admin. Le mot de
  passe est conservé dans le **trousseau** de la plateforme — jamais en
  clair, jamais écrit dans un profil, un QR de configuration ou un journal,
  et jamais transmis ailleurs que pour s'authentifier auprès de votre broker.

## Où vont les données

La seule destination réseau est le **broker MQTT que vous configurez**.
L'application admin y publie des profils (en messages retenus) à votre
demande. Elle ne transmet rien au développeur ni à des tiers ; il n'y a ni
publicité, ni profilage, ni suivi inter-applications.

## Stockage et sécurité

- Les profils et réglages de connexion sont stockés **sur votre appareil**.
- Le **mot de passe du broker est conservé dans le trousseau**.
- Les connexions au broker peuvent utiliser **TLS** (`mqtts`) pour chiffrer
  les données en transit.

## Vos choix

- **Identifiants :** stockés uniquement sur l'appareil ; supprimables à tout
  moment.
- **Profils :** vous les rédigez, les publiez et les retirez ; retirer un
  profil efface son message retenu sur votre broker.

## Rapports de diagnostic que vous nous envoyez

Il y a exactement une exception à tout ce qui précède, et la décision vous
revient à chaque fois : dans **Réglages → Journal d'événements**, vous pouvez
nous **envoyer** un rapport si vous souhaitez de l'aide. Cela n'arrive jamais
tout seul.

- Vous voyez le rapport **complet** avant qu'il ne quitte l'appareil — rien
  n'est ajouté après cet écran.
- Vous décidez **à chaque fois**.
- Vous l'envoyez depuis **votre propre application de messagerie**. L'app
  n'envoie rien en arrière-plan ; il n'existe aucun serveur à nous auquel elle
  pourrait envoyer quoi que ce soit.
- Il contient : appareil et version du système, version de l'app et du noyau,
  votre formule (free/pro) et des lignes de journal. **Jamais** de photos, de
  positions, de mots de passe, de jetons ni d'identifiants du broker — les
  motifs correspondants sont remplacés avant l'envoi.
- Un **commentaire** et une **adresse de réponse** sont facultatifs. Nous
  utilisons l'adresse uniquement pour répondre à ce rapport.

Si vous préférez garder le rapport ou le donner à votre propre service
informatique : « Partager … » sur le même écran vous le remet sous forme de
fichier texte, sans que nous en voyions quoi que ce soit.

## Enfants

Hecate est un utilitaire professionnel et ne s'adresse pas aux enfants.

## Modifications de cette politique

Si le traitement des données de l'application change, cette page et l'écran
de confidentialité intégré seront mis à jour ensemble.
