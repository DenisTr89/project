
def get_non_armstrong(n):
    """Вернуть первые n чисел, не являющимися числами армстронга
    Пример 53 : 1^3 + 5^3 + 3^3 = 153
    """
    cnt = 1 # Счетчик начала отсчета числа
    cnt_n = 0 # Счетчик количества вывода n
    arm = []
    while cnt_n <= n:
        n_str = str(cnt)
        sum = 0
        for i in n_str:
            sum += int(i)**len(n_str)
        if sum == cnt:
            cnt += 1
        else:
            arm.append(cnt)
            cnt_n += 1
            cnt += 1
    
    return arm

print(get_non_armstrong(300))