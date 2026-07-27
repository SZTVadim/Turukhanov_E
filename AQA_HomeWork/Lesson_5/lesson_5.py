# ЗАДАНИЕ 1: Добавление элементов в список
fruits = ["яблоко"]
fruits.append("банан")
fruits.extend(["апельсин", "груша"])
fruits.insert(1, "виноград")

# ЗАДАНИЕ 2: Удаление элементов из списка
fruits = ["яблоко", "банан", "апельсин", "банан"]
fruits.remove("банан")
last_fruit = fruits.pop()

# ЗАДАНИЕ 3: Поиск элементов в списке
fruits = ["яблоко", "банан", "апельсин", "банан"]
print(fruits.index("банан"))
print(fruits.count("банан"))

# ЗАДАНИЕ 4: Сортировка и реверс списка
numbers = [3, 1, 4, 1, 5, 9, 2]
numbers.sort()
numbers.reverse()
print(numbers)
