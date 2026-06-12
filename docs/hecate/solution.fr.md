# Ce que fait Hecate

Hecate résorbe cette dispersion en **une seule** application configurable — et
corrige les données là où elles naissent, au lieu de le faire après coup.

## Une application, définie par des profils

Le dialogue de saisie de chaque cas d'usage n'est **pas programmé** — c'est un
**profil** : un petit document qui déclare les étapes, les champs et les modes
de saisie autorisés, distribué aux appareils via un topic MQTT. Changez de
profil et la même application sert un nouveau cas d'usage, sans nouvelle
compilation.

## Validé à la source

Chaque champ est vérifié par rapport au format déclaré **au moment de la
saisie**, de sorte que les données erronées sont arrêtées là où elles naissent
plutôt que nettoyées en aval.

## La bonne saisie pour chaque étape

Les étapes d'un profil décident **ce qui** est saisi ; chaque étape choisit le
mode de saisie adapté à la tâche :

- **Saisie manuelle.** Tapez la valeur directement dans le champ.
- **Scan par caméra.** Pointez la caméra de l'appareil et laissez les
  frameworks de scan embarqués lire **les QR codes, les codes Data Matrix 2D,
  les codes-barres 1D et le texte imprimé** — sans aller-retour réseau ni
  service tiers.

Quel que soit le mode utilisé par une étape, la valeur passe par la **même
chaîne de validation et de saisie**, de sorte qu'un profil se comporte de façon
identique quelle que soit la provenance des données.

## Toujours géoréférencé

Chaque enregistrement porte un **point GPS** et est transmis au broker dans une
enveloppe uniforme et auto-descriptive.

## Une gouvernance avec quasiment aucune infrastructure

Il ne faut qu'un **broker MQTT et l'application** — aucun backend à exploiter,
aucune inscription à une gestion de parc. L'autorité réside dans les permissions
du broker : un administrateur publie des profils conservés (retained) ; un
utilisateur ne voit que les profils que ses identifiants l'autorisent à lire, et
saisit à partir de ceux-ci.

Parce que toutes les personnes travaillant sur un cas d'usage remplissent le
**même profil validé**, les données arrivent cohérentes, comparables et prêtes à
l'emploi — par conception, et non par nettoyage a posteriori.

---

## Comment elle supprime chaque difficulté

| Difficulté en entreprise | Comment Hecate la supprime |
| --- | --- |
| Multiples applications de saisie à usage unique | Une application ; chaque cas d'usage est un profil, pas une nouvelle compilation |
| Qualité de données incohérente | Validation de format champ par champ, bloquée à la saisie |
| Pas adapté à la mobilité | Une application iOS de terrain, utilisée là où le travail a lieu |
| Aucun contexte de localisation | Chaque enregistrement porte un point GPS |
| Infrastructure / charge informatique lourde | Broker + application uniquement ; profils livrés en messages MQTT conservés |
| Accès non encadré | Les permissions du broker décident qui peut lire quels profils |
