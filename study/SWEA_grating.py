t = int(input())

for test in range(t) :
    n, m = map(int,input().split())
    matrix = []
    fflag = 0
    first = 0
    pflag = 0
    
    for _ in range(n) :
        matrix.append(list(input()))
        
    for i in range(n) :
        for j in range(m) :
            if matrix[i][j] == "#" :
                fflag = 1
                if (i + j) % 2 == 0 :
                    first = 1
                else :
                    first = 2
            elif matrix[i][j] == "." :
                fflag = 1
                if (i + j) % 2 == 0 :
                    first = 2
                else :
                    first = 1
            if fflag == 1 :
                break
        if fflag == 1 :
            break

    for i in range(n) :
        for j in range(m) :
            if first == 0 :
                break
            elif first == 1 :
                if (i + j) % 2 == 0 :
                    if matrix[i][j] == "." :
                        pflag = 1
                        break
                else :
                    if matrix[i][j] == "#" :
                        pflag = 1
                        break
            elif first == 2 :
                if (i+j) % 2 == 0 :
                    if matrix[i][j] == "#" :
                        pflag = 1
                        break
                else :
                    if matrix[i][j] == "." :
                        pflag = 1
                        break
        if pflag == 1 :
            break
        if first == 0 :
            break

    if pflag == 1 :
        print(f"#{test+1} impossible")
    else :
        print(f"#{test+1} possible")
