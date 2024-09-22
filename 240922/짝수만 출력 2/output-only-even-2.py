b,a = map(int,input().split())
x = b
while a <= x:
    if x%2 == 0:
        print(x, end=" ")
    x-=1