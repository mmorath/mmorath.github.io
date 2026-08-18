# Qué hace Hecate

Hecate condensa esa proliferación en **una sola** app configurable — y corrige
los datos donde se crean, no después.

## Una app, definida por perfiles

El diálogo de entrada de cada caso de uso **no está programado** — es un
**perfil**: un pequeño documento que declara los pasos, los campos y los
métodos de entrada permitidos, distribuido a los dispositivos por un topic
MQTT. Cambie el perfil y la misma app sirve a un nuevo caso de uso, sin nuevo
build.

## Validado en el origen

Cada campo se comprueba contra su formato declarado **en el momento de la
captura**, de modo que los datos erróneos se detienen donde se crean en lugar
de limpiarse después en los sistemas posteriores.

## La entrada adecuada para cada paso

Los pasos de un perfil deciden **qué** se captura; cada paso elige el método
de entrada que encaja con la tarea:

- **Entrada manual.** Escriba el valor directamente en el campo.
- **Escaneo con cámara.** Apunte con la cámara del dispositivo y deje que los
  frameworks de escaneo integrados en el dispositivo lean **códigos QR,
  códigos Data Matrix 2D y códigos de barras 1D** — sin viaje de ida y vuelta
  por la red y sin servicios de terceros.

Sea cual sea el método que use un paso, el valor pasa por la **misma cadena de
validación y captura**, de modo que un perfil se comporta de forma idéntica
sin importar cómo lleguen los datos.

### Los bloques de construcción

| Bloque | Entrada | Campo resultante |
|---|---|---|
| Escanear un código QR | Código QR por cámara | Texto, con comprobación de patrón opcional |
| Escanear un código de barras | Código de barras 1D (EAN, Code 128, …) | Texto, con comprobación de patrón opcional |
| Escanear un código matricial 2D | Data Matrix por cámara | Texto, con comprobación de patrón opcional |
| Capturar una cantidad | Entrada numérica | Número |
| Marcar una lista de estado | Casillas de verificación — pueden aplicar varias | Selección múltiple |
| Elegir un motivo | Botones de opción — aplica exactamente uno | Elección (exactamente una) |
| Introducir texto | Texto libre, una línea | Texto |
| Dejar un comentario | Texto libre, multilínea | Texto, multilínea |

## Siempre georreferenciado

Cada registro lleva una **posición GPS** y se transmite al broker en un sobre
uniforme y autodescriptivo.

## Gobernanza casi sin infraestructura

Lo único que se necesita es un **broker MQTT y la app** — sin backend que
operar, sin alta en una gestión de dispositivos. La autoridad reside en los
permisos del broker: un administrador publica perfiles retenidos (retained);
un usuario solo ve los perfiles que su credencial le permite leer, y captura
según ellos.

Como todas las personas que trabajan un caso de uso rellenan el **mismo perfil
validado**, los datos llegan consistentes, comparables y listos para usarse —
por construcción, no por limpieza a posteriori.

---

## Cómo elimina cada punto de dolor

| Dolor en la empresa | Cómo lo elimina Hecate |
| --- | --- |
| Muchas apps de captura de un solo propósito | Una app; cada caso de uso es un perfil, no un nuevo build |
| Calidad de datos inconsistente | Validación de formato por campo, bloqueada en la captura |
| No habilitado para el uso móvil | Una app iOS de campo, usada donde ocurre el trabajo |
| Sin contexto de ubicación | Cada registro lleva una posición GPS |
| Infraestructura pesada / alta carga de TI | Solo broker + app; los perfiles se entregan como mensajes MQTT retenidos |
| Acceso sin gobernanza | Los permisos del broker deciden quién puede leer qué perfiles |
