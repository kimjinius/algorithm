t = int(input())

for test in range(t) :
    words = input()
    flag = 0
    for i in range(int(len(words)/2)):
        if words[i] != words[-1-i]:
            flag = 1
            break
    if flag == 0 :
        print(f'#{test+1} 1')
    else :
        print(f'#{test+1} 0')
