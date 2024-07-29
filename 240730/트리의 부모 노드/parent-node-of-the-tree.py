n = int(input())
p = [0]*n
for _ in range(n-1):
    x,y = map(int, input().split())
    p[y-1] = x

for i in range(1,n):
    print(p[i])