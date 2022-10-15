t = int(input())
for i in range(t) :
    arr = input()
    pattern = []
    pattern.append(arr[0])
    for j in range(1,30) :
        if pattern[0] == arr[j] :
            flag = 0
            for k in range(len(pattern)):
                if pattern[k] != arr[j+k] :
                    flag = 1
                    break
            if flag == 0 :
                print(f"#{i+1} {len(pattern)}")
                break
            else :
                pattern.append(arr[j])
        else :
            pattern.append(arr[j])
