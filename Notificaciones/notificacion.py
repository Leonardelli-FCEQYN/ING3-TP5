## Código proporcionado por el amigo que trabaja desde las sombras (ChatGPT)
from datetime import datetime, timedelta

class Libro:
    def __init__(self, titulo, fecha_vencimiento):
        self.titulo = titulo
        self.fecha_vencimiento = fecha_vencimiento

class Usuario:
    def __init__(self, nombre):
        self.nombre = nombre
        self.prestamos = []

    def prestar_libro(self, libro):
        self.prestamos.append(libro)

    def verificar_notificaciones(self):
        ahora = datetime.now()
        for libro in self.prestamos:
            tiempo_restante = libro.fecha_vencimiento - ahora
            if timedelta(hours=23) < tiempo_restante <= timedelta(hours=24):
                self.enviar_notificacion(libro)

    def enviar_notificacion(self, libro):
        print(f"Hola {self.nombre}, el préstamo del libro '{libro.titulo}' vence en 24 horas. Por favor, recuerda devolverlo para evitar sanciones.")

# Ejemplo de uso
if __name__ == "__main__":
    # Crear un usuario
    usuario = Usuario("Juan")

    # Añadir préstamos de libros
    libro1 = Libro("El Quijote", datetime.now() + timedelta(days=1, hours=1))
    libro2 = Libro("Cien Años de Soledad", datetime.now() + timedelta(days=2))

    usuario.prestar_libro(libro1)
    usuario.prestar_libro(libro2)

    # Verificar notificaciones
    usuario.verificar_notificaciones()
