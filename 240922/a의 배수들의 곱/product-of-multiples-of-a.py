a,b=map(int,input().split())
ans = 1
for x in range(1,b+1):
    if x%a == 0:
        ans *= x

print(ans)