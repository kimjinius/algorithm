import sys 
input = sys.stdin.readline

n = int(input())
a = []
dp = [0] * (n+1)
for i in range(n):
    a.append(list(map(int, input().split())))

M = 0
for i in range(n):
    M = max(M, dp[i])
    if i + a[i][0] > n:
        continue
    dp[i+a[i][0]] = max(M + a[i][1], dp[i + a[i][0]])

print(max(dp))
