# Primeros pasos

*De un broker vacío a su primer objeto capturado — en unos veinte minutos.*

Hecate no ejecuta **ningún backend**. No hay cuenta que crear ni servidor
nuestro entre sus dispositivos y sus datos — lo que también significa que no
existe un lugar predeterminado al que vayan sus capturas. El **broker MQTT es
la pieza que falta en el medio, y es suyo**. Esta página lo pone en marcha y
recorre un flujo de principio a fin.

!!! tip "Lo que necesita"

    1. **Un broker MQTT accesible** — el suyo o una instancia de evaluación gratuita.
    2. **[Hecate Admin](../admin/index.md)** en un iPhone o iPad, para crear y publicar el flujo.
    3. **[Hecate Capture](../capture/index.md)** en el dispositivo que vaya a escanear.

    El [Viewer](../viewer-ios/index.md) es opcional para una primera prueba — y gratuito en todo caso.

## 1 · Elegir un broker

Hecate habla MQTT estándar y no está atado a ningún broker concreto.

**Si ya opera MQTT**, úselo. Lo que Hecate necesita:

| Requisito | Para qué |
| --- | --- |
| MQTT 3.1.1 o 5 | el protocolo que hablan las apps |
| **Mensajes retenidos** (retained) | así llega un flujo publicado a un dispositivo que estaba desconectado al publicarse |
| TLS | las apps usan por defecto `mqtts` en el puerto `8883` con validación de certificado |
| Credenciales por cliente | para que cada dispositivo sea su propia identidad y pueda revocarse por separado |
| Permisos por topic | para que el Viewer sea de solo lectura de hecho, no solo por convención |

**Si no**, una instancia de evaluación alojada se crea en minutos y no cuesta
nada a escala de prueba. HiveMQ Cloud y EMQX Serverless tienen plan gratuito; un
contenedor Mosquitto en un portátil basta para una primera prueba en una red.

!!! warning "Un broker sin mensajes retenidos parecerá funcionar"

    Los dispositivos sencillamente nunca recibirán un flujo que no estuvieran ya
    escuchando en el instante exacto de su publicación. Compruebe esta capacidad
    antes de depurar cualquier otra cosa.

## 2 · Conectar la app Admin

<div class="shots">
  <figure><img src="/assets/screens/es/gs-broker-connection.png" alt="Ajustes de conexión del broker — host, puerto, protocolo y TLS"><figcaption>Conexión: host, puerto, TLS</figcaption></figure>
  <figure><img src="/assets/screens/es/gs-broker-auth.png" alt="Autenticación del broker — usuario y contraseña"><figcaption>Autenticación</figcaption></figure>
</div>

Los valores por defecto son los seguros, y debería costar trabajo debilitarlos:

| Ajuste | Por defecto |
| --- | --- |
| Esquema | `mqtts` — el `mqtt` simple existe y avisa |
| Puerto | `8883` |
| TLS | activado |
| Validar certificado | activado — desactívelo solo para un broker de desarrollo con certificado autofirmado |

Las credenciales van directamente al **llavero** del dispositivo, cifradas en
reposo. Nunca se escriben en un flujo, nunca se publican al broker y nunca
viajan en un código QR de aprovisionamiento.

Cuando la prueba de conexión funcione, **publique un flujo**. Manténgalo trivial
en la primera vuelta: un solo paso de escaneo y un campo de texto demuestran
toda la cadena. Un proceso real mal modelado no demuestra nada.

## 3 · Aprovisionar los dispositivos de campo

Una contraseña de veinte caracteres tecleada veinte veces en un terminal de
empuñadura tipo pistola: así muere un piloto antes de empezar. Hecate
aprovisiona mediante código QR.

<div class="shots">
  <figure><img src="/assets/screens/es/gs-broker-share-qr.png" alt="Compartir la configuración del broker como código QR"><figcaption>Compartir la configuración</figcaption></figure>
  <figure><img src="/assets/screens/es/gs-provisioning.png" alt="El dispositivo confirma las coordenadas del broker recibidas"><figcaption>El dispositivo confirma</figcaption></figure>
</div>

El código lleva las **coordenadas**: host, puerto, ajustes TLS, prefijos de
topics y los niveles opcionales de Unified Namespace. **No** lleva la
contraseña: un código QR colgado en la pared de un almacén es una credencial
entregada a todo el que pase. Cada dispositivo recibe una vez su propio usuario
y su propia contraseña, y ambos van al llavero.

Donde un MDM gestiona los dispositivos, esas mismas coordenadas pueden enviarse
como Managed App Configuration, y allí las credenciales *sí* pueden viajar con
ellas: una carga MDM es un canal administrativo, no un cartel. Ese canal está
implementado y verificado en campo en Android; en iOS está especificado y aún no
construido.

## 4 · Capturar — y comprobarlo usted mismo

El flujo aparece solo en el dispositivo de campo. Sin descarga, sin
actualización de la app: es el mensaje retenido haciendo su trabajo.

<div class="shots">
  <figure><img src="/assets/screens/es/capture-sent.png" alt="Objetos entregados, confirmados por el broker"><figcaption>Enviado — la captura llegó al broker</figcaption></figure>
</div>

Escanee, rellene, guarde. La validación ocurre **en el dispositivo**, contra las
reglas que escribió el autor: los datos malos nunca salen de él. ¿Sin cobertura?
Capture igualmente — las capturas terminadas esperan en una bandeja de salida y
se envían cuando vuelve la conexión. Un contador de bandeja que baja es la señal
honesta de que el broker acepta sus mensajes.

**Mire ahora el broker con algo que no sea nuestro.** Conecte
[MQTT Explorer](http://mqtt-explorer.com/) con cualquier credencial que pueda
suscribirse: el flujo retenido está bajo el prefijo de configuración, y su
captura aparece bajo el prefijo de objetos menos de un segundo después de
guardar.

Ese último paso pesa más de lo que parece. Demuestra que los datos están en *su*
infraestructura, en un formato que usted puede leer, accesibles para sistemas
que nunca han oído hablar de Hecate. Ninguna app de Hecate depende de MQTT
Explorer — es una comodidad de diagnóstico, y debe seguir siéndolo.

## Qué vive dónde en el broker

Dos árboles, alineados segmento a segmento:

```text
hecate/config/profiles/<profileId>        el flujo      — RETENIDO
hecate/assets/<profileId>/<assetUuid>     una captura   — no retenido
```

- **Los flujos son retenidos.** Un dispositivo apagado toda la semana recibe el
  actual en cuanto se conecta. Retirar un flujo significa publicar una carga
  retenida vacía — desaparece entonces de todos los dispositivos.
- **Las capturas son eventos** y no se retienen. Nada obsoleto queda varado en
  una dirección antigua cuando se renombra un flujo.
- **El identificador del flujo es un nivel de topic propio.** Eso es lo que hace
  de `hecate/assets/<profileId>/#` un filtro utilizable en lugar de un montón
  plano de UUID.

Ambos prefijos son configurables y viajan en el QR de aprovisionamiento. Si
opera un Unified Namespace, active la jerarquía y el árbol de objetos encaja en
ella:

```text
<enterprise>/<site>/<area>/<line>/assets/<profileId>/<assetUuid>
acme/plant1/line3/assets/goods-in/1E935809-BF49-4716-B1D6-40F572FECE5B
```

Las capturas llegan como un sobre autodescriptivo `{ header, data }`. Cualquier
sistema aguas abajo — historian, panel, pasarela ERP — puede suscribirse y
leerlo sin pedirnos nada.

## Permisos

Dé a cada instalación de Capture **su propio usuario de broker**: `capture-001`,
`capture-002`. Cuesta minutos en la puesta en marcha y aporta trazabilidad,
revocación por dispositivo, rotación aislada de credenciales y una respuesta de
auditoría que es un registro de topics en lugar de un encogimiento de hombros.

| App | Flujos: suscribir | Flujos: publicar | Capturas: suscribir | Capturas: publicar |
| --- | :---: | :---: | :---: | :---: |
| **Admin** | sí | **sí** | sí | no |
| **Capture** | sí | no | no | **sí** |
| **Viewer** | sí | no | sí | no |

Como reglas del broker:

```text
capture-001   SUBSCRIBE  hecate/config/profiles/#
              PUBLISH    hecate/assets/#

viewer-lobby  SUBSCRIBE  hecate/config/profiles/#
              SUBSCRIBE  hecate/assets/#

admin-anna    SUBSCRIBE  hecate/config/profiles/#
              PUBLISH    hecate/config/profiles/#
              SUBSCRIBE  hecate/assets/#
```

!!! note "Imponga el Viewer de solo lectura, no confíe en él"

    El Viewer no publica nada; así está construido. Aun así, dele una cuenta que
    solo pueda suscribirse. Un permiso que impone el broker sobrevive a una mala
    configuración, a una versión futura y a un dispositivo que instale otra
    persona.

## Cuando no funciona

| Síntoma | Causa habitual | Comprobar |
| --- | --- | --- |
| Broker inalcanzable | DNS, cortafuegos, puerto equivocado | alcanzar el host desde la misma red y el mismo puerto |
| Conexión rechazada | endpoint incorrecto, broker caído | comparar el endpoint con la consola del broker, carácter a carácter |
| Fallo de autenticación | usuario o contraseña | volver a introducirlos; el llavero conserva el anterior hasta entonces |
| Fallo de autorización | permisos de topic | la credencial conecta pero no puede tocar ese topic |
| Fallo del handshake TLS | certificado o confianza | una CA privada necesita su raíz en el dispositivo |
| No aparece ningún flujo | mensaje retenido, prefijo o permiso de suscripción | búsquelo en un explorador bajo el prefijo de configuración |
| La captura no llega | permiso de publicación, o sin conexión | una bandeja que nunca se vacía significa publicación denegada |
| El Viewer sigue vacío | permiso de suscripción al árbol de objetos | necesita el prefijo de objetos, no solo el de flujos |

La distinción que conviene interiorizar: la **autenticación** es quién es usted;
la **autorización** es qué puede tocar esa identidad. Un dispositivo que conecta
sin problemas y no publica nada ha superado la primera y fallado la segunda — y
la solución está en las reglas del broker, no en la app.

## Después de la evaluación

La instalación piloto y la de producción se diferencian en la gestión de
identidades, no en la arquitectura. Nada de lo construido en la prueba se tira.

- **Certificados en lugar de contraseñas.** El TLS mutuo (mTLS) da a cada
  dispositivo un certificado de cliente y un ciclo de vida real: emisión,
  renovación, revocación. **No** comparta un mismo certificado entre todos los
  dispositivos: eso recrea el problema de la contraseña compartida con más
  ceremonia.
- **Roles en lugar de reglas por dispositivo.** Añadir el quincuagésimo terminal
  debería ser una asignación de rol, no cinco líneas de ACL.
- **Encaje su espacio de nombres ahora**, en lugar de migrar después. El topic
  cambia; la carga útil no.
- **Conecte lo de aguas abajo.** El Viewer es una ventana en vivo, no un almacén
  de datos: mantiene las capturas en memoria y filtra en el cliente. Para
  histórico y analítica, suscriba un sistema que ya posea. Esa frontera es
  deliberada.

---

¿Atascado en algún punto? [Soporte Admin](../support/admin/index.md) ·
[Soporte de operador](../support/operator/index.md)
