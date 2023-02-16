
N = int(input())
M = int(input())
x = int(input())
y = int(input())
cont_min = 0
cont_minXY = 0
if x > y:
    cont_minXY = y
else:
    cont_minXY = x
if N > M:
    cont_min = M - x
else:
    cont_min = N - x
print(min(cont_min, cont_minXY))


