# Conditions d'utilisation

*Hecate est un produit de MMM Software & Consulting. Cette page dit en termes
clairs ce qui s'applique à l'utilisation des applications Hecate — et quel
texte fait juridiquement foi.*

!!! note "Version allemande"
    Cette page est une traduction de courtoisie. Seule la version allemande,
    les [Nutzungsbedingungen](/de/hecate/terms/){ hreflang="de" }, fait foi.

## Ce qu'est Hecate

Hecate est une famille d'applications pour iPhone, iPad et Apple TV qui saisit
des objets physiques à partir d'un **profil** configurable, les localise et les
diffuse en **MQTT** vers un broker de votre choix.

Il n'y a derrière ni backend, ni compte, ni service de notre part : les
applications ne parlent qu'au broker que vous saisissez vous-même.

## Quelle licence s'applique

L'utilisation des applications Hecate est régie par le **contrat de licence
utilisateur final standard d'Apple** :

[Apple — Licensed Application End User License
Agreement](https://www.apple.com/legal/internet-services/itunes/dev/stdeula/)

Nous n'écrivons **volontairement aucune licence propre**. Une licence rédigée
par nous ne compléterait pas celle d'Apple, elle entrerait en concurrence avec
elle — et devrait être vérifiée par un juriste avant d'améliorer quoi que ce
soit. Le champ prévu pour un CLUF propre dans App Store Connect reste donc
vide ; c'est précisément alors que le contrat standard d'Apple s'applique.
**Cette page explique, elle ne remplace rien.**

## L'offre gratuite

L'offre gratuite est **un vrai produit, pas un essai** : elle n'expire jamais,
et rien de ce que vous avez saisi ne vous est retenu. Ce qui est limité, c'est
la *quantité* — 10 saisies par jour calendaire, un profil enregistré, un profil
publié à la fois, une configuration de broker, des profils jusqu'à cinq blocs.

Ce que ces limites comptent exactement, et ce que l'offre gratuite contient par
ailleurs, est exposé intégralement sous [Free & Pro](../plans/index.fr.md) —
là et seulement là, pour que la même indication ne diverge pas à deux endroits.

## L'abonnement

!!! info "L'abonnement n'est pas encore en vente"

    Les applications livrées aujourd'hui contiennent **uniquement l'offre
    gratuite**. Aucun achat n'y figure et aucun prix n'est à payer. Ce qui suit
    s'appliquera dès qu'un abonnement sera proposé.

L'abonnement sera proposé **au mois ou à l'année**, facturé via votre compte
Apple, et il **se renouvelle automatiquement** jusqu'à sa résiliation. La
résiliation se fait dans la gestion des abonnements d'Apple ; vous n'êtes
jamais engagé au-delà d'une période de facturation.

**Nous n'annonçons pas encore de prix ici.** Les produits ne sont pas créés, et
un prix qui change encore avant la mise en vente aurait figuré à tort sur le
web. Le moment venu, il sera indiqué sur [Free & Pro](../plans/index.fr.md),
ouvertement et en entier — exactement là où nous l'avons promis.

À l'expiration de l'abonnement, vous ne perdez rien. Ce que vous avez saisi se
trouve sur votre broker et sur votre appareil, et y reste. L'app revient à
l'offre gratuite — elle ne supprime rien et ne verrouille rien de ce que vous
avez déjà créé.

## Avec qui le contrat est conclu

Les applications Hecate sont distribuées exclusivement via l'**App Store**.
Un achat ou un abonnement y est conclu avec **Apple**, et non avec nous.
La facturation, les factures, la rétractation et la résiliation passent donc
par votre compte Apple. Pour toute question sur le produit lui-même,
écrivez-nous à l'adresse ci-dessous.

## Résilier

Vous résiliez un abonnement dans la gestion des abonnements de votre compte
Apple :

[apps.apple.com/account/subscriptions](https://apps.apple.com/account/subscriptions)

La résiliation prend effet à la fin de la période de facturation en cours ;
jusque-là, l'abonnement reste actif. Nous ne pouvons ni consulter un abonnement
ni le résilier à votre place.

## Remboursement

Les achats passent entièrement par Apple ; seul Apple peut donc les rembourser
— par la voie habituelle :

[reportaproblem.apple.com](https://reportaproblem.apple.com)

**C'est Apple qui décide d'un remboursement, pas nous.** Nous ne détenons ni
vos données de paiement ni aucun moyen d'annuler un paiement. Écrivez-nous
quand même si quelque chose ne va pas : nous pouvons corriger le défaut, même
si nous ne pouvons pas déplacer l'argent.

## Si ce projet s'arrête

Hecate est un petit projet, et nous ne le cachons pas. Si le développement
s'arrêtait, nous l'annoncerions, cesserions de vendre de nouveaux abonnements
et laisserions expirer ceux en cours.

Vous gardez tout. Vos données se trouvent déjà sur votre propre broker, le
format des profils est du JSON ouvert et documenté, et les profils peuvent être
publiés sans cette app. Il n'y a rien à exporter et rien à migrer — c'est
précisément pourquoi l'abonnement mensuel est le produit principal : vous
n'êtes jamais engagé au-delà de trente jours.

## Ce que nous exploitons — et ce que nous n'exploitons pas

Hecate n'exploite aucun serveur. Il n'y a ni backend, ni compte, ni service
entre vous et vos données. L'app ne parle qu'au broker MQTT que vous saisissez
vous-même.

L'exploitation est donc entre vos mains : le broker, le réseau, les
certificats, les appareils. Si le broker est injoignable, un certificat expiré
ou une règle de gestion mal posée, l'app ne peut ni le détecter ni le réparer —
elle vous le montre et garde votre saisie sur l'appareil jusqu'à ce qu'elle
puisse être livrée.

Vérifiez les données importantes à destination. Cette app est un outil de
saisie, pas une preuve de l'endroit où un message a fini.

Ce qui figure dans les profils et les saisies relève de vous. L'app vérifie la
structure d'un profil, pas son contenu — savoir si un champ est pertinent,
autorisé ou licite, seul l'exploitant peut en juger. Il en va de même des apps
dans leur ensemble : ce sont des outils de saisie pour votre propre
exploitation ; les employer contre les règles applicables ou les droits de
tiers est un mésusage, pas leur destination.

Et : ces apps tournent sur des plateformes qui ne nous appartiennent pas. Si
Apple, Google ou un fabricant restreint une interface par une mise à jour —
caméra, Bluetooth, services d'impression, exécution en arrière-plan —, une
fonction peut être limitée ou disparaître sans que nous puissions l'empêcher.
Nous nous adaptons quand c'est possible ; il n'en naît aucun droit à ce que
chaque fonction subsiste sous chaque future version du système.

## Contact

**MMM Software & Consulting**, propriétaire : Matthias Morath<br>
Courriel : [info@hecateapps.com](mailto:info@hecateapps.com)

Les coordonnées complètes de l'éditeur figurent dans les [mentions
légales](../impressum/index.fr.md) ; ce que les apps font des données est
décrit sous [Confidentialité](../privacy/index.fr.md).
