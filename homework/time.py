
def get_time(n):
    """n - количество секунд, Выход: hh:mm:ss"""

    hh = n // 3600
    mm = (n % 3600) // 60
    ss = n - (hh * 3600 + mm * 60)
    print (f"{hh}:{mm}:{ss}")

get_time(43000)
