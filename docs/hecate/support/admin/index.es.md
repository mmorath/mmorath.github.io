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
