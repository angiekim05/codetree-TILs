n = int(input())
arr = [list(map(int,input().split())) for _ in range(n)]
dp = [[0]*(n+1) for _ in range(n+1)]

for i in range(n):
    dp[1][i+1] = max(dp[1][i],arr[1][i])
    dp[i+1][1] = max(dp[i][1],arr[i][1])

for i in range(1,n):
    for j in range(1,n):
        dp[i+1][j+1] = max(min(dp[i+1][j], dp[i][j+1]), arr[i][j])

print(dp[-1][-1])