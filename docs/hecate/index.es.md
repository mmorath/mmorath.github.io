---
hide:
  - toc
---

# Hecate

*Un sistema guiado por perfiles para georreferenciar objetos físicos — una familia de apps, un broker, sin backend.*

Hecate captura objetos físicos según un **perfil** — un flujo configurable
de escaneos y campos —, los sitúa en el mapa y los transmite por
**MQTT** al broker de su elección. Nada del dominio está programado de forma
fija: cambie el perfil y el mismo sistema sirve para carretillas elevadoras,
extintores, tomas de red o hallazgos arqueológicos — **sin nuevo build, sin
nueva app**.

!!! tip "Lo único que necesita es un broker MQTT"

    Hecate no requiere **ningún sistema backend**. La única y sola dependencia
    de red es el **broker MQTT que usted ya controla** — local (on-premise) o
    en la nube. No hay servidor del desarrollador, ni cuentas, ni analítica,
    ni rastreo — y sus datos nunca tocan la infraestructura de terceros.

Y Hecate **no es una aplicación silo**: es *usted* quien decide qué perfiles
crea y qué papel desempeñan los activos capturados en su empresa y su
operación. Como todo llega a su broker en un sobre uniforme y
autodescriptivo, cualquier sistema posterior que usted elija — un panel de
control, un historian, una entrega a un ERP, un Unified Namespace — puede
suscribirse y usar los datos. Las apps terminan en el broker; el significado
es suyo.

## El problema que resuelve

Las empresas operan una **proliferación de apps de captura de un solo
propósito** — una herramienta por caso de uso, cada una construida de forma
aislada. El resultado: calidad de datos desigual (cada app valida de manera
distinta), una captura que sigue ocurriendo en el escritorio y no donde está
el trabajo, registros que nunca dicen **dónde** está realmente el objeto — y,
por cada herramienta, un backend y una gestión de dispositivos que operar.

Hecate sustituye esa proliferación por **un sistema configurable**: los
perfiles definen *qué* se captura, la validación ocurre en el momento de la
captura, cada registro lleva su posición GPS, y todo fluye por el único
broker que usted ya controla.

[:octicons-arrow-right-24: El problema en detalle](capture/problem.md) ·
[:octicons-arrow-right-24: Cómo Hecate elimina cada uno de estos dolores](capture/solution.md)

## Las apps

<div class="grid cards" markdown>

-   :material-cellphone: __Hecate Capture__ · iPhone & iPad

    ---

    La herramienta de campo. Escanea, valida y georreferencia cada objeto
    según el perfil activo y lo publica en su broker. Funciona sin conexión
    con una bandeja de salida persistente que se vacía al reconectar.

    [:octicons-arrow-right-24: Visión general de la captura](capture/index.md)

-   :material-map-marker-radius: __Hecate Viewer__ · iPhone

    ---

    El mapa en vivo en su bolsillo. Un suscriptor puro que sitúa los activos
    en el mapa en el momento de su publicación y los desvanece tras el
    tiempo que usted elija — no captura nada y no publica nada.

    [:octicons-arrow-right-24: Visión general del visor para iPhone](viewer-ios/index.md)

-   :material-tablet: __Hecate Viewer__ · iPad

    ---

    El mapa en vivo de borde a borde. El feed ocupa una barra lateral junto
    al mapa a pantalla completa — toque una fila y el mapa vuela al pin de
    ese activo. El mismo suscriptor, diseñado para la pantalla grande.

    [:octicons-arrow-right-24: Visión general del visor para iPad](viewer-ipad/index.md)

-   :material-television: __Hecate Viewer__ · Apple TV

    ---

    El mapa en vivo como pantalla mural autónoma — para naves, oficinas y
    accesos de planta. Se empareja con la familia y muestra lo que ocurre,
    a todas horas.

    [:octicons-arrow-right-24: Visión general del visor para TV](viewer/index.md)

-   :material-tune-variant: __Hecate Admin__ · iPhone & iPad

    ---

    La autoridad de autoría. Crea, valida, versiona, publica y retira los
    perfiles que consume la aplicación de captura, y configura la conexión al
    broker que los transporta.

    [:octicons-arrow-right-24: Visión general del admin](admin/index.md)

</div>

## También en Android

La aplicación de captura también está **terminada para Android** — llegará a la
**Google Play Store a finales de 2026**. Funciona en dispositivos Android
corrientes y en escáneres industriales como el
[Honeywell CT47](https://automation.honeywell.com/us/en/products/productivity-solutions/mobile-computers/handheld-computers/ct47), cuyo motor de escaneo integrado Hecate controla
directamente.

## Capturas de pantalla

<div class="shots">
  <figure><img src="/assets/screens/es/capture-assets.png" alt="Hecate Capture — la bandeja de salida con objetos capturados en espera de entrega"><figcaption>Capture — bandeja de salida</figcaption></figure>
  <figure><img src="/assets/screens/es/capture-detail.png" alt="Hecate Capture — la vista de detalle de un activo con sus campos capturados"><figcaption>Capture — detalle del activo</figcaption></figure>
  <figure><img src="/assets/screens/es/capture-sent.png" alt="Hecate Capture — activos entregados, confirmados por el broker"><figcaption>Capture — entregados</figcaption></figure>
  <figure><img src="/assets/screens/es/admin-profiles.png" alt="Hecate Admin — la pantalla de perfiles con perfiles creados"><figcaption>Admin — perfiles</figcaption></figure>
  <figure><img src="/assets/screens/es/admin-detail.png" alt="Hecate Admin — la vista de detalle de un perfil con pasos y versiones"><figcaption>Admin — detalle del perfil</figcaption></figure>
  <figure><img src="/assets/screens/es/viewer-ios-karte.png" alt="Hecate Viewer — el mapa en directo con activos entrantes como marcadores"><figcaption>Viewer — el mapa en directo</figcaption></figure>
  <figure><img src="/assets/screens/en/viewer-ios-feed.png" alt="Hecate Viewer — el feed en directo, lo más reciente primero"><figcaption>Viewer — el feed en directo</figcaption></figure>
  <figure class="wide"><img src="/assets/screens/es/viewer-ipad-karte.png" alt="Hecate Viewer para iPad — la barra lateral con el feed junto al mapa a pantalla completa"><figcaption>Viewer para iPad — la pantalla dividida</figcaption></figure>
  <figure class="wide"><img src="/assets/screens/es/viewer-ipad-feed.png" alt="Hecate Viewer para iPad — la barra lateral es el feed en directo"><figcaption>Viewer para iPad — el feed lateral</figcaption></figure>
  <figure class="wide"><img src="/assets/screens/en/tv-wall.png" alt="Hecate Viewer para Apple TV — la pantalla mural en directo"><figcaption>Viewer para Apple TV — el muro</figcaption></figure>
</div>

## Cómo encajan entre sí

La app de **administración** es la autoridad sobre los *perfiles*; la app de
**captura** es de solo lectura sobre los perfiles y la autoridad sobre los
*activos*; los **viewers** son de solo lectura sobre todo. Todas las apps
comparten un mismo núcleo, un mismo formato de mensajes y un mismo lenguaje
visual en blanco y negro — el color proviene únicamente del acento de perfil
de cada objeto.

## El nombre & el símbolo

**Hécate** es la diosa griega de las encrucijadas, los umbrales y las llaves —
la que se alza en la frontera y guarda lo que la abre. El símbolo es el
**Strophalos** («la rueda de Hécate») — un laberinto de senderos sinuosos
alrededor de un único eje: las rutas por el campo y los mensajes que
convergen en el broker, en el centro.

## Para cada app

| | Privacidad | Soporte |
| --- | --- | --- |
| **Hecate Capture** | [Privacidad](privacy/capture/index.md) | [Soporte](support/operator/index.md) |
| **Hecate Viewer (iPhone)** | [Privacidad](privacy/viewer-ios/index.md) | [Soporte](support/operator/index.md) |
| **Hecate Viewer (iPad)** | [Privacidad](privacy/viewer-ipad/index.md) | [Soporte](support/operator/index.md) |
| **Hecate Admin** | [Privacidad](privacy/admin/index.md) | [Soporte](support/admin/index.md) |
| **Hecate Viewer (Apple TV)** | [Privacidad](privacy/viewer/index.md) | [Soporte](support/operator/index.md) |
