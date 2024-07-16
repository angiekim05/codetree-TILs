people = [input().split() for _ in range(3)]
a = 0
for x,t in people:
    if x == "Y" and int(t) >= 37:
        a += 1
if a >= 2:
    print("E")
else:
    print("N")