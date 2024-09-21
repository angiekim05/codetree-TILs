n = int(input())
tgt = [0]*51
tgt[0] = 1
tgt[1] = 1

def codetree(n):
    if tgt[n]:
        return tgt[n]
    tgt[n] = codetree(n-1)+codetree(n-2) +1
    return tgt[n]

print(codetree(n)%1000000007)