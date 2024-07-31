n = int(input())
arr = [list(map(int,input().split())) for i in range(n)]
dp = [[[0,10000] for _ in range(n+1)] for _ in range(n+1)]

def minus(x,y):
    return [abs(x-y),[x,y]]

for i in range(1,1+n):
    for j in range(1,1+n):
        dp[i][j] = sorted([minus(*dp[i-1][j]), minus(*dp[i][j-1])])[0][1]
        dp[i][j][0] = max(dp[i][j][0], arr[i-1][j-1])
        dp[i][j][1] = min(dp[i][j][1], arr[i-1][j-1])
        


print(dp[-1][-1][0] - dp[-1][-1][1])
# print(*dp,sep="\n")