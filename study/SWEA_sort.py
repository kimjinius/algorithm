t = int(input())
for test in range(t) :
    n = int(input())
    arr = list(map(int, input().split()))
    arr = sorted(arr)
    print(f'#{test+1}', end = " ")
    print(*arr)
