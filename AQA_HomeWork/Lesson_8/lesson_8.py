# ЗАДАНИЕ 1: Список и list comprehension
temps = [18, 22, -3, 25, 19, -1, 21]
new_temps = [temp * 9/5 + 32 for temp in temps]
print(new_temps)

# ЗАДАНИЕ 2: Словарь и dict comprehension
users = {
    "ivan": "qwerty",
    "maria": "12345",
    "petr": "admin",
    "anna": "pass",
    "guest": "guest"
}
new_users = {login: len(password) for login, password in users.items()}
print(new_users)

# ЗАДАНИЕ 3: Кортеж и tuple(...)
scores = (10, 7, 0, 9, 8, 5)
new_scores = tuple(x * 1.1 for x in scores)
print(new_scores)
