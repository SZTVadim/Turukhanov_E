# ЗАДАНИЕ 1: Работа с множествами
fruits = {"яблоко", "банан"}
fruits.add("апельсин")
fruits.update(["груша", "виноград"])
fruits.discard("банан")
fruits.discard("киви")
# fruits.remove("киви")
fruits_delete = fruits.pop()
print(fruits)
print(fruits_delete)

# ЗАДАНИЕ 2: Работа с кортежами
coordinates = (10, 20, 30, 20, 10, 20, 40)
print(coordinates[0])
print(coordinates[-1])
print(coordinates[1:5])
print(30 in coordinates)
print(coordinates.index(20))
print(coordinates.count(20))
print(coordinates.count(50))
print(len(coordinates))
