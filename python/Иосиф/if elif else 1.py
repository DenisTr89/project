n1 = int(input("Введите первое число: "))
n2 = int(input("Введите второе число: "))
z = input("Введите операцию: ")
m = int(input("Введите ответ: "))
if z == "+":
    print("Правильно" if n1 + n2 == m else "Неправильно")
elif z == "-":
    print("Правильно" if n1 - n2 == m else "Неправильно")
elif z == "*":
    print("Правильно" if n1 * n2 == m else "Неправильно")
elif z == "/":
    print("Правильно" if n1 / n2 == m else "Неправильно")
elif z == "//":
    print("Правильно" if n1 // n2 == m else "Неправильно")
elif z == "%":
    print("Правильно" if n1 % n2 == m else "Неправильно")
elif z == "**":
    print("Правильно" if n1 ** n2 == m else "Неправильно")