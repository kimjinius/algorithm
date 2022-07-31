n, k = map(int, input().split())
arr = []
sum = 0
for i in range(n):
    if i<k-1:
        arr.append(int(input()))
    else :
        arr.append(int(input()))
        arr2 = sorted(arr)
        if k%2 == 0 :
            sum += arr2[int((k+1)/2)-1]
        else:
            sum += arr2[int((k+2)/2)-1]
        del arr[0]
print(sum)
