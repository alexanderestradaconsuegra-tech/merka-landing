FROM nginx:alpine
RUN apk add --no-cache curl
RUN curl -L "https://raw.githubusercontent.com/alexanderestradaconsuegra-tech/merka-landing/main/index.html" -o /usr/share/nginx/html/index.html
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
