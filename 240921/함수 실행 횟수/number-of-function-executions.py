n = int(input())
tgt = [0]*51
tgt[0] = 1
tgt[1] = 1

def codetree(n):
    for i in range(2,n+1):
        tgt[i] = tgt[i-1]+tgt[i-2]+1

    return tgt[n]

print(codetree(n)%1000000007)