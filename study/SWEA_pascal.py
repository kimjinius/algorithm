t = int(input())

for num in range(t) :
    n = int(input())
    front = []
    now = []
    print(f'#{num+1}')
    for i in range(1, n+1) :
        for j in range(1, i+1) :
            if j == 1 or j == i :
                now.append(1)
            else :
                now.append(front[j-2]+front[j-1])
        for j in range(i) :
            print(now[j], end=" ")
        print()
        front = now
        now = []
