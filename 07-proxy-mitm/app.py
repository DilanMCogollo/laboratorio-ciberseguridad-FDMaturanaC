from flask import Flask, request, Response
import requests

app = Flask(__name__)

TARGET_DMZ = "https://servidor-web-dmz-dcogollo.onrender.com"

@app.route('/', defaults={'path': ''}, methods=['GET', 'POST'])
@app.route('/<path:path>', methods=['GET', 'POST'])
def mitm_proxy(path):
    print(f"\n[MITM INTERCEPTADO] Peticion entrante hacia la ruta: /{path}")
    print(f"[CABECERAS INTERCEPTADAS] {dict(request.headers)}")

    url = f"{TARGET_DMZ}/{path}"
    try:
        resp = requests.get(url, timeout=5)
        contenido_original = resp.text
    except Exception as e:
        contenido_original = f"Error al conectar con la DMZ: {str(e)}"

    # Inyeccion de codigo en la respuesta HTTP
    contenido_alterado = contenido_original + "\n\n<!-- [ALERTA MITM] Este contenido fue alterado en transito por el Proxy Interceptor -->"

    print("[MITM ALERTA] Respuesta modificada e inyectada con exito.")
    return Response(contenido_alterado, status=200, mimetype='text/html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
