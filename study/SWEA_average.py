t = int(input())

for test in range(t) :
    arr = list(map(int, input().split()))
    del arr[arr.index(max(arr))]
    del arr[arr.index(min(arr))]
    avg = round(sum(arr)/8)
    print(f'#{test+1} {avg}')
