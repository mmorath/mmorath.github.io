# Asistencia — Hecate Admin

Ayuda para los **administradores** que redactan y publican perfiles de Hecate.
(¿Usa en cambio la aplicación de captura o el visor de Apple TV? Consulte la
[asistencia para operadores](../operator/index.md).)

## Contacto

!!! note "Dirección de contacto"
    **Correo electrónico:** [info@hecateapps.com](mailto:info@hecateapps.com)

Al informar de un problema, ayuda incluir:

- su **dispositivo** y su **versión de iOS**,
- la **versión de la aplicación** (Ajustes → Información),
- el broker en el que publica (host / TLS, **nunca** la contraseña),
- qué hizo y qué esperaba que ocurriera.

## Enviarnos el registro de eventos

Desde la **versión 2.0.0**, Hecate Admin lleva un **registro de eventos**
—conexiones al broker, resultados de publicación, errores de validación— en
**Ajustes → Diagnósticos → Registro de eventos**. Ya incluye el dispositivo y
las versiones de iOS y de la aplicación, así que sustituye casi toda la lista
de arriba.

<div class="shots">
  <figure><img src="/assets/screens/es/support-admin-settings-row.png" alt="Los ajustes de Hecate Admin con la fila Registro de eventos en el grupo Diagnósticos"><figcaption>Ajustes → Registro de eventos</figcaption></figure>
  <figure><img src="/assets/screens/es/support-admin-event-log.png" alt="El registro de eventos en Hecate Admin: entradas con hora, con Actualizar, Compartir y Enviar a Hecate arriba"><figcaption>El registro de eventos</figcaption></figure>
  <figure><img src="/assets/screens/es/support-send-dialog.png" alt="El diálogo ¿Enviar el registro a Hecate? con Sí y Cancelar"><figcaption>Enviar a Hecate → Sí</figcaption></figure>
  <figure><img src="/assets/screens/es/support-share-sheet.png" alt="La hoja de compartir del sistema con el registro adjunto como archivo de texto"><figcaption>Compartir … como archivo de texto</figcaption></figure>
</div>

- :material-send-outline: **Enviar a Hecate** abre un borrador de correo para
  [info@hecateapps.com](mailto:info@hecateapps.com): verá todo lo que contiene
  y lo envía usted mismo (solo aparece si hay una cuenta de correo
  configurada).
- :material-export-variant: **Compartir el registro** pasa el informe a la hoja
  de compartir como archivo de texto, para AirDrop, Archivos o su propio
  departamento de TI.

Las contraseñas y credenciales se sustituyen antes de crear el informe. Las
tres primeras pantallas son de Hecate Admin; la hoja de compartir, de la
aplicación de captura. La guía
completa está en el
[soporte para operadores](../operator/index.md#enviarnos-el-registro-de-eventos).

## Temas frecuentes

### Conexión con el broker
La aplicación de administración se conecta al **broker MQTT que usted
configura**, mediante **TLS** (`mqtts`), con credenciales de administrador. La
contraseña se almacena únicamente en el **llavero (Keychain)** del
dispositivo.

### Redactar un perfil
Un perfil declara los **pasos**, los **campos**, las reglas de captura y un
color de acento propio de cada perfil. Cada campo puede llevar un patrón de
validación; la aplicación de administración comprueba cada perfil antes de
publicarlo, de modo que la aplicación de captura nunca reciba uno que
rechazaría.

### Publicación y versionado
Los perfiles se publican como mensajes **retenidos** (*retained*), de modo que
los dispositivos que se conectan más tarde también los reciben. Todo cambio
significativo debe publicarse con una **versión estrictamente superior** — los
dispositivos solo aplican un perfil cuando su versión es más reciente que la
que ya tienen. Para «revertir», vuelva a publicar el contenido antiguo con una
**versión nueva y superior**; nunca reutilice ni reduzca un número.

### Retirar un perfil
Para retirar un perfil de los dispositivos, **borre su mensaje retenido**
(publique una carga útil retenida vacía en su topic). Los dispositivos lo
eliminan en su siguiente reconciliación.

### Credenciales y secretos
Los perfiles son ampliamente legibles, por lo que **no deben contener
secretos**. La contraseña del broker vive en el llavero y nunca se escribe en
un perfil, en un QR de aprovisionamiento ni en un registro.

---

Consulte también la [política de privacidad de Admin](../../privacy/admin/index.md).
