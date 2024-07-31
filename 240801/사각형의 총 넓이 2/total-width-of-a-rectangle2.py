n = int(input())
rec = [list(map(int,input().split())) for _ in range(n)]
arr = [[0]*201 for _ in range(201)]
ans = 0
for r1,c1,r2,c2 in rec:
    for i in range(r1,r2):
        for j in range(c1,c2):
            arr[i+100][j+100] = 1
print(sum(sum(arr[i]) for i in range(201)))