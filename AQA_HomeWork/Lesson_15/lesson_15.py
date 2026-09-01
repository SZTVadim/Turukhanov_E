# Домашнее задание: Декораторы, @property и @classmethod

# ЗАДАНИЕ 1: Декоратор

def log_execution(func):
    def wrapper(*args, **kwargs):
        print("Функция запущена")
        result = func(*args, **kwargs)
        print("Функция завершена")
        return result

    return wrapper


@log_execution
def calculate_sum(a, b):
    return a + b


print(calculate_sum(5, 3))


# ЗАДАНИЕ 2: @property и @classmethod

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.__price = 0

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        if price < 0:
            print("Ошибка: цена не может быть отрицательной!")
        elif price > 10000:
            print("Ошибка: максимальная цена 10000 рублей!")
        else:
            self.__price = price

    @classmethod
    def create_from_string(cls, string):
        title, author = string.split("|")
        return cls(title, author)

    def get_info(self):
        return (
            f"Книга '{self.title}' автор {self.author}, "
            f"цена {self.price} руб."
        )


book1 = Book("1984", "Оруэлл")

book2 = Book.create_from_string("Мастер и Маргарита|Булгаков")

book1.price = 500
book2.price = 750
book1.price = -100
book1.price = 15000

print(book1.get_info())
print(book2.get_info())
