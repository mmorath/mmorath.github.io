---
hide:
  - toc
---

# Leaf Relief

*Un archivo sin papel para tu Mac*

**Próximamente en el Mac App Store.**

Leaf Relief convierte el papel en un archivo en el que puedes buscar: sin cuenta,
sin nube, **completamente en tu Mac**. Escanea papel o deja archivos en una carpeta
de entrada: la app reconoce el texto, archiva cada documento con el nombre que
elijas, propone título, tipo, remitente, fecha, importe y etiquetas, y lo encuentra
todo de nuevo, por texto completo, en lenguaje natural o por significado.

## En un minuto

- **Escanear o importar.** Los escáneres AirScan de la red y los escáneres USB con
  controlador para macOS escanean directamente en la app; cualquier otro escáner,
  descargas o fotos pasan por la carpeta de entrada.
- **PDF en los que se puede buscar.** Las páginas se enderezan, el texto se
  reconoce y se añade al PDF como capa en la que se puede buscar.
- **Archivado a tu manera.** Archivos PDF normales en tu propia carpeta, ordenados
  en las subcarpetas y con los nombres que tú defines; etiquetas y tipos como
  etiquetas del Finder.
- **Sugerencias en el dispositivo.** Apple Intelligence propone tipo, remitente,
  título, fecha, importe, plazo, IBAN y etiquetas, en tu Mac. No se aplica nada
  hasta que haces clic.
- **Encontrado de nuevo.** Texto completo, lenguaje natural («facturas del año
  pasado de más de 100 €»), búsqueda por significado, Spotlight y Atajos.
- **Prueba.** Cada archivado y cada cambio de página se registra y se firma con una
  clave del Secure Enclave.
- **Sin cuenta, sin nube, sin rastreo.** El desarrollador no recibe ningún dato de
  la app.

## Capturas de pantalla

<div class="shots">
  <figure class="wide"><img src="/leafrelief/assets/screens/en/light.png" alt="Leaf Relief en modo claro: barra lateral con bandeja de entrada, tipos y etiquetas, la lista de documentos de demostración, la vista previa de una factura con campos resaltados y sugerencias de tipo, remitente y etiquetas"><figcaption>Claro</figcaption></figure>
  <figure class="wide"><img src="/leafrelief/assets/screens/en/dark.png" alt="Leaf Relief en modo oscuro: el archivo con documentos de demostración, la vista previa y sugerencias de tipo, remitente y etiquetas"><figcaption>Oscuro</figcaption></figure>
</div>

*Las capturas muestran un archivo de demostración con documentos inventados y la
interfaz en inglés.*

## El problema

Cada semana llega papel –facturas, contratos, nóminas, cartas de Hacienda– y la
mayor parte hay que guardarla durante años.

### Montones de papel

Carpetas y cajas se llenan. Encontrar la carta del seguro del año pasado significa
hojearlas todas.

### PDF dispersos

Lo que ya es digital está en Descargas, en el escritorio y en adjuntos de correo,
con nombres como `scan0042.pdf`.

### Sin búsqueda

Una página escaneada es solo una imagen. Sin capa de texto, ni el Finder ni
Spotlight encuentran en ella una sola palabra.

### Servicios en la nube que leen tus documentos

Muchos servicios de archivo lo resuelven subiendo tus documentos y analizándolos en
sus servidores, incluidos extractos bancarios, informes médicos y contratos.

---

### En resumen

| Problema | |
| --- | --- |
| Montones de papel | encontrar una carta significa revisar cada carpeta |
| PDF dispersos | archivos por todas partes, con nombres sin sentido |
| Sin búsqueda | las páginas escaneadas son imágenes sin texto |
| Archivado a mano | cada documento necesita nombre, carpeta y etiquetas a mano |
| Servicios en la nube | tus documentos más privados acaban en servidores ajenos |

[:octicons-arrow-right-24: Cómo resuelve Leaf Relief cada uno de estos puntos](#que-hace-leaf-relief)

## Qué hace Leaf Relief

Leaf Relief recorre todo el camino del papel a un archivo en el que se puede buscar
en una sola app para Mac, y mantiene cada paso en tu Mac.

### Escanear o importar

- **Escanea** con escáneres AirScan de la red y escáneres USB con controlador para
  macOS, los que macOS ya conoce. Alimentador antes que cristal, doble cara si el
  alimentador lo permite, 300 ppp, modo de color *Automático*: las páginas sin
  color apreciable se guardan en escala de grises.
- **Sigue cada paso**: Escanear → Texto → Archivar → Índice, con el número de
  páginas. Puedes cancelar en cualquier momento.
- **Importa** desde la carpeta de entrada: cualquier otro escáner, descargas o
  fotos; déjalos ahí y Leaf Relief los archiva. Acepta PDF, JPEG, PNG, HEIC y TIFF;
  los PDF que ya contienen texto se toman sin cambios, las imágenes y los PDF solo
  de imagen reciben una capa de texto.
- **El reconocimiento de texto** usa el framework Vision de Apple, en español,
  inglés, alemán y francés. Antes, las páginas se enderezan; la capa de texto
  invisible queda exactamente sobre la imagen, así que seleccionar y copiar en
  Vista Previa da con la palabra.

### Archiva a tu manera

- **Subcarpetas** por año, por año y mes, por tipo, o por año y tipo, o ninguna.
- **Nombres de archivo** con fecha, tipo, un sufijo y el número de páginas; un
  nombre que ya existe recibe `-2`, `-3`…
- **Archivos PDF normales** en tu propia carpeta. Etiquetas y tipos son etiquetas
  del Finder, los campos viajan con el archivo. El índice de la app es solo un
  índice: la fuente es el PDF.
- **Tus propios tipos** con nombre, color y símbolo, junto a los incluidos.

### Sugerencias en el dispositivo

- **Apple Intelligence** lee el documento y propone tipo, remitente, título, fecha,
  importe, plazo, número de expediente, IBAN, un resumen y etiquetas, en tu Mac y en
  el idioma del documento. Ningún texto se envía a un modelo en la nube.
- **Sin Apple Intelligence**, unas reglas sencillas proponen lo que pueden: fechas,
  importes, IBAN con dígito de control, números de cliente, factura y contrato, y
  formas jurídicas como GmbH, Ltd o Inc. Las reglas entienden documentos en alemán
  e inglés.
- **Tú decides.** Las sugerencias se guardan y nunca se aplican solas. Los campos
  reconocidos se resaltan en la vista previa; un clic los aplica.

### Encuéntralo

- **Texto completo** en todo el archivo.
- **Lenguaje natural**: «facturas del año pasado de más de 100 €» se convierte en
  filtros de tipo, remitente, periodo e importe.
- **Búsqueda por significado**, para cuando recuerdas de qué trataba un documento
  pero no sus palabras. La búsqueda por significado entiende español, francés,
  alemán e inglés; la búsqueda en lenguaje natural, alemán e inglés.
- **Spotlight** también encuentra tus documentos; un resultado abre el documento
  en la app.
- **Atajos y Siri**: «Escanear documento», «Buscar documento», «Abrir último
  escaneo».
- **Los archivos que solo están en iCloud** no se descargan; se indexan por su
  nombre, sus campos y sus etiquetas.

### Prueba: un registro de cambios firmado

- **Cada archivado, importación y cambio de página**, incluidos los cambios hechos
  fuera de la app, por ejemplo en Vista Previa, se registra como eslabón de una
  cadena de hashes y se firma con una clave del Secure Enclave de este Mac.
- **Un sello** en cada documento indica lo que se sabe: *Sin cambios desde el
  escaneo*, *Editado (n×), cadena válida* o *Verificación fallida* con el motivo.
- **Exporta** un informe de verificación y la clave pública.
- **Sellos de tiempo (opcionales, desactivados por defecto)**: si los activas, solo
  una suma de comprobación (SHA-256) de cada entrada va a un servicio de sellado de
  tiempo, nunca el documento.

### Editar páginas

- **Girar, mover y eliminar páginas**, con deshacer.
- **El original se conserva.** Cada cambio se construye a partir del original, así
  que las páginas eliminadas pueden volver.
- **Corregir orientación automáticamente** endereza las páginas torcidas con el
  mismo reconocimiento que al escanear.

### Plazos y compartir

- **Plazos como recordatorios**, creados solo cuando haces clic en «Crear
  recordatorio».
- **Compartir y enviar por correo** una copia con el título como nombre, sin tus
  etiquetas ni tipos privados.
- **Un icono en la barra de menús** muestra el escaneo, el progreso y el número de
  documentos en la bandeja de entrada.

---

### Cómo resuelve cada problema

| Problema | Cómo lo resuelve Leaf Relief |
| --- | --- |
| Montones de papel | Escanear con el escáner que macOS ya conoce, directamente al archivo |
| PDF dispersos | Una carpeta de entrada para todo lo demás; archivado automático |
| Sin búsqueda | Una capa de texto en cada PDF; texto completo, lenguaje natural y significado |
| Archivado a mano | Carpetas y nombres según tu patrón; sugerencias de tipo, remitente y etiquetas |
| Servicios en la nube | Reconocimiento, sugerencias y búsqueda en tu Mac; sin cuenta, sin servidor |

## Privacidad

Leaf Relief **no tiene backend, ni cuenta, ni analítica, ni publicidad, ni
rastreo**. Tus documentos se quedan en las carpetas que eliges; solo salen de tu
Mac cuando tú los compartes. Detalles en la
[política de privacidad](privacy/index.md).

## Requisitos

- macOS 26 o posterior en un Mac con chip de Apple.
- Para las sugerencias de Apple Intelligence: Apple Intelligence activado. Sin él,
  unas reglas sencillas hacen sugerencias.
- El escáner es opcional: AirScan en la red o USB con controlador para macOS;
  cualquier otro escáner funciona a través de la carpeta de entrada.
- En español, inglés, alemán y francés. Las reglas sencillas y la búsqueda en
  lenguaje natural entienden documentos en alemán e inglés.
- Leaf Relief crea PDF estándar con una capa de texto en la que se puede buscar;
  sin PDF/A.
- Compra única, sin compras dentro de la app. Próximamente en el Mac App Store.

---

[Política de privacidad](privacy/index.md) · [Soporte](support/index.md)
