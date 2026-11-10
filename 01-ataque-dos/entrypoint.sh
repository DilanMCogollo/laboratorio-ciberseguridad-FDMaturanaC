#!/bin/sh

TARGET="https://servidor-web-dmz-fdmaturanac.onrender.com"

echo "=== SIMULACION: GENERANDO TRAFICO MASIVO HTTP ==="
echo "Enviando rafaga de peticiones concurrentes a $TARGET..."

for i in $(seq 1 30); do
  curl -s -o /dev/null "$TARGET" &
done

wait
echo "=== PRUEBA FINALIZADA ==="

# Mantiene el servicio activo en Render
python3 -m http.server 8080
