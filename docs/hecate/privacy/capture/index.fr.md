# Politique de confidentialité — Hecate

**Date d'entrée en vigueur :** 11/06/2026
**Développeur :** Matthias Morath

Hecate est un outil de terrain pour le géoréférencement d'objets physiques. Il ne
collecte que ce qui est nécessaire pour identifier et localiser les assets que
vous enregistrez. Il n'existe **aucun backend exploité par le développeur** et
**aucun service d'analytique ou de suivi tiers**, d'aucune sorte.

## Ce que nous collectons

Ce que l'application saisit est **entièrement défini par le profil** que
l'administrateur de votre organisation configure — un profil est un formulaire
personnalisable décrivant les champs et les scans d'un cas d'usage. **En tant que
développeur, nous ne créons pas ces profils et ne voyons ni les profils que vous
utilisez ni les données que vous saisissez à partir d'eux.** Ce qu'une
installation donnée collecte est donc décidé par *votre* administrateur, pas par
nous.

Pour un profil typique, l'application traite :

- **Les données de l'asset** que vous saisissez ou scannez (p. ex. numéro de
  série, numéro de commande, type).
- **Une photo facultative** de l'asset, si vous choisissez d'en prendre une.
- **La localisation précise (GPS)** au moment de la saisie — *uniquement si vous
  accordez l'autorisation de localisation*. Vous pouvez la refuser ou la révoquer
  à tout moment dans les Réglages iOS ; l'application fonctionne aussi sans.

## Où vont les données

Les données des assets sont publiées **uniquement vers le broker MQTT que vous
configurez**. Vous choisissez et contrôlez ce broker. Le développeur n'exploite
aucun serveur, ne reçoit aucune de vos données et ne voit ni les profils que vous
utilisez ni les assets que vous saisissez à partir d'eux. Il n'y a aucune
publicité, aucun profilage, ni aucun suivi inter-applications ou inter-sites.

## Stockage et sécurité

- Les assets sont stockés **sur votre appareil** jusqu'à ce que vous les
  supprimiez.
- Le **mot de passe du broker est conservé dans le trousseau iOS** — jamais en
  clair et jamais écrit dans les journaux.
- Les connexions au broker peuvent utiliser **TLS** (`mqtts`), afin que les
  données en transit soient chiffrées.

## Partage de données

Nous ne **vendons, ne louons ni ne partageons vos données** avec des tiers. La
seule transmission est la publication vers **votre propre** broker MQTT, effectuée
pour votre compte et à votre demande.

## Vos choix

- **Localisation :** accordez, refusez ou révoquez à tout moment dans
  Réglages iOS → Confidentialité.
- **Photos :** entièrement facultatives, par asset.
- **Suppression :** supprimez n'importe quel asset sur l'appareil à tout moment.
  Les données déjà publiées vers votre broker relèvent de la politique de
  conservation de *votre* broker.

## Enfants

Hecate est un utilitaire professionnel / de terrain et ne s'adresse pas aux
enfants.

## Modifications de cette politique

Si le traitement des données de l'application change, cette page et l'écran
intégré **Réglages → Confidentialité** seront mis à jour conjointement.
