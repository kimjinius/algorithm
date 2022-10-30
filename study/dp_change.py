n , m = map(int,input().split())

money = []
for _ in range(n) :
    money.append(int(input()))

money.sort(reverse = True)

change = 0

for i in money :
    change += m // i
    m = m % i
    if m == 0 :
        break

if m!= 0 :
    print(-1)
else :
    print(change)    
