# Trámites RD Exterior: plan de trabajo

Meta: ingresos pasivos con una guía PDF (US$12) para dominicanos en el exterior, con un blog SEO que lleva visitas a la tienda. Inversión: $0. Negocio hermano: Terreno Seguro RD (https://bsser.github.io/terreno-seguro-rd); enlaza a ese sitio cuando un artículo trate de propiedades.

## Estado
- [x] Producto: guía "Trámites RD desde el Exterior" (10 páginas), en el repo privado `Bsser/tramites-rd-exterior-privado`
- [x] PDF gratis: `estaticos/errores-tramites-rd.pdf`
- [x] Blog: este repo → `python build.py` genera `docs/`
- [x] Publicado en GitHub Pages: https://bsser.github.io/tramites-rd-exterior
- [x] Gumroad: https://jontastic64.gumroad.com/l/tramites-rd-exterior (publicado 2026-11-24, US$12)
- [x] Google Search Console: verificado (etiqueta meta en build.py, no quitarla) y sitemap enviado
- [x] Tarea diaria programada (9:05 a. m., tarea tramites-rd-exterior-diario)

## Rutina diaria (la tarea programada)
1. Tomar el primer tema pendiente de la cola, investigarlo con fuentes oficiales (jce.gob.do, pasaportes.gob.do, mirex.gob.do, consulados, leyes) y medios dominicanos serios, y escribir `contenido/<slug>.md` (700–1200 palabras; sin inventar cifras, tarifas ni plazos).
2. `python build.py` (debe imprimir OK) → commit → push.
3. Marcar el tema como hecho aquí y anotar la fecha en el registro.
4. Lunes: 3 publicaciones para grupos de dominicanos en el exterior en `ventas/posts-semana.md` del repo privado (las publica el dueño).
5. Día 1 del mes: revisar si cambió algún requisito importante (cédula, pasaporte, actas) y proponer en `ventas/propuesta-actualizacion.md` qué actualizar en la guía.

## Cola de temas (SEO)
- [x] Qué pasa si no renuevas la cédula a tiempo (fecha límite y consecuencias, solo con fuente oficial)
- [x] Cómo pedir una cita en citas.jce.gob.do paso a paso
- [ ] Cómo declarar en el consulado a un hijo nacido en Estados Unidos
- [ ] Transcripción del acta de nacimiento extranjera en la JCE
- [ ] Cómo apostillar un documento dominicano para usarlo en EE. UU.
- [ ] Cómo sacar un acta de nacimiento dominicana si vives fuera
- [ ] Doble nacionalidad: ¿pierdo la dominicana si me hago ciudadano de EE. UU.?
- [ ] Cómo votar desde el exterior en las elecciones dominicanas
- [ ] Renovar la licencia de conducir dominicana desde el exterior
- [ ] Comprar una casa en RD desde Nueva York: pasos para no ser estafado
- [ ] Cómo cobrar una herencia en RD si vives fuera
- [ ] Qué es la Ley 171-07 y quién puede usarla (pensionados y rentistas)
- [ ] Cómo enviar dinero a RD: qué comparar antes de elegir remesadora
- [ ] Cómo cambiar el estado civil en la cédula después de casarte fuera
- [ ] Inscribir un matrimonio celebrado en el exterior en la JCE
- [ ] Consulados dominicanos en EE. UU.: lista y servicios
- [ ] Cómo revocar un poder que diste en RD
- [ ] Traer el carro o la mudanza a RD: qué saber de aduanas
- [ ] Jubilarse en RD: seguro médico y residencia
- [ ] Errores en el acta de nacimiento: cómo corregirlos desde fuera

## Registro
- 2026-11-24: guía, PDF gratis y blog con 3 artículos creados.
- 2026-11-24: artículo que-pasa-si-no-renuevas-la-cedula-a-tiempo (plazo del exterior enero 2028 sin confirmar en nota reciente).
- 2026-11-25: artículo cita-jce-citas-jce-gob-do-paso-a-paso (lista de oficinas sin cita solo de prensa; cancelar/reprogramar y citas grupales sin confirmar).
