n = int(input())

print('* '*n)

for i in range(1, n):
    print('    '*(i//2), '  * '*((n-i+1)//2), sep="")