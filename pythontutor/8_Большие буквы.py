n = input().split()
def capitalize(string):
    s = ""
    for i in string:
        s += i[0].upper() + i[1 : len(i)] + " "
    print(s)


capitalize(n)
