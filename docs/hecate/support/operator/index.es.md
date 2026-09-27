# Asistencia — Operadores (Capture y Viewer)

Ayuda para los **operadores** sobre el terreno: la **aplicación de captura**
para iPhone/iPad y el **visor** de Apple TV. (¿Redacta perfiles o configura el
broker? Consulte la [asistencia para administradores](../admin/index.md).) ¿Ha
encontrado un error o tiene una petición? Así puede ponerse en contacto.

## Contacto

!!! note "Dirección de contacto"
    **Correo electrónico:** [info@hecateapps.com](mailto:info@hecateapps.com)

La forma más rápida de informar de un problema es **enviarnos el registro de
eventos** (véase abajo): ya incluye su dispositivo, la versión de iOS y la
versión de la aplicación. Una frase sobre qué hizo y qué esperaba que ocurriera
lo completa.

## Enviarnos el registro de eventos

Desde la **versión 2.0.0**, la aplicación de captura y Hecate Viewer en iPhone
y iPad llevan un **registro de eventos**: intentos de conexión, respuestas del
broker, actualizaciones de perfiles, entregas, errores. Normalmente es todo lo
que necesitamos para entender un problema. Ábralo en **Ajustes → Diagnósticos →
Registro de eventos**.

<div class="shots">
  <figure><img src="/assets/screens/es/support-settings-row.png" alt="La lista de ajustes con la fila Registro de eventos en el grupo Diagnósticos"><figcaption>Ajustes → Registro de eventos</figcaption></figure>
  <figure><img src="/assets/screens/es/support-event-log.png" alt="El registro de eventos: entradas con hora, las más recientes primero, con Actualizar, Compartir y Enviar a Hecate arriba"><figcaption>El registro de eventos</figcaption></figure>
  <figure><img src="/assets/screens/es/support-send-dialog.png" alt="El diálogo ¿Enviar el registro a Hecate? con Sí y Cancelar"><figcaption>Enviar a Hecate → Sí</figcaption></figure>
  <figure><img src="/assets/screens/es/support-share-sheet.png" alt="La hoja de compartir del sistema con el registro adjunto como archivo de texto"><figcaption>Compartir … como archivo de texto</figcaption></figure>
</div>

Junto a *Actualizar*, arriba a la derecha, dos botones lo envían:

- :material-send-outline: **Enviar a Hecate** abre un **borrador de correo**
  listo para [info@hecateapps.com](mailto:info@hecateapps.com). Verá todo lo
  que contiene, puede añadir una línea y lo envía usted mismo desde su propia
  aplicación de correo. (El botón solo aparece si hay una cuenta de correo
  configurada en el dispositivo.)
- :material-export-variant: **Compartir el registro** abre la hoja de compartir
  del sistema con el informe como archivo de texto — para AirDrop, Mensajes,
  Archivos o su propio departamento de TI.

Nada sale del dispositivo por sí solo. Las contraseñas y credenciales se
sustituyen antes de crear el informe; las fotos y ubicaciones nunca forman
parte de él. Las pantallas de arriba son de la aplicación de captura y el diálogo de
envío, de Hecate Admin: la pantalla es la misma en todas las aplicaciones
Hecate. El Viewer para Apple TV no tiene registro de eventos.

## Temas frecuentes

### Conexión con un broker
Hecate publica en el **broker MQTT que usted configura** en *Ajustes →
Broker*. Use allí **Probar conexión** — indica los motivos de rechazo (host
incorrecto, TLS, credenciales) en un lenguaje claro.

### Ubicación
Hecate funciona sin ubicación, pero entonces los registros no llevan posición
GPS. Conceda o revoque el permiso en cualquier momento en **Ajustes de iOS →
Privacidad → Localización → Hecate**.

### Perfiles
Los flujos de captura se entregan como **perfiles** a través de MQTT. Si no
aparece ningún perfil, compruebe que su broker conserva los documentos de
perfil retenidos y que sus credenciales tienen permiso para leerlos.

### Visor de Apple TV
El visor es una pantalla de **solo lectura**: apúntelo al mismo broker y
mostrará el flujo de activos en vivo que sus credenciales pueden leer. Si no
aparece nada, compruebe la conexión con el broker (host, TLS, credenciales) y
que realmente se estén publicando activos. El visor no captura nada y no
requiere ninguna configuración de los datos en sí.

---

Consulte también las políticas de privacidad de la
[aplicación de captura](../../privacy/capture/index.md) y del
[visor de Apple TV](../../privacy/viewer/index.md).
