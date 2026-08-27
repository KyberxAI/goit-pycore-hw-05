# Консольний бот помічник


# декоратор input_error для обробки помилок
def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)

        except ValueError:
            return "Give me name and phone please."

        except IndexError:
            return "Enter user name."

        except KeyError:
            return "Contact not found."

    return inner


# парсинг вводу користувача на команду і список аргументів
def parse_input(user_input):

    if not user_input.strip():
        return "", []

    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


# функція додавання нового контакта
@input_error
def add_contact(args, contacts):
    name, phone = args
    for contact_name in contacts.keys():
        if contact_name.lower() == name.lower():
            return f"Contact {name} already exists."
    contacts[name] = phone
    return f"Contact {name} added."


# функція зміни номера телефону вказаного контакта
@input_error
def change_contact(args, contacts):
    name, phone = args
    for contact_name in contacts.keys():
        if contact_name.lower() == name.lower():
            contacts[contact_name] = phone
            return f"Contact {contact_name} updated."
    else:
        return f"Contact {name} does not exist."


# функція виводу номера телефона по заданому імені
@input_error
def show_phone(args, contacts):
    name = args[0]
    for contact_name in contacts.keys():
        if contact_name.lower() == name.lower():
            phone = contacts[contact_name]
            return f"{phone}"
    else:
        return f"Contact {name} does not exist."


# функція виводу всіх номерів телефонів
@input_error
def show_all(contacts):
    contact_list = ""
    for key, value in contacts.items():
        contact_list = contact_list + f"Name: {key} Phone: {value}\n"
    return contact_list


# головна функція
def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        # обробка заданих команд
        if command in ["close", "exit"]:
            print("Good bye!")
            break

        elif command == "hello":
            print("How can I help you?")

        # Довідка по командам бота для користувача
        elif command == "help":
            print(
                "Список і формат команд: \n"
                "hello \n"
                "help \n"
                "add username phone \n"
                "change username phone \n"
                "phone username \n"
                "all \n"
                "close \n"
                "exit \n"
            )

        # Команда "add [ім'я] [номер телефону]"
        elif command == "add":
            # Виконати add_contact() і вивести підтвердження
            print(add_contact(args, contacts))

        # Команда "change [ім'я] [новий номер телефону]"
        elif command == "change":
            # Виконати change_contact()) і вивести підтвердження
            print(change_contact(args, contacts))

        # Команда "phone [ім'я]"
        elif command == "phone":
            # Виконати show_phone() і вивести підтвердження
            print(show_phone(args, contacts))

        # Команда "all"
        elif command == "all":
            # Виконати show_all() і вивести підтвердження
            print(show_all(contacts))

        else: # неправильно введені команди
            print("Invalid command.")


if __name__ == "__main__":
    main()
