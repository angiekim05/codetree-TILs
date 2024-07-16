a,b,c = map(int,input().split())
print(1 if a == min(a,b,c) else 0, 1 if set([a,b,c]) == set(a) else 0)