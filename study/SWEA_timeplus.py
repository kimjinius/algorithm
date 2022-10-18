t = int(input())

for test in range(t):
    h1, m1, h2, m2 = map(int, input().split())
    mflag = 0
    hflag = 0
    if m1 + m2 >= 60 :
        minute = m1 + m2 - 60
        mflag = 1
    else :
        minute = m1 + m2

    if mflag == 1 :
        if h1 + h2 + 1 >= 13 :
            hour = h1 + h2 + 1 - 12
        else :
            hour = h1 + h2 + 1
    else :
        if h1 + h2  >= 13 :
            hour = h1 + h2 - 12
        else :
            hour = h1 + h2
    print(f'#{test+1} {hour} {minute}')
    
