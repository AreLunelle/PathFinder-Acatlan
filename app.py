from collections import deque
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# ==========================
# 1. Grafo de FES Acatlán
# ==========================

mapa_fes = {
    "Entrada principal": [
        "Biblioteca",
        "Cajas",
        "Área deportiva"
    ],
    "Biblioteca": [
        "Entrada principal",
        "Cajas",
        "Cafetería",
        "Explanada principal"
    ],
    "Cafetería": [
        "Biblioteca",
        "Área deportiva"
    ],
    "Área deportiva": [
        "Entrada principal",
        "Cafetería",
        "Centro de idiomas"
    ],
    "Cajas": [
        "Entrada principal",
        "Biblioteca",
        "Explanada principal",
        "Centro de desarrollo tecnológico"
    ],
    "Explanada principal": [
        "Cajas",
        "Servicios médicos",
        "Centro de idiomas",
        "Biblioteca"
    ],
    "Centro de idiomas": [
        "Explanada principal",
        "Centro cultural",
        "Área deportiva"
    ],
    "Centro cultural": [
        "Centro de idiomas"
    ],
    "Servicios médicos": [
        "Explanada principal"
    ],
    "Centro de desarrollo tecnológico": [
        "Cajas"
    ]
}

LUGARES = list(mapa_fes.keys())


# ==========================
# 2. Algoritmo BFS
# ==========================

def buscar_camino_bfs(mapa, origen, destino):
    """
    Busca un camino desde 'origen' hasta 'destino' usando BFS.
    Retorna una lista con la ruta o None si no existe.
    """
    cola = deque([[origen]])
    visitados = set()

    while cola:
        ruta = cola.popleft()
        actual = ruta[-1]

        if actual == destino:
            return ruta

        if actual not in visitados:
            visitados.add(actual)
            for vecino in mapa.get(actual, []):
                nueva = list(ruta)
                nueva.append(vecino)
                cola.append(nueva)

    return None


# ==========================
# 3. Rutas web
# ==========================

@app.route("/")
def index():
    # Enviamos la lista de lugares al template
    return render_template("index.html", lugares=LUGARES)


@app.route("/ruta", methods=["POST"])
def ruta():
    data = request.get_json()
    origen = data.get("origen")
    destino = data.get("destino")

    if origen not in mapa_fes or destino not in mapa_fes:
        return jsonify({
            "ok": False,
            "mensaje": "Uno de los lugares seleccionados no existe en el mapa."
        })

    if origen == destino:
        return jsonify({
            "ok": False,
            "mensaje": "Ya te encuentras en ese lugar 😉"
        })

    ruta_calculada = buscar_camino_bfs(mapa_fes, origen, destino)

    if ruta_calculada:
        return jsonify({
            "ok": True,
            "ruta": ruta_calculada,
            "pasos": len(ruta_calculada) - 1
        })
    else:
        return jsonify({
            "ok": False,
            "mensaje": "No se encontró un camino entre esos dos puntos."
        })


if __name__ == "__main__":
    # debug=True para que sea fácil probar mientras desarrollas
    app.run(debug=True)
