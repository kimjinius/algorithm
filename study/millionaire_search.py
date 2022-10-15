n = int(input())

for i in range(n):
    day = int(input())
    arr = list(map(int, input().split()))
    get = 0
    max_n = arr[-1]

    for j in range(day-2, -1, -1):
        if arr[j] >= max_n :
            max_n = arr[j]
        else :
            get += max_n - arr[j]
    print('#{} {}'.format(i+1, get))
