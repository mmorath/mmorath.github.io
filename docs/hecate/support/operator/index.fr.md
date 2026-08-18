# Assistance — Opérateurs (Capture & Viewer)

Aide pour les **opérateurs** sur le terrain : **Hecate Capture** sur
iPhone/iPad et **Hecate Viewer** sur Apple TV. (Vous éditez des profils ou
configurez le broker ? Voir [l'assistance Admin](../admin/index.md).) Un bug
trouvé ou une demande ? Voici comment nous joindre.

## Contact

!!! note "Adresse de contact"
    **E-mail :** [info@hecateapps.com](mailto:info@hecateapps.com)

Pour signaler un problème, il est utile d'indiquer :

- votre **version d'iOS** et votre **appareil** (par ex. iPhone 15 Pro, iOS 18.5),
- la **version de l'app** (Réglages → À propos),
- ce que vous avez fait et ce que vous attendiez.

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
