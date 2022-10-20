t = int(input())

for test in range(t) :
    ball = 0
    s = input()
    for i in range(len(s)-1):
        m = s[i: i+2]
        if m == "(|" or m == "|)" or m == "()" :
            ball +=1
    print(f"#{test+1} {ball}")
