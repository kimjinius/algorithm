t = int(input())

for test in range(t) :
    money = int(input())
    answer = [0, 0, 0, 0, 0, 0, 0 ,0]
    while True :
        if money >= 50000 :
            while money >= 50000 :
                answer[0] += 1
                money -= 50000
        elif money >= 10000 :
            while money >= 10000 :
                answer[1] += 1
                money -= 10000
        elif money >= 5000 :
            while money>=5000 :
                answer[2] += 1
                money -= 5000
        elif money >= 1000 :
            while money>=1000 :
                answer[3] += 1
                money -= 1000
        elif money >= 500 :
            while money>=500 :
                answer[4] += 1
                money -= 500
        elif money >= 100 :
            while money>=100 :
                answer[5] += 1
                money -= 100
        elif money >= 50 :
            while money>=50 :
                answer[6] += 1
                money -= 50
        elif money >= 10 :
            while money>=10 :
                answer[7] += 1
                money -= 10

        if money == 0 :
            break
        
    print(f"#{test+1}")
    for i in range(8):
        print(answer[i], end=" ")
    print()
