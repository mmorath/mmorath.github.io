# Política de privacidad — Hecate Capture

**Fecha de entrada en vigor:** 2026-06-11
**Desarrollador:** Matthias Morath

Hecate es una herramienta de campo para georreferenciar objetos físicos.
Recopila únicamente lo necesario para identificar y localizar los activos que
usted registra. No existe **ningún backend alojado operado por el
desarrollador**, ni **analítica o rastreo de terceros** de ningún tipo.

## Qué recopilamos

Lo que la aplicación captura está **definido por completo por el perfil** que
configura el administrador de su organización — un perfil es un formulario
personalizable que describe los campos y los escaneos de un caso de uso.
**Nosotros, como desarrollador, ni creamos esos perfiles ni vemos jamás los
perfiles o los datos que usted captura con ellos.** Lo que recopila una
instalación concreta lo decide, por tanto, *su* administrador, no nosotros.

Para un perfil típico, la aplicación maneja:

- **Datos del activo** que usted introduce o escanea (p. ej., número de serie,
  número de pedido, tipo).
- **Ubicación precisa (GPS)** en el momento de la captura — *solo si usted
  concede el permiso de ubicación*. Puede rechazarlo o revocarlo en cualquier
  momento en los Ajustes de iOS; la aplicación sigue funcionando sin él.

## Adónde van los datos

Los datos de los activos se publican **únicamente en el broker MQTT que usted
configura**. Usted elige y controla ese broker. El desarrollador no opera
ningún servidor, no recibe ninguno de sus datos y nunca ve los perfiles que
usted utiliza ni los activos que captura con ellos. No hay publicidad, ni
elaboración de perfiles, ni rastreo entre aplicaciones o sitios web.

## Almacenamiento y seguridad

- Los activos se almacenan **en su dispositivo** hasta que usted los elimina.
- La **contraseña del broker se guarda en el llavero de iOS (Keychain)** —
  nunca en texto plano y nunca se escribe en los registros.
- Las conexiones con el broker pueden usar **TLS** (`mqtts`), de modo que los
  datos en tránsito van cifrados.

## Compartición de datos

**No** vendemos, alquilamos ni compartimos sus datos con terceros. La única
transmisión es la publicación en **su propio** broker MQTT, realizada en su
nombre y por indicación suya.

## Sus opciones

- **Ubicación:** conceda, rechace o revoque el permiso en cualquier momento en
  Ajustes de iOS → Privacidad.
- **Fotos:** ninguna. Hecate Capture **no puede** tomar fotos — la capacidad
  fue eliminada, no desactivada, porque una foto no puede viajar a un broker
  MQTT y Hecate no opera ningún backend de imágenes. Leer un código QR *desde*
  una foto que usted elige es algo distinto: la imagen se decodifica en el
  dispositivo y nunca se almacena ni se envía.
- **Eliminación:** elimine cualquier activo en el dispositivo en cualquier
  momento. Los datos ya publicados en su broker se rigen por la retención de
  *su* broker.

## Menores

Hecate es una utilidad profesional/de campo y no está dirigida a menores.

## Cambios en esta política

Si cambia el tratamiento de datos de la aplicación, esta página y la pantalla
**Ajustes → Privacidad** dentro de la aplicación se actualizarán conjuntamente.
