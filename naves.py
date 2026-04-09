from dado import *

class buque:
    def __init__(self, nombre, vida, ataque, defensa, velocidad):
        self.nombre = nombre
        self.vida = vida
        self.ataque = ataque
        self.defensa = defensa
        self.velocidad = velocidad

    def calculo(self, objetivo):
        ataque = self.ataque * lanzamiento()
        defensa = objetivo.defensa * lanzamiento()

        if ataque > defensa:
            daño = ataque - defensa
            objetivo.vida -= daño
            return f"Hace {daño} de daño a {objetivo.nombre}"
        else:
            daño = defensa - ataque
            self.vida -= daño
            return f"Recibe {daño} de daño de {objetivo.nombre}"
