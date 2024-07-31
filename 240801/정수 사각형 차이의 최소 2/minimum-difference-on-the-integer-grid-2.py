n = int(input())
arr = [list(map(int,input().split())) for i in range(n)]
dp = [[[0,10000] for _ in range(n)] for _ in range(n)]

def minus(x,y):
    return abs(x-y)

dp[0][0] = [arr[0][0],arr[0][0]]
for i in range(1,n):
    dp[i][0] = [max(arr[i][0], dp[i-1][0][0]),min(arr[i][0], dp[i-1][0][1])]
    dp[0][i] = [max(arr[0][i], dp[0][i-1][0]),min(arr[0][i], dp[0][i-1][1])]

for i in range(1,n):
    for j in range(1,n):
        temp1 = [max(arr[i][j], dp[i-1][j][0]),min(arr[i][j], dp[i-1][j][1])]
        temp2 = [max(arr[i][j], dp[i][j-1][0]),min(arr[i][j], dp[i][j-1][1])]
        if minus(*temp1) > minus(*temp2):
            dp[i][j] = temp2
        else:
            dp[i][j] = temp1
        


print(dp[-1][-1][0] - dp[-1][-1][1])
# print(*dp,sep="\n")