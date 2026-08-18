---
hide:
  - toc
---

# Hecate Viewer para iPhone

*Vea llegar sus activos — en vivo, en el mapa, en su bolsillo.*

Hecate Viewer es el **complemento de solo lectura** de la aplicación de
captura. Se conecta al mismo broker MQTT, **se suscribe** al flujo de activos
y coloca cada objeto entrante en un mapa en vivo en el momento de su
publicación — con un feed cronológico al lado para seguir el minuto a minuto.

Es un **visor puro**. No captura nada, no edita nada y no publica nada; todo
lo que hay en pantalla proviene de su broker y vive únicamente en memoria.

## En un minuto

- **Primero, un mapa en vivo.** Un marcador por cada activo entrante, colocado
  donde fue capturado. Las llegadas recientes pulsan en turquesa; al
  envejecer se asientan en gris. Una pestaña de feed muestra el mismo flujo,
  de lo más reciente a lo más antiguo.
- **Los activos se desvanecen con temporizador.** Elija cuánto tiempo
  permanece visible un activo recibido (minutos, o para siempre). Los
  marcadores se encogen y se desvanecen visiblemente cuando su tiempo se
  agota, y después abandonan el mapa y el feed a la vez — así el mapa solo
  muestra lo vigente.
- **Filtrar por perfil.** Un toque en un chip de perfil restringe el mapa y el
  feed a ese flujo de trabajo, en su color de acento; otro toque lo devuelve
  todo.
- **Solo lectura por diseño.** El visor únicamente *se suscribe* — nunca
  publica en el broker y nunca escribe un perfil ni un activo.
- **Mismo broker, mismos datos.** Apúntelo a su broker (o escanee un QR de
  aprovisionamiento) y mostrará exactamente lo que sus credenciales tienen
  permitido leer.
- **Un solo producto.** El mismo formato de mensajes y el mismo lenguaje
  visual en blanco y negro que las demás apps de Hecate; el color proviene
  únicamente del acento de perfil de cada objeto.

## Capturas de pantalla

<div class="shots">
  <figure><img src="/assets/screens/viewer-ios-karte.png" alt="El mapa en vivo — los activos entrantes como marcadores, con los chips de broker y de perfil encima"><figcaption>El mapa en vivo</figcaption></figure>
  <figure><img src="/assets/screens/viewer-ios-feed.png" alt="El feed en vivo — de lo más reciente a lo más antiguo, con etiquetas de frescura y colores de perfil"><figcaption>El feed en vivo</figcaption></figure>
</div>

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

---

[:octicons-arrow-right-24: Privacidad](../privacy/viewer-ios/index.md) ·
[:octicons-arrow-right-24: Soporte](../support/operator/index.md) ·
[:octicons-arrow-right-24: La aplicación de captura](../capture/index.md)
