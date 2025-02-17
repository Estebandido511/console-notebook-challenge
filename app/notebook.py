# TODO: Agrega el código de las clases del modelo aquí. Borra este comentario al terminar.

class Note:

    def __init__(self, HIGH: str, MEDIUM: str, LOW: str):
        self.HIGH = "HIGH"
        self.MEDIUM = "MEDIUM"
        self.LOW = "LOW"

    def __init__(self, code: int, title: str, text: str, importance: str):

        self.code: int = code  #codigo unico de la nota
        self.title: str = title  #titulo de la nota
        self.text: str = text  #contenido de la nota
        self.importance: str = importance  #nivel de importancia
        self.creation_date: datetime.datetime = datetime.datetime.now()  # fecha de creación
        self.tags: list[str] = []

    def add_tag(self, tag: str) -> None:
        """Agrega una etiqueta a la nota si no está repetida."""
        if tag not in self.tags:
            self.tags.append(tag)

    def __str__(self) -> str:
        """Devuelve un texto representando la nota."""
        return f"Fecha: {self.creation_date}\n{self.title}: {self.text}"


