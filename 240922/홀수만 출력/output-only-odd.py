a,b = map(int,input().split())
for x in range(a,b+1):
    if x % 2 == 1:
        print(x,end=" ")