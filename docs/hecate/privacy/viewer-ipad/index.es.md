# Política de privacidad — Hecate Viewer para iPad

**Fecha de entrada en vigor:** 2026-07-05
**Desarrollador:** Matthias Morath

Hecate Viewer es un **monitor de solo lectura**. Se conecta a un broker MQTT
que usted configura y **muestra** los activos publicados en él. Es un
suscriptor, no un sensor.

## Qué recopilamos

**Nada.** El visor:

- no ejecuta **ninguna analítica, publicidad ni rastreo de terceros** de
  ningún tipo;
- no tiene **cuentas de usuario** y no pide información personal;
- usa la **cámara únicamente** cuando usted decide escanear en los Ajustes un
  código QR de aprovisionamiento del broker — no se almacena ni se transmite
  ninguna imagen;
- usa su **ubicación únicamente** para mostrar el punto «usted está aquí» en
  el mapa en vivo, *y solo si usted concede el permiso* — nunca se almacena y
  nunca se transmite. Rechácelo o revóquelo en cualquier momento; el mapa
  simplemente pierde el punto azul.

No existe **ningún backend alojado operado por el desarrollador**. El
desarrollador no recibe ninguno de sus datos.

## Qué muestra

La aplicación se **suscribe** al broker que usted le indica y muestra los
datos de activos que recibe — los objetos, sus campos capturados y cualquier
información de ubicación o de perfil que el broker ya contiene. Esos datos se
crean en otro lugar (con la aplicación de captura) y se rigen por completo por
**su** broker y sus permisos. Los activos recibidos se mantienen **solo en
memoria**; al salir de la aplicación se descartan. También puede establecer un
límite de tiempo de visualización, tras el cual los activos mostrados
desaparecen de la pantalla por sí solos.

## Adónde van los datos

A ningún sitio nuevo. El visor solo **lee** de su broker. Nunca publica, nunca
escribe y nunca transmite datos al desarrollador ni a terceros.

## Almacenamiento y seguridad

- La aplicación conserva únicamente los **ajustes de conexión al broker** que
  usted introduce, para poder reconectarse, además de una caché de los
  **documentos de perfil** del broker (descripciones de flujos de trabajo que
  no contienen datos personales).
- Cualquier contraseña se guarda en el **llavero de iOS (Keychain)**, nunca en
  texto plano y nunca se escribe en los registros. Los registros de
  diagnóstico permanecen en el dispositivo y anotan solo la *longitud* de los
  valores sensibles, nunca su contenido.
- Las conexiones con el broker pueden usar **TLS** (`mqtts`), de modo que los
  datos en tránsito van cifrados.

## Sus opciones

- La **ubicación y la cámara** pueden concederse, rechazarse o revocarse en
  cualquier momento en los Ajustes de iOS; ambas son opcionales.
- Elimine una configuración de broker (y su contraseña del llavero) en
  cualquier momento en los Ajustes de la aplicación. Los datos de activos
  mostrados se rigen por las reglas de retención y de acceso de *su* broker.

## Menores

Hecate es una utilidad profesional/de campo y no está dirigida a menores.

## Cambios en esta política

Si cambia el tratamiento de datos de la aplicación, esta página se
actualizará.
