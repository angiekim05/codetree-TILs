n = int(input())
arr = list(map(int, input().split()))
arr.sort()

ans = (0,0)
sum_ = 2000000001

for i in range(n):
    for j in range(n-1,i-1,-1):
        if abs(arr[i]+arr[j]) < sum_:
            ans = (arr[i],arr[j])
            sum_ = abs(arr[i]+arr[j])
        elif abs(arr[i]+arr[j]) > sum_:
            break
print(*ans)