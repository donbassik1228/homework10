from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    pass

class Phone(Field):


    @staticmethod
    def is_valid(phone_number):
        return len(phone_number) == 10 and phone_number.isdigit()
    
    def __init__(self, value):
        # Валідація формату номера телефону (10 цифр)
        if not isinstance(value, str) or not value.isdigit() or len(value) != 10:
            raise ValueError("Invalid phone number format")
        super().__init__(value)

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone_number):
        phone = Phone(phone_number)
        self.phones.append(phone)

    def remove_phone(self, phone_number):
        self.phones = [phone for phone in self.phones if phone.value != phone_number]
        
    def find_phone(self, phone_number):
        for phone in self.phones:
            if phone.value == phone_number:
                return phone
        return None

    def edit_phone(self, old_phone_number, new_phone_number):
        # Перевірка валідності нового номера телефону
        if not Phone.is_valid(new_phone_number):
            raise ValueError("Invalid phone number")

        found = False
        for phone in self.phones:
            if phone.value == old_phone_number:
                # Перевірка валідності старого номера телефону
                if not Phone.is_valid(old_phone_number):
                    raise ValueError("Invalid old phone number")

                phone.value = new_phone_number
                found = True
                break
        if found:
            return
        raise ValueError("Phone number not found")


    def __str__(self):
        phones_str = '; '.join(str(phone) for phone in self.phones)
        return f"Contact name: {self.name.value}, phones: {phones_str}"

class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        return self.data.get(name)

    def delete(self, name):
        if name in self.data:
            del self.data[name]




book = AddressBook()


john_record = Record("John")
john_record.add_phone("1234567890")
john_record.add_phone("5555555555")


book.add_record(john_record)


jane_record = Record("Jane")
jane_record.add_phone("9876543210")
book.add_record(jane_record)


for name, record in book.data.items():
    print(record)


john = book.find("John")
john.edit_phone("1234567890", "1112223333")

print(john)  
try:
    found_phone = john.find_phone("5555555555")
    print(f"{john.name.value}: {found_phone}") 
except ValueError as e:
    print(e)


try:
    john.edit_phone("1111111111", "9999999999")
except ValueError as e:
    print(e)

book.delete("Jane")
