#!/bin/sh

TARGET="https://servidor-web-dmz-dcogollo.onrender.com"
RUTAS="/admin /config.php /login /secret /backup.zip /index.html"

echo "=== INICIANDO ENUMERACION DE RUTAS EN LA DMZ ==="
echo "Probando peticiones HTTP a rutas conocidas..."

for ruta in $RUTAS; do
  CODE=$(curl -o /dev/null -s -w "%{http_code}" "$TARGET$ruta")
  echo "Ruta probada: $ruta -> Codigo de respuesta HTTP: $CODE"
done

echo "=== ENUMERACION DE RUTAS FINALIZADA ==="

python3 -m http.server 8080
