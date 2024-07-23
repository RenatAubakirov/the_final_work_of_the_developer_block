import json
from datetime import datetime
from pack_animals.horse import Horse
from pack_animals.camel import Camel
from pack_animals.donkey import Donkey
from pets.dog import Dog
from pets.cat import Cat
from pets.hamster import Hamster

class AnimalRegistry:
    def __init__(self, filename='registry.json'):
        # Инициализация класса AnimalRegistry
        # Задает начальные значения и загружает данные из файла
        self.animals = []
        self.total_animals = 0
        self.filename = filename
        self.load_from_file()

    def add_animal(self, animal):
        # Добавляет новое животное в реестр и сохраняет изменения в файл
        self.animals.append(animal)
        self.total_animals += 1
        self.save_to_file()

    def teach_command(self, name, command):
        # Обучает животное новой команде, если это возможно
        for animal in self.animals:
            if animal.name == name:
                if isinstance(animal, (Dog, Cat, Hamster)):
                    animal.learn_command(command)
                    self.save_to_file()
                    return True
        return False

    def list_animals_by_birth_date(self):
        # Возвращает список животных, отсортированный по дате рождения
        return sorted(self.animals, key=lambda animal: animal.birth_date)

    def get_commands(self, name):
        # Получает список команд для животного по имени
        for animal in self.animals:
            if animal.name == name:
                if isinstance(animal, (Dog, Cat, Hamster)):
                    return animal.commands
        return None

    def save_to_file(self):
        # Сохраняет данные о животных в файл в формате JSON
        with open(self.filename, 'w', encoding='utf-8') as file:
            data = {
                'total_animals': self.total_animals,
                'animals': []
            }
            for animal in self.animals:
                if isinstance(animal, Horse):
                    animal_data = {
                        'class': 'PackAnimal',
                        'subclass': 'Horse',
                        'name': animal.name,
                        'birth_date': animal.birth_date.strftime('%Y-%m-%d'),
                        'abilities': animal.abilities,
                        'load_capacity': animal.load_capacity
                    }
                elif isinstance(animal, Camel):
                    animal_data = {
                        'class': 'PackAnimal',
                        'subclass': 'Camel',
                        'name': animal.name,
                        'birth_date': animal.birth_date.strftime('%Y-%m-%d'),
                        'abilities': animal.abilities,
                        'load_capacity': animal.load_capacity
                    }
                elif isinstance(animal, Donkey):
                    animal_data = {
                        'class': 'PackAnimal',
                        'subclass': 'Donkey',
                        'name': animal.name,
                        'birth_date': animal.birth_date.strftime('%Y-%m-%d'),
                        'abilities': animal.abilities,
                        'load_capacity': animal.load_capacity
                    }
                elif isinstance(animal, Dog):
                    animal_data = {
                        'class': 'Pet',
                        'subclass': 'Dog',
                        'name': animal.name,
                        'birth_date': animal.birth_date.strftime('%Y-%m-%d'),
                        'abilities': animal.abilities,
                        'commands': animal.commands
                    }
                elif isinstance(animal, Cat):
                    animal_data = {
                        'class': 'Pet',
                        'subclass': 'Cat',
                        'name': animal.name,
                        'birth_date': animal.birth_date.strftime('%Y-%m-%d'),
                        'abilities': animal.abilities,
                        'commands': animal.commands
                    }
                elif isinstance(animal, Hamster):
                    animal_data = {
                        'class': 'Pet',
                        'subclass': 'Hamster',
                        'name': animal.name,
                        'birth_date': animal.birth_date.strftime('%Y-%m-%d'),
                        'abilities': animal.abilities,
                        'commands': animal.commands
                    }
                data['animals'].append(animal_data)
            json.dump(data, file, ensure_ascii=False, indent=4)

    def load_from_file(self):
        # Загружает данные из файла и восстанавливает состояние реестра
        try:
            with open(self.filename, 'r', encoding='utf-8') as file:
                data = json.load(file)
                if isinstance(data, list):
                    # Преобразование старого форматав новый
                    self.total_animals = len(data)
                    data = {
                        'total_animals': self.total_animals,
                        'animals': data
                    }
                else:
                    self.total_animals = data.get('total_animals', 0)

                for item in data['animals']:
                    if item['class'] == 'PackAnimal':
                        if item['subclass'] == 'Horse':
                            animal = Horse(item['name'], datetime.strptime(item['birth_date'], '%Y-%m-%d'), item['abilities'], item['load_capacity'])
                        elif item['subclass'] == 'Camel':
                            animal = Camel(item['name'], datetime.strptime(item['birth_date'], '%Y-%m-%d'), item['abilities'], item['load_capacity'])
                        elif item['subclass'] == 'Donkey':
                            animal = Donkey(item['name'], datetime.strptime(item['birth_date'], '%Y-%m-%d'), item['abilities'], item['load_capacity'])
                    elif item['class'] == 'Pet':
                        if item['subclass'] == 'Dog':
                            animal = Dog(item['name'], datetime.strptime(item['birth_date'], '%Y-%m-%d'), item['abilities'])
                            animal.commands = item.get('commands', [])
                        elif item['subclass'] == 'Cat':
                            animal = Cat(item['name'], datetime.strptime(item['birth_date'], '%Y-%m-%d'), item['abilities'])
                            animal.commands = item.get('commands', [])
                        elif item['subclass'] == 'Hamster':
                            animal = Hamster(item['name'], datetime.strptime(item['birth_date'], '%Y-%m-%d'), item['abilities'])
                            animal.commands = item.get('commands', [])
                    self.animals.append(animal)
        except FileNotFoundError:
            # Если файл не найден, продолжаем без загрузки
            pass

