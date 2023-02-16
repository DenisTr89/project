def pow1(a, n):
    """Возведение числа в степень с помощью рекурсии"""
    if n == 0:
        return 1
    else:
        return pow1(a, n-1) * a
print (pow1(2, 4))