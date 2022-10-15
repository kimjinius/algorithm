n = int(input())

for i in range(1, n+1) :
    digit = len(str(i))
    #print("digit = "+  str(digit))
    flag = 0
    front = i
    for j in range(digit):
        back = front%10
        front = int(front/10)
        if back == 0 :
            pass
        elif back % 3 == 0 :
            print("-", end="")
            flag = 1
    if flag == 0 :
        print(i, end= "")
    print(" ", end="")
