# biblioteca.py
# Clase Biblioteca y excepciones del sistema

from modelos import Libro, Miembro


# ── Excepciones ──

class LibroNoEncontradoError(Exception):
    """Se muestra cuando el ISBN buscado no existe en la biblioteca."""
    pass


class MiembroNoEncontradoError(Exception):
    """Se muestra cuando el DNI buscado no corresponde a ningún miembro."""
    pass


class LibroNoDisponibleError(Exception):
    """Se muestra cuando se intenta prestar un libro que ya está prestado."""
    pass


class LibroNoPrestadoError(Exception):
    """Se muestra cuando se intenta devolver un libro que el miembro no tiene."""
    pass


class ISBNDuplicadoError(Exception):
    """Se muestra cuando se intenta agregar un libro con ISBN ya existente."""
    pass


class DNIDuplicadoError(Exception):
    """Se muestra cuando se intenta agregar un miembro con DNI ya existente."""
    pass


# ── Clase principal ──

class Biblioteca:
    def __init__(self):
        self.libros = []      # Lista de objetos Libro
        self.miembros = []    # Lista de objetos Miembro

    # ── Búsquedas internas ──

    def _buscar_libro(self, isbn):
        """Devuelve el Libro con ese ISBN o muestra LibroNoEncontradoError."""
        for libro in self.libros:
            if libro.isbn == isbn:
                return libro
        raise LibroNoEncontradoError(f"No existe ningún libro con ISBN '{isbn}'.")

    def _buscar_miembro(self, dni):
        """Devuelve el Miembro con ese DNI o muestra MiembroNoEncontradoError."""
        for miembro in self.miembros:
            if miembro.dni == dni:
                return miembro
        raise MiembroNoEncontradoError(f"No existe ningún miembro con DNI '{dni}'.")

    # ── Alta de los libros y miembros ──

    def agregar_libro(self, libro):
        """Agrega un libro; Muestra ISBNDuplicadoError si el ISBN ya existe."""
        for l in self.libros:
            if l.isbn == libro.isbn:
                raise ISBNDuplicadoError(f"Ya existe un libro con ISBN '{libro.isbn}'.")
        self.libros.append(libro)

    def agregar_miembro(self, miembro):
        """Agrega un miembro; Muestra DNIDuplicadoError si el DNI ya existe."""
        for m in self.miembros:
            if m.dni == miembro.dni:
                raise DNIDuplicadoError(f"Ya existe un miembro con DNI '{miembro.dni}'.")
        self.miembros.append(miembro)

    # ── Préstamo y devolución ──

    def prestar_libro(self, isbn, dni):
        """
        Presta el libro (isbn) al miembro (dni).
        Muestra una excepción si el libro no existe, el miembro no existe
        o el libro no está disponible.
        """
        libro = self._buscar_libro(isbn)
        miembro = self._buscar_miembro(dni)

        if not libro.esta_disponible():
            raise LibroNoDisponibleError(
                f"El libro '{libro.titulo}' no está disponible "
                f"(lo tiene DNI: {libro.prestado_a})."
            )

        libro.prestar(dni)
        miembro.tomar_libro(libro)
        print(f"  Libro '{libro.titulo}' prestado a {miembro.nombre} correctamente.")

    def devolver_libro(self, isbn, dni):
        """
        Registra la devolución del libro (isbn) por parte del miembro (dni).
        Muestra una excepción si el libro o el miembro no existen,
        o si el miembro no tenía ese libro.
        """
        libro = self._buscar_libro(isbn)
        miembro = self._buscar_miembro(dni)

        if libro not in miembro.libros_prestados:
            raise LibroNoPrestadoError(
                f"{miembro.nombre} no tiene prestado el libro '{libro.titulo}'."
            )

        libro.devolver()
        miembro.devolver_libro(libro)
        print(f"Libro '{libro.titulo}' devuelto por {miembro.nombre} correctamente.")

    # ── Consultas ──

    def mostrar_libros(self):
        if not self.libros:
            print("No hay libros registrados.")
            return
        print("  ── Libros ──")
        for libro in self.libros:
            print(f"{libro}")

    def mostrar_miembros(self):
        if not self.miembros:
            print("No hay miembros registrados.")
            return
        print("  ── Miembros ──")
        for miembro in self.miembros:
            print(f"{miembro}")
