n = int(input())
time = 45
count_ch = n // 2
count_ne = n - count_ch
print(9+(5 + count_ch*15 + count_ne*5 + time*n)//60, (5 + count_ch*15 + count_ne*5 + time*n) % 60)