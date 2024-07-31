a,b = map(int,input().split())

s = a//b
print(s,end=".")
a = a%b * 10
for i in range(20):
    print(a//b, end="")
    a = a%b * 10