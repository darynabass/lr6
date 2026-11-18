# Лабораторна робота №6
# Сучасні засоби розробки та парадигми програмування


# 1. Імперативне програмування

print("1. Імперативне програмування")

numbers = [10, 20, 30, 40, 50]

total = 0

for number in numbers:
    total += number

print("Список чисел:", numbers)
print("Сума елементів:", total)


# 2. Об'єктно-орієнтоване програмування

print("\n2. Об'єктно-орієнтоване програмування")


class Car:
    def __init__(self, model):
        self.model = model
        self.running = False

    def start(self):
        self.running = True
        print(f"{self.model} запущено.")

    def stop(self):
        self.running = False
        print(f"{self.model} зупинено.")


car = Car("Tesla Model S")

car.start()
car.stop()


# 3. Функціональне програмування

print("\n3. Функціональне програмування")

numbers = [2, 4, 6, 8, 10]

squares = list(map(lambda x: x ** 2, numbers))

print("Початковий список:", numbers)
print("Квадрати чисел:", squares)
