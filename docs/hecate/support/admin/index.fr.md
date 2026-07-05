# Assistance — Hecate Admin

Aide pour les **administrateurs** qui rédigent et publient des profils Hecate.
(Vous utilisez plutôt l'application de saisie ou un viewer ? Voir
[l'assistance opérateurs](../operator/index.md).)

## Contact

!!! note "Adresse de contact"
    **E-mail :** _à confirmer avant la soumission._

Lorsque vous signalez un problème, il est utile d'indiquer :

- votre **appareil** et votre **version d'iOS**,
- la **version de l'application** (Réglages → À propos),
- le broker vers lequel vous publiez (hôte / TLS, **jamais** le mot de
  passe),
- ce que vous avez fait et ce que vous attendiez.

## Sujets fréquents

### Connexion au broker
L'application admin se connecte au **broker MQTT que vous configurez**, en
**TLS** (`mqtts`), avec des identifiants admin. Le mot de passe n'est stocké
que dans le **trousseau** de l'appareil.

### Rédiger un profil
Un profil déclare les **étapes**, les **champs**, les règles de saisie et une
couleur d'accent propre au profil. Chaque champ peut porter un motif de
validation ; l'application admin vérifie un profil avant sa publication, pour
que l'application de saisie n'en reçoive jamais un qu'elle rejetterait.

### Publication & versionnage
Les profils sont publiés en messages **retenus**, si bien que les appareils
qui se connectent plus tard les reçoivent quand même. Toute modification
significative doit être publiée sous une **version strictement supérieure** —
les appareils n'appliquent un profil que si sa version est plus récente que
celle qu'ils détiennent. Pour « revenir en arrière », republiez l'ancien
contenu sous une **nouvelle version supérieure** ; ne réutilisez ni ne
diminuez jamais un numéro.

### Retirer un profil
Pour retirer un profil des appareils, **effacez son message retenu** (publiez
une charge utile retenue vide sur son topic). Les appareils le suppriment à
leur prochaine réconciliation.

### Identifiants & secrets
Les profils sont largement lisibles : ils **ne doivent donc contenir aucun
secret**. Le mot de passe du broker vit dans le trousseau et n'est jamais
écrit dans un profil, un QR de configuration ou un journal.

---

Voir aussi la [politique de confidentialité de l'admin](../../privacy/admin/index.md).
