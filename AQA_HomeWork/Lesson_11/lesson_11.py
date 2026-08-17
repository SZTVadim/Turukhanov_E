# ЗАДАНИЕ 1: Функции и условия
# 1. Создайте функцию calculate_total(price, tax_percent):
def calculate_total(price, tax_percent):
    if tax_percent > 20 or price < 0:
        return "ОШИБКА.Введен налог больше 20% или цена меньше нуля"
    return f"Итоговая цена с налогом:{price + ((price*tax_percent) / 100)}"

# 2. Создайте функцию get_level(points):


def get_level(points):
    if points >= 100:
        return "Эксперт"
    elif points >= 50:
        return "Продвинутый"
    elif points >= 20:
        return "Начинающий"
    else:
        return "Новичок"

# ЗАДАНИЕ 2: Функции с условиями и match/case


def process_status(status):
    match status:
        case "active":
            return "Статус активен"
        case "inactive":
            return "Статус неактивен"
        case "pending":
            return "Статус в ожидании"
        case "blocked":
            return "Статус заблокирован"
        case _:
            return "Неизвестный статус"
