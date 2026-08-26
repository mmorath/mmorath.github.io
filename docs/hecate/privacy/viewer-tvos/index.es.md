# Política de privacidad — Hecate Viewer TV

**Fecha de entrada en vigor:** 24/08/2026
**Desarrollador:** Matthias Morath

Hecate Viewer TV es una **pantalla**. Funciona en un Apple TV, se conecta al
broker MQTT que usted configure y **muestra** en un muro en vivo los activos
publicados en él. Es un suscriptor, no un sensor.

## Qué recopilamos

**Nada.** La app:

- no tiene **cámara** y no captura imágenes;
- no tiene **acceso a la fototeca** y no lee ninguno de sus archivos;
- no solicita **ubicación** ni registra datos de GPS — un Apple TV no se mueve,
  así que el muro representa las posiciones que registró su app de *captura* y no
  le pide nada al televisor;
- no tiene **cuentas de usuario** ni solicita información personal;
- no ejecuta **análisis, publicidad ni seguimiento de terceros** de ningún tipo;
- no contiene **ningún SDK de informes de fallos**.

No existe **ningún backend gestionado por el desarrollador**. El desarrollador no
recibe ninguno de sus datos.

## Las dos cosas con las que habla

Esta es toda la actividad de red de la app:

1. **Su red local, una vez, para configurarse.** Escribir con el mando es
   penoso, así que el televisor nunca escribe. En su lugar muestra un código QR y
   espera en su red local a que **Hecate Viewer en su iPhone o iPad** le entregue
   la configuración del broker. tvOS le pide permiso de acceso a la red local la
   primera vez; la entrega va cifrada, viaja solo entre sus dos dispositivos y no
   llega a ningún servidor nuestro. La configuración —incluidas las credenciales
   del broker— pasa directamente al llavero del dispositivo.
2. **Su broker MQTT, para suscribirse.** Después de eso, la app **lee** del
   broker al que usted la apuntó, y de nada más.

## Qué muestra

La app **se suscribe** a su broker y muestra los datos de activos que recibe: los
objetos, sus campos capturados y la información de ubicación o de perfil que el
broker ya tenga. Esos datos se crean en otro lugar (en la app de captura) y se
rigen por completo por **su** broker y sus permisos. Los activos recibidos se
mantienen **solo en memoria**; al cerrar la app se descartan.

## Adónde van los datos

A ningún sitio nuevo. La app solo **lee** de su broker. Nunca publica, nunca
escribe y nunca transmite datos al desarrollador ni a terceros.

## Almacenamiento y seguridad

- La app guarda únicamente los **ajustes de conexión al broker** con los que fue
  emparejada, para poder reconectarse tras un corte de luz sin volver a
  emparejarse, más una caché de los **documentos de perfil** del broker
  (descripciones de flujo de trabajo y sus colores, que no contienen datos
  personales).
- La contraseña del broker se guarda en el **llavero del dispositivo**, nunca en
  texto plano y nunca en los registros. Los registros de diagnóstico permanecen en
  el dispositivo y anotan solo la *longitud* de los valores sensibles, nunca su
  contenido.
- Las conexiones al broker pueden usar **TLS** (`mqtts`), de modo que los datos en
  tránsito van cifrados.
- El único otro estado almacenado es una preferencia de visualización —a qué
  perfil o zona está limitado el muro— en los ajustes propios de la app.

## Sus opciones

- El **acceso a la red local** puede denegarse o revocarse en cualquier momento
  en los ajustes de tvOS. Tenga en cuenta que el emparejamiento es la única vía de
  configuración de la app: si lo deniega, el muro no tendrá nada que mostrar.
- Vuelva a emparejar el Apple TV cuando quiera para apuntarlo a otro broker. Los
  datos de activos mostrados se rigen por las reglas de retención y acceso de
  **su** broker.

## Menores

Hecate es una utilidad profesional/de campo y no está dirigida a menores.

## Cambios en esta política

Si cambia el tratamiento de datos de la app, esta página se actualizará.

---

[:octicons-arrow-right-24: La app para Apple TV](../../viewer-tvos/index.md) ·
[:octicons-arrow-right-24: Soporte](../../support/operator/index.md)
