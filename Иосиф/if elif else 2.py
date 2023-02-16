n = int(input("Введите месяц: "))
if n in (12, 1, 2):
    print (f"{n} месяц это зима")
elif n in (3, 4, 5):
    print (f"{n} месяц это весна")
elif n in (6, 7, 8):
    print (f"{n} месяц это лето")
elif n in (9, 10, 11):
    print (f"{n} месяц это осень")
    