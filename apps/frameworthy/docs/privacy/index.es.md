# Política de privacidad — Frameworthy

**Fecha de entrada en vigor:** 2026-10-20
**Desarrollador:** Matthias Morath

Frameworthy es una app para Mac que procesa los vídeos que abres en ella,
**todo en tu Mac**.

!!! note "En resumen"
    Sin cuenta, sin servidor, sin análisis, sin publicidad, sin seguimiento. Tus
    vídeos, tu audio y tus textos nunca salen de tu Mac. La única conexión de red
    propia de la app es la descarga única de los modelos de hablantes desde
    Hugging Face, y no contiene datos de usuario.

## Qué recopilamos

**Nada.** La app **no tiene backend**, no envía datos a **ningún servidor** y no
contiene **análisis, publicidad ni seguimiento**. El desarrollador no recibe ningún
dato de la app.

## Qué procesa la app, en tu Mac

- **Los vídeos que abres**: se leen del disco, se convierten y se escriben en la
  carpeta de salida que elijas (por defecto: `~/Movies/Frameworthy`). La app se
  ejecuta en el App Sandbox de macOS: solo puede abrir los archivos y carpetas que
  elijas, y recuerda ese permiso para que los vídeos de la cola continúen tras un
  reinicio.
- **El texto hablado**: se reconoce con el reconocimiento de voz de Apple en el
  dispositivo. El audio nunca sale de tu Mac. macOS puede descargar una vez un modelo
  de voz para el idioma elegido; esa descarga no contiene datos de usuario.
- **Las correcciones y los títulos de capítulos**: los genera Apple Intelligence en el
  dispositivo. No se envía ningún texto a un modelo en la nube.
- **Las traducciones**: en el dispositivo con el framework Translation de Apple; macOS
  puede descargar paquetes de idioma una vez, después de que lo confirmes.
- **Los hablantes**: se distinguen en el dispositivo. Los modelos de hablantes se
  descargan una vez desde Hugging Face (`FluidInference/speaker-diarization-coreml`);
  esa descarga no envía datos de usuario. Es la única conexión de red que establece la
  propia app.
- **Las transcripciones, los subtítulos y los capítulos**: se guardan junto a tus
  vídeos convertidos.

## Qué guarda la app

Todo se queda en el contenedor de la app en tu Mac
(`~/Library/Containers/com.mmorath.frameworthy`): tus ajustes, la cola de trabajos y
un archivo de registro local con rutas de archivos y detalles del procesamiento. Nada
de ello se sube. Al eliminar la app se elimina el contenedor.

## Cesión de datos

Ninguna. La app no comparte datos con el desarrollador ni con terceros.

## Menores

La app no recopila datos de nadie, tampoco de menores.

## Cambios

Si cambia el tratamiento de datos de la app, esta página se actualiza y cambia la
fecha de entrada en vigor.

## Contacto

Consulta [Soporte](../support/index.es.md).
