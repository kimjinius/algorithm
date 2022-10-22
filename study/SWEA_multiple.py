t = int(input())

for test in range(t) :
    n = int(input())
    if 0 <= n < 10 :
        print(f"#{test+1} impossible")
    else :
        for i in range(2, 10):
            mult = n * i
            
