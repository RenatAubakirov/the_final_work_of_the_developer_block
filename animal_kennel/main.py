from animal_registry import AnimalRegistry
import commands

def main():
    registry = AnimalRegistry()

    menu_options = {
        "1": commands.add_animal,
        "2": commands.teach_command,
        "3": commands.list_animals_by_birth_date,
        "4": commands.show_commands,
        "5": commands.show_total_animals,
        "0": exit
    }

    while True:
        print("\nМеню:")
        print("1. Добавить животное")
        print("2. Обучить животное новой команде")
        print("3. Показать животных по дате рождения")
        print("4. Показать команды, которые знает животное")
        print("5. Показать общее количество животных")
        print("0. Выход")

        choice = input("Выберите опцию: ").strip()

        if choice in menu_options:
            menu_options[choice](registry)
        else:
            print("Неправильный выбор. Пожалуйста, выберите снова.")

if __name__ == "__main__":
    main()


