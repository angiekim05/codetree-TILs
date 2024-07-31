import sys
import copy

N = int(sys.stdin.readline())
field = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
min_field = copy.deepcopy(field)
max_field = copy.deepcopy(field) 

for i in range(N):
    for j in range(N):
        if i == 0 and j == 0:
            continue
        elif i == 0:
            max_field[i][j] = max((max_field[i][j], max_field[i][j-1]))
            min_field[i][j] = min((min_field[i][j], min_field[i][j-1]))
        elif j == 0:
            max_field[i][j] = max((max_field[i-1][j], max_field[i][j]))
            min_field[i][j] = min((min_field[i-1][j], min_field[i][j]))
        else:
            max_val, min_val = 0, 0
            max1, min1,= max_field[i-1][j], min_field[i-1][j]
            max2, min2 = max_field[i][j-1], min_field[i][j-1]
            max_val = max2 if abs(max1-min1) > abs(max2-min2) else max1
            min_val = min2 if abs(max1-min1) > abs(max2-min2) else min1
            max_field[i][j] = max((max_val, max_field[i][j]))
            min_field[i][j] = min((min_val, min_field[i][j]))

print(abs(min_field[i][j]-max_field[i][j]))