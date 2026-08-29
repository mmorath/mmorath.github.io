---
hide:
  - toc
---

# Hecate Viewer TV

*El muro en vivo — legible desde el otro extremo de la sala, y nadie tiene que
tocarlo.*

Hecate Viewer TV convierte un Apple TV en un **muro de activos en vivo** para su
instalación de Hecate. La app se conecta al mismo broker MQTT que la app de
captura, **se suscribe** al flujo de activos y muestra cada objeto entrante en un
mapa en vivo a pantalla completa, con un feed cronológico al lado: en un monitor
de taller, en una oficina o en la entrada de la planta.

Es un **visor puro**. No captura nada, no edita nada y no publica nada; todo lo
que aparece en pantalla vino de su broker y vive solo en memoria.

## En un minuto

- **Configuración desde el iPhone, no desde el mando.** El televisor muestra un
  código QR; usted lo escanea en Hecate Viewer en su iPhone o iPad y envía la
  configuración del broker —credenciales incluidas— cifrada por su red local. El
  muro se llena en segundos. Sin escribir con el mando, nunca.
- **Un mapa pensado para la sala.** Un pin por cada activo entrante, situado donde
  fue capturado. Las llegadas recientes laten en turquesa; al envejecer se apagan
  a gris. El feed de la barra lateral lista el mismo flujo, lo más nuevo primero,
  con los colores del perfil y etiquetas de frescura.
- **El mando es opcional.** Enfoque una fila del feed para resaltar su pin, haga
  clic para acercarse y clic de nuevo para ver todos los campos capturados. Si se
  lo deja solo, el muro compone su propia imagen y se mantiene al día.
- **Honesto sobre su propio estado.** Cuando el flujo se queda en silencio, el
  muro lo dice: primero un tinte de reposo, después un velo de datos rancios y
  luego un estado de reconexión claro que se recupera por sí solo. Una pantalla que
  finge estar en directo es peor que una que admite estar sin conexión.
- **Hecho para quedarse encendido.** La protección contra el quemado desplaza la
  composición en pantallas desatendidas, y el muro mantiene la pantalla despierta
  para que una instalación 24/7 no se duerma a mitad de turno.
- **Filtrar por perfil y por zona.** Limite el muro a un perfil de captura o a una
  zona del emplazamiento desde el overlay de Play/Pausa; los activos ocultos siguen
  contándose, así que los totales nunca mienten.
- **Un solo producto.** El mismo formato de datos y el mismo lenguaje visual en
  blanco y negro que el resto de las apps Hecate; el color viene únicamente del
  acento de perfil de cada objeto.

## Capturas de pantalla

<div class="shots">
  <figure class="wide"><img src="/assets/screens/es/tv-wall.png" alt="Hecate Viewer TV — el muro en vivo: feed lateral junto al mapa a pantalla completa con los activos entrantes como pines"><figcaption>El muro — feed lateral y mapa en vivo</figcaption></figure>
</div>

*Las capturas proceden de versiones de desarrollo. Algunas pueden mostrar funciones que requieren una suscripción o que llegarán en una versión posterior — lo que incluye hoy el nivel gratuito se indica en [Free & Pro](../plans/index.es.md).*

## Qué muestra

El muro representa el flujo de activos en vivo del broker: los campos capturados
de cada objeto, su color y nombre de perfil, y su posición en el mapa. El
**historial retenido** del broker llena la pantalla en el momento de conectar, así
que el muro nunca arranca vacío mientras haya historia que mostrar; todo lo
posterior llega en directo. Lo que aparece está gobernado por completo por **su
broker y sus permisos**, no por la app.

## Puesta en marcha

Instale la app y mostrará un código de emparejamiento. Abra
[Hecate Viewer para iPhone](../viewer-ios/index.md) o
[para iPad](../viewer-ipad/index.md), elija su broker y envíelo al Apple TV: la
configuración cruza su red local cifrada y la contraseña pasa directamente al
llavero del dispositivo. El muro se conecta y arranca por sí solo, y sigue
emparejado entre reinicios.

No hay nada que configurar sobre los datos en sí, porque los datos los definen sus
perfiles y los publica la app de captura.

!!! note "Necesita uno de los visores de teléfono para configurarlo"

    El emparejamiento es la única vía de configuración, a propósito: introducir el
    nombre de host de un broker y una contraseña con el mando de un televisor es un
    suplicio. Instale primero Hecate Viewer en un iPhone o iPad de la misma red.

---

[:octicons-arrow-right-24: Privacidad](../privacy/viewer-tvos/index.md) ·
[:octicons-arrow-right-24: Soporte](../support/operator/index.md) ·
[:octicons-arrow-right-24: El visor para iPhone](../viewer-ios/index.md)
