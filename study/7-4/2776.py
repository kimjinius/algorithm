import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    num1 = set(map(int, input().split()))
    m = int(input())
    num2 = list(map(int, input().split()))
    for i in num2:
        if i in num1:
            print(1)
        else :
            print(0)
