n = int(input())

a = n // 5
flag = 0
for i in range(a,-1,-1):
    b = int(n - (i*5))
    if b%3 == 0 :
        flag = 1
        m = int(b/3)
        n = i
        break

if flag == 0 :
    print("-1")
else :
    print(m+n)
