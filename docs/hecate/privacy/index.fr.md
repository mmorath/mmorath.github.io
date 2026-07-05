---
hide:
  - toc
---

# Confidentialité

Chaque application Hecate a sa **propre** politique de confidentialité, car
chacune traite les données différemment. Choisissez l'application que vous
utilisez :

<div class="grid cards" markdown>

-   :material-cellphone: __Application de saisie__

    ---

    Enregistre des actifs, y compris la **position** et une identité
    d'appareil — des données personnelles au sens du RGPD.

    [:octicons-arrow-right-24: Confidentialité saisie](capture/index.md)

-   :material-map-marker-radius: __Hecate Viewer__ · iPhone

    ---

    Un pur abonné avec carte en direct. Position uniquement pour le point
    « vous êtes ici » ; **rien n'est stocké, rien n'est transmis**.

    [:octicons-arrow-right-24: Confidentialité viewer iPhone](viewer-ios/index.md)

-   :material-tablet: __Hecate Viewer__ · iPad

    ---

    Le même pur abonné, conçu pour le grand écran. Traitement des données
    identique : **rien n'est stocké, rien n'est transmis**.

    [:octicons-arrow-right-24: Confidentialité viewer iPad](viewer-ipad/index.md)

-   :material-television: __Viewer Apple TV__ · *prévu*

    ---

    Un pur abonné. **Ne collecte rien** — pas de caméra, pas de position, pas
    de comptes.

    [:octicons-arrow-right-24: Confidentialité viewer](viewer/index.md)

-   :material-tune-variant: __Application admin__

    ---

    Rédige les profils et détient les identifiants du broker. **Aucune
    télémétrie.**

    [:octicons-arrow-right-24: Confidentialité admin](admin/index.md)

</div>

Pour toutes les applications Hecate : **aucun backend du développeur**,
**aucune analyse tierce**, **aucun suivi**. La seule destination réseau est le
broker MQTT que *vous* configurez et contrôlez.
