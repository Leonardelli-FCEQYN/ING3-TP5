# Código proporcionado por el amigo que trabaja desde las sombras (ChatGPT)
class Socio:
    def __init__(self, id_socio, nombre, nivel):
        self.id_socio = id_socio
        self.nombre = nombre
        self.nivel = nivel
        self.prestamos_activos = 0

class Biblioteca:
    def __init__(self):
        self.socios = {}
        self.niveles = {
            'Básico': 2,
            'Intermedio': 5,
            'Avanzado': 10
        }

    def dar_alta_socio(self, id_socio, nombre, nivel):
        if id_socio in self.socios:
            print(f"El socio con ID {id_socio} ya está dado de alta.")
            return
        if nivel not in self.niveles:
            print(f"Nivel {nivel} no válido. Los niveles válidos son: {', '.join(self.niveles.keys())}")
            return
        nuevo_socio = Socio(id_socio, nombre, nivel)
        self.socios[id_socio] = nuevo_socio
        print(f"Socio {nombre} con ID {id_socio} y nivel {nivel} dado de alta correctamente.")

    def dar_baja_socio(self, id_socio):
        if id_socio not in self.socios:
            print(f"El socio con ID {id_socio} no existe.")
            return
        socio = self.socios[id_socio]
        if socio.prestamos_activos > 0:
            print(f"El socio {socio.nombre} tiene préstamos activos y no puede ser dado de baja.")
            return
        del self.socios[id_socio]
        print(f"Socio {socio.nombre} con ID {id_socio} dado de baja correctamente.")

    def listar_socios(self):
        if not self.socios:
            print("No hay socios registrados.")
            return
        print("Lista de socios:")
        for socio in self.socios.values():
            print(f"ID: {socio.id_socio}, Nombre: {socio.nombre}, Nivel: {socio.nivel}, Préstamos Activos: {socio.prestamos_activos}")

# Ejemplo de uso
if __name__ == "__main__":
    biblioteca = Biblioteca()

    # Dar de alta a algunos socios
    biblioteca.dar_alta_socio(1, "Juan Pérez", "Básico")
    biblioteca.dar_alta_socio(2, "María Gómez", "Intermedio")
    biblioteca.dar_alta_socio(3, "Luis Martínez", "Avanzado")

    # Listar socios
    biblioteca.listar_socios()

    # Intentar dar de alta a un socio ya existente
    biblioteca.dar_alta_socio(1, "Ana López", "Intermedio")

    # Dar de baja a un socio sin préstamos activos
    biblioteca.dar_baja_socio(2)

    # Intentar dar de baja a un socio con préstamos activos
    biblioteca.socios[3].prestamos_activos = 1
    biblioteca.dar_baja_socio(3)

    # Listar socios después de las bajas
    biblioteca.listar_socios()

    #Agrego esta linea para finalizar el issue