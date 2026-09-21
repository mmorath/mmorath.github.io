# Política de privacidad — Hecate Admin

**Fecha de entrada en vigor:** 2026-06-18
**Desarrollador:** Matthias Morath

Hecate Admin es una **herramienta de redacción**. Se utiliza para crear y
publicar los **perfiles** que configuran la aplicación de captura y para
establecer la conexión con su broker MQTT. No es una aplicación de
recopilación de datos.

## Qué recopilamos

**Ni telemetría ni datos personales.** La aplicación de administración:

- no solicita **ubicación** y no tiene **cámara**;
- no ejecuta **ninguna analítica, publicidad ni rastreo de terceros**;
- no envía **nada** al desarrollador — no existe **ningún backend alojado**.

## Qué maneja

- **Los perfiles que usted redacta.** Un perfil describe los campos y los
  pasos de un flujo de captura. Los perfiles son **configuración, no datos
  personales**, y **no deben contener secretos** — son ampliamente legibles
  por los dispositivos que se suscriben a ellos.
- **Las credenciales del broker.** Para publicar perfiles, la aplicación se
  conecta a **su** broker MQTT con credenciales de administrador. La
  contraseña se guarda en el **llavero (Keychain)** de la plataforma — nunca
  en texto plano, nunca se escribe en un perfil, en un QR de aprovisionamiento
  ni en un registro, y nunca se transmite a ningún sitio salvo para
  autenticarse ante su broker.

## Adónde van los datos

El único destino de red es el **broker MQTT que usted configura**. La
aplicación de administración publica allí los perfiles (como mensajes
retenidos, *retained*) por indicación suya. No transmite nada al desarrollador
ni a terceros, y no hay publicidad, elaboración de perfiles ni rastreo entre
aplicaciones.

## Almacenamiento y seguridad

- Los perfiles y los ajustes de conexión se almacenan **en su dispositivo**.
- La **contraseña del broker se guarda en el llavero (Keychain)**.
- Las conexiones con el broker pueden usar **TLS** (`mqtts`), de modo que los
  datos en tránsito van cifrados.

## Sus opciones

- **Credenciales:** se almacenan solo en el dispositivo; elimínelas en
  cualquier momento.
- **Perfiles:** usted los redacta, los publica y los retira; retirar un perfil
  borra su mensaje retenido en su broker.

## Informes de diagnóstico que usted nos envía

Hay una única excepción a todo lo anterior, y la decisión es suya cada vez: en
**Ajustes → Registro de eventos** puede **enviarnos** un informe si desea ayuda.
Nunca ocurre por sí solo.

- Usted ve el informe **completo** antes de que salga del dispositivo: nada se
  añade después de esa pantalla.
- Usted decide **en cada ocasión**.
- Lo envía desde **su propia aplicación de correo**. La app no envía nada en
  segundo plano; no existe ningún servidor nuestro al que pudiera enviarlo.
- Contiene: dispositivo y versión del sistema, versión de la app y del núcleo,
  su plan (free/pro) y líneas de registro. **Nunca** fotos, ubicaciones,
  contraseñas, tokens ni credenciales del broker: los patrones correspondientes
  se sustituyen antes del envío.
- Un **comentario** y una **dirección de respuesta** son opcionales. Usamos la
  dirección únicamente para responder a ese informe.

Si prefiere quedarse el informe o dárselo a su propio departamento de TI:
«Compartir …» en la misma pantalla se lo entrega como archivo de texto, sin que
nosotros veamos nada.

## Menores

Hecate es una utilidad profesional y no está dirigida a menores.

## Cambios en esta política

Si cambia el tratamiento de datos de la aplicación, esta página y la pantalla
de privacidad dentro de la aplicación se actualizarán conjuntamente.
