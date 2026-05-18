# main.py
# Entrada del sistema de gestión de biblioteca
# Visual marca como error el import de bilioteca pero el cógidog se ejecuta sin problemas.
from modelos import Libro, Miembro
from biblioteca import (
    Biblioteca,
    LibroNoEncontradoError,
    MiembroNoEncontradoError,
    LibroNoDisponibleError,
    LibroNoPrestadoError,
    ISBNDuplicadoError,
    DNIDuplicadoError,
)


def mostrar_menu():
    print("\n" + "=" * 42)
    print("   SISTEMA DE GESTIÓN DE BIBLIOTECA")
    print("=" * 42)
    print("  1. Agregar libro")
    print("  2. Agregar miembro")
    print("  3. Mostrar todos los libros")
    print("  4. Mostrar todos los miembros")
    print("  5. Prestar libro")
    print("  6. Devolver libro")
    print("  0. Salir")
    print("=" * 42)


def main():
    biblioteca = Biblioteca()

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ").strip()

        # ── 1. Agregar libro ──
        if opcion == "1":
            titulo = input("Título: ").strip()
            autor  = input("Autor: ").strip()
            isbn   = input("ISBN: ").strip()

            if not titulo or not autor or not isbn:
                print("  Error: todos los campos son obligatorios.")
                continue

            try:
                libro = Libro(titulo, autor, isbn)
                biblioteca.agregar_libro(libro)
                print(f"Libro '{titulo}' agregado exitosamente.")
            except ISBNDuplicadoError as e:
                print(f"Error: {e}")

        # ── 2. Agregar miembro ──
        elif opcion == "2":
            nombre = input("Nombre: ").strip()
            dni    = input("DNI: ").strip()

            if not nombre or not dni:
                print("Error: todos los campos son obligatorios.")
                continue

            try:
                miembro = Miembro(nombre, dni)
                biblioteca.agregar_miembro(miembro)
                print(f"Miembro '{nombre}' agregado exitosamente.")
            except DNIDuplicadoError as e:
                print(f"Error: {e}")

        # ── 3. Mostrar libros ──
        elif opcion == "3":
            biblioteca.mostrar_libros()

        # ── 4. Mostrar miembros ──
        elif opcion == "4":
            biblioteca.mostrar_miembros()

        # ── 5. Prestar libro ──
        elif opcion == "5":
            isbn = input("ISBN del libro a prestar: ").strip()
            dni  = input("DNI del miembro: ").strip()

            try:
                biblioteca.prestar_libro(isbn, dni)
            except (LibroNoEncontradoError, MiembroNoEncontradoError,
                    LibroNoDisponibleError) as e:
                print(f"Error: {e}")

        # ── 6. Devolver libro ──
        elif opcion == "6":
            isbn = input("ISBN del libro a devolver: ").strip()
            dni  = input("DNI del miembro: ").strip()

            try:
                biblioteca.devolver_libro(isbn, dni)
            except (LibroNoEncontradoError, MiembroNoEncontradoError,
                    LibroNoPrestadoError) as e:
                print(f"Error: {e}")

        # ── 0. Salir ──
        elif opcion == "0":
            print("¡Nos vemos!")
            break

        else:
            print("Inválido. Ingrese una opcción del 0 al 6.")


if __name__ == "__main__":
    main()
