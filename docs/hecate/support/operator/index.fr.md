# Assistance — Opérateurs (Capture & Viewer)

Aide pour les **opérateurs** sur le terrain : **Hecate Capture** sur
iPhone/iPad et **Hecate Viewer** sur Apple TV. (Vous éditez des profils ou
configurez le broker ? Voir [l'assistance Admin](../admin/index.md).) Un bug
trouvé ou une demande ? Voici comment nous joindre.

## Contact

!!! note "Adresse de contact"
    **E-mail :** [info@hecateapps.com](mailto:info@hecateapps.com)

Le plus simple pour signaler un problème est de **nous envoyer le journal des
événements** (voir ci-dessous) : il contient déjà votre appareil, votre version
d'iOS et la version de l'app. Une phrase sur ce que vous avez fait et ce que
vous attendiez le rend complet.

## Nous envoyer le journal des événements

Depuis la **version 2.0.0**, l'app de capture et Hecate Viewer sur iPhone et
iPad tiennent un **journal des événements** : tentatives de connexion, réponses
du broker, mises à jour de profils, livraisons, erreurs. C'est en général tout
ce qu'il nous faut pour comprendre un problème. Ouvrez-le sous **Réglages →
Diagnostics → Journal des événements**.

<div class="shots">
  <figure><img src="/assets/screens/fr/support-settings-row.png" alt="La liste des réglages avec la ligne Journal des événements dans le groupe Diagnostics"><figcaption>Réglages → Journal des événements</figcaption></figure>
  <figure><img src="/assets/screens/fr/support-event-log.png" alt="Le journal des événements : entrées horodatées, les plus récentes en premier, avec en haut Actualiser, Partager et Envoyer à Hecate"><figcaption>Le journal des événements</figcaption></figure>
  <figure><img src="/assets/screens/fr/support-send-dialog.png" alt="La boîte de dialogue Envoyer le journal à Hecate ? avec Oui et Annuler"><figcaption>Envoyer à Hecate → Oui</figcaption></figure>
  <figure><img src="/assets/screens/fr/support-share-sheet.png" alt="La feuille de partage du système avec le journal joint en fichier texte"><figcaption>Partager … en fichier texte</figcaption></figure>
</div>

À côté d'*Actualiser*, en haut à droite, deux boutons l'envoient :

- :material-send-outline: **Envoyer à Hecate** ouvre un **brouillon d'e-mail**
  prêt à l'emploi pour [info@hecateapps.com](mailto:info@hecateapps.com). Vous
  voyez tout ce qu'il contient, ajoutez une ligne si vous le souhaitez et
  l'envoyez vous-même depuis votre propre app de messagerie. (Le bouton
  n'apparaît que si un compte de messagerie est configuré sur l'appareil.)
- :material-export-variant: **Partager le journal** ouvre la feuille de partage
  du système avec le rapport en fichier texte — pour AirDrop, Messages,
  Fichiers ou votre propre service informatique.

Rien ne quitte l'appareil de lui-même. Les mots de passe et identifiants sont
remplacés avant la création du rapport ; photos et positions n'en font jamais
partie. Les écrans ci-dessus viennent de l'app de capture, la boîte de dialogue
d'envoi de Hecate Admin — l'écran est le même dans toutes les apps Hecate. Le Viewer pour Apple TV n'a pas de journal des événements.

## Sujets fréquents

### Connexion à un broker
Hecate publie vers le **broker MQTT que vous configurez** sous
*Réglages → Broker*. Utilisez-y **Tester la connexion** : elle indique les
motifs de refus (hôte incorrect, TLS, identifiants) en langage clair.

### Localisation
Hecate fonctionne sans localisation, mais les enregistrements ne portent alors
aucun relevé GPS. Accordez ou retirez l'autorisation à tout moment dans
**Réglages iOS → Confidentialité → Service de localisation → Hecate**.

### Profils
Les déroulés de saisie sont livrés sous forme de **profils** via MQTT. Si aucun
profil n'apparaît, vérifiez que votre broker détient bien les documents de
profil retenus (*retained*) et que vos identifiants ont le droit de les lire.

### Hecate Viewer sur Apple TV
Le viewer est un affichage **en lecture seule** : pointez-le vers le même
broker et il montre le flux d'actifs en direct que vos identifiants peuvent
lire. Si rien n'apparaît, vérifiez la connexion au broker (hôte, TLS,
identifiants) et que des actifs sont bien publiés. Le viewer ne saisit rien et
ne demande aucune configuration des données elles-mêmes.

---

Voir aussi les politiques de confidentialité de
[Hecate Capture](../../privacy/capture/index.md) et du
[viewer Apple TV](../../privacy/viewer/index.md).
