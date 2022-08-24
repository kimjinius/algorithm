import sys 
input = sys.stdin.readline

n, k = map(int, input().split())
a = []

for i in range(n):
    b = int(input())
    if b<=k :
        a.append(b)
    else :
        break
    
count = 0
for i in range(len(a)-1, -1, -1):
    count += k//a[i]
    k = k%a[i]


print(count)
