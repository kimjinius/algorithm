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
            if i < n/10 :
                print(f'#{test+1} A+')
                break
            elif i < n/10*2 :
                print(f'#{test+1} A0')
                break
            elif i < n/10*3 :
                print(f'#{test+1} A-')
                break
            elif i < n/10*4 :
                print(f'#{test+1} B+')
                break
            elif i < n/10*5 :
                print(f'#{test+1} B0')
                break
            elif i < n/10*6 :
                print(f'#{test+1} B-')
                break
            elif i < n/10*7 :
                print(f'#{test+1} C+')
                break
            elif i < n/10*8 :
                print(f'#{test+1} C0')
                break
            elif i < n/10*9 :
                print(f'#{test+1} C-')
                break
            elif i < n/10*10 :
                print(f'#{test+1} D0')
                break
