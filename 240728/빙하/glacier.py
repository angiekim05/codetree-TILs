from collections import deque

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
total = sum(sum(row) for row in arr)  # 전체 빙하의 개수 카운트

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < m

def melt():
    can_be_melt = []
    visited = [[0] * m for _ in range(n)]

    q = deque()
    q.append((0, 0))  # 외부에서 시작
    while q:
        x, y = q.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if not in_range(nx, ny):
                continue
            if visited[nx][ny]:
                continue
            visited[nx][ny] = 1
            
            if arr[nx][ny] == 1:  # 빙하인 경우
                can_be_melt.append((nx,ny))  # 녹일 수 있는 빙하 담기
            else:
                q.append((nx, ny))  # 물인 경우 큐에 추가
    
    for x,y in can_be_melt: # 동시에 빙하 녹이기
        arr[x][y] = 0

    return len(can_be_melt), new

t = 0
while total:
    cnt, arr = melt()
    t += 1
    total -= cnt 
    if total == 0: # 녹일 빙하가 남아있지 않으면 종료
        print(t, cnt)
        break