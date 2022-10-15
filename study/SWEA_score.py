t = int(input())
for test in range(t) :
    n, k = map(int, input().split())
    score_list=[]
    for i in range(n) :
        middle, last, task = map(int, input().split())
        score_list.append([i+1, int( middle*0.35 + last*0.45 + task*0.2 ) ])
    score_list.sort(key=lambda x:-x[1])

    for i in range(n):
        if score_list[i][0] == k :
            if i == 0 :
                print(f'#{test+1} A+')
                break
            elif i == 1 :
                print(f'#{test+1} A0')
                break
            elif i == 2 :
                print(f'#{test+1} A-')
                break
            elif i == 3 :
                print(f'#{test+1} B+')
                break
            elif i == 4 :
                print(f'#{test+1} B0')
                break
            elif i == 5 :
                print(f'#{test+1} B-')
                break
            elif i == 6 :
                print(f'#{test+1} C+')
                break
            elif i == 7 :
                print(f'#{test+1} C0')
                break
            elif i == 8 :
                print(f'#{test+1} C-')
                break
            elif i == 9 :
                print(f'#{test+1} D0')
                break
