from collections import deque

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
total = sum(sum(row) for row in arr)  # 전체 빙하의 개수 카운트

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def can_go(x, y):
    return 0 <= x < n and 0 <= y < m

def melted():
    new = [[arr[i][j] for j in range(m)] for i in range(n)]
    visited = [[0] * m for _ in range(n)]

    q = deque()
    q.append((0, 0))  # 외부에서 시작
    cnt = 0
    while q:
        x, y = q.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if not can_go(nx, ny):
                continue
            if visited[nx][ny]:
                continue
            visited[nx][ny] = 1
            
            if arr[nx][ny] == 1:  # 빙하인 경우
                new[nx][ny] = 0  # 녹임
                cnt += 1
            else:
                q.append((nx, ny))  # 물인 경우 큐에 추가
    return cnt, new

t = 0
while total:
    cnt, arr = melted()
    t += 1
    total -= cnt
    if total == 0:
        print(t, cnt)
        break