# Домашнее задание: Классы и инициализация
#
# ЗАДАНИЕ 1: Класс Book (Книга)


class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def get_info(self):
        return f"'{self.title}' автор {self.author}, {self.pages} стр."

    def is_long(self):
        return self.pages > 300


book1 = Book("Корешка", "Кожемятько", 290)
book2 = Book("Что было дальше", "Володин", 310)
book3 = Book("Успех", "Горбушенко", 50)
print(book1.get_info(), book1.is_long())
print(book2.get_info(), book2.is_long())
print(book3.get_info(), book3.is_long())


class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance - amount < 0:
            print("Недостаточно средств")
            return False
        else:
            self.balance -= amount
            return True

    def get_balance(self):
        return self.balance


new_user_1 = BankAccount("Туруханов Э.Ю.")
new_user_1.deposit(1000)
new_user_1.withdraw(250)
new_user_1.withdraw(1100)
print(new_user_1.get_balance())
