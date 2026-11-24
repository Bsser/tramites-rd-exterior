"""Genera el sitio estático en docs/ a partir de contenido/*.md.

Cada .md empieza con cabecera:
    titulo: ...
    descripcion: ...
    fecha: 2026-11-24
    ---
Uso: python build.py
"""
import datetime, html, pathlib, shutil
import markdown

SITIO = "https://bsser.github.io/tramites-rd-exterior"
TIENDA = "https://jontastic64.gumroad.com/l/tramites-rd-exterior"
PRECIO = "US$12"

RAIZ = pathlib.Path(__file__).parent
SALIDA = RAIZ / "docs"

PLANTILLA = """<!doctype html>
<html lang="es"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{titulo}</title>
<meta name="description" content="{descripcion}">
<link rel="canonical" href="{url}">
<meta name="google-site-verification" content="4F6GvPItG1MgDsxIkhHlMnWlIL_Nr4-tKKIEYM5F8QM">
<link rel="stylesheet" href="{base}estilo.css">
</head><body>
<header><a class="marca" href="{base}">Trámites RD Exterior</a><span>Trámites en República Dominicana para dominicanos fuera del país</span></header>
<main>{cuerpo}</main>
<footer>Guía independiente, no afiliada a la JCE, la DGP ni al MIREX. Confirma requisitos y tarifas en jce.gob.do, pasaportes.gob.do y mirex.gob.do.</footer>
</body></html>"""

CTA = f"""<aside class="cta">
<h3>¿Tienes trámites pendientes en RD?</h3>
<p>La guía <b>Trámites RD desde el Exterior</b> explica paso a paso la cédula nueva, el pasaporte electrónico, las actas, los hijos nacidos fuera y los poderes, con checklist por trámite. PDF de 10 páginas.</p>
<a class="boton" href="{TIENDA}">Descargar la guía · {PRECIO}</a>
<p class="gratis">¿Prefieres empezar gratis? <a href="https://jontastic64.gumroad.com/l/errores-tramites-gratis">Descarga los 10 errores que te hacen perder el viaje (PDF)</a>.</p>
<p class="gratis">¿Vives fuera y te interesan los dos temas? <a href="https://jontastic64.gumroad.com/l/pack-dominicano">Pack Dominicano: terreno + trámites, 2 guías por US$17</a>.</p>
<p class="gratis">Herramienta gratis: <a href="https://bsser.github.io/calculadoras-rd/">calculadoras de regalía pascual, salario neto y prestaciones laborales</a>.</p>
</aside>"""


def leer(md_path):
    cabecera, cuerpo = md_path.read_text(encoding="utf-8").split("\n---\n", 1)
    meta = dict(l.split(":", 1) for l in cabecera.strip().splitlines())
    meta = {k.strip(): v.strip() for k, v in meta.items()}
    meta["slug"] = md_path.stem
    meta["html"] = markdown.markdown(cuerpo, extensions=["tables"])
    return meta


def pagina(ruta, base, **campos):
    campos = {k: html.escape(v) if k in ("titulo", "descripcion") else v for k, v in campos.items()}
    ruta.parent.mkdir(parents=True, exist_ok=True)
    ruta.write_text(PLANTILLA.format(base=base, **campos), encoding="utf-8")


def construir():
    if SALIDA.exists():
        shutil.rmtree(SALIDA)
    SALIDA.mkdir()
    for f in (RAIZ / "estaticos").iterdir():
        shutil.copy(f, SALIDA / f.name)

    hoy = datetime.date.today().isoformat()
    # ponytail: artículos con fecha futura se omiten -> permite dejar programados en cola
    arts = [a for a in map(leer, (RAIZ / "contenido").glob("*.md")) if a["fecha"] <= hoy]
    arts.sort(key=lambda a: a["fecha"], reverse=True)

    for a in arts:
        cuerpo = f"<article><h1>{html.escape(a['titulo'])}</h1><p class='fecha'>{a['fecha']}</p>{a['html']}</article>" + CTA.replace("{base}", "../")
        pagina(SALIDA / a["slug"] / "index.html", "../", titulo=a["titulo"] + " | Trámites RD Exterior",
               descripcion=a["descripcion"], url=f"{SITIO}/{a['slug']}/", cuerpo=cuerpo)

    lista = "".join(f"<li><a href='{a['slug']}/'>{html.escape(a['titulo'])}</a><p>{html.escape(a['descripcion'])}</p></li>" for a in arts)
    portada = ("<section class='hero'><h1>Tus trámites en RD, desde donde vivas</h1>"
               "<p>Guías claras para dominicanos en el exterior: cédula nueva, pasaporte, actas, hijos nacidos fuera, poderes y propiedades.</p></section>"
               f"<ul class='lista'>{lista}</ul>" + CTA.replace("{base}", ""))
    pagina(SALIDA / "index.html", "", titulo="Trámites RD Exterior — Cédula, pasaporte y actas para dominicanos fuera del país",
           descripcion="Guías prácticas para dominicanos en el exterior: renovar la cédula nueva, el pasaporte electrónico, pedir actas, declarar hijos y dar poderes.",
           url=f"{SITIO}/", cuerpo=portada)

    urls = [f"{SITIO}/"] + [f"{SITIO}/{a['slug']}/" for a in arts]
    (SALIDA / "sitemap.xml").write_text(
        '<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'
        + "".join(f"<url><loc>{u}</loc></url>" for u in urls) + "</urlset>", encoding="utf-8")
    (SALIDA / "robots.txt").write_text(f"User-agent: *\nAllow: /\nSitemap: {SITIO}/sitemap.xml\n", encoding="utf-8")
    (SALIDA / ".nojekyll").write_text("")
    return arts


if __name__ == "__main__":
    arts = construir()
    # autocomprobación: cada artículo publicado tiene la llamada a la tienda y aparece en el sitemap
    mapa = (SALIDA / "sitemap.xml").read_text(encoding="utf-8")
    for a in arts:
        assert TIENDA in (SALIDA / a["slug"] / "index.html").read_text(encoding="utf-8"), a["slug"]
        assert f"/{a['slug']}/" in mapa, a["slug"]
    print(f"OK: {len(arts)} artículos publicados en docs/")
