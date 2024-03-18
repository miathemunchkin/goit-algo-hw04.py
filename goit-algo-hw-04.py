goit-slgo-hw-04.py

Завдання 1
def total_salary(path):
    total_salary = 0
    num_developers = 0

    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                # Розділення рядка на ім'я та заробітну плату за комою
                name, salary = line.strip().split(',')
                # Підрахунок загальної заробітної плати
                total_salary += int(salary)
                num_developers += 1

        # Обчислення середньої заробітної плати
        if num_developers > 0:
            average_salary = total_salary / num_developers
        else:
            average_salary = 0

        return total_salary, average_salary

    except FileNotFoundError:
        print("Файл не знайдено.")
        return None, None
    except Exception as e:
        print("Виникла помилка при обробці файлу:", e)
        return None, None

# Приклад використання функції
total, average = total_salary("path/to/salary_file.txt")
if total is not None and average is not None:
    print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")


Завдання 2
def get_cats_info(path):
    cats_info = []

    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                # Розділення рядка на ідентифікатор, ім'я та вік кота за комою
                cat_id, name, age = line.strip().split(',')
                # Створення словника з інформацією про кота та додавання його до списку
                cat_info = {"id": cat_id, "name": name, "age": age}
                cats_info.append(cat_info)

    except FileNotFoundError:
        print("Файл не знайдено.")
    except Exception as e:
        print("Виникла помилка при обробці файлу:", e)

    return cats_info

# Приклад використання функції
cats_info = get_cats_info("path/to/cats_file.txt")
print(cats_info)


Завдання 4
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, args

def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

def change_contact(args, contacts):
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return "Contact updated."
    else:
        return "Contact not found."

def show_contacts(contacts):
    if contacts:
        for name, phone in contacts.items():
            print(f"Name: {name}, Phone: {phone}")
    else:
        print("No contacts found.")

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "show":
            show_contacts(contacts)
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()