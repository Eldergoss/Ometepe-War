import random

def lanzamiento():
    valor_alto = 6
    valor_bajo = 1
    return random.randint(valor_bajo, valor_alto)


def menu_acciones():
    print("\n--- TURNO ---")
    print("1. Atacar")
    print("2. Defender")

    opcion = input("Elegí una opción: ")
    return opcion