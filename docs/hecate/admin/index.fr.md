---
hide:
  - toc
---

# Hecate Admin

*L'autorité d'édition des profils Hecate — iPhone & iPad.*

!!! info "En développement"

    Hecate Admin est en **développement actif** et pas encore disponible pour
    tous. Cette page décrit ce que fait l'application et sa direction.

Hecate Admin est le compagnon de [l'application de saisie](../capture/index.md).
Là où l'application de saisie *suit* un profil, l'application admin est
l'**autorité** qui **crée, valide, versionne, publie et retire** ces profils —
et configure la connexion au broker qui les transporte.

Un *profil* est le flux configurable de scans, de champs et de photos qui dit
à l'application de saisie ce qu'est un objet et comment l'enregistrer. C'est
dans Hecate Admin que ce profil est écrit, vérifié et gouverné.

## En une minute

- **Éditer des profils.** Définissez les étapes, champs, règles de saisie et
  l'accent de couleur qui façonnent un flux de saisie — sans code, sans
  nouveau build.
- **Validé avant publication.** Un profil est vérifié contre son schéma et son
  contrat de versionnage, pour que l'application de saisie n'en reçoive
  jamais un qu'elle rejetterait en silence.
- **Versionnage sûr.** Les versions restent monotones ; un « retour arrière »
  est une republication sous une version supérieure, jamais un rollback — les
  appareils ne peuvent pas être rétrogradés.
- **Broker uniquement.** Les profils sont publiés en messages MQTT
  **retenus** ; pour en retirer un, son message retenu est effacé. Pas de
  serveur, pas de seconde dépendance réseau.
- **Les identifiants restent à leur place.** Le credential admin du broker vit
  dans le **trousseau** de l'appareil et n'est jamais écrit dans un profil,
  un QR de configuration, un journal, ni nulle part où il pourrait fuir.
- **Pas de télémétrie.** L'application admin ne collecte ni localisation, ni
  analyses d'usage, ni suivi d'aucune sorte.

## Comment les profils atteignent les appareils

L'application admin publie chaque profil en message **retenu** sous
`<configPrefix>/profiles/<id>` (par défaut `hecate/config`). Le drapeau
« retained » permet à un appareil qui se connecte *plus tard* de recevoir
quand même le profil courant ; l'application de saisie ne l'applique que si sa
version est strictement plus récente que celle qu'elle détient. Pour
**retirer** un profil, l'application admin efface ce message retenu, et les
appareils le suppriment à leur prochaine réconciliation.

## Identité visuelle

Hecate Admin partage le langage visuel de l'application de saisie : une
interface **strictement noir et blanc**, **sans couleur de marque globale** —
la seule couleur est l'accent propre à chaque profil, qui le suit dans sa
ligne, sa pastille et sa fiche détaillée. Le symbole est le Strophalos
commun.

---

[:octicons-arrow-right-24: Confidentialité](../privacy/admin/index.md) ·
[:octicons-arrow-right-24: Assistance](../support/admin/index.md) ·
[:octicons-arrow-right-24: L'application de saisie](../capture/index.md)
