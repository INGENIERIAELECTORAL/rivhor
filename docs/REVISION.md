# Informe de revisión de la web implementada

Fecha de la revisión: 24 de octubre de 2026.
Motor: Chromium (Playwright, headless, Linux). WebKit y Firefox no estaban disponibles en el entorno y no se han probado.
Servidor de pruebas: `python3 -m http.server 8000 --directory public`.
Capturas revisadas en `docs/capturas/` (reducidas al 50 % cuando superan 900 px de ancho).

## Rutas revisadas

Las 14 páginas principales y las dos páginas 404, por ruta directa con recarga.

`/`, `/es/`, `/office/`, `/es/office/`, `/data/`, `/es/data/`, `/development/`, `/es/development/`, `/campaign-systems/`, `/es/campaign-systems/`, `/impact/`, `/es/impact/`, `/cybersecurity/`, `/es/cybersecurity/`, `/404.html`, `/es/404.html`.

## Matriz de anchos

Anchos CSS 320, 360, 390, 430, 768, 820, 1024, 1280 y 1440 px, altura de ventana 900 px, orientación vertical, factor de escala 1. Las 16 rutas en cada ancho (144 combinaciones). Antes de medir se esperó a `networkidle` y `document.fonts.ready`, se abrieron todos los `details` (bios y campos opcionales del formulario) y se recorrió la página completa.

Resultado por combinación

- `documentElement.scrollWidth` igual a `clientWidth` en las 144 combinaciones. Sin desplazamiento horizontal.
- Ningún elemento con caja fuera del ancho disponible (medición de `getBoundingClientRect` sobre todos los elementos del cuerpo, excluyendo el interior de SVG decorativos).
- Fondo calculado de `html`, `body` y cabecera `rgb(255, 255, 255)` en todas.
- Sin mensajes de error ni advertencia en consola, sin errores de página, sin recursos fallidos ni respuestas HTTP 4xx/5xx.

Inspección visual de capturas (no solo medición): inicio EN y ES a 320, 390, 768 y 1440; Office EN y ES a 390, 1024 y 1440; Data ES a 1440; 404 a 768. Se revisaron cabecera, hero, bloque Office, tarjetas de fundadores con bios abiertas, línea del tiempo, otras líneas, formulario, cierre y pie.

## Pruebas adicionales

| Prueba | Resultado |
| --- | --- |
| Preferencia de sistema oscura (`color-scheme: dark`) en `/es/` a 1280 px | Fondo de `html`, `body`, cabecera y pie blanco. `color-scheme` calculado `light`. |
| Movimiento reducido en `/` a 390 px | Ningún bloque `.rv` con opacidad distinta de 1. Ningún trazo SVG con `stroke-dashoffset` distinto de 0. |
| Fuentes bloqueadas (peticiones `.woff2` abortadas) en `/es/` y `/es/office/` a 360 px | Sin desbordamiento con las fuentes de respaldo. Captura revisada. |
| Zoom 200 % (ventana de 1440 px con escala 2, anchura efectiva 720 px) en `/es/` | Sin desbordamiento. Captura revisada. |
| Anchura efectiva 320 px | Cubierta por la matriz en ambos idiomas. |
| Sin JavaScript en `/es/` a 390 px | Navegación visible, bios completas presentes en el HTML, formulario con `action`, `method="post"`, `required` en correo y autorización, autorización sin marcar, `noValidate` desactivado. Ningún bloque oculto. |
| Teclado en `/` a 390 px | Primer Tab llega al enlace Ir al contenido. El botón de menú recibe foco, abre con Enter (`aria-expanded="true"`), el selector de idioma sigue visible, Escape cierra y devuelve el foco al botón. `overflow` del cuerpo `visible` tras cerrar. Al pulsar un enlace del menú, el menú se cierra. |
| Anclas con cabecera fija | `#team` queda a 159 px del borde superior con la cabecera terminando en 79 px. `#form-es` queda a 100 px con la cabecera en 79 px. Ningún título oculto. |
| Bios | `details` abre y cierra con Enter, el foco permanece en `summary`. Texto completo legible y desplazable con la página. |
| Selector de idioma | En las 14 páginas principales el enlace lleva a la ruta equivalente y cambian `html lang`, `title` y `description`. Cada página tiene un único `h1`, `main` y `footer`. Desde `/office/#form-en` el selector lleva a `/es/office/#form-es`. Desde `/es/#progress` lleva a `/#progress`. Sin JavaScript el selector lleva a la ruta equivalente (sin conservar ancla). |
| Enlaces y recursos | 57 destinos internos únicos (páginas, anclas, CSS, JS, imágenes, fuentes) comprobados con HTTP 200 y existencia de cada ancla en su destino. Sin enlaces rotos. |
| Texto público | Comprobación automática de dos puntos y punto y coma en el texto visible y en atributos `alt`, `placeholder`, `aria-label`, `content`, `value`, `title` y `legend` de las 16 páginas. Sin apariciones (se excluyen URL y código). |
| Contenido antiguo | Sin correos de ejemplo, ubicación del pie, modo oscuro ni referencias a Vigenta. Contacto único `hi@rivhor.com`. |

## Formularios (red interceptada, sin envíos reales)

Los cuatro formularios (general EN `#waitlist`, general ES `#lista-espera`, Office EN `#form-en`, Office ES `#form-es`) se probaron a 430 px con el endpoint `https://formspree.io/f/mwllvkqw` interceptado por Playwright. Se añadió además un bloqueo general de `https://formspree.io/**` para registrar cualquier petición no interceptada. Resultado: 0 peticiones salieron hacia Formspree. Correo de prueba `prueba@example.com`, nombre y negocio ficticios.

| Caso | Resultado en los cuatro formularios |
| --- | --- |
| Envío vacío | Sin petición. Errores de correo y autorización visibles en su idioma. Mensaje general. Foco en el campo de correo. |
| Correo inválido y sin autorización | Sin petición. Error de formato de correo y de autorización. Sin éxito. |
| Correo válido sin autorización | Sin petición. Error de autorización y foco en la casilla. |
| Éxito simulado (`200`, `{"ok": true}`) con doble clic y Enter durante el envío | Una sola petición. Botón deshabilitado y texto de envío durante la espera. Después el formulario se oculta, aparece el bloque de confirmación y recibe el foco. `localStorage`, `sessionStorage` y cookies vacíos. URL sin parámetros. |
| Payload capturado | `POST`, `Accept: application/json`, `multipart/form-data` con boundary generado por el navegador. Campos `subject`, `source`, `product`, `language`, `consent_message`, `email`, `name`, `company`, `updates_optin=yes` y, en Office, `modules` con las dos selecciones múltiples. Valores de `product`, `source` y `language` correctos en cada variante. |
| `422` con error de campo `email` | Sin éxito. Error de correo marcado y mensaje general. Datos conservados. Botón activo. |
| `400` sin error de correo | Sin éxito. Mensaje de no confirmado. Datos conservados. |
| `403` | Sin éxito. Mensaje de verificación adicional y aparece el botón nativo. Datos conservados. Al pulsar explícitamente el botón nativo se realiza un `POST` normal (`Accept` de documento HTML) hacia el endpoint, interceptado en la prueba. No se envía nada sin pulsarlo. |
| `429` | Sin éxito. Mensaje de límite temporal. Datos conservados. |
| `500` | Sin éxito. Mensaje de no confirmado. Datos conservados. |
| `200` con HTML | Sin éxito. Mensaje de no confirmado. Datos conservados. |
| Fallo de conexión | Sin éxito. Mensaje de conexión que advierte que la solicitud podría haberse recibido. Datos conservados. Sin reintento. |
| Timeout (respuesta retenida 25 s, aborto a los 20 s) | Sin éxito. Mismo mensaje de conexión. Datos conservados. Botón vuelve a estar activo. Una sola petición. |

En todos los casos de error el mensaje recibe el foco, es legible y no se recorta. La lista de espera general y la de Office usan IDs distintos y cada ruta sirve solo su idioma.

## Problemas detectados y corregidos durante la revisión

1. Titular del hero con una palabra huérfana ("A" / "Un") al final de la primera línea. Se mostró la segunda frase como bloque propio.
2. Párrafos sin separación en el bloque destacado de Office y en los módulos de la página Office. Se añadió separación entre párrafos.
3. Separación excesiva entre el hero y el texto en las páginas de detalle. Se redujo el relleno.
4. Botón de menú en una segunda fila a 320 px. A 430 px o menos el botón muestra solo el icono con su nombre accesible oculto visualmente, de modo que logo, idioma y menú caben en una fila.
5. Enlaces de navegación de las páginas 404 apuntaban a anclas inexistentes de la propia página. Ahora apuntan al inicio del idioma correspondiente.

## Pendiente o no ejecutado

- WebKit y Firefox no estaban disponibles. No se afirma su compatibilidad.
- No se probó en dispositivos físicos ni en navegadores de escritorio con interfaz gráfica. La prueba de zoom 200 % se aproximó con escala de dispositivo 2 y ventana de 720 px, no con el zoom del navegador.
- Formspree: no se ha verificado en el panel el destinatario `hi@rivhor.com`, su verificación, restricciones de dominio, filtros ni condiciones del plan. Las respuestas aceptadas en las pruebas fueron simuladas y no demuestran la entrega de notificaciones al buzón. Revisar antes de lanzar.
- Las redirecciones de Vercel (`cleanUrls`, `trailingSlash`) y el servicio automático de `404.html` no se han comprobado en Vercel, solo la existencia física de las rutas.
- Sin dominio confirmado no se han añadido `canonical`, `hreflang` absolutos, Open Graph, sitemap ni robots. El README documenta cómo añadirlos.
- No se ha hecho push ni despliegue. GitHub y Vercel se conectarán después.
