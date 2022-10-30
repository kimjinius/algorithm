n = int(input())
arr = list(map(int, input().split()))

dp = [0] * n

for i in range(n) :
    if i == 0 :
        dp[i] = arr[i]
    elif i == 1 :
        dp[i] = max(dp[0], arr[i])
    else :
        if dp[i-2] + arr[i] < dp[i-1] :
            dp[i] = dp[i-1]
        else :
            dp[i] = dp[i-2] + arr[i]

print(dp[n-1])
