n = int(input())
arr = []
MAX = 0
for i in range(n):
    arr.append(list(map(int,input().split())))
    MAX = max(MAX, *arr[i])
dp = [[MAX+1] * n for _ in range(n)]

ans = 1000
for lower_bound in range(1,MAX+1):
    dp[0][0] = arr[0][0] if arr[0][0] >= lower_bound else 101

    for i in range(1,n):
        dp[i][0] = max(arr[i][0] if arr[i][0] >= lower_bound else 101, dp[i-1][0])
        dp[0][i] = max(arr[0][i] if arr[0][i] >= lower_bound else 101, dp[0][i-1])
        
    for i in range(1,n):
        for j in range(1,n):
            dp[i][j] = max(min(dp[i-1][j],dp[i][j-1]), arr[i][j] if arr[i][j] >= lower_bound else 101)

    ans = min(ans, dp[-1][-1]-lower_bound)
print(ans)