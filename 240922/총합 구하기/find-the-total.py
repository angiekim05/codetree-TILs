a,b = map(int,input().split())
ans = 0
for x in range(a,b+1):
    if x % 6 == 0 and x%8 != 0:
        ans += x
print(ans)