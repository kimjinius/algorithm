n = int(input())

for i in range(n):
    day = int(input())
    arr = list(map(int, input().split()))
    sum = 0
    while True:

        if len(arr) <= 1 :
            print("#" + str(i+1) + " " + str(sum))
            break

        if 

        max_index = [i for i, value in enumerate(arr) if value == max(arr)]
        if max_index[-1] == 0 :
            arr = arr[1:]
            
        else:
            for j in range(max_index[-1]) :
                sum = sum + arr[max_index[-1]] - arr[j]
            arr = arr[max_index[-1] + 1 :]

