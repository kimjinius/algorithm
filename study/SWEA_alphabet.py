t = int(input())

for test in range(t):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    quest = input()
    cnt = 0
    for i in range(len(quest)):
        if quest[i] == alphabet[i] :
            cnt +=1
        else :
            break
    print(f"#{test+1} {cnt}")
