# TODO: Agrega el código de las clases del modelo aquí. Borra este comentario al terminar.
import datetime

class Note:

    def __init__(self, high: str, medium: str, low: str):
        self.high = "HIGH"
        self.medium = "MEDIUM"
        self.low = "LOW"

    def __init__(self, code: int, title: str, text: str, importance: str):

        self.code: int = code  #codigo unico de la nota
        self.title: str = title  #titulo de la nota
        self.text: str = text  #contenido de la nota
        self.importance: str = importance  #nivel de importancia
        self.creation_date: datetime.datetime = datetime.datetime.now()  # fecha de creación
        self.tags: list[str] = []

    def add_tag(self, tag: str) -> None:
        #Agrega una etiqueta a la nota si no está repetida.
        if tag not in self.tags:
            self.tags.append(tag)

    def __str__(self) -> str:
        #Devuelve un texto representando la nota
        return f"Fecha: {self.creation_date}\n{self.title}: {self.text}"

class Notebook:

    def __init__(self):
        #Inicializa un cuaderno vacío
        self.notes: list[Note] = []

    def add_note(self, title: str, text: str, importance: str) -> int:
        #Agrega una nueva nota y devuelve su código único
        new_code: int = len(self.notes) + 1
        note: Note = Note(new_code, title, text, importance)
        self.notes.append(note)
        return new_code

    def delete_note(self, code: int) -> bool:
        #Elimina una nota por su código
        for note in self.notes:
            if note.code == code:
                self.notes.remove(note)
                return True
        return False

    def list_notes(self) -> None:
        #Muestra todas las notas en el cuaderno
        if not self.notes:
            print("No hay notas registradas.")
        else:
            for note in self.notes:
                print(f"{note.code} - {note.title}: {note.text}")

    def list_important_notes(self) -> None:
        #Muestra solo las notas importantes (HIGH o MEDIUM)
        for note in self.notes:
            if note.importance in [Note.HIGH, Note.MEDIUM]:
                print(f"{note.code} - {note.title}: {note.text}")

    def notes_by_tag(self, tag: str) -> None:
        #Muestra todas las notas que tienen una etiqueta específica
        found: bool = False
        for note in self.notes:
            if tag in note.tags:
                print(f"{note.code} - {note.title}: {note.text}")
                found = True
        if not found:
            print("No hay notas con esa etiqueta.")

    def tag_with_most_notes(self) -> None:
        #Encuentra la etiqueta más usada en todas las notas.
        tag_count: dict[str, int] = {}

        for note in self.notes:
            for tag in note.tags:
                tag_count[tag] = tag_count.get(tag, 0) + 1

        if not tag_count:
            print("No hay etiquetas registradas.")
            return

        most_used_tag: str = max(tag_count, key=tag_count.get)
        print(f"La etiqueta más usada es: {most_used_tag}")

