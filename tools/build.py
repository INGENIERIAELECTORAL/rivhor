#!/usr/bin/env python3
"""Generador local de la web de RIVHOR.

Produce los HTML finales dentro de public/ a partir de los textos aprobados.
No es necesario para ver la web. Solo sirve para mantener cabeceras y pies
coherentes al editar contenido. Uso desde la raíz del repositorio

    python3 tools/build.py
"""
from pathlib import Path
import html

ROOT = Path(__file__).resolve().parent.parent
PUB = ROOT / "public"
TOOLS = ROOT / "tools"

ENDPOINT = "https://formspree.io/f/mwllvkqw"
EMAIL = "hi@rivhor.com"

# ---------------------------------------------------------------------------
# Textos de interfaz
# ---------------------------------------------------------------------------
UI = {
    "en": {
        "skip": "Skip to content", "open_menu": "Open menu", "close_menu": "Close menu",
        "nav_label": "Main navigation", "lang_label": "Change language",
        "footer": "RIVHOR · A project in development",
        "footer_stage": "We are a project in development. We are not an established company yet.",
        "footer_write": "Write to us at",
        "office_details": "Explore Rivhor Office", "office_waitlist": "I want early access",
        "line_details": "Explore the proposal", "read_bio": "Read biography", "close_bio": "Close biography",
        "back_home": "Back to home", "back_lines": "Explore other lines", "updates": "Get updates",
        "alt_logo": "RIVHOR", "alt_adilene": "Adilene Rivera, RIVHOR co-founder", "alt_jared": "Jared Hortiales, RIVHOR co-founder",
        "breadcrumb_home": "Home", "status_word": "Status", "in_dev": "In development",
        "nf_title": "We could not find this page", "nf_body": "You can return to the homepage and explore what we are building.",
        "nf_es_title": "No encontramos esta página", "nf_es_body": "Puedes volver al inicio y seguir conociendo lo que estamos preparando.",
        "modules_title": "What Office will bring together",
        "progress_lead": "Three moments that explain where we are. The current work is in progress. The 2027 dates are goals, not confirmed launches.",
        "other_lead": "Rivhor Office is our main product. We are also defining other ways to make technology more accessible to businesses and organizations.",
        "hero_cap": "two people, one sketch at a time",
        "office_cap": "an illustrative sketch, not a finished screen",
        "closing_note": "a dream taking shape",
    },
    "es": {
        "skip": "Ir al contenido", "open_menu": "Abrir menú", "close_menu": "Cerrar menú",
        "nav_label": "Navegación principal", "lang_label": "Cambiar idioma",
        "footer": "RIVHOR · Un proyecto en desarrollo",
        "footer_stage": "Somos un proyecto en desarrollo. Todavía no somos una empresa constituida.",
        "footer_write": "Escríbenos a",
        "office_details": "Conoce Rivhor Office", "office_waitlist": "Quiero acceso anticipado",
        "line_details": "Conoce la propuesta", "read_bio": "Ver biografía", "close_bio": "Cerrar biografía",
        "back_home": "Volver al inicio", "back_lines": "Ver otras líneas", "updates": "Recibir novedades",
        "alt_logo": "RIVHOR", "alt_adilene": "Adilene Rivera, cofundadora de RIVHOR", "alt_jared": "Jared Hortiales, cofundador de RIVHOR",
        "breadcrumb_home": "Inicio", "status_word": "Estado", "in_dev": "En desarrollo",
        "nf_title": "No encontramos esta página", "nf_body": "Puedes volver al inicio y seguir conociendo lo que estamos preparando.",
        "modules_title": "Lo que reunirá Office",
        "progress_lead": "Tres momentos que explican dónde estamos. El trabajo actual está en marcha. Las fechas de 2027 son metas, no lanzamientos confirmados.",
        "other_lead": "Rivhor Office es nuestro producto principal. También estamos definiendo otras formas de poner la tecnología al alcance de empresas y organizaciones.",
        "hero_cap": "dos personas, un trazo a la vez",
        "office_cap": "un boceto ilustrativo, no una pantalla terminada",
        "closing_note": "un sueño en marcha",
    },
}

NAV = [
    ("story", "Our Story", "Nuestra historia"),
    ("office", "Rivhor Office", "Rivhor Office"),
    ("team", "Founders", "Fundadores"),
    ("progress", "Our Progress", "Nuestros avances"),
]

META = {
    "home": {"es": ("RIVHOR · Un sueño que estamos construyendo", "Conoce RIVHOR, el proyecto de dos jóvenes migrantes que prepara software bilingüe para la comunidad latina y las pequeñas empresas."),
             "en": ("RIVHOR · A dream we're building", "Meet RIVHOR, a project by two young migrants building bilingual software for the Latino community and small businesses.")},
    "office": {"es": ("Rivhor Office · En desarrollo", "Conoce el software bilingüe que estamos diseñando para documentos, llamadas asistidas, cotizaciones y agenda de pequeños negocios."),
               "en": ("Rivhor Office · In development", "Explore the bilingual software we are designing for documents, assisted calls, estimates, and scheduling for small businesses.")},
    "data": {"es": ("Rivhor Data · En desarrollo", "Nuestra propuesta de datos, tableros y automatización para comenzar con una necesidad concreta y ampliar la solución conforme crezca el negocio."),
             "en": ("Rivhor Data · In development", "Our proposed data, dashboard, and automation services start with a specific need and can grow with the business.")},
    "development": {"es": ("Rivhor Development · En desarrollo", "La línea de aplicaciones, portales e integraciones a medida que estamos preparando para empresas y organizaciones."),
                    "en": ("Rivhor Development · In development", "The custom application, portal, and integration services we are preparing for businesses and organizations.")},
    "campaign-systems": {"es": ("Rivhor Campaign Systems · En desarrollo", "Nuestra propuesta de herramientas de información y coordinación para organizaciones estadounidenses del ámbito electoral."),
                         "en": ("Rivhor Campaign Systems · In development", "Our proposed information and coordination tools for U.S. campaigns and civic organizations.")},
    "impact": {"es": ("Rivhor Impact · En desarrollo", "Identidad digital, contenido y sitios institucionales que estamos preparando para organizaciones sin fines de lucro."),
               "en": ("Rivhor Impact · In development", "The digital identity, content, and organizational website services we are preparing for nonprofits.")},
    "cybersecurity": {"es": ("Rivhor Cybersecurity · En desarrollo", "Una división en desarrollo para identificar riesgos y mejorar las prácticas de seguridad digital de empresas y organizaciones."),
                      "en": ("Rivhor Cybersecurity · In development", "A division in development focused on identifying risks and improving digital security practices for businesses and organizations.")},
    "404": {"es": ("No encontramos esta página · RIVHOR", "Página no encontrada. Vuelve al inicio de RIVHOR en español o en inglés."),
            "en": ("Page not found · RIVHOR", "Page not found. Return to the RIVHOR homepage in English or Spanish.")},
}

# ---------------------------------------------------------------------------
# Contenido de inicio
# ---------------------------------------------------------------------------
HOME = {
    "en": {
        "h1": ("RIVHOR.", "A dream we're building."),
        "story": [
            "RIVHOR began as a dream shared by two young immigrants who saw an opportunity to use their passions to support the Latino community and small businesses.",
            "We want to create high-quality software at fair prices. Our main focus is Rivhor Office, a bilingual tool to help small business owners organize their work and communicate in English and Spanish.",
            "Today, RIVHOR is a project in development. We are defining our products and laying the foundations for what it will become. This website offers a first look at that journey.",
        ],
        "office_eyebrow": "our main product",
        "office_h2": "Rivhor Office",
        "office_sub": "The bilingual software we're building",
        "office_p": [
            "We are designing a platform where owners can keep documents together, understand notices, make calls with English–Spanish assistance, and prepare estimates and appointments from their phones.",
            "An internal chat will help find files, create folders, and prepare tasks. Owners will review the documents they share, the estimates they send, and the commitments they confirm.",
            "We want to make those tasks easier and help language become less of an obstacle in everyday work.",
        ],
        "office_status": "Product in development",
        "office_modules": ["Organized documents", "Assisted calls", "Estimates and scheduling", "Administrative chat"],
        "team_h2": "The people building RIVHOR",
        "team_lead": "Adilene Rivera and Jared Hortiales are shaping this project. Their backgrounds and the work they are preparing are part of RIVHOR's story.",
        "progress_h2": "Our progress",
        "other_h2": "Other areas we're preparing",
        "closing_h2": "What's next",
        "closing_p": "We will keep sharing progress on RIVHOR and Rivhor Office. We want this space to show what we are building and the people behind it.",
        "closing_big": "RIVHOR is a dream taking shape. We look forward to sharing more with you.",
    },
    "es": {
        "h1": ("RIVHOR.", "Un sueño que estamos construyendo."),
        "story": [
            "RIVHOR nace del sueño de dos jóvenes migrantes que encontraron en sus pasiones una forma de aportar a la comunidad latina y a las pequeñas empresas.",
            "Queremos crear software de alta calidad a precios justos. Nuestra principal apuesta es Rivhor Office, una herramienta bilingüe para ayudar a los dueños de pequeños negocios a organizar su trabajo y comunicarse entre español e inglés.",
            "Hoy somos un proyecto en desarrollo. Estamos definiendo nuestros productos y construyendo las bases de lo que será RIVHOR. Esta web es una primera mirada a ese camino.",
        ],
        "office_eyebrow": "nuestro producto principal",
        "office_h2": "Rivhor Office",
        "office_sub": "El software bilingüe que estamos construyendo",
        "office_p": [
            "Estamos diseñando una plataforma para que el propietario pueda reunir sus documentos, entender avisos, hacer llamadas con asistencia entre español e inglés y preparar cotizaciones y citas desde el celular.",
            "Un chat interno ayudará a localizar archivos, crear carpetas y preparar tareas. El propietario revisará los documentos que se comparten, las propuestas que se envían y los compromisos que se confirman.",
            "Queremos que esas tareas sean más sencillas y que el idioma deje de complicar el trabajo de cada día.",
        ],
        "office_status": "Producto en desarrollo",
        "office_modules": ["Documentos organizados", "Llamadas asistidas", "Cotizaciones y agenda", "Chat administrativo"],
        "team_h2": "Las personas detrás de RIVHOR",
        "team_lead": "Adilene Rivera y Jared Hortiales son quienes están dando forma a este proyecto. Sus trayectorias y el trabajo que están preparando son parte de la historia de RIVHOR.",
        "progress_h2": "Nuestros avances",
        "other_h2": "Otras líneas que estamos preparando",
        "closing_h2": "Lo que viene",
        "closing_p": "Seguiremos compartiendo cómo avanzan el proyecto y Rivhor Office. Queremos que este espacio muestre lo que estamos construyendo y las personas que lo hacen posible.",
        "closing_big": "RIVHOR es un sueño en marcha. Pronto podremos compartir más contigo.",
    },
}

MILESTONES = [
    {"id": "now", "state": "in_progress",
     "en": ("Now", "Shaping RIVHOR", "We are working on our identity and the design of Rivhor Office. We are defining how documents, assisted calls, and estimates can come together in a useful tool for small businesses.", "In progress"),
     "es": ("Ahora", "Le damos forma a RIVHOR", "Trabajamos en nuestra identidad y en el diseño de Rivhor Office. Estamos definiendo cómo reunir documentos, llamadas asistidas y cotizaciones en una herramienta que resulte útil para los pequeños negocios.", "En marcha")},
    {"id": "registration", "state": "planned",
     "en": ("June 2027", "Establishing the company", "Our goal is to complete RIVHOR's formal registration and take the next step toward turning this project into a company.", "Goal"),
     "es": ("Junio de 2027", "Constituir la empresa", "Nuestra meta es completar el registro formal de RIVHOR y dar el siguiente paso para convertir este proyecto en una empresa.", "Meta")},
    {"id": "flagship", "state": "planned",
     "en": ("December 2027", "Preparing Rivhor Office", "We want to have our bilingual software ready and begin a new stage with the people who will use it. We will share progress and confirm availability as development moves forward.", "Goal"),
     "es": ("Diciembre de 2027", "Preparar Rivhor Office", "Queremos tener listo nuestro software bilingüe y comenzar una nueva etapa junto a quienes lo utilizarán. Compartiremos los avances y confirmaremos su disponibilidad conforme progrese el desarrollo.", "Meta")},
]

# Líneas secundarias. (id, nombre, estado EN, estado ES, resumen inicio EN, resumen inicio ES, icono)
LINES = [
    ("data", "Rivhor Data", "Offering being defined", "Oferta en definición",
     "Organized information, dashboards, automation, and analysis for businesses that need to understand results and reduce manual work.",
     "Organización de información, tableros, automatización y análisis para negocios que necesitan comprender sus resultados y reducir tareas manuales.", "dashboard"),
    ("development", "Rivhor Development", "Service model in preparation", "Modelo de servicio en preparación",
     "Custom applications, portals, and systems that can start with a specific need and grow with the organization.",
     "Aplicaciones, portales y sistemas a medida que puedan comenzar con una necesidad concreta y crecer junto a la organización.", "code"),
    ("campaign-systems", "Rivhor Campaign Systems", "Functional proposal being defined", "Propuesta funcional en definición",
     "Information and coordination systems for teams, volunteers, documents, and internal reports in U.S. electoral organizations.",
     "Sistemas de información y coordinación para equipos, voluntariado, documentos y reportes de organizaciones estadounidenses del ámbito electoral.", "map"),
    ("impact", "Rivhor Impact", "Offering in preparation", "Oferta en preparación",
     "Visual identity and organizational websites to help nonprofits explain their mission, share their work, and welcome participation.",
     "Identidad visual y sitios institucionales para que las organizaciones sin fines de lucro presenten su misión, muestren su trabajo y faciliten la participación.", "web"),
    ("cybersecurity", "Rivhor Cybersecurity", "Division in development", "División en desarrollo",
     "A division in development to help identify risks and improve digital security practices.",
     "Una división en desarrollo para ayudar a identificar riesgos y mejorar las prácticas de seguridad digital.", "shield"),
]

# Páginas de detalle de las líneas secundarias. subtítulo + párrafos
DETAIL = {
    "data": {
        "en": ("Information that helps businesses understand their work", [
            "We want more businesses to use their information without having to build a specialist department from the start.",
            "We are preparing a service line to connect sources, organize records, and build dashboards for sales, customers, inventory, and other operations. We also plan to automate reports and tasks that are currently handled manually.",
            "The proposed scope includes assistants using authorized information, survey and review analysis, business customer segmentation, and forecasting where enough suitable data exists. Each project will need to explain its sources, methods, and limitations.",
            "The intention is to begin with a specific need and an investment the business can manage, without building an internal data department. Each project will define its deliverables, maintenance needs, and external tool costs before expanding the solution.",
        ]),
        "es": ("Información que ayude a entender el negocio", [
            "Queremos que más empresas puedan utilizar sus datos sin tener que crear un departamento especializado desde el principio.",
            "Estamos preparando una propuesta para conectar fuentes, ordenar registros y construir tableros que permitan dar seguimiento a ventas, clientes, inventarios y otros aspectos de la operación. También contemplamos automatizar reportes y tareas que hoy se realizan de forma manual.",
            "El alcance incluye asistentes con información autorizada, análisis de encuestas y reseñas, segmentación comercial y pronósticos cuando existan datos suficientes para evaluarlos. Cada proyecto deberá explicar de dónde viene la información, cómo se obtienen los resultados y qué límites tienen.",
            "La intención es comenzar con una necesidad concreta y una inversión que el negocio pueda asumir, sin crear un departamento de datos propio. Cada proyecto definirá sus entregables, el mantenimiento necesario y los costos de herramientas externas antes de ampliar la solución.",
        ]),
    },
    "development": {
        "en": ("Tools that fit the way each organization works", [
            "We are defining a service line for custom applications, portals, and internal systems.",
            "The proposed tools can support customer requests, records, inventory, forms, approvals, and connections between existing platforms. We also plan to assess modernization of existing systems when that is an appropriate way to meet the need.",
            "We want each project to have a clear scope, testing, documentation, and a handoff that helps the organization continue using its software. Staged development can help manage investment and review what works.",
            "Service availability will be announced when the delivery model is ready.",
        ]),
        "es": ("Herramientas que se adapten al trabajo de cada organización", [
            "Estamos definiendo una línea de desarrollo de aplicaciones, portales y sistemas a medida.",
            "La propuesta contempla herramientas para solicitudes de clientes, expedientes, inventarios, formularios, aprobaciones e integraciones entre plataformas. También podremos evaluar la modernización de sistemas existentes cuando esa sea la mejor forma de resolver la necesidad.",
            "Queremos que cada proyecto tenga un alcance comprensible, pruebas, documentación y una entrega que permita seguir utilizando la herramienta. Las funciones se construirán por etapas cuando eso ayude a cuidar la inversión y revisar lo que funciona.",
            "La disponibilidad de estos servicios se anunciará cuando el modelo esté preparado.",
        ]),
    },
    "campaign-systems": {
        "en": ("Information and coordination for U.S. organizations", [
            "We are shaping support systems for campaigns, committees, consultancies, and civic organizations.",
            "The proposal combines public election data and maps with tools for teams, volunteers, shifts, events, documents, and internal reporting. It also includes issue tracking and receipt organization for administrative review.",
            "Observer support and election-period modules will need to reflect the requirements of each jurisdiction. Public data will identify sources and distinguish preliminary from certified results.",
            "The scope of each engagement and the roles of participants will require review before contracting. Electoral and financial decisions will remain with the authorized client team.",
        ]),
        "es": ("Información y coordinación para organizaciones estadounidenses", [
            "Estamos dando forma a sistemas de apoyo para campañas, comités, consultoras y organizaciones cívicas.",
            "La propuesta reúne información electoral pública y cartografía con herramientas para organizar equipos, voluntariado, turnos, eventos, documentos y reportes internos. También contempla seguimiento de incidencias y organización de comprobantes para revisión administrativa.",
            "Los módulos de apoyo a observadores y de seguimiento de jornada deberán responder a las condiciones de cada jurisdicción. Los datos públicos identificarán su fuente y distinguirán resultados preliminares de certificados.",
            "El alcance de cada proyecto y las funciones de sus participantes se revisarán antes de contratar. Las decisiones electorales y financieras permanecerán en el equipo autorizado del cliente.",
        ]),
    },
    "impact": {
        "en": ("A digital identity for sharing a mission", [
            "We want to help nonprofits explain who they are, show their work, and make it easier for people to get involved.",
            "The proposal includes visual identity, organizational content, and mobile-friendly websites. Each organization will be able to present its story, team, programs, activities, and reports using information it has reviewed and approved.",
            "We also plan to include domains, institutional email, and contact, volunteer, and event tools. Where appropriate, a website can connect to an organization-approved donation provider.",
            "The intention is to begin with a digital presence that fits available resources and expand as activities grow. Handoff will include access and guidance for keeping it current.",
        ]),
        "es": ("Una identidad digital para dar a conocer una misión", [
            "Queremos ayudar a organizaciones sin fines de lucro a explicar quiénes son, mostrar lo que hacen y facilitar que otras personas se sumen.",
            "La propuesta incluye identidad visual, contenido institucional y sitios adaptados al celular. Cada organización podrá presentar su historia, equipo, programas, actividades e informes con información que haya revisado y aprobado.",
            "También contemplamos dominio, correo institucional y herramientas para contacto, voluntariado y eventos. Cuando corresponda, el sitio podrá conectarse con un proveedor de donaciones aprobado por la organización.",
            "La idea es comenzar con una presencia digital que tenga sentido para sus recursos y ampliarla conforme crezcan sus actividades. La entrega incluirá los accesos y la orientación necesaria para actualizarla.",
        ]),
    },
    "cybersecurity": {
        "en": ("Building digital security foundations", [
            "We are preparing a division to help small businesses and organizations identify risks and improve practical security measures.",
            "Planned areas include configuration reviews, access management, vulnerability tracking, application security, backups, and staff awareness.",
            "We want to establish services with clear methods, tools, and scope. Availability will be announced when delivery capacity is in place.",
        ]),
        "es": ("Seguridad digital desde las bases", [
            "Estamos preparando una división para ayudar a pequeñas empresas y organizaciones a identificar riesgos y mejorar sus prácticas de seguridad.",
            "Las áreas previstas incluyen revisión de configuraciones, gestión de accesos, seguimiento de vulnerabilidades, seguridad de aplicaciones, respaldos y capacitación.",
            "Queremos definir servicios con métodos, herramientas y alcances claros. Su disponibilidad se comunicará cuando exista capacidad para ofrecerlos.",
        ]),
    },
}

OFFICE = {
    "en": {
        "sub": "The bilingual software we're building",
        "intro": [
            "Rivhor Office is our main product. We are designing it for owners of construction, landscaping, lawn care, cleaning, and property maintenance businesses who need to organize their work and communicate in English and Spanish.",
            "The idea is to bring documents, assisted calls, estimates, and scheduling together, with modules that businesses can use according to their needs. Owners will be able to check outstanding tasks from their phones and review each action before sharing information or accepting commitments.",
        ],
        "modules": [
            ("Documents you can find and understand", "documents", [
                "Owners will be able to upload files or photos, organize folders by customer, job, or administrative process, and find information through an internal chat. We want to make it easier to read notices, track expiration dates, and prepare documents for an accountant, administrative adviser, or insurance agent.",
                "Requirements guides will need to show their source, jurisdiction, and review date. Reading and translation will provide support. Original files will remain available, and matters requiring professional review will be identified before an owner acts.",
            ]),
            ("Calls with English and Spanish assistance", "call", [
                "Voice assistance will support calls that the owner makes to third parties. It will help interpret the conversation, formulate questions, and ask for clarification while the owner stays in control of responses and commitments.",
                "Transcripts and summaries will depend on consent and applicable conditions. Important names, amounts, dates, and agreements will need confirmation. The assistant should flag what it has not understood rather than present an assumption as a fact.",
            ]),
            ("Estimates and appointments from your phone", "estimate", [
                "We want businesses to prepare estimates with their logo, services, materials, labor, and terms through simple templates. Calculations will show their components so owners can review them before sending.",
                "Scheduling will help organize site visits, appointments, and jobs. We also plan to provide price references with sources, dates, and locations to support comparisons. These ranges will not replace a business's actual costs or determine its final price.",
            ]),
            ("A chat to help prepare the work", "chat", [
                "The internal chat will help find files, create folders, prepare documents, and gather information for an estimate. Owners will review recipients, files, and content before sharing. Access controls and activity records should make it possible to identify who made each change.",
            ]),
        ],
        "closing": "Office is still in development. We will share progress and confirm availability as the work moves forward.",
        "closing_note": "The capabilities described here are planned. They are not active features of this website.",
    },
    "es": {
        "sub": "El software bilingüe que estamos construyendo",
        "intro": [
            "Rivhor Office es nuestro producto principal. Lo estamos diseñando para propietarios de empresas de construcción, jardinería, corte de césped, limpieza y mantenimiento que necesitan organizar su trabajo y comunicarse entre español e inglés.",
            "La idea es reunir documentos, llamadas asistidas, cotizaciones y agenda en un mismo lugar, con módulos que puedan utilizarse según las necesidades de cada negocio. El propietario podrá consultar sus pendientes desde el celular y revisar cada acción antes de compartir información o aceptar compromisos.",
        ],
        "modules": [
            ("Documentos que puedas encontrar y entender", "documents", [
                "Podrás subir archivos o fotografías, organizar carpetas por cliente, trabajo o trámite y localizar información con ayuda de un chat interno. Queremos facilitar la lectura de avisos, el seguimiento de vencimientos y la preparación de una carpeta para un contador, gestor o agente de seguros.",
                "Las guías de requisitos deberán mostrar su fuente, jurisdicción y fecha de revisión. La lectura y traducción serán de apoyo. Los originales seguirán disponibles y los asuntos que necesiten una revisión profesional se señalarán antes de que el propietario actúe.",
            ]),
            ("Llamadas con asistencia entre español e inglés", "call", [
                "El agente de voz acompañará las llamadas que el propietario haga a terceros. Ayudará a interpretar la conversación, formular preguntas y pedir aclaraciones mientras el dueño mantiene el control de las respuestas y los compromisos.",
                "La transcripción y el resumen dependerán del consentimiento y de las condiciones aplicables. Los nombres, importes, fechas y acuerdos importantes necesitarán confirmación. El asistente podrá señalar lo que no haya entendido en lugar de presentar una suposición como un hecho.",
            ]),
            ("Cotizaciones y citas desde el celular", "estimate", [
                "Queremos que cada negocio pueda preparar cotizaciones con su logo, servicios, materiales, mano de obra y condiciones mediante plantillas sencillas. Los cálculos mostrarán sus componentes para que el propietario pueda revisarlos antes del envío.",
                "La agenda ayudará a organizar visitas, citas y trabajos. También contemplamos referencias de precios con fuente, fecha y zona para orientar una comparación. Esos rangos no sustituirán los costos reales del negocio ni decidirán el precio final.",
            ]),
            ("Un chat para preparar el trabajo", "chat", [
                "El chat interno ayudará a buscar archivos, crear carpetas, preparar documentos y reunir información para una cotización. El propietario revisará destinatarios, archivos y contenido antes de compartirlos. Los accesos y el registro de acciones deberán permitir saber quién hizo cada cambio.",
            ]),
        ],
        "closing": "Office sigue en desarrollo. Compartiremos los avances y confirmaremos su disponibilidad conforme progrese el trabajo.",
        "closing_note": "Las capacidades descritas aquí son previstas. No son funciones activas de este sitio.",
    },
}

TEAM = [
    {
        "id": "adilene-rivera", "name": "Adilene Rivera", "photo": "/assets/team/adilene-rivera.png", "alt_key": "alt_adilene",
        "role": {"es": "Cofundadora y CEO de RIVHOR", "en": "Co-Founder & CEO"},
        "short": {
            "es": "Estudió Hospitality Management en Florida International University y obtuvo un Associate of Science en Hospitality and Culinary Arts por Rockland Community College. Cuenta con experiencia en coordinación de proyectos, administración y gestión de servicios. Se desempeña como coordinadora de proyectos recreativos en Jawonio y asistente administrativa en Rivera’s Services INC.",
            "en": "She studied Hospitality Management at Florida International University and earned an Associate of Science in Hospitality and Culinary Arts from Rockland Community College. Her experience includes project coordination, administration, and service management. She works as a Recreational Project Coordinator at Jawonio and as an Administrative Assistant at Rivera’s Services INC.",
        },
        "long": {
            "es": "Adilene Rivera es cofundadora y CEO de RIVHOR. Su trayectoria profesional comprende coordinación de proyectos, administración, gestión de turnos y atención al cliente en empresas y organizaciones de Nueva York y Florida.\n\nEstudió Hospitality Management en Florida International University entre 2022 y 2024. Previamente obtuvo el grado de Associate of Science en Hospitality and Culinary Arts por Rockland Community College, donde estudió entre 2020 y 2022. Durante su formación participó en la National Society of Leadership and Success y se desempeñó como tesorera del Honors Newsletter Club.\n\nDesde septiembre de 2025 trabaja como Recreational Project Coordinator en Jawonio. Asimismo, desde diciembre de 2022 se desempeña como asistente administrativa en Rivera’s Services INC, en Sloatsburg, Nueva York. En esta empresa realiza tareas de atención al cliente, cuentas por pagar y cobrar, captura de datos y coordinación de permisos de transporte conforme a los requisitos locales y federales.\n\nEntre agosto de 2024 y julio de 2025 fue gerente de turno en Taco TPKA, en Sloatsburg. Sus responsabilidades incluyeron la configuración y administración del sistema Toast POS, el control de cajas, la conciliación de transacciones y la resolución de consultas y quejas de clientes. Durante el primer mes de operación del restaurante desarrolló e implementó estrategias de promoción, actividades con la comunidad y campañas en redes sociales para atraer y retener clientes.\n\nTambién trabajó como mesera en The Tuxedo Club, en Nueva York, entre marzo de 2022 y noviembre de 2025. Como parte de su trayectoria en hospitalidad, realizó una estancia profesional en el área de Alimentos y Bebidas del Seminole Hard Rock Hotel & Casino Hollywood, en Florida, entre febrero y mayo de 2024.",
            "en": "Adilene Rivera is Co-Founder and CEO of the RIVHOR project. Her professional background includes project coordination, administration, shift management, and customer service in businesses and organizations in New York and Florida.\n\nShe studied Hospitality Management at Florida International University from 2022 to 2024. She previously earned an Associate of Science in Hospitality and Culinary Arts from Rockland Community College, where she studied from 2020 to 2022. During her studies, she participated in the National Society of Leadership and Success and served as treasurer of the Honors Newsletter Club.\n\nSince September 2025, she has worked as a Recreational Project Coordinator at Jawonio. She has also worked as an Administrative Assistant at Rivera’s Services INC in Sloatsburg, New York, since December 2022. Her responsibilities there include customer service, accounts payable and receivable, data entry, and coordinating transportation permits in accordance with local and federal requirements.\n\nFrom August 2024 to July 2025, she was a Shift Manager at Taco TPKA in Sloatsburg. Her responsibilities included setting up and administering Toast POS, cash management, transaction reconciliation, and resolving customer inquiries and complaints. During the restaurant’s first month of operation, she developed and implemented promotional strategies, community activities, and social media campaigns to attract and retain customers.\n\nShe also worked as a server at The Tuxedo Club in New York from March 2022 to November 2025. As part of her hospitality experience, she completed a professional placement in Food and Beverage at Seminole Hard Rock Hotel & Casino Hollywood in Florida from February to May 2024.",
        },
    },
    {
        "id": "jared-hortiales", "name": "Jared Hortiales", "photo": "/assets/team/jared-hortiales.png", "alt_key": "alt_jared",
        "role": {"es": "Cofundador y director del proyecto RIVHOR", "en": "Co-Founder & Project Director"},
        "short": {
            "es": "Se ha desempeñado como director en Grupo Horva de México y consultor en Ingeniería Electoral Consultores. Es egresado de Ciencias Políticas y Administración Pública, Seguridad Pública y Derecho, y de la Maestría en Administración Pública y Gobierno. Actualmente cursa estudios en computación y ciberseguridad en MIU City University y Saint Leo University.",
            "en": "He has served as a director at Grupo Horva de México and as a consultant at Ingeniería Electoral Consultores. He has completed undergraduate programs in Political Science and Public Administration, Public Security, and Law, as well as a master’s program in Public Administration and Government. He is currently pursuing studies in computing and cybersecurity at MIU City University and Saint Leo University.",
        },
        "long": {
            "es": "Jared Hortiales es cofundador y director del proyecto RIVHOR. Se ha desempeñado como director en Grupo Horva de México y como consultor en Ingeniería Electoral Consultores. Colabora como columnista en medios nacionales, entre ellos el Sistema Público de Radiodifusión del Estado Mexicano y la Revista de la Cámara de Diputados.\n\nEs egresado de las licenciaturas en Ciencias Políticas y Administración Pública por la Universidad Autónoma del Estado de México, Seguridad Pública por la Universidad Digital del Estado de México y Derecho por la Universidad Virtual del Estado de Guanajuato. También es egresado de la Maestría en Administración Pública y Gobierno por la UDEMÉX.\n\nEs beneficiario de una beca de la Organización de los Estados Americanos y el Organismo Internacional de Juventud para Iberoamérica para cursar Ingeniería en Ciencias de la Computación y el Máster en Ciencias de la Ciberseguridad en MIU City University, en Miami, Florida. Asimismo, estudia Ingeniería en Sistemas Computacionales con especialización en Ciberseguridad en la División de Estudios Internacionales de Latinoamérica de Saint Leo University, en Florida.\n\nEn 2024 participó como delegado en la Cumbre del Futuro, durante la Semana de Alto Nivel de las Naciones Unidas en Nueva York. Ha sido distinguido como representante de México ante el Major Group for Children and Youth para el ECOSOC 2025 y 2026. También ha participado como delegado del World Bank Group Youth Summit 2025 y 2026 en Washington, D. C., y del Foro Político de Alto Nivel de las Naciones Unidas en Nueva York.\n\nEn Europa participó como representante juvenil en el FAO World Food Forum 2025, realizado en Roma, y como delegado juvenil en el Youth Forum 16 de la UNCTAD, celebrado en Ginebra en 2025.\n\nEs autor de La nueva era de la ingeniería electoral, presentada en el Biscayne Bay Campus de Florida International University, así como de Politikids y Programa Alternativo de Gobierno.\n\nRecibió el Premio Municipal de la Juventud 2025 en la categoría de Humanismo en Tijuana, el Premio Estatal de la Juventud de Baja California 2024 y el Youth Leadership Award 2023 de los Napolitan Victory Awards. Ha obtenido certificaciones en Gobierno, Seguridad y Desarrollo Web por instituciones como la Universidad de California en San Diego, Full Sail University y The New School.\n\nComo conferencista fue orador invitado en Strengthening Civil Society Voices in Drug Policy for Sustainable Development, realizado en el marco del Foro Político de Alto Nivel de las Naciones Unidas en el John Jay College of Criminal Justice, en Nueva York. También participó como ponente en la Cumbre Mundial de Comunicación Política en Florida International University, en Miami, y ha intervenido en el Senado de la República y la Cámara de Diputados en México.",
            "en": "Jared Hortiales is Co-Founder and Project Director of RIVHOR. He has served as a director at Grupo Horva de México and as a consultant at Ingeniería Electoral Consultores. He contributes as a columnist to Mexican outlets, including the Sistema Público de Radiodifusión del Estado Mexicano and the Revista de la Cámara de Diputados.\n\nHe has completed undergraduate programs in Political Science and Public Administration at the Universidad Autónoma del Estado de México, Public Security at the Universidad Digital del Estado de México, and Law at the Universidad Virtual del Estado de Guanajuato. He has also completed a master’s program in Public Administration and Government at UDEMÉX.\n\nHe received a scholarship from the Organization of American States and the Organismo Internacional de Juventud para Iberoamérica to pursue Computer Science Engineering and a Master of Science in Cybersecurity at MIU City University in Miami, Florida. He is also studying Computer Systems Engineering with a specialization in Cybersecurity in the Latin American International Studies Division of Saint Leo University in Florida.\n\nIn 2024, he participated as a delegate in the Summit of the Future during the United Nations High-Level Week in New York. He has been recognized as a representative of Mexico to the Major Group for Children and Youth for ECOSOC 2025 and 2026. He has also participated as a delegate in the World Bank Group Youth Summit in Washington, D.C., in 2025 and 2026, and in the United Nations High-Level Political Forum in New York.\n\nIn Europe, he participated as a youth representative in the FAO World Food Forum 2025 in Rome and as a youth delegate in UNCTAD Youth Forum 16 in Geneva in 2025.\n\nHe is the author of La nueva era de la ingeniería electoral, presented at Florida International University’s Biscayne Bay Campus, as well as Politikids and Programa Alternativo de Gobierno.\n\nHe received Tijuana’s Municipal Youth Award 2025 in the Humanism category, the Baja California State Youth Award 2024, and the Napolitan Victory Awards’ Youth Leadership Award 2023. He has obtained certifications in government, security, and web development from institutions including the University of California San Diego, Full Sail University, and The New School.\n\nAs a speaker, he was invited to Strengthening Civil Society Voices in Drug Policy for Sustainable Development, held during the United Nations High-Level Political Forum at John Jay College of Criminal Justice in New York. He also spoke at the Cumbre Mundial de Comunicación Política at Florida International University in Miami and has addressed events at Mexico’s Senate and Chamber of Deputies.",
        },
    },
]

# ---------------------------------------------------------------------------
# Dibujos (SVG inline, sin palabras)
# ---------------------------------------------------------------------------
ARROW = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M4 12h15M13 5l7 7-7 7"/></svg>'
CHECK = '<svg class="d" viewBox="0 0 26 26" aria-hidden="true"><path class="b" d="M4 14l6 6L22 6"/></svg>'

ART = {
    # Dos personajes construyendo juntos un plano
    "hero": '''<svg class="d draw" viewBox="0 0 320 240" aria-hidden="true">
<path d="M60 52c26 0 44 20 42 46-2 28-20 46-44 45C33 142 15 122 17 96 19 70 36 52 60 52z"/>
<path class="b" d="M40 104c6 9 14 13 22 12 7-1 13-5 17-13"/>
<path d="M46 86c0 3-1 5-1 5M74 84c0 3-1 5-1 5"/>
<path d="M218 68c0-6 4-10 10-10h50c6 0 10 4 10 10v50c0 6-4 10-10 10h-50c-6 0-10-4-10-10z"/>
<path d="M253 58V42"/><circle cx="253" cy="39" r="4" class="f"/>
<path class="b" d="M236 100c5 7 12 9 17 9s12-2 17-9"/>
<path d="M238 84l4 3 4-3M260 84l4 3 4-3"/>
<path d="M104 150h116v70H104z"/><path d="M104 168h116"/>
<path d="M120 186h50M120 202h74"/>
<path class="b" d="M184 186h22"/>
<path d="M92 142c6-8 14-10 20-6M232 142c-6-8-14-10-20-6"/>
<path class="b" d="M160 22v10M160 46v10M146 36h10M174 36h10M150 26l6 6M170 46l6 6M176 26l-6 6M150 46l-6 6"/>
<path class="t" d="M20 220c30-6 60-6 90-2M240 218c20-6 40-6 60-2"/>
</svg>''',
    # Office: teléfono, documento con sonrisa, burbuja de llamada y hoja de cotización
    "office": '''<svg class="d draw" viewBox="0 0 460 320" aria-hidden="true">
<path d="M30 90c0-8 6-14 14-14h60l14 14h110c8 0 14 6 14 14v110c0 8-6 14-14 14H44c-8 0-14-6-14-14z"/>
<path d="M30 116h212"/>
<path d="M52 146h120M52 170h90M52 194h110"/>
<path class="b" d="M200 184l6 6 10-12"/>
<path d="M280 50c0-10 8-18 18-18h70c10 0 18 8 18 18v200c0 10-8 18-18 18h-70c-10 0-18-8-18-18z"/>
<path d="M312 42h42"/>
<path d="M296 86h74v26h-74zM296 126h74v26h-74z"/>
<path class="b" d="M310 166h74v26h-74z"/>
<path d="M318 220c0 14 10 24 20 28M304 210c0 24 12 40 32 46"/>
<path class="b" d="M324 258c6 6 14 6 20 0"/>
<path d="M150 240h150v50H150z"/><path d="M166 262h60M166 278h40"/><path class="b" d="M246 266h36"/>
<path class="b" d="M420 110c14-8 26 0 20 14"/>
<path class="t" d="M60 262c20-4 50-4 70 0"/>
</svg>''',
    "cierre": '''<svg class="d draw" viewBox="0 0 120 120" aria-hidden="true"><circle cx="60" cy="60" r="42"/><path class="b" d="M38 64c8 14 16 18 22 18s14-4 22-18"/><path d="M44 50l6-4 6 4M64 50l6-4 6 4"/><path class="b" d="M100 24l4-8M108 34l8-2M92 18l1-9"/></svg>''',
    "nube": '''<svg class="d draw" viewBox="0 0 140 110" aria-hidden="true"><path d="M36 86c-14 0-22-10-20-22 2-10 12-16 22-14 2-18 18-30 36-28 18 2 28 16 28 30 12-2 24 6 24 18 0 10-10 16-22 16z"/><path class="b" d="M58 66c4-4 10-4 14 0s10 4 14 0"/><path d="M58 50c0 2 0 4 0 4M84 50c0 2 0 4 0 4"/><path class="b" d="M118 22c4-4 10-4 12 2"/></svg>''',
    # iconos de línea
    "dashboard": '''<svg class="d" viewBox="0 0 110 110" aria-hidden="true"><path d="M16 90h78"/><path d="M26 90V56M46 90V38M66 90V48M86 90V24"/><path class="b" d="M22 50c14-18 30-10 44-22 6-5 12-8 20-8"/><path class="b" d="M80 20l8 1-2 8"/></svg>''',
    "code": '''<svg class="d" viewBox="0 0 110 110" aria-hidden="true"><path d="M34 32L14 55l20 23M76 32l20 23-20 23M64 24L46 86"/><path class="b" d="M48 96c6 6 14 6 20 0"/></svg>''',
    "map": '''<svg class="d" viewBox="0 0 110 110" aria-hidden="true"><path d="M16 30l26-10 26 10 26-10v60l-26 10-26-10-26 10z"/><path d="M42 20v60M68 30v60"/><path class="b" d="M56 44c0 10-8 18-8 18s-8-8-8-18a8 8 0 0 1 16 0z"/><path class="b" d="M80 52l6 6 10-12"/></svg>''',
    "web": '''<svg class="d" viewBox="0 0 110 110" aria-hidden="true"><path d="M18 30c0-6 4-10 10-10h54c6 0 10 4 10 10v40c0 6-4 10-10 10H28c-6 0-10-4-10-10z"/><path d="M40 92h30M55 80v12"/><path d="M30 36h8M30 48h20"/><path class="b" d="M62 44c0 10 8 14 14 14s14-4 14-14"/><circle class="f" cx="68" cy="34" r="3"/><circle class="f" cx="84" cy="34" r="3"/></svg>''',
    "shield": '''<svg class="d" viewBox="0 0 110 110" aria-hidden="true"><path d="M55 14l34 12v30c0 22-14 38-34 46-20-8-34-24-34-46V26z"/><path d="M42 50v-6a13 13 0 0 1 26 0v6"/><path d="M38 50h34v24H38z"/><path class="b" d="M48 66c4 4 10 4 14 0"/></svg>''',
    "documents": '''<svg class="d draw" viewBox="0 0 110 110" aria-hidden="true"><path d="M22 18h50l16 16v58H22z"/><path d="M72 18v16h16"/><path d="M34 50h40M34 64h40M34 78h26"/><path class="b" d="M78 86c6 6 12 6 18 0"/></svg>''',
    "call": '''<svg class="d draw" viewBox="0 0 110 110" aria-hidden="true"><path d="M30 18c0-6 4-10 10-10h30c6 0 10 4 10 10v74c0 6-4 10-10 10H40c-6 0-10-4-10-10z"/><path d="M46 16h18"/><path d="M44 42h32M44 56h20"/><path class="b" d="M86 30c8 6 10 14 4 22M92 22c12 10 14 24 6 36"/><path class="b" d="M48 80c4 4 10 4 14 0"/></svg>''',
    "estimate": '''<svg class="d draw" viewBox="0 0 110 110" aria-hidden="true"><path d="M20 24h70v62H20z"/><path d="M20 40h70"/><path d="M32 54h26M32 68h20"/><path class="b" d="M66 54h14M66 68h14"/><path d="M40 86v10M70 86v10M30 96h50"/><path class="b" d="M92 16l4-8M100 24l8-2"/></svg>''',
    "chat": '''<svg class="d draw" viewBox="0 0 110 110" aria-hidden="true"><path d="M16 26c0-6 4-10 10-10h40c6 0 10 4 10 10v22c0 6-4 10-10 10H40l-14 12V58h0c-6 0-10-4-10-10z"/><path class="b" d="M44 54c0-6 4-10 10-10h30c6 0 10 4 10 10v20c0 6-4 10-10 10h-2v12l-14-12H54c-6 0-10-4-10-10z"/><path d="M30 32h24M30 42h14"/><path class="b" d="M58 62h22M58 72h14"/></svg>''',
}

# ---------------------------------------------------------------------------
# Utilidades
# ---------------------------------------------------------------------------
def e(text):
    return html.escape(text, quote=True)


def paragraphs(items, cls=None):
    c = f' class="{cls}"' if cls else ""
    return "\n".join(f"<p{c}>{e(p)}</p>" for p in items)


def page_url(page_id, lang):
    base = "/es/" if lang == "es" else "/"
    if page_id == "404":
        return f"{base}404.html"
    return base if page_id == "home" else f"{base}{page_id}/"


def head(lang, page_id):
    title, desc = META[page_id][lang]
    other = "es" if lang == "en" else "en"
    return f'''<!doctype html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="color-scheme" content="light">
<meta name="theme-color" content="#ffffff">
<title>{e(title)}</title>
<meta name="description" content="{e(desc)}">
<link rel="alternate" hreflang="{lang}" href="{page_url(page_id, lang)}">
<link rel="alternate" hreflang="{other}" href="{page_url(page_id, other)}">
<link rel="alternate" hreflang="x-default" href="{page_url(page_id, 'en')}">
<link rel="icon" type="image/png" sizes="32x32" href="/assets/brand/favicon-32.png?v=2">
<link rel="icon" type="image/png" sizes="64x64" href="/assets/brand/favicon-64.png?v=2">
<link rel="icon" type="image/png" sizes="192x192" href="/assets/brand/icon-192.png?v=2">
<link rel="apple-touch-icon" sizes="180x180" href="/assets/brand/apple-touch-icon.png?v=2">
<link rel="preload" href="/assets/fonts/outfit-latin-wght-normal.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="/assets/css/styles.css?v=2">
<link rel="stylesheet" href="/assets/css/waitlist.css?v=2">
<script src="/assets/js/site.js?v=2" defer></script>
<script src="/assets/js/waitlist.js?v=2" defer></script>
</head>'''


def header(lang, page_id):
    t = UI[lang]
    home = page_url("home", lang)
    other = "es" if lang == "en" else "en"
    nav_items = []
    for anchor, en_label, es_label in NAV:
        label = en_label if lang == "en" else es_label
        href = f"#{anchor}" if page_id == "home" else f"{home}#{anchor}"
        current = ' aria-current="page"' if (page_id == "office" and anchor == "office") else ""
        nav_items.append(f'<li><a href="{href}"{current}>{e(label)}</a></li>')
    en_cur = ' aria-current="true"' if lang == "en" else ""
    es_cur = ' aria-current="true"' if lang == "es" else ""
    en_lang = ' lang="en"' if lang != "en" else ""
    es_lang = ' lang="es"' if lang != "es" else ""
    return f'''<body>
<a class="skip" href="#main">{e(t["skip"])}</a>
<header class="site-header">
  <div class="wrap">
    <a class="brand" href="{home}"><img src="/assets/brand/simbolo-rivhor-160.png" alt="" width="160" height="160"><span class="brand-name">RIVHOR</span></a>
    <nav class="lang" aria-label="{e(t["lang_label"])}">
      <a href="{page_url(page_id, 'en')}"{en_cur}{en_lang} data-lang-link hreflang="en">EN</a>
      <a href="{page_url(page_id, 'es')}"{es_cur}{es_lang} data-lang-link hreflang="es">ES</a>
    </nav>
    <button class="menu-btn" type="button" data-menu-button aria-expanded="false" aria-controls="site-nav">
      <svg class="ico-open" viewBox="0 0 20 20" aria-hidden="true"><path d="M3 5h14M3 10h14M3 15h14"/></svg>
      <svg class="ico-close" viewBox="0 0 20 20" aria-hidden="true"><path d="M4 4l12 12M16 4L4 16"/></svg>
      <span class="lbl-open">{e(t["open_menu"])}</span><span class="lbl-close">{e(t["close_menu"])}</span>
    </button>
    <nav class="nav" id="site-nav" data-menu aria-label="{e(t["nav_label"])}">
      <ul>{"".join(nav_items)}</ul>
    </nav>
  </div>
</header>
<main id="main">'''


def footer(lang, page_id):
    t = UI[lang]
    home = page_url("home", lang)
    other = "es" if lang == "en" else "en"
    other_label = "Español" if other == "es" else "English"
    links = []
    for anchor, en_label, es_label in NAV:
        label = en_label if lang == "en" else es_label
        links.append(f'<a href="{home}#{anchor}">{e(label)}</a>')
    links.append(f'<a href="{page_url(page_id, other)}" lang="{other}" hreflang="{other}" data-lang-link>{other_label}</a>')
    return f'''</main>
<footer class="site-footer">
  <div class="wrap">
    <div>
      <div class="brand brand-footer"><img src="/assets/brand/simbolo-rivhor-160.png" alt="" width="160" height="160"><span class="brand-name">RIVHOR</span></div>
      <p><strong>{e(t["footer"])}</strong></p>
      <p>{e(t["footer_stage"])}</p>
      <p>{e(t["footer_write"])} <a href="mailto:{EMAIL}">{EMAIL}</a></p>
    </div>
    <nav class="fl" aria-label="{e(t["nav_label"])}">{"".join(links)}</nav>
  </div>
</footer>
<script>document.documentElement.classList.add('js');</script>
</body>
</html>
'''


def form_fragment(name):
    text = (TOOLS / f"formulario-{name}.html").read_text(encoding="utf-8")
    # El fragmento usa class="wrap rw-layout". Se mantiene y hereda el contenedor del sitio.
    return text


# ---------------------------------------------------------------------------
# Páginas
# ---------------------------------------------------------------------------
def home_page(lang):
    t = UI[lang]
    c = HOME[lang]
    office_url = page_url("office", lang)
    form_anchor = "form-en" if lang == "en" else "form-es"
    brand, tagline = c["h1"]

    modules = "".join(f"<li>{CHECK}<span>{e(m)}</span></li>" for m in c["office_modules"])

    founders = []
    for p in TEAM:
        long_paras = "".join(f"<p>{e(x)}</p>" for x in p["long"][lang].split("\n\n"))
        founders.append(f'''<li class="founder rv">
  <div class="founder-top">
    <img class="portrait" src="{p["photo"]}" alt="{e(t[p["alt_key"]])}" width="400" height="400" loading="lazy">
    <div class="founder-id"><h3>{e(p["name"])}</h3><p class="role">{e(p["role"][lang])}</p></div>
  </div>
  <p class="bio">{e(p["short"][lang])}</p>
  <details>
    <summary><span class="s-open">{e(t["read_bio"])}</span><span class="s-close">{e(t["close_bio"])}</span></summary>
    <div class="bio-full">{long_paras}</div>
  </details>
</li>''')

    timeline = []
    for m in MILESTONES:
        when, title, desc, state = m[lang]
        timeline.append(f'''<li data-state="{m["state"]}" class="rv">
  <span class="when">{e(when)}</span>
  <h3>{e(title)}</h3>
  <p>{e(desc)}</p>
  <span class="state">{e(state)}</span>
</li>''')

    lines = []
    for lid, name, st_en, st_es, sum_en, sum_es, icon in LINES:
        status = st_en if lang == "en" else st_es
        summary = sum_en if lang == "en" else sum_es
        lines.append(f'''<li class="rv">
  {ART[icon]}
  <h3><a class="link" href="{page_url(lid, lang)}">{e(name)}</a></h3>
  <span class="tag">{e(status)}</span>
  <p>{e(summary)}</p>
  <a class="link" href="{page_url(lid, lang)}">{e(t["line_details"])}</a>
</li>''')

    body = f'''
<section class="hero" id="story" aria-labelledby="story-title">
  <div class="wrap">
    <div class="hero-copy">
      <span class="stage"><i aria-hidden="true"></i>{e(t["in_dev"])}</span>
      <h1 id="story-title">{e(brand)} <span class="u">{e(tagline)}</span></h1>
      <div class="copy">
        <p class="lead">{e(c["story"][0])}</p>
        <p>{e(c["story"][1])}</p>
        <p>{e(c["story"][2])}</p>
      </div>
      <div class="actions">
        <a class="btn" href="{office_url}">{e(t["office_details"])}{ARROW}</a>
        <a class="btn ghost" href="#team">{e(NAV[2][1] if lang == "en" else NAV[2][2])}</a>
      </div>
    </div>
    <div class="hero-art" aria-hidden="true">{ART["hero"]}<span class="cap">{e(t["hero_cap"])}</span></div>
  </div>
</section>

<section class="section featured" id="office" aria-labelledby="office-title">
  <div class="wrap">
    <div class="featured-copy">
      <span class="eyebrow">{e(c["office_eyebrow"])}</span>
      <h2 id="office-title">{e(c["office_h2"])}</h2>
      <p class="lead"><strong>{e(c["office_sub"])}</strong></p>
      {paragraphs(c["office_p"])}
      <ul class="modules">{modules}</ul>
      <p style="margin-top:22px"><span class="status">{e(c["office_status"])}</span></p>
      <div class="actions">
        <a class="btn" href="{office_url}#{form_anchor}">{e(t["office_waitlist"])}{ARROW}</a>
        <a class="btn ghost" href="{office_url}">{e(t["office_details"])}</a>
      </div>
    </div>
    <div class="featured-art" aria-hidden="true">{ART["office"]}<span class="cap">{e(t["office_cap"])}</span></div>
  </div>
</section>

<section class="section" id="team" aria-labelledby="team-title">
  <div class="wrap">
    <div class="section-head">
      <h2 id="team-title">{e(c["team_h2"])}</h2>
      <p class="lead">{e(c["team_lead"])}</p>
    </div>
    <ul class="team">{"".join(founders)}</ul>
  </div>
</section>

<section class="section" id="progress" aria-labelledby="progress-title">
  <div class="wrap">
    <div class="section-head">
      <h2 id="progress-title">{e(c["progress_h2"])}</h2>
      <p class="lead">{e(t["progress_lead"])}</p>
    </div>
    <ol class="timeline">{"".join(timeline)}</ol>
  </div>
</section>

<section class="section" id="other-lines" aria-labelledby="other-title">
  <div class="wrap">
    <div class="section-head">
      <h2 id="other-title">{e(c["other_h2"])}</h2>
      <p class="lead">{e(t["other_lead"])}</p>
    </div>
    <ul class="lines">{"".join(lines)}</ul>
  </div>
</section>

<div class="section" style="padding:0">
{form_fragment("rivhor-" + lang)}
</div>

<section class="section closing" id="closing" aria-labelledby="closing-title">
  <div class="wrap">
    <div>
      <span class="eyebrow">{e(t["closing_note"])}</span>
      <h2 id="closing-title">{e(c["closing_h2"])}</h2>
      <p class="lead" style="margin-top:14px;max-width:56ch">{e(c["closing_p"])}</p>
      <p class="big">{e(c["closing_big"])}</p>
    </div>
    <div aria-hidden="true">{ART["cierre"]}</div>
  </div>
</section>
'''
    return head(lang, "home") + header(lang, "home") + body + footer(lang, "home")


def office_page(lang):
    t = UI[lang]
    o = OFFICE[lang]
    home = page_url("home", lang)
    form_anchor = "form-en" if lang == "en" else "form-es"
    mods = []
    for title, icon, paras in o["modules"]:
        mods.append(f'''<article class="module rv">
  <div class="m-copy"><h2>{e(title)}</h2>{paragraphs(paras)}</div>
  <div class="m-art" aria-hidden="true">{ART[icon]}</div>
</article>''')
    body = f'''
<section class="detail-hero" aria-labelledby="office-title">
  <div class="wrap">
    <div>
      <p class="crumbs"><a href="{home}">{e(t["breadcrumb_home"])}</a><span aria-hidden="true">›</span><span>Rivhor Office</span></p>
      <span class="status" style="margin-top:14px">{e(HOME[lang]["office_status"])}</span>
      <h1 id="office-title">Rivhor Office</h1>
      <p class="lead"><strong>{e(o["sub"])}</strong></p>
      <div class="prose" style="margin-top:14px">{paragraphs(o["intro"])}</div>
      <div class="actions">
        <a class="btn" href="#{form_anchor}">{e(t["office_waitlist"])}{ARROW}</a>
        <a class="btn ghost" href="{home}#other-lines">{e(t["back_lines"])}</a>
      </div>
    </div>
    <div class="art" aria-hidden="true">{ART["office"]}<span class="cap">{e(t["office_cap"])}</span></div>
  </div>
</section>

<section class="section" aria-labelledby="modules-title">
  <div class="wrap">
    <div class="section-head"><h2 id="modules-title">{e(t["modules_title"])}</h2></div>
    {"".join(mods)}
    <div class="aside-note">
      <p><strong>{e(o["closing"])}</strong></p>
      <p class="muted">{e(o["closing_note"])}</p>
    </div>
  </div>
</section>

<div class="section" style="padding:0">
{form_fragment("office-" + lang)}
</div>

<section class="section" aria-label="{e(t["back_home"])}">
  <div class="wrap">
    <div class="actions" style="margin-top:0">
      <a class="btn ghost" href="{home}">{e(t["back_home"])}</a>
      <a class="btn ghost" href="{home}#other-lines">{e(t["back_lines"])}</a>
    </div>
  </div>
</section>
'''
    return head(lang, "office") + header(lang, "office") + body + footer(lang, "office")


def line_page(lid, lang):
    t = UI[lang]
    home = page_url("home", lang)
    entry = next(x for x in LINES if x[0] == lid)
    _, name, st_en, st_es, _, _, icon = entry
    status = st_en if lang == "en" else st_es
    sub, paras = DETAIL[lid][lang]
    waitlist = "#waitlist" if lang == "en" else "#lista-espera"
    body = f'''
<section class="detail-hero" aria-labelledby="line-title">
  <div class="wrap">
    <div>
      <p class="crumbs"><a href="{home}">{e(t["breadcrumb_home"])}</a><span aria-hidden="true">›</span><a href="{home}#other-lines">{e(HOME[lang]["other_h2"])}</a><span aria-hidden="true">›</span><span>{e(name)}</span></p>
      <span class="status" style="margin-top:14px">{e(status)}</span>
      <h1 id="line-title">{e(name)}</h1>
      <p class="lead"><strong>{e(sub)}</strong></p>
    </div>
    <div class="art" aria-hidden="true">{ART[icon]}</div>
  </div>
</section>

<section class="section" aria-labelledby="line-title">
  <div class="wrap">
    <div class="prose">{paragraphs(paras)}</div>
    <div class="actions">
      <a class="btn" href="{home}{waitlist}">{e(t["updates"])}{ARROW}</a>
      <a class="btn ghost" href="{home}#other-lines">{e(t["back_lines"])}</a>
      <a class="btn ghost" href="{home}">{e(t["back_home"])}</a>
    </div>
  </div>
</section>
'''
    return head(lang, lid) + header(lang, lid) + body + footer(lang, lid)


def not_found_page(lang):
    """404 con dos accesos de idioma claros."""
    t = UI[lang]
    en, es = UI["en"], UI["es"]
    body = f'''
<section class="nf">
  <div class="wrap">
    <div class="nf-art" aria-hidden="true">{ART["nube"]}</div>
    <div class="box" lang="en">
      <span class="eyebrow">404</span>
      <h1>{e(en["nf_title"])}</h1>
      <p>{e(en["nf_body"])}</p>
      <div class="actions"><a class="btn" href="/">{e(en["back_home"])}{ARROW}</a></div>
    </div>
    <div class="box" lang="es">
      <span class="eyebrow">404</span>
      <h2 style="font-size:clamp(1.9rem,4.4vw,3rem);margin:8px 0 14px">{e(es["nf_title"])}</h2>
      <p>{e(es["nf_body"])}</p>
      <div class="actions"><a class="btn" href="/es/">{e(es["back_home"])}{ARROW}</a></div>
    </div>
  </div>
</section>
'''
    return head(lang, "404") + header(lang, "404") + body + footer(lang, "404")


def write(path, content):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    print("wrote", path.relative_to(ROOT))


def main():
    for lang in ("en", "es"):
        base = PUB / "es" if lang == "es" else PUB
        write(base / "index.html", home_page(lang))
        write(base / "office" / "index.html", office_page(lang))
        for lid, *_ in LINES:
            write(base / lid / "index.html", line_page(lid, lang))
    write(PUB / "404.html", not_found_page("en"))
    write(PUB / "es" / "404.html", not_found_page("es"))


if __name__ == "__main__":
    main()
