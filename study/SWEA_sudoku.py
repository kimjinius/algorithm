t = int(input())

for test in range(t) :
    sudoku = []
    for i in range(9):
        sudoku.append(list(map(int, input().split())))

    flag = 0
    
    for i in range(9) :

        for key in range(1, 10) :
            if sudoku[i].count(key) != 1 :
                flag = 1
                break
        if flag == 1 :
            break
        
        for key in range(1,10):
            if [k[i] for k in sudoku].count(key) != 1 :
                flag = 1
                break
        if flag == 1 :
            break

    for i in range(3):
        for j in range(3) :
            cnt_x = [0] * 10
            for k in range(3) :
                 for l in range(3):
                     cnt_x[sudoku[3*i+k][3*j+l]] +=1
            for k in range(1, 10):
                if cnt_x[k] != 1 :
                    flag = 1
                    break
        if flag == 1 :
            break
    if flag == 1 :
        print(f'#{test+1} 0')
    else :
        print(f'#{test+1} 1')

        
