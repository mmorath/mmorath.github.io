# Premiers pas

*D'un broker vide à votre premier objet saisi — en une vingtaine de minutes.*

Hecate n'exécute **aucun backend**. Il n'y a pas de compte à créer ni de serveur
de l'éditeur entre vos appareils et vos données — ce qui signifie aussi qu'il
n'existe pas d'endroit par défaut où vos saisies pourraient aller. Le **broker
MQTT est le maillon manquant, et il est le vôtre**. Cette page le met en place
et déroule un flux de bout en bout.

!!! tip "Ce qu'il vous faut"

    1. **Un broker MQTT accessible** — le vôtre, ou une instance d'évaluation gratuite.
    2. **[Hecate Admin](../admin/index.md)** sur iPhone ou iPad, pour rédiger et publier le flux.
    3. **[Hecate Capture](../capture/index.md)** sur l'appareil qui scannera.

    Le [Viewer](../viewer-ios/index.md) est facultatif pour un premier test — et gratuit dans tous les cas.

## 1 · Choisir un broker

Hecate parle le MQTT standard et n'est lié à aucun broker particulier.

**Si vous exploitez déjà MQTT**, servez-vous-en. Ce qu'Hecate exige :

| Exigence | Pourquoi |
| --- | --- |
| MQTT 3.1.1 ou 5 | le protocole que parlent les applications |
| **Messages retenus** (retained) | c'est ainsi qu'un flux publié atteint un appareil qui était hors ligne au moment de la publication |
| TLS | les applications utilisent par défaut `mqtts` sur le port `8883`, validation du certificat activée |
| Identifiants par client | pour que chaque appareil soit sa propre identité et puisse être révoqué seul |
| Droits par topic | pour rendre le Viewer réellement en lecture seule, et pas seulement par convention |

**Sinon**, une instance d'évaluation hébergée se crée en quelques minutes et ne
coûte rien à l'échelle d'un essai. HiveMQ Cloud et EMQX Serverless proposent
tous deux une offre gratuite ; un conteneur Mosquitto sur un portable suffit
pour un premier test sur un seul réseau.

!!! warning "Un broker sans messages retenus donnera l'impression de fonctionner"

    Les appareils ne recevront simplement jamais un flux qu'ils n'écoutaient pas
    déjà à l'instant précis de sa publication. Vérifiez cette capacité avant de
    chercher quoi que ce soit d'autre.

## 2 · Connecter l'application Admin

<div class="shots">
  <figure><img src="/assets/screens/fr/gs-broker-connection.png" alt="Paramètres de connexion au broker — hôte, port, protocole et TLS"><figcaption>Connexion : hôte, port, TLS</figcaption></figure>
  <figure><img src="/assets/screens/fr/gs-broker-auth.png" alt="Authentification du broker — nom d'utilisateur et mot de passe"><figcaption>Authentification</figcaption></figure>
</div>

*Les captures proviennent de versions de développement. Certaines peuvent montrer des fonctions nécessitant un abonnement ou prévues pour une version ultérieure — ce que l'offre gratuite contient aujourd'hui est indiqué sous [Free & Pro](../plans/index.fr.md).*

Les valeurs par défaut sont les valeurs sûres, et il doit falloir un effort pour
les affaiblir :

| Réglage | Par défaut |
| --- | --- |
| Schéma | `mqtts` — le `mqtt` simple existe et déclenche un avertissement |
| Port | `8883` |
| TLS | activé |
| Valider le certificat | activé — à désactiver uniquement pour un broker de développement à certificat auto-signé |

Les identifiants vont directement dans le **trousseau** de l'appareil, chiffrés
au repos. Ils ne sont jamais écrits dans un flux, jamais publiés vers le broker,
jamais transportés dans un QR code de provisionnement.

Lorsque le test de connexion réussit, **publiez un flux**. Gardez-le trivial
pour le premier essai — une seule étape de scan et un champ texte suffisent à
prouver toute la chaîne. Un vrai processus mal modélisé ne prouve rien.

## 3 · Provisionner les appareils de terrain

Un mot de passe de vingt caractères, saisi vingt fois sur un terminal à
poignée-pistolet : voilà comment un pilote meurt avant de commencer. Hecate
provisionne par QR code.

<div class="shots">
  <figure><img src="/assets/screens/fr/gs-broker-share-qr.png" alt="Partager la configuration du broker sous forme de QR code"><figcaption>Partager la configuration</figcaption></figure>
  <figure><img src="/assets/screens/fr/gs-provisioning.png" alt="L'appareil confirme les coordonnées de broker reçues"><figcaption>L'appareil confirme</figcaption></figure>
</div>

Le code porte les **coordonnées** : hôte, port, réglages TLS, préfixes de topics
et les niveaux Unified Namespace facultatifs. Il ne porte **pas** le mot de
passe — un QR code affiché sur le mur d'un entrepôt est un identifiant remis à
tous ceux qui passent. Chaque appareil reçoit une fois son propre nom
d'utilisateur et son propre mot de passe, qui vont au trousseau.

Là où un MDM gère les appareils, les mêmes coordonnées peuvent être poussées en
Managed App Configuration, et les identifiants *peuvent* alors voyager avec
elles : une charge utile MDM est un canal d'administration, pas une affiche. Ce
canal est implémenté et vérifié sur le terrain sous Android ; sous iOS il est
spécifié et pas encore réalisé.

## 4 · Saisir, puis vérifier par vous-même

Le flux apparaît tout seul sur l'appareil de terrain. Pas de téléchargement, pas
de mise à jour d'application — c'est le message retenu qui fait son travail.

<div class="shots">
  <figure><img src="/assets/screens/fr/capture-sent.png" alt="Objets livrés, confirmés par le broker"><figcaption>Envoyé — la saisie a atteint le broker</figcaption></figure>
</div>

Scannez, remplissez, enregistrez. La validation a lieu **sur l'appareil**,
contre les règles écrites par l'auteur : les mauvaises données ne le quittent
jamais. Pas de réseau ? Saisissez quand même — les saisies terminées attendent
dans une file d'attente et partent au retour de la connexion. Un compteur de
file qui baisse est le signe honnête que le broker accepte vos messages.

**Regardez maintenant le broker avec un outil qui n'est pas le nôtre.**
Connectez [MQTT Explorer](http://mqtt-explorer.com/) avec n'importe quel
identifiant autorisé à s'abonner : le flux retenu se trouve sous le préfixe de
configuration, et votre saisie arrive sous le préfixe des objets moins d'une
seconde après l'enregistrement.

Cette dernière étape pèse plus lourd qu'il n'y paraît. Elle prouve que les
données sont dans *votre* infrastructure, dans un format que vous savez lire,
accessibles à des systèmes qui n'ont jamais entendu parler d'Hecate. Aucune
application Hecate ne dépend de MQTT Explorer — c'est un outil de diagnostic, et
il doit le rester.

## Ce qui se trouve où sur le broker

Deux arborescences, alignées segment par segment :

```text
hecate/config/profiles/<profileId>        le flux      — RETENU
hecate/assets/<profileId>/<assetUuid>     une saisie   — non retenu
```

- **Les flux sont retenus.** Un appareil éteint toute la semaine reçoit le flux
  courant dès qu'il se connecte. Retirer un flux consiste à publier une charge
  utile retenue vide — il disparaît alors de tous les appareils.
- **Les saisies sont des événements** et ne sont pas retenues. Rien de périmé ne
  reste bloqué à une ancienne adresse quand un flux est renommé.
- **L'identifiant du flux est un niveau de topic à part entière.** C'est ce qui
  fait de `hecate/assets/<profileId>/#` un filtre utilisable plutôt qu'un tas
  plat d'UUID.

Les deux préfixes sont configurables et voyagent dans le QR de provisionnement.
Si vous exploitez un Unified Namespace, activez la hiérarchie et l'arborescence
des objets s'y insère :

```text
<enterprise>/<site>/<area>/<line>/assets/<profileId>/<assetUuid>
acme/plant1/line3/assets/goods-in/1E935809-BF49-4716-B1D6-40F572FECE5B
```

Les saisies arrivent dans une enveloppe auto-descriptive `{ header, data }`.
N'importe quel système en aval — historian, tableau de bord, passerelle ERP —
peut s'y abonner et la lire sans rien nous demander.

## Droits

Donnez à chaque installation de Capture **son propre utilisateur broker** :
`capture-001`, `capture-002`. Cela coûte quelques minutes à la mise en place et
apporte la traçabilité, la révocation par appareil, la rotation isolée des
identifiants et une réponse d'audit qui est un journal de topics plutôt qu'un
haussement d'épaules.

| Application | Flux : s'abonner | Flux : publier | Saisies : s'abonner | Saisies : publier |
| --- | :---: | :---: | :---: | :---: |
| **Admin** | oui | **oui** | oui | non |
| **Capture** | oui | non | non | **oui** |
| **Viewer** | oui | non | oui | non |

En règles de broker :

```text
capture-001   SUBSCRIBE  hecate/config/profiles/#
              PUBLISH    hecate/assets/#

viewer-lobby  SUBSCRIBE  hecate/config/profiles/#
              SUBSCRIBE  hecate/assets/#

admin-anna    SUBSCRIBE  hecate/config/profiles/#
              PUBLISH    hecate/config/profiles/#
              SUBSCRIBE  hecate/assets/#
```

!!! note "Imposez le Viewer en lecture seule, ne lui faites pas confiance"

    Le Viewer ne publie rien ; c'est ainsi qu'il est construit. Donnez-lui
    malgré tout un compte qui ne peut que s'abonner. Un droit imposé par le
    broker survit à une erreur de configuration, à une version future et à un
    appareil installé par quelqu'un d'autre.

## Quand cela ne marche pas

| Symptôme | Cause habituelle | À vérifier |
| --- | --- | --- |
| Broker injoignable | DNS, pare-feu, mauvais port | joindre l'hôte depuis le même réseau, sur le même port |
| Connexion refusée | mauvais point de terminaison, broker arrêté | comparer le point de terminaison à la console du broker, caractère par caractère |
| Échec d'authentification | nom d'utilisateur ou mot de passe | ressaisir sur l'appareil ; le trousseau garde l'ancien jusque-là |
| Échec d'autorisation | droits sur les topics | l'identifiant se connecte mais n'a pas le droit de toucher ce topic |
| Échec de la poignée de main TLS | certificat ou confiance | une AC privée exige sa racine sur l'appareil |
| Aucun flux n'apparaît | message retenu, préfixe ou droit d'abonnement | le chercher dans un explorateur sous le préfixe de configuration |
| La saisie n'arrive pas | droit de publication, ou hors ligne | une file qui ne se vide jamais signifie publication refusée |
| Le Viewer reste vide | droit d'abonnement sur l'arborescence des objets | il lui faut le préfixe des objets, pas seulement celui des flux |

La distinction à intégrer : l'**authentification**, c'est qui vous êtes ;
l'**autorisation**, c'est ce que cette identité a le droit de toucher. Un
appareil qui se connecte sans problème et ne publie rien a réussi la première et
échoué à la seconde — et le correctif est dans les règles du broker, pas dans
l'application.

## Après l'évaluation

L'installation pilote et l'installation de production diffèrent par la gestion
des identités, pas par l'architecture. Rien de ce que vous avez construit lors
du test n'est perdu.

- **Des certificats plutôt que des mots de passe.** Le TLS mutuel (mTLS) donne à
  chaque appareil un certificat client et un vrai cycle de vie : émission,
  renouvellement, révocation. Ne partagez **pas** un certificat unique entre
  tous les appareils — cela recrée le problème du mot de passe partagé avec plus
  de cérémonie.
- **Des rôles plutôt que des règles par appareil.** Ajouter le cinquantième
  terminal devrait être une affectation de rôle, pas cinq lignes d'ACL.
- **Intégrez votre espace de noms maintenant**, plutôt que de migrer plus tard.
  Le topic change ; la charge utile non.
- **Branchez l'aval.** Le Viewer est une fenêtre en direct, pas un entrepôt de
  données — il garde les saisies en mémoire et filtre côté client. Pour
  l'historique et l'analyse, abonnez un système que vous possédez déjà. Cette
  frontière est délibérée.

---

Bloqué quelque part ? [Assistance Admin](../support/admin/index.md) ·
[Assistance opérateur](../support/operator/index.md)
