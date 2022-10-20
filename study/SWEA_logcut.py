t = int(input())

for test in range(t) :
    n = int(input())
    if n % 2 == 0 :
        print(f"#{test+1} Alice")
    else :
        print(f"#{test+1} Bob")
