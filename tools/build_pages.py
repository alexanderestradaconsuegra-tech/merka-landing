# Genera las paginas SEO de Merka POS (una carpeta por pagina, con index.html).
import json,os
V='20261112'; BASE='https://merkapos.pro'
WA='https://wa.me/56992025527?text=Hola%2C%20quiero%20informaci%C3%B3n%20de%20Merka%20POS.'
PAGES=[
{'slug':'sistema-pos-minimarket','title':'Sistema POS para minimarket en Chile | Merka POS',
 'desc':'Sistema POS para minimarket: cobra rápido, controla el stock, cierra la caja y emite boleta electrónica del SII. Desde $8.990 al mes, 30 días gratis.',
 'h1':'Sistema POS para minimarket, hecho para el día a día del rubro.',
 'lead':'Merka POS nació de la necesidad de un minimarket: cobrar rápido, saber qué falta en las repisas y cerrar la caja sin descuadres. Funciona en el navegador, en celular, tablet o computador.',
 'sections':[
  ('Lo que necesita un minimarket de su sistema',['Cobrar con efectivo, tarjeta, transferencia o pago mixto en pocos segundos, escaneando el código de barras.','Que el stock baje solo con cada venta y avise cuando un producto llega al mínimo.','Cerrar la caja por turno, contando los billetes y viendo la diferencia.','Llevar el fiado con límite por cliente, historial de pagos y aviso de vencimiento.','Vender por peso con balanza de códigos de barras: productos a granel, quesos, fiambres.','Ver la ganancia real: ventas menos costos menos gastos.']),
  ('Boleta electrónica sin hacerla a mano',['Cada venta con efectivo o tarjeta puede generar su boleta electrónica del SII, a través de Tuu, con el detalle de lo que compró el cliente.','Se imprime en 80 mm o se guarda en PDF, y si anulas una venta sale la nota de crédito.','Necesitas inicio de actividades, firma electrónica y habilitar los documentos en Tuu. Qué ventas llevan boleta lo defines tú con tu contador.']),
  ('Equipo con límites y registro',['Cada cajero ve y hace solo lo que le permites.','Si alguien elimina una venta, queda anotado en el registro de acciones.'])],
 'faq':[('¿Sirve para un minimarket pequeño?','Sí. Funciona con un solo dispositivo y crece con tu negocio: usuarios ilimitados con permisos, sin instalar nada.'),
        ('¿Necesito comprar equipos especiales?','No. Funciona en el navegador. Si usas lector de códigos de barras o balanza con código EAN-13, el sistema los reconoce.'),
        ('¿Cuánto cuesta?','Oferta de lanzamiento: $8.990 al mes, con todo incluido. El precio normal es $15.000 al mes. Tienes 30 días gratis, sin tarjeta.')]},
{'slug':'software-punto-de-venta-chile','title':'Software punto de venta en Chile con boleta electrónica | Merka POS',
 'desc':'Software de punto de venta en la nube para comercios de Chile: ventas, inventario, caja, fiado, reportes y boleta electrónica SII. 30 días gratis.',
 'h1':'Software de punto de venta en Chile, simple, claro y accesible.',
 'lead':'Un software de punto de venta para vender, controlar el inventario y estar al día con la boleta electrónica, sin instalar nada y sin pagar de más.',
 'sections':[
  ('Qué incluye',['Terminal de ventas con lector de códigos de barras.','Inventario con fotos, categorías, precios por volumen y alertas de reposición.','Cierre de caja por turno y reportes de ganancia por día, semana, mes o año.','Crédito a clientes y cuentas por pagar a proveedores.','Usuarios ilimitados con permisos y registro de acciones.','Boleta electrónica del SII al cobrar, a través de Tuu, con nota de crédito.']),
  ('Pensado para comercios chilenos',['Precios en pesos chilenos y boleta electrónica según el SII.','Venta por peso con balanza para queserías, carnicerías y venta a granel.','Funciona en celular, tablet y computador, con tus datos separados de los de otros negocios.']),
  ('Seguridad',['Conexión cifrada (HTTPS).','La llave de la boleta electrónica se guarda cifrada.','Merka POS no guarda números de tarjeta.'])],
 'faq':[('¿Es un software en la nube?','Sí. Lo abres desde el navegador en app.merkapos.pro, sin instalar programas. Necesita conexión a internet.'),
        ('¿Emite factura?','Por ahora solo boleta electrónica y nota de crédito.'),
        ('¿Hay contrato?','No. Son 30 días gratis, sin tarjeta, y puedes cancelar cuando quieras.')]},
{'slug':'boleta-electronica-minimarket','title':'Boleta electrónica para minimarket: cómo emitirla desde tu POS | Merka POS',
 'desc':'Qué necesita un minimarket para emitir boleta electrónica del SII desde su sistema de ventas: firma electrónica, habilitación y conexión. Pasos claros.',
 'h1':'Boleta electrónica para minimarket: cómo emitirla desde tu sistema de ventas.',
 'lead':'Emitir boleta electrónica no tiene que ser complicado. Esto es lo que necesitas y cómo se conecta con Merka POS. Merka POS no entrega asesoría tributaria: qué ventas llevan boleta lo define tu contador.',
 'sections':[
  ('Lo que necesitas antes de empezar',['Inicio de actividades en el SII.','Firma electrónica del representante legal.','Documentos electrónicos habilitados con Tuu, que demora de 3 a 7 días hábiles una vez completa la información.']),
  ('Cómo se conecta con Merka POS',['Ingresas la llave que te entrega Tuu en Configuración, en el panel.','Pulsas "Probar conexión" y haces pruebas con documentos de prueba.','Cuando cobras una venta con efectivo o tarjeta, la boleta se emite sola y se imprime en 80 mm.','Si anulas la venta, el sistema emite la nota de crédito.']),
  ('Qué tener en cuenta',['Si tu máquina de tarjetas ya emite boleta, puede duplicarse: conviene dejar una sola fuente por medio de pago.','La transferencia no emite boleta si así lo decide tu negocio y tu contador.','El costo de emisión depende de tu plan con Tuu.'])],
 'faq':[('¿Necesito firma electrónica?','Sí, el representante legal necesita firma electrónica para habilitar los documentos.'),
        ('¿Cuánto demora la habilitación?','Con el proveedor demora de 3 a 7 días hábiles una vez completa la información.'),
        ('¿Es obligatorio emitir boleta electrónica?','Depende de tu situación ante el SII. Confírmalo con tu contador.')]},
]
def esc(t): return t.replace('&','&amp;').replace('<','&lt;').replace('>','&gt;')
def page(pg):
    url=f"{BASE}/{pg['slug']}/"
    secs=''.join(f"<section class='pg__s'><h2>{esc(h)}</h2><ul>{''.join('<li>'+esc(x)+'</li>' for x in items)}</ul></section>" for h,items in pg['sections'])
    faq=''.join(f"<details><summary>{esc(q)}</summary><p>{esc(a)}</p></details>" for q,a in pg['faq'])
    others=''.join(f"<li><a href='/{o['slug']}/'>{esc(o['h1'].rstrip('.'))}</a></li>" for o in PAGES if o['slug']!=pg['slug'])
    graph={"@context":"https://schema.org","@graph":[
     {"@type":"WebPage","@id":url+"#page","url":url,"name":pg['title'],"description":pg['desc'],"inLanguage":"es-CL","isPartOf":{"@id":BASE+"/#site"}},
     {"@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":1,"name":"Merka POS","item":BASE+"/"},{"@type":"ListItem","position":2,"name":pg['h1'].rstrip('.'),"item":url}]},
     {"@type":"FAQPage","mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in pg['faq']]}]}
    return f"""<!doctype html>
<html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(pg['title'])}</title>
<meta name="description" content="{esc(pg['desc'])}">
<meta name="robots" content="index,follow,max-snippet:-1,max-image-preview:large">
<link rel="canonical" href="{url}"><link rel="alternate" hreflang="es-CL" href="{url}">
<meta name="theme-color" content="#F1F1EE">
<link rel="icon" type="image/svg+xml" href="/favicon.svg"><link rel="icon" href="/favicon.ico" sizes="any"><link rel="apple-touch-icon" href="/apple-touch-icon.png">
<meta property="og:type" content="article"><meta property="og:locale" content="es_CL"><meta property="og:site_name" content="Merka POS"><meta property="og:title" content="{esc(pg['title'])}"><meta property="og:description" content="{esc(pg['desc'])}"><meta property="og:url" content="{url}"><meta property="og:image" content="{BASE}/og-image.png?v={V}">
<meta name="twitter:card" content="summary_large_image">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Manrope:wght@400;500;600;700;800&family=JetBrains+Mono:wght@500;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/site.css?v={V}">
<script type="application/ld+json">{json.dumps(graph,ensure_ascii=False)}</script>
</head><body class="pg">
<header class="nav pg__nav"><div class="wrap nav__bar"><a class="brand brand--logo" href="/" aria-label="Merka POS, inicio"><img src="/media/logo-merka-pos-dark.svg" width="155" height="48" alt="Merka POS"></a><a class="btn btn-primary btn-sm" href="https://app.merkapos.pro/">Probar 30 días gratis</a></div></header>
<main><div class="wrap pg__w">
<nav class="pg__bc" aria-label="Migas de pan"><a href="/">Merka POS</a> / <span>{esc(pg['h1'].rstrip('.'))}</span></nav>
<h1>{esc(pg['h1'])}</h1>
<p class="pg__lead">{esc(pg['lead'])}</p>
<div class="pg__cta"><a class="btn btn-primary" href="https://app.merkapos.pro/">Probar 30 días gratis</a><a class="btn btn-ghost" href="{WA}" rel="noopener">Hablar por WhatsApp</a></div>
<p class="pg__price">Oferta de lanzamiento: <b>$8.990 al mes</b> (precio normal $15.000), con todo incluido. Sin tarjeta y sin contrato.</p>
{secs}
<section class="pg__s"><h2>Preguntas frecuentes</h2><div class="pg__faq">{faq}</div></section>
<section class="pg__s pg__more"><h2>Más sobre Merka POS</h2><ul><li><a href="/">Merka POS, punto de venta con boleta electrónica</a></li>{others}</ul></section>
</div></main>
<footer class="pg__ft"><div class="wrap">Merka POS es un software de <a href="https://autix.pro" rel="noopener">Autix</a>. SII y Tuu son marcas de sus respectivos titulares y se mencionan solo para indicar compatibilidad. &copy; 2026 Merka POS.</div></footer>
</body></html>"""
for pg in PAGES:
    os.makedirs(pg['slug'],exist_ok=True)
    open(f"{pg['slug']}/index.html",'w',encoding='utf-8').write(page(pg))
urls=[(BASE+'/','1.0')]+[(f"{BASE}/{p['slug']}/",'0.8') for p in PAGES]
sm='<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'+''.join(f"  <url><loc>{u}</loc><lastmod>2026-11-12</lastmod><changefreq>monthly</changefreq><priority>{pr}</priority></url>\n" for u,pr in urls)+'</urlset>\n'
open('sitemap.xml','w',encoding='utf-8').write(sm)
open('robots.txt','w').write(f"User-agent: *\nAllow: /\nDisallow: /health\n\nSitemap: {BASE}/sitemap.xml\n")
print('ok',[p['slug'] for p in PAGES])
