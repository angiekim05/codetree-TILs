from collections import deque
n = int(input())
t = [[] for _ in range(n+1)]
for _ in range(n-1):
    a,b,c = map(int,input().split())
    t[a].append((b,c))
    t[b].append((a,c))

def bfs(x):
    q = deque([x])
    visited = [0]*(n+1)
    visited[x] = -1
    while q:
        x = q.popleft()
        for nx, nd in t[x]:
            if not visited[nx]:
                visited[nx] = visited[x] + nd
                q.append(nx)
    return visited

temp = bfs(1)
y = temp.index(max(temp))
print(max(bfs(y))+1)