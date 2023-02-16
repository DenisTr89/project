s = input()
cnt = 0
for i in range(1, len(s)):
    if s[i] == s[i-1]:
        cnt += 1
        break
print ("Все в порядке" if cnt == 0 else "Есть повторение")
    
