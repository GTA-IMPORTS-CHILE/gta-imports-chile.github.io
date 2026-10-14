"""Build the GTA Imports product-showcase website into docs/ (served by GitHub Pages).

    python3 build/prepare_images.py   # only when photos change
    python3 build/build_site.py       # every content/design change

Content lives in catalog.py; styles in site.css. All internal links are RELATIVE, so one build works on any
preview address and on www.gta-imports.cl. Informational only (ruling 2026-10-13): no prices, no cart, no forms,
no outbound listing links. Brands on the site: DEWALT + STANLEY only (CRAFTSMAN removed 10-14, no permission).
Tracking: GA4 G-TBT2MG4KZP + GTM-N36ZQXMX + Search Console meta, copied verbatim from the Odoo site.
"""
import html
import re
import shutil
import sys
from datetime import date
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from catalog import FAMILIES, FILTERS_BLOCK, PHOTOS, PRODUCTS, REDIRECTS, SITE_PHOTOS  # noqa: E402

DOCS = HERE.parent / "docs"
DOMAIN = "https://www.gta-imports.cl"
EMAIL = "contacto@gta-imports.cl"
# contact = email + WhatsApp link only; no phone number is published (ruling 10-14)
WHATSAPP = "https://wa.me/56972899843"
ADDRESS = "Antonio Bellet 193, Of. 1210, Providencia, Santiago"
RUT = "78.208.318-K"
YOUTUBE = "https://www.youtube.com/@GTAIMPORTSCHILE"
WA_ICON = ('<svg viewBox="0 0 32 32" width="30" height="30" aria-hidden="true"><path fill="#fff" d="M16 3.2A12.7 12.7 0 0 0 5.1 22.4L3.3 28.8l6.6-1.7A12.7 12.7 0 1 0 16 3.2zm0 23.2c-2 0-3.9-.5-5.6-1.5l-.4-.2-3.9 1 1-3.8-.3-.4A10.5 10.5 0 1 1 16 26.4zm5.8-7.9c-.3-.2-1.9-.9-2.2-1-.3-.1-.5-.2-.7.2-.2.3-.8 1-1 1.2-.2.2-.4.2-.7.1-.3-.2-1.4-.5-2.6-1.6-1-.9-1.6-1.9-1.8-2.2-.2-.3 0-.5.1-.7l.5-.6c.2-.2.2-.3.3-.6.1-.2 0-.4 0-.6l-1-2.4c-.3-.6-.5-.5-.7-.5h-.6c-.2 0-.6.1-.9.4-.3.3-1.2 1.1-1.2 2.8s1.2 3.2 1.4 3.5c.2.2 2.4 3.6 5.7 5 .8.4 1.4.6 1.9.7.8.3 1.5.2 2.1.1.6-.1 1.9-.8 2.1-1.5.3-.7.3-1.3.2-1.5-.1-.1-.3-.2-.6-.4z"/></svg>')
YT_ICON = ('<svg viewBox="0 0 28 20" width="28" height="20" aria-hidden="true"><rect width="28" height="20" rx="5" '
           'fill="#FF0000"/><path d="M11 5.5v9l8-4.5z" fill="#fff"/></svg>')
SITE_IMG = {k: i for i, (k, _) in enumerate(SITE_PHOTOS, 1)}
BY_SLUG = {p["slug"]: p for p in PRODUCTS}
e = html.escape

TRACKING = """<meta name="google-site-verification" content="MgfLMvsqfg8H_wJaj-ikzs3J_aV6HfYmVcIwYYJ7itk"/>
<script async src="https://www.googletagmanager.com/gtag/js?id=G-TBT2MG4KZP"></script>
<script>
window.dataLayer = window.dataLayer || [];
function gtag(){dataLayer.push(arguments);}
gtag('consent', 'default', {'ad_storage': 'denied', 'ad_user_data': 'denied', 'ad_personalization': 'denied', 'analytics_storage': 'denied'});
gtag('js', new Date());
gtag('config', 'G-TBT2MG4KZP');
gtag('consent', 'update', {'ad_storage': 'granted', 'ad_user_data': 'granted', 'ad_personalization': 'granted', 'analytics_storage': 'granted'});
</script>
<script>(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':
new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],
j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
})(window,document,'script','dataLayer','GTM-N36ZQXMX');</script>"""
GTM_NOSCRIPT = ('<noscript><iframe src="https://www.googletagmanager.com/ns.html?id=GTM-N36ZQXMX" height="0" '
                'width="0" style="display:none;visibility:hidden"></iframe></noscript>')

NAV = [("productos/", "Productos"), ("empresa/", "Empresa"), ("donde-comprar/", "Dónde comprar"),
       ("preguntas-frecuentes/", "FAQ")]
PAGES = []


def img(slug, n=1, small=False):
    return f"assets/img/{slug}/{n}{'-s' if small else ''}.jpg"


def site_img(key, small=False):
    return img("site", SITE_IMG[key], small)


def page(path, title, description, body, current=None):
    """path relative to docs ('' = home, 'productos/x/', '404.html'); writes the file."""
    root = "/" if path == "404.html" else ("../" * path.count("/") or "./")
    canon = f"{DOMAIN}/{path}"
    nav = "".join(f'<a href="{root}{h}"{" aria-current=page" if h == current else ""}>{t}</a>' for h, t in NAV)
    fam_links = "".join(f'<li><a href="{root}productos/#{f["id"]}">{e(f["name"])}</a></li>' for f in FAMILIES)
    out = f"""<!doctype html>
<html lang="es-CL">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(title)}</title>
<meta name="description" content="{e(description)}">
<link rel="canonical" href="{canon}">
<meta property="og:type" content="website"><meta property="og:title" content="{e(title)}">
<meta property="og:description" content="{e(description)}"><meta property="og:url" content="{canon}">
<meta property="og:image" content="{DOMAIN}/{site_img('hero')}"><meta property="og:locale" content="es_CL">
<link rel="icon" href="{root}assets/favicon.png">
<link rel="stylesheet" href="{root}assets/site.css">
{TRACKING}
</head>
<body>
{GTM_NOSCRIPT}
<a class="skip" href="#main">Ir al contenido</a>
<div class="topbar"><div class="wrap"><span>Importador y distribuidor autorizado</span><span>DEWALT · STANLEY</span></div></div>
<header class="site"><div class="wrap">
<div class="brandrow"><a class="brand" href="{root}"><img src="{root}{site_img('logo', True)}" alt="GTA Imports Chile" width="40" height="40"><span>GTA IMPORTS CHILE</span></a>
<a class="yt" href="{YOUTUBE}" rel="noopener" title="GTA Imports Chile en YouTube" aria-label="YouTube">{YT_ICON}</a></div>
<nav class="main" aria-label="Principal">{nav}</nav>
</div></header>
<main id="main">
{body.replace('@ROOT@', root)}
</main>
<footer class="site"><div class="wrap">
<div class="fgrid">
<div><a class="brand" href="{root}"><img src="{root}{site_img('logo', True)}" alt="" width="40" height="40"><span style="color:#000">GTA IMPORTS CHILE</span></a>
<p style="margin-top:16px">Importador y distribuidor de herramientas y equipos originales Stanley Black &amp; Decker en Chile.</p></div>
<div><h4>Productos</h4><ul>{fam_links}</ul></div>
<div><h4>Empresa</h4><ul><li><a href="{root}empresa/">Sobre nosotros</a></li><li><a href="{root}donde-comprar/">Dónde comprar</a></li>
<li><a href="{root}preguntas-frecuentes/">Preguntas frecuentes</a></li><li><a href="{root}garantia-y-devoluciones/">Garantía y devoluciones</a></li>
<li><a href="{root}privacidad/">Privacidad</a></li></ul></div>
<div><h4>Contacto</h4><ul><li><a href="mailto:{EMAIL}">{EMAIL}</a></li><li><a href="{WHATSAPP}" rel="noopener">WhatsApp</a></li>
<li><a class="ytlink" href="{YOUTUBE}" rel="noopener">{YT_ICON}<span>YouTube</span></a></li></ul></div>
</div>
<div class="legal">© {date.today().year} GTA IMPORTS CHILE SpA · RUT {RUT}. GTA IMPORTS CHILE SpA es un importador y distribuidor autorizado independiente.
STANLEY® y DEWALT® son marcas registradas de Stanley Black &amp; Decker, Inc., utilizadas bajo licencia por el fabricante de los productos. Este sitio es operado por GTA Imports Chile y no por el titular de las marcas.</div>
</div></footer>
<div class="wa-bubble" id="wabubble" hidden><button type="button" class="wa-x" aria-label="Cerrar" id="wax">×</button>
<a href="{WHATSAPP}" rel="noopener"><img src="{root}{site_img('logo', True)}" alt="" width="44" height="44"><span>Hola. ¿En qué podemos ayudarte? Escríbenos por WhatsApp.</span></a></div>
<a class="wa-float" href="{WHATSAPP}" rel="noopener" aria-label="Escríbenos por WhatsApp" title="Escríbenos por WhatsApp">{WA_ICON}</a>
<script>(function(){{var b=document.getElementById('wabubble'),k='wa_closed',c=false;
try{{c=sessionStorage.getItem(k)==='1'}}catch(_){{}}
if(!c)setTimeout(function(){{b.hidden=false}},2500);
document.getElementById('wax').addEventListener('click',function(){{b.hidden=true;try{{sessionStorage.setItem(k,'1')}}catch(_){{}}}});}})();</script>
</body>
</html>
"""
    dest = DOCS / path / "index.html" if (path == "" or path.endswith("/")) else DOCS / path
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(out, encoding="utf-8")
    PAGES.append(path)


def card(p):
    return (f'<a class="card" href="@ROOT@productos/{p["slug"]}/"><div class="ph"><img src="@ROOT@{img(p["slug"], 1, True)}" '
            f'alt="{e(p["brand"])} {e(p["name"])} {e(p["model"])}" loading="lazy"></div><div class="tx">'
            f'<span class="mono">{e(p["brand"])} · {e(p["model"])}</span><h3>{e(p["name"])}</h3>'
            f'<span class="tag">{e(p["tagline"])}</span></div></a>')


def fam(fid):
    return [p for p in PRODUCTS if p["family"] == fid]


def family(fid):
    return next(f for f in FAMILIES if f["id"] == fid)


def video(vid, title):
    return (f'<section class="block"><div class="wrap"><div class="head"><div><span class="eyebrow">Video</span>'
            f'<h2>{e(title)}</h2></div><a href="{YOUTUBE}" rel="noopener">Más videos en YouTube</a></div>'
            f'<div class="video"><iframe src="https://www.youtube-nocookie.com/embed/{vid}" title="{e(title)}" loading="lazy" '
            f'allow="accelerometer; encrypted-media; gyroscope; picture-in-picture; fullscreen" allowfullscreen></iframe></div>'
            f'</div></section>')


def stats_row():
    return """<div class="stats">
<div class="stat"><b>50%</b><span>menos ruido que la línea DEWALT tradicional</span></div>
<div class="stat"><b>30%</b><span>menor consumo energético</span></div>
<div class="stat"><b>3×</b><span>mayor vida útil</span></div>
</div>"""


def distributor_band():
    return f"""<section class="band" id="contacto"><div class="wrap">
<div><span class="eyebrow">Distribuye nuestros productos</span><h2>Sé parte de nuestra red</h2>
<p>Trabajamos con distribuidores, ferreterías y tiendas especializadas a lo largo de todo Chile. Si estás interesado en ofrecer estos productos en tu negocio, no dudes en contactarnos.</p></div>
<ul class="contact-list">
<li><span class="mono">Correo</span><a href="mailto:{EMAIL}">{EMAIL}</a></li>
<li><span class="mono">WhatsApp</span><a href="{WHATSAPP}" rel="noopener">Envíanos un mensaje</a></li>
</ul></div></section>"""


# ------------------------------------------------------------------ pages
def build_home():
    vac, inf, acc = fam("aspiradoras"), fam("infladores"), fam("accesorios")
    body = f"""
<section class="hero-full" style="background-image:url('@ROOT@{site_img('hero')}')"><div class="scrim"><div class="wrap">
<span class="eyebrow">DEWALT · STANLEY</span>
<h1>Tecnología profesional para el día a día</h1>
<p class="sub">Ahora en Chile al precio justo.</p>
<div class="btns"><a class="btn light" href="@ROOT@productos/">Conozca nuestros productos</a><a class="btn outline-light" href="@ROOT@donde-comprar/">Dónde comprar</a></div>
</div></div></section>
<section class="block"><div class="wrap">
<div class="split">
<div><span class="eyebrow">01 · DEWALT</span><h2>Aspiradora DEWALT Stealthsonic</h2>
<p class="quote">"La silenciosa"</p>
<p>La aspiradora inteligente, modelo premium, frente a la DeWalt tradicional: 50% menos ruido, misma potencia, 30% menos consumo energético y hasta 3 veces más duración de vida útil.</p>
</div>
<div class="grid two">{"".join(card(p) for p in vac)}</div>
</div>
{stats_row()}
</div></section>
<section class="block"><div class="wrap split">
<div class="shot"><img src="@ROOT@{site_img('inflator_life')}" alt="Compresor STANLEY 12V para auto inflando un neumático" loading="lazy"></div>
<div><span class="eyebrow">02 · STANLEY</span><h2>Infladores y compresores para auto 12V</h2>
<p>Compresores e infladores portátiles para auto: compactos, profesionales y siempre listos. Desde el compresor 12V que vive en el maletero hasta el mini inflador inalámbrico que cabe en la guantera.</p>
<p>Pantalla digital, presión ajustable, corte automático, linterna LED y función powerbank para cargar tu celular.</p>
<div class="rows">{"".join(card(p) for p in inf)}</div></div>
</div></section>
<section class="block"><div class="wrap">
<div class="head"><div><span class="eyebrow">03 · DEWALT</span><h2>Accesorios para aspiradora DEWALT</h2>
<p><strong style="color:#000">Alta durabilidad y calidad superior.</strong> Compatibles con equipos de las líneas Stealthsonic, así como con otras aspiradoras Dewalt. Por otra parte, tanto las mangueras como los adaptadores están diseñados para un uso universal, compatibles con otras marcas.</p></div>
<a href="@ROOT@productos/#accesorios">Ver todos</a></div>
<div class="grid">{"".join(card(p) for p in acc)}</div>
</div></section>
<section class="block"><div class="wrap">
<div class="head"><div><span class="eyebrow">Calidad sobre cantidad</span><h2>Beneficios y ventajas</h2></div></div>
<div class="pillars">
<div class="pillar"><span class="mono">01</span><h3>Fabricante reconocido, productos con certificación internacional</h3><p>El departamento de investigación y desarrollo trabaja constantemente con tecnología de vanguardia, respaldada por certificaciones internacionales. Siempre un paso adelante de la competencia.</p></div>
<div class="pillar"><span class="mono">02</span><h3>Calidad y durabilidad</h3><p>Productos respaldados por marcas líderes en el mercado, probados y distribuidos a nivel mundial. Con garantía de fábrica y una red de centros de servicio a lo largo de Chile.</p></div>
<div class="pillar"><span class="mono">03</span><h3>Inversión que vale la pena</h3><p>Compra inteligente: mayor rendimiento y menor consumo energético, al precio justo. Disfruta de una vida útil más prolongada y un desempeño eficiente por más tiempo.</p></div>
</div></div></section>
{distributor_band()}
"""
    page("", "Aspiradoras DEWALT y compresores e infladores STANLEY | GTA Imports Chile",
         "Importador y distribuidor autorizado en Chile de aspiradoras profesionales DEWALT Stealthsonic y de "
         "compresores e infladores para auto STANLEY. Productos originales, con garantía.", body)


def build_catalog():
    secs = []
    for i, f in enumerate(FAMILIES, 1):
        grid = "grid two" if f["id"] == "aspiradoras" else "grid"
        secs.append(f"""<section class="block" id="{f['id']}"><div class="wrap">
<div class="head"><div><span class="eyebrow">{i:02d} · {e(f['brand'])}</span><h2>{e(f['name'])}</h2><p>{e(f['blurb'])}</p></div></div>
<div class="{grid}">{"".join(card(p) for p in fam(f['id']))}</div></div></section>""")
    body = ('<div class="page-head"><div class="wrap"><span class="eyebrow">Catálogo 2026</span><h1>Productos</h1>'
            '<p>Aspiradoras DEWALT Stealthsonic, infladores y compresores para auto STANLEY y accesorios para aspiradora DEWALT.</p>'
            '</div></div>' + "".join(secs) + distributor_band())
    page("productos/", "Productos | GTA Imports Chile",
         "Catálogo GTA Imports Chile: aspiradoras DEWALT Stealthsonic 20 L y 38 L, infladores y compresores 12V para "
         "auto STANLEY, filtros HEPA y accesorios para aspiradora DEWALT.", body, "productos/")


def filters_block(current):
    items = []
    for it in FILTERS_BLOCK["items"]:
        src = site_img(it["img"][5:], True) if it["img"].startswith("site:") else img(it["img"], 1, True)
        inner = (f'<div class="ph"><img src="@ROOT@{src}" alt="Filtro DEWALT {e(it["name"])} {e(it["model"])}" loading="lazy"></div>'
                 f'<div class="tx"><span class="mono">{e(it["name"]).upper()} · {e(it["model"])}</span><h3>{e(it["spec"])}</h3>'
                 f'<span class="tag">Garantiza una mejor calidad del aire, capturando partículas de hasta {e(it["size"])} con una eficiencia del {e(it["eff"])}.</span>'
                 + ('<span class="status">No disponible</span>' if not it["slug"] else
                    ('<span class="status here">Estás viendo este filtro</span>' if it["slug"] == current else '')) + '</div>')
        items.append(f'<a class="card" href="@ROOT@productos/{it["slug"]}/">{inner}</a>' if it["slug"] and it["slug"] != current
                     else f'<div class="card static">{inner}</div>')
    return (f'<section class="block tinted"><div class="wrap"><div class="head"><div><span class="eyebrow">Compara</span>'
            f'<h2>{e(FILTERS_BLOCK["title"])}</h2><p>{e(FILTERS_BLOCK["intro"])}</p></div></div>'
            f'<div class="grid three">{"".join(items)}</div></div></section>')


def brand_cards(brand):
    keys = ("dw_guarantee", "dw_brand") if brand == "DEWALT" else ("st_guarantee", "st_brand")
    alts = {"DEWALT": ("Garantía de herramienta DEWALT", "DEWALT — Solidez garantizada"),
            "STANLEY": ("Garantía limitada STANLEY de 1 año", "STANLEY — La marca del profesional")}[brand]
    return ('<section class="block"><div class="wrap"><div class="bcards">' +
            "".join(f'<img src="@ROOT@{site_img(k)}" alt="{a}" loading="lazy">' for k, a in zip(keys, alts)) +
            '</div></div></section>')


def build_product(p):
    n = len(PHOTOS[p["slug"]])
    fam_name = family(p["family"])["name"]
    thumbs = "".join(f'<a href="@ROOT@{img(p["slug"], i)}" data-full="@ROOT@{img(p["slug"], i)}"{" aria-current=true" if i == 1 else ""}>'
                     f'<img src="@ROOT@{img(p["slug"], i, True)}" alt="" loading="lazy"></a>' for i in range(1, n + 1))
    chips = "".join(f"<li>{e(h)}</li>" for h in p.get("highlights", []))
    specs = "".join(f"<tr><th>{e(k)}</th><td>{e(v)}</td></tr>" for k, v in p["specs"])
    acc = f'<details class="acc"><summary>Especificaciones</summary><table class="specs">{specs}</table></details>'
    if p.get("includes"):
        acc += ('<details class="acc"><summary>Incluye</summary><ul class=inc>' +
                "".join(f"<li>{e(x)}</li>" for x in p["includes"]) + "</ul></details>")
    acc += f'<details class="acc"><summary>Garantía</summary><p>{e(p["warranty"])}</p></details>'
    rel = [BY_SLUG[s] for s in p.get("related", [])]
    rel_html = (f'<section class="block"><div class="wrap"><div class="head"><div><span class="eyebrow">Complementa</span>'
                f'<h2>Productos relacionados</h2></div></div><div class="grid">{"".join(card(r) for r in rel)}</div></div></section>') if rel else ""
    extra = ""
    if p.get("filters_block"):
        extra += filters_block(p["slug"])
    if p.get("video"):
        vt = {"aspiradoras": "La aspiradora inteligente", "infladores": "Pequeño en tamaño, grande en conveniencia",
              "accesorios": "Construido para limpiar, hecho para durar"}[p["family"]]
        extra += video(p["video"], vt)
    if p.get("cards"):
        extra += brand_cards(p["cards"])
    body = f"""<div class="wrap"><div class="crumbs"><a href="@ROOT@productos/">Productos</a> / <a href="@ROOT@productos/#{p['family']}">{e(fam_name)}</a> / {e(p['model'])}</div>
<div class="pdp">
<div class="gallery"><div class="main"><img id="mainimg" src="@ROOT@{img(p['slug'])}" alt="{e(p['brand'])} {e(p['name'])} {e(p['model'])}"></div>
{('<div class="thumbs">' + thumbs + '</div>') if n > 1 else ''}</div>
<div class="info"><span class="eyebrow">{e(p['brand'])}</span><span class="model">{e(p['model'])}</span>
<h1>{e(p['name'])}</h1><p class="tagline">{e(p['tagline'])}</p>
<p class="lead">{e(p['lead'])}</p>{''.join(f'<p>{e(b)}</p>' for b in p['body'])}
{('<ul class="chips">' + chips + '</ul>') if chips else ''}
<div class="accs">{acc}</div>
<div class="btns"><a class="btn primary" href="@ROOT@donde-comprar/">Dónde comprar</a><a class="btn ghost" href="mailto:{EMAIL}?subject={e(p['model'])}">Consultar</a></div>
</div></div></div>
{extra}
{rel_html}
<script>document.querySelectorAll('.thumbs a').forEach(function(a){{a.addEventListener('click',function(ev){{ev.preventDefault();
document.getElementById('mainimg').src=a.dataset.full;document.querySelectorAll('.thumbs a').forEach(function(b){{b.removeAttribute('aria-current')}});
a.setAttribute('aria-current','true')}})}});</script>"""
    page(f"productos/{p['slug']}/", f"{p['brand']} {p['name']} {p['model']} | GTA Imports Chile",
         f"{p['brand']} {p['name']} {p['model']}: {p['tagline']}. {p['lead']}"[:300], body, "productos/")


def build_empresa():
    body = f"""<div class="page-head"><div class="wrap"><span class="eyebrow">Sobre nosotros</span>
<h1>Calidad sobre cantidad; herramientas pro para tareas diarias</h1>
<p>Importador y distribuidor autorizado para aspiradoras DeWalt e infladores Stanley en Chile.</p></div></div>
<div class="wrap"><div class="prose">
<h2>Red de distribución</h2>
<p>Trabajamos con distribuidores, ferreterías y tiendas especializadas a lo largo de todo Chile. Si estás interesado en ofrecer estos productos en tu negocio, no dudes en contactarnos.</p>
<p><strong>Precios competitivos para todo tipo de cliente.</strong></p>
<h2>Nuestra historia</h2>
<p>GTA IMPORTS nace de un grupo ferretero familiar con más de 40 años de experiencia, consolidado en el mercado gracias a su conocimiento profundo del sector y a la confianza de sus clientes. Nos especializamos en:</p>
<ul><li><strong>Importaciones internacionales</strong>, asegurando productos de calidad y proveedores confiables.</li>
<li><strong>Comercio tradicional</strong>, manteniendo la cercanía y servicio personalizado que caracteriza a nuestra esencia familiar.</li>
<li><strong>Comercio electrónico</strong>, con soluciones modernas que amplían el alcance y la eficiencia de nuestras operaciones.</li>
<li><strong>Distribución de marcas</strong>, construyendo relaciones sólidas y a largo plazo con fabricantes líderes del sector.</li></ul>
</div>
<div class="stats" style="margin-bottom:64px">
<div class="stat"><b>+40</b><span>años de experiencia del grupo ferretero familiar</span></div>
<div class="stat"><b>+60</b><span>países donde nuestros productos tienen presencia</span></div>
<div class="stat"><b>Calidad</b><span>y garantía: productos originales con garantía de fábrica</span></div>
<div class="stat"><b>Ventaja</b><span>tecnología de vanguardia, siempre un paso adelante de la competencia</span></div>
</div></div>
{distributor_band()}"""
    page("empresa/", "Sobre GTA Imports Chile | Importador y distribuidor autorizado DEWALT y STANLEY",
         "GTA Imports Chile SpA: importador y distribuidor autorizado de aspiradoras DeWalt Stealthsonic y compresores "
         "Stanley en Chile. Distribuidor independiente; productos originales con garantía.", body, "empresa/")


def build_donde():
    body = f"""<div class="page-head"><div class="wrap"><span class="eyebrow">Comercio electrónico</span><h1>Dónde comprar</h1>
<p>Encuentra nuestros productos en las principales tiendas online de Chile. Busca la marca y el modelo, o escríbenos y te orientamos.</p></div></div>
<div class="wrap"><div class="channels">
<div class="channel"><div class="logo"><img src="../{site_img('ch_ml', True)}" alt="Mercado Libre"></div><span class="mono">Tienda online</span><h2>Mercado Libre</h2><p>Aspiradoras, compresores y accesorios, con envío a todo Chile.</p></div>
<div class="channel"><div class="logo"><img src="../{site_img('ch_sodimac', True)}" alt="Sodimac"></div><span class="mono">Tiendas online</span><h2>Falabella · Sodimac</h2><p>Disponibles en falabella.com y sodimac.cl.</p></div>
</div>
<p class="note" style="margin-bottom:72px">¿Eres empresa, ferretería o distribuidor? Escríbenos a <a href="mailto:{EMAIL}">{EMAIL}</a>.</p></div>"""
    page("donde-comprar/", "Dónde comprar DEWALT y STANLEY | GTA Imports Chile",
         "Compra aspiradoras DEWALT y compresores STANLEY originales de GTA Imports en Mercado Libre, Falabella y Sodimac.",
         body, "donde-comprar/")


FAQ = [
    ("Devoluciones y garantías", [
        ("¿Puedo devolver mi compra? ¿Cuántos días tengo para hacerlo?", "Sí, tienes 10 días corridos desde la recepción del producto para ejercer el derecho de retracto según la normativa chilena. Las compras realizadas en Mercado Libre, Falabella o Sodimac se gestionan a través de la tienda donde compraste."),
        ("¿Qué incluye la garantía de mis productos?", "Todos nuestros productos cuentan con 6 meses de garantía legal, que incluye reparación, cambio o devolución, según la elección del cliente. Además, cada herramienta eléctrica incluye una garantía comercial de fábrica adicional: 1 año para productos Stanley y 3 años para productos DeWalt. Esta garantía comercial aplica únicamente a la herramienta eléctrica (no a los accesorios) y cubre exclusivamente defectos de fabricación. No es válida en casos de uso incorrecto, uso excesivo o desgaste propio del uso: aplica solo cuando el producto llega con un defecto o deja de funcionar debido a una falla de origen. Toda garantía debe ser evaluada y validada por el fabricante, tal como ocurre con cualquier herramienta eléctrica de marca."),
        ("¿Cómo hago válida la garantía?", "Contacta con nuestro servicio técnico con el producto y la factura. Evaluaremos el caso y procederemos, según corresponda, a reparación o reemplazo. Más detalles en nuestra política de garantía y devoluciones."),
    ]),
    ("Productos", [
        ("¿Los productos son originales?", "Sí. Todos nuestros productos son originales, importados por GTA IMPORTS CHILE SpA, importador y distribuidor autorizado independiente."),
        ("¿Qué filtro necesito para mi aspiradora?", "El filtro de cartucho estándar DXVC4001 (5 micrones, 95%) sirve para residuos de obra, aserrín, tierra y cenizas frías; el filtro HEPA DXVC4003 (0,3 micrones, 99,97%) para polvo fino de interior, pelo de mascota, polen y alérgenos. Ambos son lavables y reutilizables."),
    ]),
    ("Compras", [
        ("¿Dónde puedo comprar?", "Nuestros productos están disponibles en Mercado Libre, Falabella y Sodimac. Revisa la página Dónde comprar."),
        ("¿Venden a empresas y distribuidores?", f"Sí. Escríbenos a {EMAIL} o por WhatsApp y te enviaremos nuestras condiciones."),
    ]),
    ("Contacto y soporte", [
        ("¿Dónde puedo hacer consultas o presentar reclamos?", f"Puedes escribir a {EMAIL} o enviarnos un mensaje por WhatsApp."),
        ("¿Puedo visitar una tienda física o punto de retiro?", "Actualmente operamos solo en línea y a través de nuestra red de distribuidores."),
    ]),
]


def build_faq():
    parts = [f"<h2>{e(sec)}</h2>" + "".join(f'<details class="faq"><summary>{e(q)}</summary><div>{e(a)}</div></details>' for q, a in qs)
             for sec, qs in FAQ]
    body = ('<div class="page-head"><div class="wrap"><span class="eyebrow">Ayuda</span><h1>Preguntas frecuentes</h1></div></div>'
            f'<div class="wrap"><div class="prose">{"".join(parts)}</div></div>')
    page("preguntas-frecuentes/", "Preguntas frecuentes | GTA Imports Chile",
         "Garantía, devoluciones, filtros, dónde comprar y contacto: preguntas frecuentes de GTA Imports Chile.",
         body, "preguntas-frecuentes/")


def build_garantia():
    body = f"""<div class="page-head"><div class="wrap"><span class="eyebrow">Políticas</span><h1>Garantía y devoluciones</h1></div></div>
<div class="wrap"><div class="prose">
<h2>Política de garantía y devoluciones</h2>
<h3>Plazo y condiciones para devoluciones</h3>
<p>Aceptamos devoluciones dentro de los 10 días corridos desde la recepción del producto. El producto debe estar en condición original, sin uso, con empaques, accesorios y etiquetas intactas. De no cumplir estas condiciones, puede rechazarse la devolución. Las compras realizadas en Mercado Libre, Falabella o Sodimac se gestionan a través de la tienda donde compraste.</p>
<h3>Motivos válidos de devolución</h3>
<ul><li>El producto presenta defectos de fabricación.</li><li>El producto recibido no es el solicitado.</li><li>Arrepentimiento de la compra (derecho de retracto).</li></ul>
<h3>Proceso de devolución</h3>
<ul><li>Contacta a nuestro equipo de atención al cliente dentro de los primeros 10 días post-recepción.</li>
<li>Indica tu número de pedido y describe el motivo de la devolución.</li>
<li>Te informaremos si corresponde un retiro por parte de nosotros o si debes enviar el producto a una dirección que te facilitaremos.</li></ul>
<h3>Reembolsos o reemplazos</h3>
<p>Si procede la devolución, podrás elegir entre el reembolso completo al medio de pago original (menos costo de envío si aplica) o el reemplazo por un producto equivalente sin costo adicional. Procesamos reembolsos dentro de 7 a 10 días hábiles tras recibir el producto devuelto.</p>
<h3>Costos de devolución</h3>
<p>Si la devolución es por error nuestro (producto defectuoso o equivocado), GTA Imports cubrirá el costo del envío de retorno. En caso de devolución voluntaria sin defecto, el cliente asumirá los gastos de envío.</p>
<h3>Productos excluidos</h3>
<p>Productos usados, dañados por el cliente o sin embalaje original.</p>
<h2>Garantía limitada</h2>
<h3>¿Qué cubre?</h3>
<p>Defectos de fabricación, fallos en componentes y funcionamiento bajo condiciones normales de uso, respaldados por Alton Industry Ltd. La garantía es gestionada en Chile por GTA IMPORTS CHILE SpA (RUT {RUT}).</p>
<h3>¿Qué no cubre?</h3>
<p>Daños por uso indebido, modificaciones no autorizadas, accidentes, desgaste normal, negligencia o desastres naturales.</p>
<h3>¿Cómo hacerla válida?</h3>
<p>Contacta a nuestro servicio técnico con producto y factura. Revisaremos el equipo y, de corresponder, procederemos a su reparación o reemplazo por uno nuevo o equivalente.</p>
<h2>Datos del importador y servicio técnico en Chile</h2>
<table class="specs"><tr><th>Empresa</th><td>GTA IMPORTS CHILE SpA · RUT {RUT}</td></tr><tr><th>Dirección</th><td>{ADDRESS}</td></tr>
<tr><th>Correo</th><td><a href="mailto:{EMAIL}">{EMAIL}</a></td></tr><tr><th>WhatsApp</th><td><a href="{WHATSAPP}" rel="noopener">Envíanos un mensaje</a></td></tr></table>
</div></div>"""
    page("garantia-y-devoluciones/", "Garantía y devoluciones | GTA Imports Chile",
         "Política de garantía y devoluciones de GTA Imports Chile: garantía legal, garantía comercial de fábrica DEWALT y STANLEY.",
         body)


def build_privacy():
    body = f"""<div class="page-head"><div class="wrap"><span class="eyebrow">Políticas</span><h1>Política de privacidad</h1></div></div>
<div class="wrap"><div class="prose">
<h2>1. Alcance y aceptación</h2>
<p>Esta Política de Privacidad describe cómo GTA IMPORTS CHILE SpA ("GTA Imports", "nosotros", "nuestro") recopila, utiliza y divulga su información personal cuando visita gta-imports.cl y se comunica con nosotros respecto al sitio ("Servicios"). Al acceder o usar nuestros Servicios, usted acepta que recopilemos, utilicemos y divulguemos su información como se indica en esta política.</p>
<h2>2. Cambios en la política</h2>
<p>La presente política podrá actualizarse para reflejar cambios en prácticas, normativa o razones operativas. Toda versión revisada estará publicada en el sitio con su respectiva fecha de "Última actualización".</p>
<h2>3. Información que recopilamos</h2>
<ul><li><strong>Directamente del usuario:</strong> datos de contacto y detalles de atención al cliente (lo que comparta en sus comunicaciones por correo, teléfono o WhatsApp).</li>
<li><strong>Automáticamente:</strong> datos de uso como IP, navegador, interacción con el sitio y cookies (incluido Google Analytics y Google Tag Manager).</li>
<li><strong>De terceros:</strong> proveedores (alojamiento, analítica, videos de YouTube incrustados) que recogen datos en nuestro nombre.</li></ul>
<h2>4. Uso de la información</h2>
<p>Utilizamos sus datos para responder consultas y prestar atención al cliente, analizar el comportamiento y mejorar el sitio, y para seguridad y prevención de fraudes. No realizamos envíos de promociones por email o WhatsApp, salvo que el usuario nos lo autorice expresamente en el futuro.</p>
<h2>5. Cookies y tecnologías similares</h2>
<p>Usamos cookies necesarias y analíticas (Google Analytics). El navegador permite rechazarlas, aunque algunas funciones pueden dejar de funcionar correctamente.</p>
<h2>6. Divulgación de información</h2>
<p>Podemos compartir datos con proveedores de servicios (hosting, analítica), con afiliados o en contextos de fusiones, obligaciones legales o defensa legal, y cuando el usuario lo autorice.</p>
<h2>7. Usuarios menores de edad</h2>
<p>Nuestros servicios no están dirigidos a menores. Si padres o tutores creen que almacenamos información de un menor, pueden solicitarnos su eliminación vía nuestro contacto.</p>
<h2>8. Seguridad y conservación</h2>
<p>Aunque implementamos seguridad técnica adecuada (SSL, acceso limitado), no garantizamos seguridad total. Conservamos datos según la relación contractual o exigencias legales.</p>
<h2>9. Derechos del usuario</h2>
<p>De acuerdo a la legislación chilena, usted puede solicitar acceso, rectificación, eliminación, oposición, portabilidad de datos, revocación del consentimiento y restricción del tratamiento. No se discriminará por ejercer estos derechos.</p>
<h2>10. Reclamaciones y autoridad</h2>
<p>Para reclamos, contáctenos primero. Si no está conforme, puede dirigirse a la autoridad de protección de datos que corresponda en Chile.</p>
<h2>11. Transferencias internacionales</h2>
<p>Podemos transferir su información a servicios ubicados fuera de Chile (como Google Analytics, YouTube y el hosting del sitio). Nos aseguramos de aplicar mecanismos adecuados de protección conforme a las normativas aplicables.</p>
<h2>12. Contacto</h2>
<p>Para ejercer derechos, realizar consultas o presentar reclamos, escríbanos a <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>
<p class="note">Última actualización: {date.today():%d-%m-%Y}.</p>
</div></div>"""
    page("privacidad/", "Política de privacidad | GTA Imports Chile",
         "Política de privacidad de GTA Imports Chile SpA.", body)


def build_404():
    body = ('<div class="page-head"><div class="wrap"><span class="eyebrow">Error 404</span><h1>Esta página no existe</h1>'
            '<p>Puede que la dirección haya cambiado con nuestro nuevo sitio.</p><div class="btns" style="margin-top:28px">'
            '<a class="btn primary" href="/">Ir al inicio</a><a class="btn ghost" href="/productos/">Ver productos</a></div></div></div>')
    page("404.html", "Página no encontrada | GTA Imports Chile", "Página no encontrada.", body)


def build_redirects():
    for old, new in REDIRECTS.items():
        target = "../" * (old.count("/") + 1) + new
        d = DOCS / old
        d.mkdir(parents=True, exist_ok=True)
        (d / "index.html").write_text(
            f'<!doctype html><html lang="es-CL"><head><meta charset="utf-8"><title>GTA Imports Chile</title>'
            f'<meta name="robots" content="noindex"><link rel="canonical" href="{DOMAIN}/{new}">'
            f'<meta http-equiv="refresh" content="0; url={target}"></head><body><a href="{target}">Continuar</a></body></html>',
            encoding="utf-8")


def build_meta():
    urls = "".join(f"<url><loc>{DOMAIN}/{p}</loc></url>" for p in PAGES if p != "404.html")
    (DOCS / "sitemap.xml").write_text('<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'
                                      + urls + "</urlset>\n", encoding="utf-8")
    (DOCS / "robots.txt").write_text(f"User-agent: *\nAllow: /\nSitemap: {DOMAIN}/sitemap.xml\n", encoding="utf-8")
    (DOCS / ".nojekyll").write_text("", encoding="utf-8")


def main():
    for child in DOCS.iterdir():               # wipe generated html (keep assets/ and CNAME)
        if child.name in ("assets", "CNAME"):
            continue
        shutil.rmtree(child) if child.is_dir() else child.unlink()
    shutil.copy(HERE / "site.css", DOCS / "assets" / "site.css")
    from PIL import Image
    Image.open(DOCS / site_img("logo")).resize((64, 64), Image.LANCZOS).save(DOCS / "assets" / "favicon.png")
    build_home(); build_catalog(); build_empresa(); build_donde(); build_faq(); build_garantia(); build_privacy(); build_404()
    for p in PRODUCTS:
        build_product(p)
    build_redirects(); build_meta()
    bad, craftsman = [], []
    for f in DOCS.rglob("*.html"):
        text = f.read_text(encoding="utf-8")
        if "craftsman" in text.lower():
            craftsman.append(str(f.relative_to(DOCS)))
        for ref in re.findall(r'(?:href|src)="([^"]+)"', text) + re.findall(r"url\('([^']+)'\)", text):
            if ref.startswith(("http", "mailto:", "tel:", "#", "/")):
                continue
            t = f.parent / ref.split("#")[0].split("?")[0]
            t = t / "index.html" if (ref.endswith("/") or ref in ("./", "")) else t
            if not t.exists():
                bad.append(f"{f.relative_to(DOCS)} -> {ref}")
    print(f"built {len(PAGES)} pages + {len(REDIRECTS)} redirects into {DOCS}")
    if bad or craftsman:
        print("BROKEN LINKS:", *sorted(set(bad))[:40], sep="\n  ")
        print("CRAFTSMAN MENTIONS (must be none):", *craftsman, sep="\n  ")
        sys.exit(1)


if __name__ == "__main__":
    main()
