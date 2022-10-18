t = int(input())

for test in range(t) :
    n , k = map(int, input().split())
    cnt = 0
    matrix = []
    for _ in range(n) :
        matrix.append(list(map(str, input().split())))

    for i in range(n) :
        result=""
        for s in matrix[i]:
            result = result + s
        for i in result.split("0") :
            if len(i) == k :
                cnt += 1

    for i in range(n) :
        result = ""
        for j in range(n) :
            result += matrix[j][i]
        for i in result.split("0") :
            if len(i) == k :
                cnt += 1
    print(f'#{test+1} {cnt}')
