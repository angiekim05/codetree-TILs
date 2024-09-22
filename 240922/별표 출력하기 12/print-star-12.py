n = int(input())

print('* '*n)

for i in range(1, n):
    print('    '*(i//2), '  * '*(n//2-i//2), sep="")