# Política de privacidad — Hecate para Apple TV

**Fecha de entrada en vigor:** 2026-06-18
**Desarrollador:** Matthias Morath

La aplicación de Hecate para Apple TV es un **visor de solo lectura**. Se
conecta a un broker MQTT que usted configura y **muestra** los activos
publicados en él. Es un suscriptor, no un sensor.

## Qué recopilamos

**Nada.** El visor:

- no tiene **cámara** y no captura imágenes;
- no solicita **ubicación** y no registra datos GPS;
- no tiene **cuentas de usuario** y no pide información personal;
- no ejecuta **ninguna analítica, publicidad ni rastreo de terceros** de
  ningún tipo.

No existe **ningún backend alojado operado por el desarrollador**. El
desarrollador no recibe ninguno de sus datos.

## Qué muestra

La aplicación se **suscribe** al broker que usted le indica y muestra los
datos de activos que recibe — los objetos, su estado y cualquier información
de ubicación o de perfil que el broker ya contiene. Esos datos se crean en
otro lugar (con la aplicación de captura) y se rigen por completo por **su**
broker y sus permisos. El visor ni los crea ni los almacena de forma
persistente; presenta el flujo en vivo mientras está en ejecución.

## Adónde van los datos

A ningún sitio nuevo. El visor solo **lee** de su broker. Nunca publica, nunca
escribe y nunca transmite datos al desarrollador ni a terceros.

## Almacenamiento y seguridad

- La aplicación conserva en el dispositivo únicamente los **ajustes de
  conexión al broker** que usted introduce, para poder reconectarse. Cualquier
  contraseña se guarda en el llavero (Keychain) de la plataforma, nunca en
  texto plano y nunca se escribe en los registros.
- Las conexiones con el broker pueden usar **TLS** (`mqtts`), de modo que los
  datos en tránsito van cifrados.

## Sus opciones

Como el visor no recopila nada, no hay nada de lo que desistir, que exportar o
que eliminar más allá de los ajustes de conexión al broker, que usted puede
cambiar o eliminar en el dispositivo en cualquier momento. Los datos de
activos mostrados se rigen por las reglas de retención y de acceso de *su*
broker.

## Menores

Hecate es una utilidad profesional/de campo y no está dirigida a menores.

## Cambios en esta política

Si cambia el tratamiento de datos de la aplicación, esta página se
actualizará.
