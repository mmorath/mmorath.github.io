---
hide:
  - toc
---

# Hecate Capture

*Georreferenciación universal de objetos, guiada por perfiles*

Hecate Capture es una app iOS pensada para el campo, dedicada a la
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
  <figure><img src="/assets/screens/es/capture-assets.png" alt="La bandeja de salida de activos — objetos capturados a la espera de entrega"><figcaption>Activos &amp; bandeja de salida</figcaption></figure>
  <figure><img src="/assets/screens/es/capture-detail.png" alt="La vista de detalle de un activo con sus campos capturados"><figcaption>Detalle del activo</figcaption></figure>
  <figure><img src="/assets/screens/es/capture-sent.png" alt="Historial de entrega de los activos enviados"><figcaption>Historial de entrega</figcaption></figure>
  <figure><img src="/assets/screens/es/capture-settings.png" alt="El centro de ajustes"><figcaption>Ajustes</figcaption></figure>
</div>

*Las capturas proceden de versiones de desarrollo. Algunas pueden mostrar funciones que requieren una suscripción o que llegarán en una versión posterior — lo que incluye hoy el nivel gratuito se indica en [Free & Pro](../plans/index.es.md).*


## El problema

Las empresas operan una **proliferación de apps de un solo propósito** para
registrar datos a lo largo de sus pasos de proceso — una herramienta por caso
de uso, cada una construida de forma aislada. De ahí se derivan tres fallos.

### Calidad inconsistente

Cada app valida (o no valida) sus entradas de manera distinta, de modo que los
datos que llegan a los sistemas posteriores son desiguales y difícilmente
confiables.

### No habilitado para el uso móvil

Gran parte de esta captura sigue ocurriendo en un escritorio — no donde está
realmente el trabajo.

### Sin contexto de ubicación

Casi nada de esto está georreferenciado, de modo que un registro rara vez dice
**dónde** está realmente el objeto que describe.

---

### En resumen

| Dolor en la empresa | |
| --- | --- |
| Muchas apps de captura de un solo propósito | un nuevo build por caso de uso |
| Calidad de datos inconsistente | cada app valida de manera distinta |
| No habilitado para el uso móvil | la captura ocurre en un escritorio |
| Sin contexto de ubicación | los registros no dicen *dónde* |
| Infraestructura pesada / alta carga de TI | un backend y una gestión de dispositivos por herramienta |
| Acceso sin gobernanza | ninguna regla uniforme sobre quién puede capturar qué |

[:octicons-arrow-right-24: Cómo Hecate elimina cada uno de estos puntos](#que-hace-hecate-capture)

## Qué hace Hecate Capture

Hecate condensa esa proliferación en **una sola** app configurable — y corrige
los datos donde se crean, no después.

### Una app, definida por perfiles

El diálogo de entrada de cada caso de uso **no está programado** — es un
**perfil**: un pequeño documento que declara los pasos, los campos y los
métodos de entrada permitidos, distribuido a los dispositivos por un topic
MQTT. Cambie el perfil y la misma app sirve a un nuevo caso de uso, sin nuevo
build.

### Validado en el origen

Cada campo se comprueba contra su formato declarado **en el momento de la
captura**, de modo que los datos erróneos se detienen donde se crean en lugar
de limpiarse después en los sistemas posteriores.

### La entrada adecuada para cada paso

Los pasos de un perfil deciden **qué** se captura; cada paso elige el método
de entrada que encaja con la tarea:

- **Entrada manual.** Escriba el valor directamente en el campo.
- **Escaneo con cámara.** Apunte con la cámara del dispositivo y deje que los
  frameworks de escaneo integrados en el dispositivo lean **códigos QR,
  códigos Data Matrix 2D y códigos de barras 1D** — sin viaje de ida y vuelta
  por la red y sin servicios de terceros.

Sea cual sea el método que use un paso, el valor pasa por la **misma cadena de
validación y captura**, de modo que un perfil se comporta de forma idéntica
sin importar cómo lleguen los datos.

### Los bloques de construcción

| Bloque | Entrada | Campo resultante |
|---|---|---|
| Escanear un código QR | Código QR por cámara | Texto, con comprobación de patrón opcional |
| Escanear un código de barras | Código de barras 1D (EAN, Code 128, …) | Texto, con comprobación de patrón opcional |
| Escanear un código matricial 2D | Data Matrix por cámara | Texto, con comprobación de patrón opcional |
| Capturar una cantidad | Entrada numérica | Número |
| Marcar una lista de estado | Casillas de verificación — pueden aplicar varias | Selección múltiple |
| Elegir un motivo | Botones de opción — aplica exactamente uno | Elección (exactamente una) |
| Introducir texto | Texto libre, una línea | Texto |
| Dejar un comentario | Texto libre, multilínea | Texto, multilínea |

### Siempre georreferenciado

Cada registro lleva una **posición GPS** y se transmite al broker en un sobre
uniforme y autodescriptivo.

### Gobernanza casi sin infraestructura

Lo único que se necesita es un **broker MQTT y la app** — sin backend que
operar, sin alta en una gestión de dispositivos. La autoridad reside en los
permisos del broker: un administrador publica perfiles retenidos (retained);
un usuario solo ve los perfiles que su credencial le permite leer, y captura
según ellos.

Como todas las personas que trabajan un caso de uso rellenan el **mismo perfil
validado**, los datos llegan consistentes, comparables y listos para usarse —
por construcción, no por limpieza a posteriori.

---

### Cómo elimina cada punto de dolor

| Dolor en la empresa | Cómo lo elimina Hecate |
| --- | --- |
| Muchas apps de captura de un solo propósito | Una app; cada caso de uso es un perfil, no un nuevo build |
| Calidad de datos inconsistente | Validación de formato por campo, bloqueada en la captura |
| No habilitado para el uso móvil | Una app iOS de campo, usada donde ocurre el trabajo |
| Sin contexto de ubicación | Cada registro lleva una posición GPS |
| Infraestructura pesada / alta carga de TI | Solo broker + app; los perfiles se entregan como mensajes MQTT retenidos |
| Acceso sin gobernanza | Los permisos del broker deciden quién puede leer qué perfiles |

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
