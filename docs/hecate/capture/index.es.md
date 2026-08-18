---
hide:
  - toc
---

# Hecate

*Georreferenciación universal de objetos, guiada por perfiles*

Hecate es una app iOS pensada para el campo, dedicada a la
**georreferenciación de objetos físicos**. Cada objeto se captura según un
**perfil** — un flujo configurable de escaneos y campos —, se sitúa
en el mapa con una posición GPS y se transmite por **MQTT** al broker de su
elección.

Nada del dominio está programado de forma fija. Cambie el perfil y la misma
app captura carretillas elevadoras, extintores, tomas de red o hallazgos
arqueológicos — sin nuevo build.

## En un minuto

- **Una app, muchos casos de uso.** Cada caso de uso es un *perfil*, no una
  app aparte.
- **Validado en el origen.** Cada campo se comprueba contra su formato
  declarado en el mismo momento de la captura.
- **Siempre localizado.** Cada registro lleva una posición GPS y aparece en
  el mapa.
- **Transmitido por MQTT.** Publicado en *su propio* broker en un sobre
  uniforme y autodescriptivo — sin backend del desarrollador, sin analítica,
  sin rastreo.
- **Funciona sin conexión.** Una bandeja de salida persistente conserva los
  registros fuera de cobertura y se vacía al reconectar.

## Capturas de pantalla

<div class="shots">
  <figure><img src="/assets/screens/assets.png" alt="La bandeja de salida de activos — objetos capturados a la espera de entrega"><figcaption>Activos &amp; bandeja de salida</figcaption></figure>
  <figure><img src="/assets/screens/detail.png" alt="La vista de detalle de un activo con sus campos capturados"><figcaption>Detalle del activo</figcaption></figure>
  <figure><img src="/assets/screens/sent.png" alt="Historial de entrega de los activos enviados"><figcaption>Historial de entrega</figcaption></figure>
  <figure><img src="/assets/screens/settings.png" alt="El centro de ajustes"><figcaption>Ajustes</figcaption></figure>
</div>

## Siga leyendo

<div class="grid cards" markdown>

-   :material-alert-circle-outline: __El problema__

    ---

    Por qué una proliferación de apps de captura de un solo propósito deja
    los datos inconsistentes, atados al escritorio y ciegos a la ubicación.

    [:octicons-arrow-right-24: El problema](problem.md)

-   :material-checkbox-marked-circle-outline: __Qué hace Hecate__

    ---

    Cómo una sola app guiada por perfiles resuelve esa proliferación y
    corrige los datos en el origen.

    [:octicons-arrow-right-24: Qué hace Hecate](solution.md)

</div>

## El nombre & el símbolo

**Hécate** es la diosa griega de las encrucijadas, los umbrales y las llaves —
la que se alza en la frontera y guarda lo que la abre. Una herramienta de
campo vive exactamente en ese límite: entre el objeto físico frente a usted y
los sistemas digitales que deben conocerlo. Hecate lo **localiza**, **guía**
la captura, lo **lleva** hasta el broker y **guarda las llaves** que abren el
camino.

El símbolo es el **Strophalos** («la rueda de Hécate») — un laberinto de
senderos sinuosos alrededor de un único eje: las rutas por el campo y los
mensajes que convergen en el broker, en el centro.
