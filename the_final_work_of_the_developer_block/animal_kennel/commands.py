from datetime import datetime
from pack_animals.horse import Horse
from pack_animals.camel import Camel
from pack_animals.donkey import Donkey
from pets.dog import Dog
from pets.cat import Cat
from pets.hamster import Hamster

def add_animal(registry):
    """Добавление нового животного в реестр."""
    # Запрашиваем у пользователя, к какому классу относится животное (вьючные/домашние)
    class_type = input("Введите класс (вьючные/домашние): ").strip().lower()
    animal = None  # Определяем переменную animal для хранения создаваемого животного

    # Обработка ввода для вьючных животных
    if class_type == 'вьючные':
        # Запрашиваем дополнительные данные для создания вьючного животного
        sub_class = input("Введите подкласс (Лошадь/Верблюд/Осел): ").strip().lower()
        name = input("Введите имя: ").strip()
        birth_date_str = input("Введите дату рождения (ГГГГ-ММ-ДД): ").strip()
        birth_date = validate_date(birth_date_str)  # Проверяем корректность даты
        if birth_date is None:
            print("Неправильный формат даты. Попробуйте снова.")
            return
        abilities = input("Введите способности: ").strip()
        load_capacity_str = input("Введите грузоподъемность (только число, например 10): ").strip()
        try:
            load_capacity = float(load_capacity_str.replace('кг', '').strip())
        except ValueError:
            print("Неправильный формат грузоподъемности. Попробуйте снова.")
            return
        
        # Создаем экземпляр соответствующего подкласса вьючного животного
        if sub_class == 'лошадь':
            animal = Horse(name, birth_date, abilities, load_capacity)
        elif sub_class == 'верблюд':
            animal = Camel(name, birth_date, abilities, load_capacity)
        elif sub_class == 'осел':
            animal = Donkey(name, birth_date, abilities, load_capacity)

    # Обработка ввода для домашних животных
    elif class_type == 'домашние':
        # Запрашиваем дополнительные данные для создания домашнего животного
        sub_class = input("Введите подкласс (Собака/Кошка/Хомяк): ").strip().lower()
        name = input("Введите имя: ").strip()
        birth_date_str = input("Введите дату рождения (ГГГГ-ММ-ДД): ").strip()
        birth_date = validate_date(birth_date_str)  # Проверяем корректность даты
        if birth_date is None:
            print("Неправильный формат даты. Попробуйте снова.")
            return
        abilities = input("Введите способности: ").strip()
        
        # Создаем экземпляр соответствующего подкласса домашнего животного
        if sub_class == 'собака':
            animal = Dog(name, birth_date, abilities)
        elif sub_class == 'кошка':
            animal = Cat(name, birth_date, abilities)
        elif sub_class == 'хомяк':
            animal = Hamster(name, birth_date, abilities)
    
    # Добавляем животное в реестр, если оно было создано
    if animal:
        registry.add_animal(animal)
    else:
        print("Неправильный подкласс или класс. Попробуйте снова.")

def validate_date(date_str):
    """Проверка и преобразование строки даты в объект datetime."""
    try:
        return datetime.strptime(date_str, "%Y-%m-%d")  # Преобразуем строку в объект datetime
    except ValueError:
        return None  # Возвращаем None, если формат даты неверный

def teach_command(registry):
    """Обучение животного новой команде."""
    name = input("Введите имя животного: ").strip()
    command = input("Введите команду для обучения: ").strip()
    if registry.teach_command(name, command):  # Пытаемся обучить команду
        print(f"{name} выучил команду: {command}")
    else:
        print(f"Животное с именем {name} не найдено.")

def list_animals_by_birth_date(registry):
    """Вывод списка животных, отсортированного по дате рождения."""
    animals = registry.list_animals_by_birth_date()  # Получаем отсортированный список животных
    for animal in animals:
        print(f"{animal.name}, {animal.birth_date.strftime('%Y-%m-%d')}, {animal.abilities}")

def show_commands(registry):
    """Показ команд, которые знает животное."""
    name = input("Введите имя животного: ").strip()
    commands = registry.get_commands(name)  # Получаем список команд для указанного животного
    if commands is not None:
        print(f"{name} знает команды: {', '.join(commands)}")
    else:
        print(f"Животное с именем {name} не найдено или не является домашним.")

def show_total_animals(registry):
    """Вывод общего количества созданных животных """
    print(f"Общее количество животных: {registry.total_animals}")



