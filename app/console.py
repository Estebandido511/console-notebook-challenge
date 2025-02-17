# TODO: Agrega el código de las clases de la interfaz de usuario aquí. Borra este comentario al terminar.

class Console:
    def __init__(self):
        #Inicializa la interfaz con un cuaderno vacío.
        self.notebook: Notebook = Notebook()

    def show_menu(self) -> None:
        #Muestra el menú principal y permite elegir opciones.
        while True:
            print("1. Agregar nota")
            print("2. Listar notas")
            print("3. Agregar etiqueta a nota")
            print("4. Listar notas importantes")
            print("5. Eliminar nota")
            print("6. Mostrar notas por etiqueta")
            print("7. Mostrar etiqueta con más notas")
            print("8. Salir")
            option: str = input("Seleccione una opción: ")

            if option == "1":
                self.add_note()
            elif option == "2":
                self.list_notes()
            elif option == "3":
                self.add_tag_to_note()
            elif option == "4":
                self.list_important_notes()
            elif option == "5":
                self.delete_note()
            elif option == "6":
                self.show_notes_by_tag()
            elif option == "7":
                self.show_most_used_tag()
            elif option == "8":
                print("Salir")
                break
            else:
                print("Opción inválida. Intente nuevamente.")







