from collections import deque

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
# 3. Bot en consola
# ==========================

def mostrar_lugares_numerados():
    print("\nLugares disponibles en PathFinder Acatlán:\n")
    for i, lugar in enumerate(LUGARES, start=1):
        print(f"  {i}) {lugar}")
    print()


def pedir_lugar(mensaje):
    """
    Solo acepta números del 1 al 10 o 'salir'.
    """
    while True:
        mostrar_lugares_numerados()
        respuesta = input(mensaje).strip()

        if respuesta.lower() == "salir":
            return None

        if respuesta.isdigit():
            numero = int(respuesta)
            if 1 <= numero <= len(LUGARES):
                return LUGARES[numero - 1]

        print("\nLamentamos los inconvenientes, el número no se encuentra disponible.")
        print("Recuerda elegir solo del 1 al 10 de los lugares que hay disponibles.\n")


def pathfinder_bot():
    print("==============================================")
    print("   🤖 PathFinder Acatlán – Guía de rutas      ")
    print("==============================================")
    print("\nEscribe 'salir' en cualquier momento para terminar.\n")

    while True:
        origen = pedir_lugar("¿Desde dónde sales? (número): ")
        if origen is None:
            print("\nGracias por usar PathFinder Acatlán. ¡Hasta luego! 💛")
            break

        destino = pedir_lugar("¿A dónde quieres llegar? (número): ")
        if destino is None:
            print("\nGracias por usar PathFinder Acatlán. ¡Hasta luego! 💛")
            break

        if origen == destino:
            print("\nYa te encuentras en ese lugar\n")
            continue

        ruta = buscar_camino_bfs(mapa_fes, origen, destino)

        if ruta:
            print("\n✅ Ruta sugerida:")
            for paso in ruta:
                print("   →", paso)
            print(f"\nNúmero de pasos: {len(ruta) - 1}\n")
        else:
            print("\n❌ No se encontró un camino entre esos dos puntos.\n")

        seguir = input("¿Quieres buscar otra ruta? (si/no): ").strip().lower()
        if seguir != "si":
            print("\nGracias por usar PathFinder Acatlán. ¡Que tengas un gran día en la FES! ✨")
            break


if __name__ == "__main__":
    pathfinder_bot()
