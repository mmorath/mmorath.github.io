---
hide:
  - toc
---

# Hecate Admin

*La autoridad de creación de los perfiles de Hecate — iPhone y iPad.*

Hecate Admin es el complemento de la
[aplicación de captura](../capture/index.md). Donde la aplicación de captura
*sigue* un perfil, la aplicación de administración es la **autoridad** que
**crea, valida, versiona, publica y retira** esos perfiles — y configura la
conexión al broker que los transporta.

Un *perfil* es el flujo de trabajo configurable de escaneos y campos que le
dice a la aplicación de captura qué es un objeto y cómo registrarlo. Hecate
Admin es donde ese perfil se escribe, se comprueba y se gobierna.

## En un minuto

- **Redactar perfiles.** Defina los pasos, los campos, las reglas de captura y
  el acento propio de cada perfil que dan forma a un flujo de captura — sin
  código y sin compilar una nueva app.
- **Validado antes de publicar.** Cada perfil se comprueba contra su esquema y
  su contrato de versionado, de modo que la aplicación de captura nunca reciba
  uno que descartaría en silencio.
- **Versionado seguro.** Las versiones se mantienen monótonas; «revertir» es
  republicar con una versión superior, nunca un rollback — así los
  dispositivos no pueden ser degradados.
- **Solo broker.** Los perfiles se publican como mensajes MQTT **retained**;
  para retirar uno, se borra su mensaje retained. Sin servidor, sin una
  segunda dependencia de red.
- **Las credenciales no se mueven.** La credencial de administración del
  broker vive en el **llavero** (Keychain) del dispositivo y nunca se escribe
  en un perfil, en un QR de aprovisionamiento, en un registro ni en ningún
  lugar donde pudiera filtrarse.
- **Sin telemetría.** La aplicación de administración no recopila ubicación,
  ni analíticas de uso, ni rastreo de ningún tipo.

## Cómo llegan los perfiles a los dispositivos

La aplicación de administración publica cada perfil como mensaje **retained**
en `<configPrefix>/profiles/<id>` (por defecto `hecate/config`). La marca
retained permite que un dispositivo que se conecte *más tarde* reciba
igualmente el perfil vigente; la aplicación de captura solo lo aplica cuando
su versión es estrictamente más nueva que la que ya posee. Para **retirar** un
perfil, la aplicación de administración borra ese mensaje retained, y los
dispositivos lo descartan en su siguiente reconciliación.

## Identidad de diseño

Hecate Admin comparte el lenguaje visual de la aplicación de captura: una
interfaz **estrictamente en blanco y negro**, **sin color de marca global** —
el único color es el acento propio de cada perfil, que lo acompaña en su fila,
su muestra y su tarjeta de detalle. La marca es el Strophalos compartido.

---

[:octicons-arrow-right-24: Privacidad](../privacy/admin/index.md) ·
[:octicons-arrow-right-24: Soporte](../support/admin/index.md) ·
[:octicons-arrow-right-24: La aplicación de captura](../capture/index.md)
