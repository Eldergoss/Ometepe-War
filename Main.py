from naves import *
from dado import *

# crear buques correctamente
buque_a = buque("El Nicarao", 100, 10, 20, 10)
buque_b = buque("El Ometepe Hambriento", 100, 10, 20, 11)

# combate
while buque_a.vida > 0 and buque_b.vida > 0:

    print(f"\n{'='*40}")
    print(f"{buque_a.nombre} VIDA: {buque_a.vida}")
    print(f"{buque_b.nombre} VIDA: {buque_b.vida}")
    print(f"{'='*40}")

    opcion = menu_acciones()

    if opcion == "1":
        # El método calculo() ya aplica el daño y retorna un mensaje
        mensaje = buque_a.calculo(buque_b)
        print(f"\n⚔️ {mensaje}")

    elif opcion == "2":
        print(f"\n🛡️ {buque_a.nombre} se defiende (menos daño próximo turno)")
        # Aquí puedes agregar lógica de defensa si quieres

    else:
        print("\n❌ Opción inválida")

# resultado
print(f"\n{'='*40}")
print("🏆 FIN DEL COMBATE 🏆")
if buque_a.vida > 0:
    print(f"✨ Ganador: {buque_a.nombre} ✨")
else:
    print(f"✨ Ganador: {buque_b.nombre} ✨")
print(f"{'='*40}")
