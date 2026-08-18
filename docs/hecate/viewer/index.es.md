---
hide:
  - toc
---

# Hecate para Apple TV

*Una pantalla mural en vivo para sus activos de Hecate — solo lectura, en la
pantalla grande.*

La app de Hecate para Apple TV convierte cualquier pantalla en una **vista en
vivo de los objetos que su equipo está capturando**. Se conecta al mismo
broker MQTT que la aplicación de captura, **se suscribe** al flujo de activos
y muestra los registros a medida que llegan — en un monitor de planta, en una
oficina o en la entrada de una instalación.

Es un **visor puro**. No captura nada, no edita nada y no almacena nada
propio.

## En un minuto

- **En vivo, sin intervención.** Los activos aparecen y se actualizan a medida
  que se publican; la pantalla se mantiene al día sin interacción alguna.
- **Solo lectura por diseño.** El visor únicamente *se suscribe* — nunca
  publica en el broker y nunca escribe un perfil ni un activo.
- **Mismo broker, mismos datos.** Apúntelo a su broker y mostrará exactamente
  lo que sus credenciales tienen permitido leer. Los datos en sí no requieren
  configuración aparte.
- **No recopila nada.** Sin cámara, sin ubicación, sin cuentas, sin analíticas
  — es una pantalla, no un sensor.
- **Un solo producto.** El mismo formato de mensajes y el mismo lenguaje
  visual en blanco y negro que las demás apps de Hecate; el color proviene
  únicamente del acento de perfil de cada objeto.

## Qué muestra

El visor representa el flujo de activos en vivo del broker — los objetos, su
estado actual y (cuando existen) su ubicación y su acento de perfil. Como lee
los mismos perfiles retained y los mismos topics de activos que el resto del
sistema, lo que aparece en pantalla lo gobiernan por completo **su broker y
sus permisos**, no la app.

## Puesta en marcha

Conecte la app a su broker MQTT (host, puerto, TLS, credenciales). Una vez
conectada, el visor se suscribe y comienza a mostrar — no hay nada que
configurar sobre los datos en sí, porque los datos los definen sus perfiles y
los publica la aplicación de captura.

---

[:octicons-arrow-right-24: Privacidad](../privacy/viewer/index.md) ·
[:octicons-arrow-right-24: Soporte](../support/operator/index.md) ·
[:octicons-arrow-right-24: La aplicación de captura](../capture/index.md)
