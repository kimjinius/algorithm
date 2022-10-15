t = int(input())

for test in range(t):
    n, m = map(int, input().split())
    matrix = []
    for i in range(n):
        matrix.append(list(map(int, input().split())))
    maxn = 0
    for i in range(n-m+1) :
        for j in range(n-m+1) :
            sumn = 0
            for k in range(m):
                for h in range(m) :
                    sumn = sumn + matrix[k+i][h+j]
            if sumn >= maxn :
                maxn = sumn
    print(f'#{test+1} {maxn}')
