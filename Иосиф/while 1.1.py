n = int(input("Введите число: "))
lst = []
while n < 100:
    lst.append(n)
    n = int(input("Введите число: "))

for x in range(1, 100):
    if lst[-1] % x == 0:
        print (x, end = " ")

    