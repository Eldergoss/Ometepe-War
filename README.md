# ⚓ Batalla Naval - Sistema de Combate por Turnos

Un sistema de combate por turnos inspirado en juegos como Yu-Gi-Oh, donde dos naves se enfrentan calculando daño basado en ataque vs defensa con un componente aleatorio.

## 🎮 Mecánica de Combate

El combate funciona de la siguiente manera:

- **Ataque > Defensa**: El defensor recibe daño igual a `ataque - defensa`
- **Defensa > Ataque**: El atacante recibe daño igual a `defensa - ataque`
- **Ataque = Defensa**: No hay daño para ninguno

### Componente Aleatorio
Cada ataque y defensa se multiplica por un valor aleatorio de `lanzamiento()` (simulando un dado o factor sorpresa).

## 📁 Estructura del Proyecto
