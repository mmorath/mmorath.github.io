---
hide:
  - toc
---

# Hecate pour Apple TV

*Un affichage mural en direct pour vos actifs Hecate — en lecture seule, sur grand écran.*

!!! info "Sur la feuille de route"

    Le viewer Apple TV est **prévu** et pas encore disponible. Cette page
    décrit le concept. Aujourd'hui, la vue en direct existe sous la forme de
    [Hecate Viewer pour iPhone](../viewer-ios/index.md) et
    [pour iPad](../viewer-ipad/index.md).

L'application Hecate pour Apple TV transforme n'importe quel écran en **vue en
direct des objets que votre équipe saisit**. Elle se connecte au même broker
MQTT que l'application de saisie, **s'abonne** au flux d'actifs et affiche les
enregistrements à mesure qu'ils arrivent — sur un écran d'atelier, au bureau
ou à l'entrée d'un site.

C'est un **pur viewer**. Il ne saisit rien, ne modifie rien et ne stocke rien
en propre.

## En une minute

- **En direct, sans intervention.** Les actifs apparaissent et se mettent à
  jour au fil des publications ; l'écran reste à jour sans aucune
  interaction.
- **Lecture seule, par conception.** Le viewer ne fait que *s'abonner* — il ne
  publie jamais vers le broker et n'écrit ni profil ni actif.
- **Même broker, mêmes données.** Pointez-le vers votre broker et il montre
  exactement ce que vos identifiants ont le droit de lire. Aucune
  configuration séparée des données elles-mêmes.
- **Rien n'est collecté.** Pas de caméra, pas de localisation, pas de comptes,
  pas d'analyses — c'est un affichage, pas un capteur.
- **Un seul produit.** Le même format de messages et le même langage visuel
  noir et blanc que les autres applications Hecate ; la couleur vient
  uniquement de l'accent de profil de chaque objet.

## Ce qu'il montre

Le viewer affiche le flux d'actifs en direct du broker — les objets, leur état
courant et (le cas échéant) leur position et leur accent de profil. Comme il
lit les mêmes profils retenus et les mêmes topics d'actifs que le reste du
système, ce qui apparaît à l'écran est entièrement gouverné par **votre broker
et ses permissions**, pas par l'application.

## Mise en route

Connectez l'application à votre broker MQTT (hôte, port, TLS, identifiants).
Une fois connecté, le viewer s'abonne et commence à afficher — il n'y a rien à
configurer sur les données elles-mêmes : elles sont définies par vos profils
et publiées par l'application de saisie.

---

[:octicons-arrow-right-24: Confidentialité](../privacy/viewer/index.md) ·
[:octicons-arrow-right-24: Assistance](../support/operator/index.md) ·
[:octicons-arrow-right-24: L'application de saisie](../capture/index.md)
