# RIVHOR · Web institucional

Sitio estático bilingüe (inglés en `/`, español en `/es/`) de RIVHOR, un proyecto en desarrollo. HTML, CSS y JavaScript nativos, sin dependencias de compilación. Rivhor Office es el producto principal. Las otras cinco líneas (Data, Development, Campaign Systems, Impact y Cybersecurity) tienen página de detalle con su estado de preparación.

Estado del encargo: construido y revisado localmente. No se ha publicado ni conectado a GitHub o Vercel. Ver `docs/REVISION.md` para el informe de pruebas y los pendientes.

## Estructura

```
rivhor-web/
├── README.md
├── vercel.json              configuración estática para Vercel
├── .gitignore
├── public/                  la web completa, lista para servir tal cual
│   ├── index.html           inicio en inglés
│   ├── 404.html             página de error con accesos EN y ES
│   ├── office/ data/ development/ campaign-systems/ impact/ cybersecurity/
│   │   └── index.html       detalles en inglés
│   ├── es/
│   │   ├── index.html       inicio en español
│   │   ├── 404.html         error en español
│   │   └── office/ data/ development/ campaign-systems/ impact/ cybersecurity/
│   │       └── index.html   detalles en español
│   └── assets/
│       ├── css/styles.css   estilos compartidos (fondo blanco permanente)
│       ├── css/waitlist.css estilos del formulario recibido
│       ├── js/site.js       menú móvil, aparición suave, ancla al cambiar idioma
│       ├── js/waitlist.js   envío del formulario (POST nativo + fetch)
│       ├── brand/           logotipos PNG originales y favicons en contenedor cuadrado
│       ├── team/            retratos originales 400×400
│       └── fonts/           Outfit y Caveat (woff2) con sus licencias OFL
├── tools/
│   ├── build.py             generador local opcional de los HTML (Python 3, sin dependencias)
│   └── formulario-*.html    los cuatro fragmentos activos del formulario que inserta build.py
└── docs/
    ├── REVISION.md          informe de la revisión realizada y pendientes
    └── capturas/            capturas revisadas de escritorio y móvil
```

Catorce páginas principales (inicio y seis detalles por idioma) más dos páginas 404. Todas existen físicamente, abren por ruta directa con barra final y contienen su contenido en el HTML sin depender de JavaScript.

## Vista previa local

Desde la raíz del repositorio, con Python 3

```sh
python3 -m http.server 8000 --directory public
```

Abrir http://localhost:8000/ y http://localhost:8000/es/. Las páginas interiores responden en rutas como http://localhost:8000/office/ o http://localhost:8000/es/data/.

Sin Python se puede usar cualquier servidor de archivos estáticos que sirva la carpeta `public` desde la raíz, por ejemplo `npx serve public` si Node está instalado. Es necesario un servidor y no abrir los archivos con doble clic, porque los recursos se enlazan con rutas absolutas (`/assets/...`).

La vista previa local no reproduce las redirecciones de Vercel (`cleanUrls`, `trailingSlash`) ni sirve `404.html` automáticamente para rutas inexistentes. Los archivos sí responden en sus rutas físicas.

## Editar contenido

Hay dos formas válidas.

1. Editar directamente los HTML de `public/`. Es suficiente para cambios puntuales.
2. Editar los textos en `tools/build.py` y regenerar todo con `python3 tools/build.py` desde la raíz. Mantiene cabecera, pie, metadatos y enlaces de idioma coherentes en las 16 páginas. El generador solo usa la biblioteca estándar de Python. No es necesario para servir ni publicar la web.

Si se usa el generador, conviene no editar a mano los HTML generados, porque la siguiente regeneración los sobrescribe.

Reglas editoriales que sigue el sitio: fondo blanco en todas las páginas, sin modo oscuro, sin emojis, sin dos puntos ni punto y coma en textos públicos, Outfit para contenido y Caveat solo para anotaciones cortas.

## Formularios

Hay cuatro formularios (general EN/ES en inicio y Office EN/ES en su página) que envían a `https://formspree.io/f/mwllvkqw` con `method="POST"` nativo y mejora con `fetch` en `assets/js/waitlist.js`. Campos obligatorios `email` y `updates_optin` (sin marcar). Opcionales `name`, `company` y, solo en Office, `modules`. Campos ocultos `subject`, `source`, `product`, `language` y `consent_message`.

Solo se muestra confirmación cuando la respuesta HTTP es correcta y el JSON incluye `ok: true`. Los errores conservan lo escrito y no reintentan. No se guardan datos del formulario en el navegador.

Pendiente antes de publicar, en el panel de Formspree: comprobar que el destinatario es `hi@rivhor.com`, que está verificado, las restricciones de dominio, filtros y condiciones del plan. Las pruebas de este repositorio se hicieron con respuestas simuladas y no demuestran la entrega al buzón.

## Subir a GitHub

1. Crear un repositorio vacío en GitHub (o elegir uno existente). No incluir README, licencia ni `.gitignore` generados por GitHub para evitar conflictos.
2. Desde esta carpeta `rivhor-web`, que es la raíz del repositorio

```sh
git init
git add .
git commit -m "Web institucional de RIVHOR"
git branch -M main
git remote add origin <URL del repositorio>
git push -u origin main
```

Sustituir `<URL del repositorio>` por la dirección real. El contenido de esta carpeta es la raíz del repositorio, sin otra carpeta anidada.

No subir el paquete de materiales, las referencias originales ni archivos `.env`.

## Conectar a Vercel

1. En Vercel, importar el repositorio de GitHub.
2. Root Directory: la raíz del repositorio (dejar el valor por defecto).
3. Framework Preset: Other.
4. Build Command: vacío. Output Directory: `public`. `vercel.json` ya fija estos valores (`framework: null`, `buildCommand: ""`, `outputDirectory: "public"`, `cleanUrls: true`, `trailingSlash: true`).
5. No se necesitan variables de entorno ni claves. El endpoint de Formspree es público y está en el HTML.
6. Vercel sirve `public/404.html` para rutas inexistentes en sitios estáticos. Comprobarlo tras el primer despliegue.
7. Configurar el dominio cuando exista uno confirmado.

Configuración de Vercel consultada el 24 de octubre de 2026. Verificar cambios en https://vercel.com/docs/project-configuration/vercel-json al implementar.

## Metadatos pendientes de dominio

Cada página incluye `title`, `description` y enlaces `hreflang` relativos entre su versión en inglés y en español. Cuando exista dominio confirmado, añadir en el `head` de cada página (o en `tools/build.py` y regenerar)

- `<link rel="canonical" href="https://DOMINIO/ruta/">`
- `hreflang` con URL absolutas
- Open Graph (`og:title`, `og:description`, `og:image` con el logo completo)
- `public/sitemap.xml` y `public/robots.txt`

No se han incluido marcadores de posición ni analítica.

## Atribuciones y licencias

- Outfit. Copyright 2021 The Outfit Project Authors. SIL Open Font License 1.1. Licencia en `public/assets/fonts/LICENSE-Outfit.txt`.
- Caveat. SIL Open Font License 1.1. Licencia en `public/assets/fonts/LICENSE-Caveat.txt`.
- Logotipos, fotografías, textos y código de este sitio pertenecen a RIVHOR y sus fundadores. No se otorga ninguna licencia abierta sobre ellos.
