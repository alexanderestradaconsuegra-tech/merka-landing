FROM nginx:1.27-alpine

# Los archivos se copian del repositorio que EasyPanel clona en el build
# (antes se descargaban con curl desde la rama main: la capa se cacheaba y no era trazable).
COPY nginx.conf /etc/nginx/conf.d/default.conf
COPY security-headers.conf /etc/nginx/snippets/security-headers.conf
COPY index.html icon-192.png icon-512.png og-image.png /usr/share/nginx/html/
COPY media/ /usr/share/nginx/html/media/

EXPOSE 80
HEALTHCHECK --interval=30s --timeout=3s --retries=3 \
  CMD wget -qO- http://127.0.0.1/health || exit 1
CMD ["nginx", "-g", "daemon off;"]
