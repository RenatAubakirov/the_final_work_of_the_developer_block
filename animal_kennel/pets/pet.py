from datetime import date

class Pet:
    """Класс для домашних животных."""
    def __init__(self, name: str, birth_date: date, abilities: str, commands=None):
        if commands is None:
            commands = []
        self.name = name  # Имя животного
        self.birth_date = birth_date  # Дата рождения животного
        self.abilities = abilities  # Способности (отличительная черта)
        self.commands = commands  # Список команд, которые знает животное

    def __str__(self):
        return f"{self.__class__.__name__}: {self.name}, {self.birth_date}, {self.abilities}, Commands: {', '.join(self.commands)}"

    def learn_command(self, command: str):
        """Метод для обучения животного новой команде."""
        if command not in self.commands:
            self.commands.append(command)
