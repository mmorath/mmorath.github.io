# Política de privacidad — Leaf Relief

**Fecha de entrada en vigor:** 2026-10-21
**Desarrollador:** Matthias Morath

Leaf Relief es una app para Mac para un archivo sin papel. Procesa tus documentos
**completamente en tu Mac**.

## Qué recopilamos

**Nada.** La app **no tiene backend**, **no tiene cuenta** y **no contiene analítica,
publicidad ni rastreo**. El desarrollador no recibe ningún dato de la app. Por eso, la
información de privacidad de la app en el App Store indica **«Datos no recopilados»**.

## Qué procesa la app, en tu Mac

- **Documentos** en la carpeta de archivo y la carpeta de entrada que elijas. La app se
  ejecuta en el entorno aislado (App Sandbox) de macOS: solo puede abrir las carpetas
  que elegiste y recuerda ese permiso (como marcador).
- **Escaneos** de un escáner que elijas (USB, o AirScan en tu red local). Las imágenes de
  las páginas permanecen 14 días en la caché de la app para que se pueda repetir un paso
  que haya fallado.
- **Reconocimiento de texto** con el framework Vision de Apple, en tu Mac.
- **Sugerencias** (tipo, remitente, fecha, importe, plazo…) con Apple Intelligence, en
  el dispositivo. Ningún texto se envía a un modelo en la nube.
- **Búsqueda** con un índice en el contenedor de la app (SQLite, con la incrustación de
  frases de Apple para la búsqueda por significado).
- **Spotlight:** títulos, remitentes, tipos, etiquetas y texto están en el índice de
  Spotlight de este Mac.
- **Recordatorios** para los plazos: la app solo los crea cuando haces clic en «Crear
  recordatorio»; macOS pide permiso una vez.
- **Registro de cambios:** los cambios en los documentos se firman con una clave del
  Secure Enclave de este Mac y se anotan en el índice y en el archivo.

## Red

- **Los escáneres de tu red local** (AirScan) se encuentran mediante Bonjour; macOS pide
  permiso para la red local.
- **Sellos de tiempo (opcionales, desactivados por defecto):** si los activas, solo se
  envía una suma de comprobación (SHA-256) de cada entrada del registro de cambios al
  servicio de sellado de tiempo freetsa.org, nunca el contenido de un documento.

La app no establece ninguna otra conexión.

## Compartir

Un documento o el registro solo sale de tu Mac cuando tú lo compartes («Compartir»,
«Enviar por correo»). La copia no lleva etiquetas ni tipos. El registro contiene pasos y
nombres de archivo, ningún contenido de documentos; tu carpeta de inicio, tus
direcciones de correo y tus claves se sustituyen al exportarlo.

## Eliminar

Cuando eliminas la app, macOS borra su contenedor (índice, ajustes, caché). Tus
documentos en la carpeta de archivo se quedan donde están.

## Contacto

Preguntas: `kubisch-gemacht3p@icloud.com`

---

[Leaf Relief](../index.md) · [Soporte](../support/index.md)
