b,a = map(int,input().split())
for x in range(b,a-1,-1):
    if x%2 == 1:
        print(x,end=" ")