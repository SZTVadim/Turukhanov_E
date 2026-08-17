# ЗАДАНИЕ 1: Распаковка списка и слияние
statuses = ["queued", "running", "testing", "deploy", "done"]
first, *middle, last = statuses
new_statuses = [*middle, *["failed", "skipped"]]
print(first)
print(new_statuses)
print(last)

# ЗАДАНИЕ 2: Словарь, слияние и вызов функции

# Дано:
browser = {"browser": "chrome", "timeout": 3000}
options = {"headless": True, "timeout": 5000}


def start_session(browser, timeout, headless):
    return f"{browser}, timeout={timeout}, headless={headless}"


config = {**browser, **options}
print(start_session(**config))
print(config)
