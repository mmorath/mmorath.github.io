# Asistencia — Operadores (Capture y Viewer)

Ayuda para los **operadores** sobre el terreno: la **aplicación de captura**
para iPhone/iPad y el **visor** de Apple TV. (¿Redacta perfiles o configura el
broker? Consulte la [asistencia para administradores](../admin/index.md).) ¿Ha
encontrado un error o tiene una petición? Así puede ponerse en contacto.

## Contacto

!!! note "Dirección de contacto"
    **Correo electrónico:** [info@hecateapps.com](mailto:info@hecateapps.com)

Al informar de un problema, ayuda incluir:

- su **versión de iOS** y su **dispositivo** (p. ej., iPhone 15 Pro, iOS 18.5),
- la **versión de la aplicación** (Ajustes → Información),
- qué hizo y qué esperaba que ocurriera.

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
