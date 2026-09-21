# Politique de confidentialité — Hecate Capture

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
- **Photos :** aucune. Hecate Capture **ne peut pas** prendre de photo — la capacité a
  été supprimée, pas désactivée : une photo ne peut pas voyager vers un broker MQTT et
  Hecate n'exploite aucun backend d'images. Lire un QR code *depuis* une photo que vous
  choisissez est autre chose : l'image est décodée sur l'appareil, jamais stockée ni envoyée.
- **Suppression :** supprimez n'importe quel asset sur l'appareil à tout moment.
  Les données déjà publiées vers votre broker relèvent de la politique de
  conservation de *votre* broker.

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

Hecate est un utilitaire professionnel / de terrain et ne s'adresse pas aux
enfants.

## Modifications de cette politique

Si le traitement des données de l'application change, cette page et l'écran
intégré **Réglages → Confidentialité** seront mis à jour conjointement.
