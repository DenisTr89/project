n = list(map(int, input().split()))
print([x for x in n if x % 2 != 0 and abs(x) > 10])
