a = int(input())
for x in range(1,a+1):
    if (x%2==0 and x%4!=0) or ((x//8)%2==0) or (x%7 < 4):
        continue
    print(x, end=" ")