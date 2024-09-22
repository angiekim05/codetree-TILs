n = int(input())
arr = [list(map(int,input().split())) for _ in range(n)]
dp = [[0]*(n+1) for _ in range(n+1)]

for i in range(n):
    for j in range(n):
        dp[i+1][j+1] = max(min(dp[i+1][j], dp[i][j+1]), arr[i][j])

print(dp[-1][-1])