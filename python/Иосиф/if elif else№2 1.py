n = int(input("Введите количество людей: "))
money  = int(input("Введите количество денег: "))
money_pizza = int(input("Введите цену за одну пиццу: "))

if money_pizza > money:
    print("Вы не можете заказать ни одной пиццы")
elif money // money_pizza == 1:
    print("Вы можете заказать только одну пиццу")
elif (money // money_pizza) == n:
    print(f"Для {n} человек, как раз хватит {n} пицц")
elif (money // money_pizza) > n:
    print(f"Для {n} человек, {money // money_pizza} пицц слишком много")
else:
    print(f"Для {n} человек, {money // money_pizza} пицц не хватит")