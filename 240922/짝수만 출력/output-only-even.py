a,b = map(int,input().split())
x = a
while x <= b:
    if x%2 == 0:
        print(x, end=" ")
    x += 1