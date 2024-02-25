from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    def __init__(self, value):
        if not self.validate_name(value):
            raise ValueError("Invalid name")
        super().__init__(value)

    def validate_name(self, value):
        return len(value) > 1

class Phone(Field):
    def __init__(self, value):
        if not self.validate_phone(value):
            raise ValueError("Invalid phone number")
        super().__init__(value)

    def validate_phone(self, value):
        return len(str(value)) == 10 and str(value).isdigit()

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def remove_phone(self, phone):
        self.phones = [p for p in self.phones if str(p) != str(phone)]

    def edit_phone(self, old_phone, new_phone):
        for i, phone in enumerate(self.phones):
            if str(phone) == str(old_phone):
                self.phones[i] = Phone(new_phone)
                break

    def find_phone(self, phone):
        for p in self.phones:
            if str(p) == str(phone):
                return p
        return None

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(str(p) for p in self.phones)}"

class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        return self.data.get(name)

    def delete(self, name):
        del self.data[name]
    

if __name__ == "__main__":
    # Створення нової адресної книги
    book = AddressBook()

    # Створення запису для John
    john_record = Record("John")
    john_record.add_phone("1234567890")
    john_record.add_phone("5555555555")

    # Додавання запису John до адресної книги
    book.add_record(john_record)

    # Створення та додавання нового запису для Jane
    jane_record = Record("Jane")
    jane_record.add_phone("9876543210")
    book.add_record(jane_record)
    # Виведення всіх записів у книзі
    for name, record in book.data.items():
        print(record)
    print("---")
    # Знаходження та редагування телефону для John
    john = book.find("John")
    john.edit_phone("1234567890", "1112223333")
    print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555
    # Пошук конкретного телефону у записі John
    found_phone = john.find_phone("5555555555")
    print(f"{john.name}: {found_phone}")  # Виведення: 5555555555

    # Видалення запису Jane
    book.delete("Jane")

