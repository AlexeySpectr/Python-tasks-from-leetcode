import pickle
import os

class AddressBook:
    FILE_NAME = "contacts.pkl"

    def __init__(self, name, age, number, address):
        self.name = name
        self.age = age
        self.number = number
        self.address = address

    def printf(self, idx):
        print(
            f"[{idx}] Имя: {self.name}, Возраст: {self.age}, Телефон: {self.number}, Адрес: {self.address}"
        )

    @classmethod
    def load_contacts(cls):
        """Загрузка контактов из файла"""
        if os.path.exists(cls.FILE_NAME):
            with open(cls.FILE_NAME, "rb") as f:
                return pickle.load(f)
        return []

    @classmethod
    def save_contacts(cls, contacts):
        """Сохранение контактов в файл"""
        with open(cls.FILE_NAME, "wb") as f:
            pickle.dump(contacts, f)

    # ================= CRUD ==================
    @classmethod
    def add_contact(cls):
        name = input("Введите имя: ")
        age = input("Введите возраст: ")
        number = input("Введите номер телефона: ")
        address = input("Введите адрес: ")

        contacts = cls.load_contacts()
        new_contact = AddressBook(name, age, number, address)
        contacts.append(new_contact)
        cls.save_contacts(contacts)
        print(f"Контакт {name} добавлен")

    @classmethod
    def view_contacts(cls):
        contacts = cls.load_contacts()
        if not contacts:
            print("Адресная книга пуста")
            return
        for i, c in enumerate(contacts, start=1):
            c.printf(i)

    @classmethod
    def search_contact(cls):
        name = input("Введите имя для поиска: ")
        contacts = cls.load_contacts()
        for c in contacts:
            if c.name.lower() == name.lower():
                print("Контакт найден:")
                c.printf("?")
                return
        print("Контакт не найден")

    @classmethod
    def delete_contact(cls):
        name = input("Введите имя для удаления: ")
        contacts = cls.load_contacts()
        for c in contacts:
            if c.name.lower() == name.lower():
                contacts.remove(c)
                cls.save_contacts(contacts)
                print(f"Контакт {name} удалён")
                return
        print(f"Контакт {name} не найден")

    @classmethod
    def edit_contact(cls):
        name = input("Введите имя контакта для изменения: ")
        contacts = cls.load_contacts()
        for c in contacts:
            if c.name.lower() == name.lower():
                print("Оставьте поле пустым, если не хотите менять")
                new_name = input("Новое имя: ")
                new_age = input("Новый возраст: ")
                new_number = input("Новый телефон: ")
                new_address = input("Новый адрес: ")

                if new_name:
                    c.name = new_name
                if new_age:
                    c.age = new_age
                if new_number:
                    c.number = new_number
                if new_address:
                    c.address = new_address

                cls.save_contacts(contacts)
                print(f"Контакт {name} обновлён")
                return
        print(f"Контакт {name} не найден")


# ================= Консольное меню =================
def main():
    while True:
        print("\n===== АДРЕСНАЯ КНИГА =====")
        print("1. Добавить контакт")
        print("2. Показать все контакты")
        print("3. Найти контакт")
        print("4. Изменить контакт")
        print("5. Удалить контакт")
        print("0. Выход")

        choice = input("Выберите действие: ")

        if choice == "1":
            AddressBook.add_contact()
        elif choice == "2":
            AddressBook.view_contacts()
        elif choice == "3":
            AddressBook.search_contact()
        elif choice == "4":
            AddressBook.edit_contact()
        elif choice == "5":
            AddressBook.delete_contact()
        elif choice == "0":
            print("Выход...")
            break
        else:
            print("Неверный выбор, попробуйте снова")

if __name__ == "__main__":
    main()