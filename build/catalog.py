"""The website's content: products, specs, photos, videos, families. Spanish (customer-facing).

Sources (2026-10-13/14): Odoo product web descriptions + the live Odoo site's blocks (copied on request), the
CATÁLOGO 2026 v2 specs (company/catalogo), BRAND/PRODUCT PHOTOS, the GTA YouTube channel (@GTAIMPORTSCHILE).
Rulings: peak-HP convention (4HP/5HP), "20 Litros", 20 L cord = 5 m (GTA paid extra), no watts/kPa, NO prices,
NO outbound listing links. B+D BXUVXA01 OFF. **CRAFTSMAN OFF the site — no permission to use the mark (ruling 10-14).**
Photo refs: "brand:<under BRAND/PRODUCT PHOTOS>" · "logo:<file in BRAND/LOGO>" · "ws:<under the workspace>" ·
"static:<file in build/assets_static>" (images taken from the old Odoo site that exist nowhere else).
"""

FAMILIES = [
    {"id": "aspiradoras", "name": "Aspiradoras DEWALT Stealthsonic", "brand": "DEWALT",
     "blurb": "La aspiradora inteligente, modelo premium, frente a la DeWalt tradicional: 50% menos ruido, misma "
              "potencia, 30% menos consumo energético y hasta 3 veces más duración de vida útil."},
    {"id": "infladores", "name": "Infladores y compresores para auto 12V", "brand": "STANLEY",
     "blurb": "Compresores e infladores portátiles para auto, compactos y profesionales: pantalla digital, presión "
              "ajustable, corte automático, linterna LED y función powerbank."},
    {"id": "accesorios", "name": "Accesorios para aspiradora DEWALT", "brand": "DEWALT",
     "blurb": "Alta durabilidad y calidad superior. Compatibles con equipos de las líneas Stealthsonic, así como con "
              "otras aspiradoras Dewalt. Por otra parte, tanto las mangueras como los adaptadores están diseñados "
              "para un uso universal, compatibles con otras marcas."},
]

WARRANTY_DEWALT = "6 meses de garantía legal + 3 años de garantía comercial de fábrica DEWALT (defectos de fabricación)."
WARRANTY_STANLEY = "6 meses de garantía legal + 1 año de garantía comercial de fábrica STANLEY (defectos de fabricación)."
WARRANTY_ACC = "6 meses de garantía legal."

# brand cards shown at the foot of a product page (ruling 10-14: vacuums → DEWALT pair, Stanley → Stanley pair)
BRAND_CARDS = {
    "DEWALT": ["logo:DEWALT Guarantee Banner.jpg", "logo:DEWALT Logo Banner.jpg"],
    "STANLEY": ["brand:CAR12V_INFL_ST/GARANTIA STANLEY.webp", "brand:CAR12V_INFL_ST/DISTRIBUIDOR OFICIAL.webp"],
}

PRODUCTS = [
    # ---------------------------------------------------------------- vacuums
    {"slug": "aspiradora-dewalt-stealthsonic-20l", "family": "aspiradoras", "brand": "DEWALT",
     "model": "DXV20S-QT", "name": "Aspiradora Stealthsonic 20 L", "chip": "20 L | 5 GAL",
     "tagline": "Seco / mojado · 4 HP · acero inoxidable",
     "lead": "La Stealthsonic compacta: 65 dB(A), tanque de acero inoxidable de 20 litros y cable de 5 metros "
             "para moverse por toda la casa, el taller o la obra sin cambiar de enchufe.",
     "body": ["En casa, limpia sin interrumpir el descanso de la familia; en hoteles, trabaja sin molestar a los "
              "huéspedes; en talleres y espacios de trabajo, mejora el confort sin sacrificar rendimiento.",
              "Compatible con toda la línea de filtros y accesorios DEWALT: cartucho estándar, HEPA, esponja para "
              "trabajo húmedo y bolsas de polvo."],
     "highlights": ["50% más silenciosa", "Misma potencia", "30% menor consumo energético", "3× mayor vida útil"],
     "specs": [("Capacidad", "20 L · 5 gal"), ("Potencia", "4 HP (peak)"), ("Voltaje", "220–240 V ~50/60 Hz"),
               ("Tanque", "Acero inoxidable"), ("Flujo de aire", "85 CFM"), ("Nivel de ruido", "65 dB(A)"),
               ("Cable", "5 m"), ("Manguera", "48 mm × 2,1 m"), ("Uso", "Seco y mojado, con puerto de drenaje")],
     "includes": ["2 varillas de extensión 48 mm (DXVA19-1202)", "Manguera 48 mm × 2,1 m (DXVA19-2558)",
                  "Boquilla genérica 48 mm (DXVA19-1300)", "Boquilla para rincones 48 mm (DXVA19-1400)",
                  "Cepillo para superficies 48 mm (DXVA19-2591)", "Bolsa de accesorios",
                  "Filtro de cartucho seco/mojado (DXVC4001)", "Bolsa de filtro para polvo (DXVA19-4104)"],
     "warranty": WARRANTY_DEWALT, "video": "fJYHWVcLDMk", "cards": "DEWALT",
     "related": ["aspiradora-dewalt-stealthsonic-38l", "filtro-hepa-dewalt-dxvc4003", "filtro-cartucho-dewalt-dxvc4001",
                 "filtro-esponja-dewalt-dxva20-1200a", "bolsas-polvo-dewalt-dxva19-4204", "manguera-dewalt-dxva19-2558",
                 "silenciador-dewalt-dxva22-2520"]},
    {"slug": "aspiradora-dewalt-stealthsonic-38l", "family": "aspiradoras", "brand": "DEWALT",
     "model": "DXV38S-QT", "name": "Aspiradora Stealthsonic 38 L", "chip": "38 L | 10 GAL",
     "tagline": "Seco / mojado · 5 HP · acero inoxidable",
     "lead": "La aspiradora seco/mojado con tecnología silenciosa: 65 dB(A), la mitad del ruido percibido de una "
             "aspiradora estándar, con tanque de acero inoxidable de 38 litros, drenaje incorporado y bolsa de "
             "accesorios a bordo.",
     "body": ["En casa, limpia sin interrumpir el descanso de la familia; en hoteles, trabaja sin molestar a los "
              "huéspedes; en talleres e industria, mejora el confort del entorno sin sacrificar rendimiento.",
              "Su cuerpo de acero inoxidable es más liviano, más resistente y más duradero, con hasta 3 veces más "
              "vida útil."],
     "highlights": ["50% más silenciosa", "Misma potencia", "30% menor consumo energético", "3× mayor vida útil"],
     "specs": [("Capacidad", "38 L · 10 gal"), ("Potencia", "5 HP (peak)"), ("Voltaje", "220–240 V ~50/60 Hz"),
               ("Tanque", "Acero inoxidable"), ("Flujo de aire", "90 CFM"), ("Nivel de ruido", "65 dB(A)"),
               ("Cable", "3 m"), ("Manguera", "48 mm × 2,1 m"), ("Dimensiones", "54,4 × 42,9 × 67,6 cm"),
               ("Uso", "Seco y mojado, con puerto de drenaje")],
     "includes": ["Varilla de extensión 48 mm (DXVA19-1200A)", "Manguera 48 mm × 2,1 m (DXVA19-2558)",
                  "Boquilla genérica 48 mm (DXVA19-1300)", "Boquilla para rincones 48 mm (DXVA19-1400)",
                  "Cepillo para superficies 48 mm (DXVA19-2591)", "Cepillo redondo 48 mm (DXVA19-2400)",
                  "Adaptador para herramientas 48 mm (DXVA19-2780)", "Bolsa de accesorios con soporte para filtros (DXVA19-5256)",
                  "Filtro de cartucho lavable seco/mojado (DXVC6910)", "Filtro de espuma (DXVA19-1600)",
                  "Bolsa de filtro para polvo (DXVA19-4201)"],
     "warranty": WARRANTY_DEWALT, "video": "fJYHWVcLDMk", "cards": "DEWALT",
     "related": ["aspiradora-dewalt-stealthsonic-20l", "manguera-dewalt-dxva19-2558", "silenciador-dewalt-dxva22-2520"]},
    # ---------------------------------------------------------------- inflators
    {"slug": "compresor-stanley-12v-auto", "family": "infladores", "brand": "STANLEY",
     "model": "SXIF0001", "name": "Compresor digital 12V para auto",
     "tagline": "10 bar · 150 PSI · luz LED",
     "lead": "Compacto, resistente y práctico para el uso diario: se conecta al encendedor del auto y ofrece un "
             "inflado preciso gracias a su pantalla digital con presión ajustable y modos preestablecidos.",
     "body": ["Incorpora luz LED para trabajar con poca luz, patas antivibración, estructura de TPU duradera y "
              "espacio integrado para guardar boquillas y cable."],
     "highlights": ["Pantalla digital", "Modos preestablecidos", "Luz LED", "Almacenamiento integrado"],
     "specs": [("Alimentación", "12 V DC · encendedor del auto"), ("Presión máxima", "10 bar · 150 PSI"),
               ("Flujo de aire", "23 L/min @ 0 bar"), ("Tiempo de inflado", "6 min (0–2,5 bar; 195/60 R15)"),
               ("Cable", "3 m"), ("Peso neto", "1,1 kg")],
     "includes": ["2 boquillas", "1 aguja para balones", "2 adaptadores", "2 fusibles", "Bolsa de transporte"],
     "warranty": WARRANTY_STANLEY, "cards": "STANLEY", "related": ["mini-compresor-stanley-portatil"]},
    {"slug": "mini-compresor-stanley-portatil", "family": "infladores", "brand": "STANLEY",
     "model": "SXIF0101", "name": "Mini compresor portátil 12V",
     "tagline": "Inalámbrico · powerbank · 150 PSI",
     "lead": "Infla hasta 4 neumáticos de auto u 8 de bicicleta desde cero con una carga completa. Ultra compacto "
             "(0,58 kg), con pantalla digital, corte automático, luz LED y función powerbank para cargar el celular.",
     "body": ["Dos fuentes de energía: su batería recargable por USB-C o el cable al encendedor del auto. Siempre "
              "listo para emergencias, viajes o el uso diario."],
     "highlights": ["Inalámbrico", "Corte automático", "Powerbank USB", "5 modos preestablecidos"],
     "specs": [("Alimentación", "Batería recargable 22,2 Wh (6.000 mAh) · cable 12 V"),
               ("Presión máxima", "10 bar · 150 PSI"), ("Flujo de aire", "14,2 L/min @ 0 bar"),
               ("Neumáticos por carga", "4 (195/55 R15)"),
               ("Tiempo de inflado", "12 min 40 s (0–2,5 bar) · 45 s relleno 30–36 PSI"),
               ("Peso neto", "0,58 kg")],
     "includes": ["Manguera de aire 29 cm", "Cable para encendedor 3 m", "Cable USB-C 1 m", "3 adaptadores de válvula",
                  "Fusible de repuesto", "Bolsa de transporte"],
     "warranty": WARRANTY_STANLEY, "video": "94NvC9-nRrk", "cards": "STANLEY", "related": ["compresor-stanley-12v-auto"]},
    # ---------------------------------------------------------------- accessories (related = fits first, then the rest)
    {"slug": "filtro-hepa-dewalt-dxvc4003", "family": "accesorios", "brand": "DEWALT",
     "model": "DXVC4003", "name": "Filtro HEPA", "tagline": "0,3 micrones · 99,97 %",
     "lead": "Filtro de cartucho HEPA lavable y reutilizable para aspiradoras seco/mojado DEWALT. Captura "
             "partículas de hasta 0,3 micrones con una eficiencia del 99,97 %.",
     "body": ["Ideal para polvo fino de interior, tapicería, pelo de mascota, polen y alérgenos. Sistema Clean "
              "Connect: se instala y se retira girándolo, de forma rápida, fácil y segura."],
     "specs": [("Eficiencia", "99,97 % hasta 0,3 micrones"), ("Tipo", "Cartucho lavable y reutilizable"),
               ("Compatible con", "DXV20S-QT (20 L)")],
     "warranty": WARRANTY_ACC, "video": "Jm2kwOkVaV8", "filters_block": True,
     "fits": ["aspiradora-dewalt-stealthsonic-20l"]},
    {"slug": "filtro-cartucho-dewalt-dxvc4001", "family": "accesorios", "brand": "DEWALT",
     "model": "DXVC4001", "name": "Filtro de cartucho estándar", "tagline": "5 micrones · 95 %",
     "lead": "Filtro de cartucho lavable y reutilizable para aspiradoras seco/mojado DEWALT. Recoge partículas "
             "de hasta 5 micrones con una eficiencia del 95 %.",
     "body": ["Para residuos húmedos, aserrín y virutas, escombros de obra, tierra y polvo de concreto, y cenizas "
              "frías. Sistema Clean Connect: instalación y extracción rápida, fácil y segura."],
     "specs": [("Eficiencia", "95 % hasta 5 micrones"), ("Tipo", "Cartucho lavable y reutilizable"),
               ("Compatible con", "DXV20S-QT (20 L)")],
     "warranty": WARRANTY_ACC, "video": "ecjU69-xx7g", "filters_block": True,
     "fits": ["aspiradora-dewalt-stealthsonic-20l"]},
    {"slug": "filtro-esponja-dewalt-dxva20-1200a", "family": "accesorios", "brand": "DEWALT",
     "model": "DXVA20-1200A", "name": "Filtro de esponja", "tagline": "Para trabajo húmedo",
     "lead": "Filtro de espuma de polietileno para recoger líquidos: protege el motor y prolonga su vida útil.",
     "body": ["De instalación rápida y eficaz. Puede usarse junto al filtro de sólidos o de manera independiente, "
              "en el hogar, el taller o entornos industriales."],
     "specs": [("Material", "Polietileno"), ("Uso", "Trabajo húmedo"), ("Compatible con", "DXV20S-QT (20 L)")],
     "warranty": WARRANTY_ACC, "fits": ["aspiradora-dewalt-stealthsonic-20l"]},
    {"slug": "bolsas-polvo-dewalt-dxva19-4204", "family": "accesorios", "brand": "DEWALT",
     "model": "DXVA19-4204", "name": "Bolsas de polvo (pack de 3)", "tagline": "Desechables · limpieza en seco",
     "lead": "Bolsa de filtro desechable de cartón: se instala fácilmente dentro del tanque y permite vaciar "
             "grandes desórdenes sin levantar polvo.",
     "body": ["Ideal para limpieza en seco. Pack de 3 unidades."],
     "specs": [("Contenido", "3 bolsas"), ("Material", "Cartón / papel filtrante"), ("Uso", "Limpieza en seco"),
               ("Compatible con", "DXV20S-QT (20 L)")],
     "warranty": WARRANTY_ACC, "fits": ["aspiradora-dewalt-stealthsonic-20l"]},
    {"slug": "manguera-dewalt-dxva19-2558", "family": "accesorios", "brand": "DEWALT",
     "model": "DXVA19-2558", "name": "Manguera súper flexible", "tagline": "48 mm × 2,1 m",
     "lead": "Manguera de 48 mm (1-7/8\") de diámetro y 2,1 metros de largo para aspiradoras DEWALT seco/mojado "
             "de 20 a 38 litros.",
     "body": ["Aporta versatilidad para llegar fácilmente a rincones, grietas y espacios reducidos en el hogar, "
              "el trabajo o la obra. Diseño de uso universal: compatible también con otras marcas del mismo diámetro."],
     "specs": [("Diámetro", "48 mm · 1-7/8\""), ("Largo", "2,1 m"), ("Compatible con", "DXV20S-QT · DXV38S-QT")],
     "warranty": WARRANTY_ACC, "fits": ["aspiradora-dewalt-stealthsonic-20l", "aspiradora-dewalt-stealthsonic-38l"]},
    {"slug": "silenciador-dewalt-dxva22-2520", "family": "accesorios", "brand": "DEWALT",
     "model": "DXVA22-2520", "name": "Silenciador", "tagline": "Puertos 1-7/8\" y 2-1/2\"",
     "lead": "Reduce el ruido de la aspiradora sin reducir la potencia de succión: encaja en el puerto de escape "
             "para un ambiente de trabajo más cómodo.",
     "body": ["Para aspiradoras seco/mojado DEWALT con puertos de escape de 1-7/8\" y 2-1/2\"."],
     "specs": [("Puertos", "1-7/8\" y 2-1/2\""), ("Compatible con", "DXV20S-QT · DXV38S-QT")],
     "warranty": WARRANTY_ACC, "fits": ["aspiradora-dewalt-stealthsonic-20l", "aspiradora-dewalt-stealthsonic-38l"]},
]
_ACCS = [p["slug"] for p in PRODUCTS if p["family"] == "accesorios"]
for _p in PRODUCTS:
    if _p["family"] == "accesorios":
        _p["related"] = _p["fits"] + [s for s in _ACCS if s != _p["slug"]]

# the old site's "FILTROS" comparison block (HEPA + cartucho pages). DXVC4002 is not carried → shown as not available.
# Old-site typos fixed: HEPA "99.7%" → 99,97 %, "0.5 micras" → 0,3 micrones (the product's own spec).
FILTERS_BLOCK = {
    "title": "Filtros", "intro": "Se adaptan a la línea de aspiradora en seco/mojado DEWALT STEALTHSONIC y clásica.",
    "items": [
        {"name": "Standard", "model": "DXVC4001", "spec": "5 micrones | 95% eficiencia", "size": "5 micrones",
         "eff": "95%", "slug": "filtro-cartucho-dewalt-dxvc4001", "img": "filtro-cartucho-dewalt-dxvc4001"},
        {"name": "Premium", "model": "DXVC4002", "spec": "1 micrón | 99% eficiencia", "size": "1 micrón",
         "eff": "99%", "slug": None, "img": "site:filt_prem"},
        {"name": "HEPA", "model": "DXVC4003", "spec": "0,3 micrones | 99,97% eficiencia", "size": "0,3 micrones",
         "eff": "99,97%", "slug": "filtro-hepa-dewalt-dxvc4003", "img": "filtro-hepa-dewalt-dxvc4003"},
    ]}

# first photo = the card / main photo (a clean product-only "profile" shot); banners/infographics after.
_V38, _V20, _C12, _ST, _ACC = ("brand:ASP_DW_10G_SS_QT/", "brand:ASP_DW_5G_SS_QT/", "brand:CAR12V_INFL_ST/",
                               "brand:MINI_INFL_ST/", "brand:DEWALT VAC ACCESSORIES/")
PHOTOS = {
    "aspiradora-dewalt-stealthsonic-38l": [_V38 + f for f in (
        "DXV38S-QT_.jpg", "DXV38S-QT_WA1.jpg", "DXV38S-QT_WA2.jpg", "DXV38S-QT_F7.jpg", "DXV08SL-QT_G.jpg",
        "ASP_DW_10G_SS_QT_2.jpg", "ASP_DW_10G_SS_QT_1.jpg", "ASP_DW_10G_SS_QT_3.jpg", "ASP_DW_10G_SS_QT_4.jpg",
        "ASP_DW_10G_SS_QT_5.jpg")],
    "aspiradora-dewalt-stealthsonic-20l": [_V20 + f for f in (
        "DXV05S-QT_WA.jpg", "DXV20S-QT - 1.jpg", "DXV05S-QT_G.jpg", "DXV05S-QT_4.jpg", "DXV05S-QT_F6.jpg",
        "DXV05S-QT_A2.jpg", "DXV05S-QT_F1.jpg", "DXV05S-QT_F2.jpg", "DXV20P-QT - 7.webp", "DXV20S-QT - 2.jpg")],
    "compresor-stanley-12v-auto": [_C12 + f for f in (
        "SXIF0001_.jpg", "D_NQ_NP_2X_700784-MLA99781949140_122025-F.webp",
        "D_NQ_NP_2X_698457-MLA99781978828_122025-F.webp", "SXIF0001_3.jpg",
        "D_NQ_NP_2X_741315-MLA100268918739_122025-F.webp", "D_NQ_NP_2X_832466-MLA99781969020_122025-F.webp",
        "D_NQ_NP_2X_988124-MLA99782135492_122025-F.webp", "SXIF0001_6.jpg")],
    "mini-compresor-stanley-portatil": [_ST + f for f in (
        "STANLEY MINI INFLATOR.jpg", "STANLEY MINI INFLATOR 1.jpg", "STANLEY MINI INFLATOR 5.jpg",
        "STANLEY MINI INFLATOR 2.jpg", "STANLEY MINI INFLATOR 4.jpg")],
    "filtro-hepa-dewalt-dxvc4003": [_ACC + "FIL_HEPA_DW_CH/" + f for f in
                                    ("DXVC4003_perfil.webp", "13.png", "14.png", "15.png", "16.png")],
    "filtro-cartucho-dewalt-dxvc4001": [_ACC + "FIL_CAR_DW_CH/" + f for f in
                                        ("DXVC4001_perfil.webp", "1.png", "18.png", "3.png")],
    "filtro-esponja-dewalt-dxva20-1200a": [_ACC + f for f in ("FIL_ESP_DW_CH.png", "FIL_ESP_DW_CH (2).png")],
    "bolsas-polvo-dewalt-dxva19-4204": [_ACC + f for f in ("BOL_POL_DW_CH.jpg", "BOL_POL_DW_CH 2.jpg")],
    "manguera-dewalt-dxva19-2558": [_ACC + "MANG_CH_DW.webp"],
    "silenciador-dewalt-dxva22-2520": [_ACC + "SIL_DW.webp"],
}

# site-wide photos → docs/assets/img/site/<n>.jpg, n = position (1-based) in this list
SITE_PHOTOS = [
    ("hero", _V20 + "DXV08SL-QT_A9.jpg"),                      # the old site's full-width intro banner photo
    ("inflator_life", _C12 + "D_NQ_NP_2X_700784-MLA99781949140_122025-F.webp"),
    ("logo", "logo:LOGO GTA IMPORTS.png"),
    ("dw_guarantee", BRAND_CARDS["DEWALT"][0]), ("dw_brand", BRAND_CARDS["DEWALT"][1]),
    ("st_guarantee", BRAND_CARDS["STANLEY"][0]), ("st_brand", BRAND_CARDS["STANLEY"][1]),
    ("filt_prem", "static:filt-prem.webp"),
    ("ch_ml", "static:ch-ml.webp"), ("ch_sodimac", "static:ch-sodimac.webp"),
]

# old Odoo URLs → new pages (stub redirect pages, so indexed links keep working)
_ODOO_PRODUCT = {
    "asp-dw-10g-ss-qt-dewalt-aspiradora-38l-silenciosa-stealthsonic-profesional-5hp-dxv38s-qt-172": "productos/aspiradora-dewalt-stealthsonic-38l/",
    "asp-dw-10g-ss-qt-dewalt-aspiradora-silenciosa-stealthsonic-seco-mojado-38l-172": "productos/aspiradora-dewalt-stealthsonic-38l/",
    "asp-dw-5g-ss-qt-dewalt-aspiradora-20l-silenciosa-stealthsonic-profesional-4hp-dxv20s-qt-10": "productos/aspiradora-dewalt-stealthsonic-20l/",
    "asp-dw-5g-ss-qt-dewalt-aspiradora-silenciosa-stealthsonic-seco-mojado-19l-10": "productos/aspiradora-dewalt-stealthsonic-20l/",
    "car12v-infl-st-stanley-mini-compresor-digital-12v-auto-150-psi-sxif0001-16": "productos/compresor-stanley-12v-auto/",
    "cmxptxa1201-craftsman-mini-compresor-portatil-auto-12v-10-bar-cmxptxa1201-176": "productos/#infladores",
    "fil-car-dw-ch-dewalt-filtro-de-cartucho-seco-mojado-aspiradora-15-a-30-litros-dxvc4001-17": "productos/filtro-cartucho-dewalt-dxvc4001/",
    "fil-hepa-dw-ch-dewalt-filtro-hepa-premium-seco-mojado-aspiradora-15-a-30-litros-dxvc4003-18": "productos/filtro-hepa-dewalt-dxvc4003/",
    "fil-esp-dw-ch-dewalt-filtro-de-esponja-para-aspiradora-15-a-30-litros-dxva20-1200a-19": "productos/filtro-esponja-dewalt-dxva20-1200a/",
    "bol-pol-dw-ch-dewalt-3-piezas-de-bolsas-de-carton-para-polvo-para-aspiradora-de-15-a-30-litros-dxva19-4204-20": "productos/bolsas-polvo-dewalt-dxva19-4204/",
    "mang-ch-dw-dewalt-manguera-super-flexible-aspiradora-48mm-x-2-1m-1-7-8-dxva19-2558-21": "productos/manguera-dewalt-dxva19-2558/",
    "sil-dw-dewalt-silenciador-aspiradora-1-7-8-2-1-2-dxva22-2520-22": "productos/silenciador-dewalt-dxva22-2520/",
}
REDIRECTS = {"shop": "productos/", "tienda": "productos/", "about-us": "empresa/", "aboutus": "empresa/",
             "faq-s": "preguntas-frecuentes/", "contactus": "empresa/#contacto", "privacy": "privacidad/",
             "politica-de-devolucion": "garantia-y-devoluciones/",
             "shop/category/aspiradoras-1": "productos/#aspiradoras", "shop/category/infladores-2": "productos/#infladores",
             "shop/category/accesorios-14": "productos/#accesorios", "shop/category/repuestos-6": "productos/#accesorios",
             "shop/cart": "productos/"}
REDIRECTS.update({f"shop/{k}": v for k, v in _ODOO_PRODUCT.items()})
