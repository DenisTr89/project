x1 = int(input())
x2 = int(input())
if x1 > x2:
    print("x1 должен быть меньше x2")
elif (x1 > 0 and x2 > 0) or (x1 < 0 and x2 < 0):
    x = int(input())
    if x in range(x1, x2):
        print(f"{x} входит в отрезок[{x1}, {x2}]")
    else:
        print(f"{x} не входит в отрезок[{x1}, {x2}]")
else:
    print("x1, x2 должны быть либо оба положительными, либо оба отрицательными числами!")


