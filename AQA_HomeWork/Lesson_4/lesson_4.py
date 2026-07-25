# ЗАДАНИЕ 1: Работа с типами данных
text = "Привет"
integer_number = 42
float_number = 3.14
numbers = [1, 2, 3]
print("\tЗАДАНИЕ 1: Работа с типами данных")
print("Тип данных строки:", type(text))
print("Тип данных целого числа:", type(integer_number))
print("Тип данных числа с точкой:", type(float_number))
print("Тип данных списка:", type(numbers))

# ЗАДАНИЕ 2: Преобразование регистра строк
text_2 = "python PROGRAMMING"
print("\tЗАДАНИЕ 2: Преобразование регистра строк")
print(text_2.lower())
print(text_2.upper())
print(text_2.capitalize())
print(text_2.title())

# ЗАДАНИЕ 3: Удаление пробелов
text_3 = "  Hello World  "
print("\tЗАДАНИЕ 3: Удаление пробелов")
print(text_3.strip())
print(text_3.lstrip())
print(text_3.rstrip())

# ЗАДАНИЕ 4: Разделение и объединение строк
text_4 = "яблоко,банан,апельсин,груша"
new_text_4 = text_4.split(",")
print("\tЗАДАНИЕ 4: Разделение и объединение строк")
print(new_text_4)
new2_text_4 = " | ".join(new_text_4)
print(new2_text_4)

# ЗАДАНИЕ 5: Замена подстрок
print("\tЗАДАНИЕ 5: Замена подстрок")
text_5 = "Я изучаю Python. Python - это круто!"
new_text_5 = text_5.replace("Python", "Java")
print(new_text_5)

# ЗАДАНИЕ 6: Поиск и подсчет
print("\tЗАДАНИЕ 6: Поиск и подсчет")
text_6 = "Python программирование на Python"
print(text_6.find("Python"))
print(text_6.count("Python"))
print(text_6.find("Java"))

# ЗАДАНИЕ 7: Проверка типа символов
print("\tЗАДАНИЕ 7: Проверка типа символов")
text_7 = "Hello123"
text_8 = "12345"
text_9 = "Hello"
text_10 = "   "
print(text_7.isalnum())
print(text_9.isalpha())
print(text_8.isdigit())
print(text_10.isspace())

# ЗАДАНИЕ 8: Срезы строк
print("\tЗАДАНИЕ 8: Срезы строк")
text_11 = "Python very good"
print(text_11[:3])
print(text_11[-3:])
print(text_11[::2])
print("4:", text_11[::-1])

# ЗАДАНИЕ 9: Экранирование символов
print("\tЗАДАНИЕ 9: Экранирование символов")
print("Он сказал: \"Привет\"")
print("Первая строка\nВторая строка")
