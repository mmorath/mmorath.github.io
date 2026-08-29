---
hide:
  - toc
---

# Hecate Viewer para iPad

*El mapa en vivo, de borde a borde — con el feed siempre a su lado.*

Hecate Viewer para iPad es el **complemento de solo lectura** de la aplicación
de captura, dispuesto para la pantalla grande. Se conecta al mismo broker
MQTT, **se suscribe** al flujo de activos y lo muestra todo a la vez: el feed
en vivo como **barra lateral** y el **mapa** ocupando el resto — sin pestañas,
ambos paneles siempre a la vista, tanto en vertical como en horizontal.

Es un **visor puro**. No captura nada, no edita nada y no publica nada; todo
lo que hay en pantalla proviene de su broker y vive únicamente en memoria.

## En un minuto

- **Barra lateral y mapa, juntos.** Cada activo entrante aparece como fila del
  feed *y* como marcador en el momento de su publicación. Las llegadas
  recientes pulsan en turquesa; al envejecer se asientan en gris.
- **Toque una fila, vuele a su marcador.** La barra lateral es el índice del
  mapa: tocar una fila acerca el mapa a ese activo y lo rodea con un anillo —
  toque de nuevo (o toque una zona vacía del mapa) para soltarlo. El botón de
  información de la fila, o el propio marcador, abre el detalle completo.
- **Los activos se desvanecen con temporizador.** Elija cuánto tiempo
  permanece visible un activo recibido (minutos, o para siempre). Los
  marcadores se encogen y se desvanecen visiblemente cuando su tiempo se
  agota, y después abandonan la barra lateral y el mapa a la vez — así la
  pantalla solo muestra lo vigente.
- **Filtrar por perfil.** Un toque en un chip de perfil restringe ambos
  paneles a ese flujo de trabajo, en su color de acento; otro toque lo
  devuelve todo.
- **Solo lectura por diseño.** El visor únicamente *se suscribe* — nunca
  publica en el broker y nunca escribe un perfil ni un activo.
- **Un solo producto.** El mismo formato de mensajes y el mismo lenguaje
  visual en blanco y negro que las demás apps de Hecate; el color proviene
  únicamente del acento de perfil de cada objeto.

## Capturas de pantalla

<div class="shots">
  <figure><img src="/assets/screens/es/viewer-ipad-karte.png" alt="Hecate Viewer para iPad — la disposición dividida: el feed en vivo como barra lateral junto al mapa a pantalla completa, con los activos entrantes como marcadores"><figcaption>La disposición dividida — feed lateral y mapa en vivo</figcaption></figure>
</div>

*Las capturas proceden de versiones de desarrollo. Algunas pueden mostrar funciones que requieren una suscripción o que llegarán en una versión posterior — lo que incluye hoy el nivel gratuito se indica en [Free & Pro](../plans/index.es.md).*

## Qué muestra

El visor representa el flujo de activos en vivo del broker — los campos
capturados de cada objeto, el color y el nombre de su perfil, y su posición
en el mapa. El backlog **retained** del broker llena la pantalla en el momento
de conectarse, de modo que nunca abrirá sobre un mapa vacío mientras haya
historial que mostrar; todo lo demás llega en vivo. Lo que aparece lo
gobiernan por completo **su broker y sus permisos**, no la app.

## Puesta en marcha

Conecte la app a su broker MQTT — escanee un QR de aprovisionamiento de su
administrador o introduzca a mano host, puerto, TLS y credenciales (la
contraseña va directamente al llavero del dispositivo). Cargue los perfiles
una vez, elija cuánto tiempo deben permanecer los activos en pantalla, y
observe. No hay nada que configurar sobre los datos en sí, porque los datos
los definen sus perfiles y los publica la aplicación de captura.

En iPhone, la misma vista en vivo se ofrece como
[Hecate Viewer para iPhone](../viewer-ios/index.md) con una disposición de
pestañas Karte/Feed — la app para iPad vuelve a esas pestañas cuando comparte
la pantalla en Split View.

---

[:octicons-arrow-right-24: Privacidad](../privacy/viewer-ipad/index.md) ·
[:octicons-arrow-right-24: Soporte](../support/operator/index.md) ·
[:octicons-arrow-right-24: El visor para iPhone](../viewer-ios/index.md)
