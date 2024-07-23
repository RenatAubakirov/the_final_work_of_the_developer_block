from datetime import date

class PackAnimal:
    """Класс для вьючных животных."""
    def __init__(self, name: str, birth_date: date, abilities: str, load_capacity: float):
        self.name = name  # Имя животного
        self.birth_date = birth_date  # Дата рождения животного
        self.abilities = abilities  # Способности (отличительная черта)
        self.load_capacity = load_capacity  # Грузоподъемность

    def __str__(self):
        return f"{self.__class__.__name__}: {self.name}, {self.birth_date}, {self.abilities}, {self.load_capacity}kg"
