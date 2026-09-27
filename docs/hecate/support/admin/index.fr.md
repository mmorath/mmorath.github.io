# Assistance — Hecate Admin

Aide pour les **administrateurs** qui rédigent et publient des profils Hecate.
(Vous utilisez plutôt l'application de saisie ou un viewer ? Voir
[l'assistance opérateurs](../operator/index.md).)

## Contact

!!! note "Adresse de contact"
    **E-mail :** [info@hecateapps.com](mailto:info@hecateapps.com)

Lorsque vous signalez un problème, il est utile d'indiquer :

- votre **appareil** et votre **version d'iOS**,
- la **version de l'application** (Réglages → À propos),
- le broker vers lequel vous publiez (hôte / TLS, **jamais** le mot de
  passe),
- ce que vous avez fait et ce que vous attendiez.

## Nous envoyer le journal des événements

Depuis la **version 2.0.0**, Hecate Admin tient un **journal des événements** —
connexions au broker, résultats de publication, erreurs de validation — sous
**Réglages → Diagnostics → Journal des événements**. Il contient déjà
l'appareil, la version d'iOS et celle de l'app, et remplace ainsi l'essentiel
de la liste ci-dessus.

<div class="shots">
  <figure><img src="/assets/screens/fr/support-admin-settings-row.png" alt="Les réglages de Hecate Admin avec la ligne Journal des événements dans le groupe Diagnostics"><figcaption>Réglages → Journal des événements</figcaption></figure>
  <figure><img src="/assets/screens/fr/support-admin-event-log.png" alt="Le journal des événements dans Hecate Admin : entrées horodatées, avec en haut Actualiser, Partager et Envoyer à Hecate"><figcaption>Le journal des événements</figcaption></figure>
  <figure><img src="/assets/screens/fr/support-send-dialog.png" alt="La boîte de dialogue Envoyer le journal à Hecate ? avec Oui et Annuler"><figcaption>Envoyer à Hecate → Oui</figcaption></figure>
  <figure><img src="/assets/screens/fr/support-share-sheet.png" alt="La feuille de partage du système avec le journal joint en fichier texte"><figcaption>Partager … en fichier texte</figcaption></figure>
</div>

- :material-send-outline: **Envoyer à Hecate** ouvre un brouillon d'e-mail pour
  [info@hecateapps.com](mailto:info@hecateapps.com) — vous voyez tout ce qu'il
  contient et l'envoyez vous-même (visible seulement si un compte de messagerie
  est configuré).
- :material-export-variant: **Partager le journal** transmet le rapport à la
  feuille de partage en fichier texte — pour AirDrop, Fichiers ou votre service
  informatique.

Les mots de passe et identifiants sont remplacés avant la création du rapport.
Les trois premiers écrans viennent de Hecate Admin, la feuille de partage de
l'app de capture. Le
guide complet se trouve dans le
[support opérateurs](../operator/index.md#nous-envoyer-le-journal-des-evenements).

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
