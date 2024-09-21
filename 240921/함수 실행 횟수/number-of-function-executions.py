n = int(input())
ans = 0
def codetree(n):
    global ans
    ans += 1
    if n<2:
        return n 
    else:
        return codetree(n-1) + codetree(n-2)

codetree(n)
print(ans%1000000007)