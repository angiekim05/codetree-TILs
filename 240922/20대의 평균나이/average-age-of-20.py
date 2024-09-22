s = 0
cnt = 0
while True:
    x = int(input())
    if 20 <= x < 30:
        s += x
        cnt += 1
    else:
        break
print("{:.02f}".format(s/cnt))