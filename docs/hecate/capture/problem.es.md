# El problema

Las empresas operan una **proliferación de apps de un solo propósito** para
registrar datos a lo largo de sus pasos de proceso — una herramienta por caso
de uso, cada una construida de forma aislada. De ahí se derivan tres fallos.

## Calidad inconsistente

Cada app valida (o no valida) sus entradas de manera distinta, de modo que los
datos que llegan a los sistemas posteriores son desiguales y difícilmente
confiables.

## No habilitado para el uso móvil

Gran parte de esta captura sigue ocurriendo en un escritorio — no donde está
realmente el trabajo.

## Sin contexto de ubicación

Casi nada de esto está georreferenciado, de modo que un registro rara vez dice
**dónde** está realmente el objeto que describe.

---

## En resumen

| Dolor en la empresa | |
| --- | --- |
| Muchas apps de captura de un solo propósito | un nuevo build por caso de uso |
| Calidad de datos inconsistente | cada app valida de manera distinta |
| No habilitado para el uso móvil | la captura ocurre en un escritorio |
| Sin contexto de ubicación | los registros no dicen *dónde* |
| Infraestructura pesada / alta carga de TI | un backend y una gestión de dispositivos por herramienta |
| Acceso sin gobernanza | ninguna regla uniforme sobre quién puede capturar qué |

[:octicons-arrow-right-24: Cómo Hecate elimina cada uno de estos puntos](solution.md)
