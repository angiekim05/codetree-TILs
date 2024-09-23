r,c,k = map(int,input().split())
forest = [[1]+[0]*c for _ in range(r+2)]
exits = set()
dx = [-1,0,1,0]
dy = [0,1,0,-1]

def init_forest():
    global exits
    exits = set()
    for i in range(r+1):
        for j in range(1,c+1):
            forest[i][j] = 0
    return

def can_go_south(x,y):
    if forest[x+1][y-1] or forest[x+2][y] or forest[x+1][y+1]:
        return False
    return True

def can_go_west(x,y):
    if y-2 < 1 or forest[x-1][y-1] or forest[x][y-2] or forest[x+1][y-1] or forest[x+1][y-2] or forest[x+2][y-1]:
        return False
    return True

def can_go_east(x,y):
    if y+2 > c or forest[x-1][y+1] or forest[x][y+2] or forest[x+1][y+1] or forest[x+1][y+2] or forest[x+2][y+1]:
        return False
    return True

def in_range(x,y):
    return 1<=x<=r and 1<=y<=c

def get_row(fx,fy):
    res = fx
    stack = [(fx,fy)]
    visited = [[0]*(c+1) for _ in range(r+1)]
    visited[fx][fy] = 1
    while stack:
        x,y = stack.pop()
        golam_numb = forest[x][y]
        for i in range(4):
            nx,ny = x+dx[i], y+dy[i]
            if not in_range(nx,ny):
                continue
            if visited[nx][ny]:
                continue
            if forest[nx][ny] == 0:
                continue
            if forest[nx][ny] == golam_numb or (x,y) in exits:
                visited[nx][ny] = 1
                stack.append((nx,ny))
                res = max(res,nx)

                if res == r:
                    return res
    # print(exits)
    # print(fx,fy)
    # print(*visited[1:], sep="\n")
    # print()
    return res

def go_down(idx,y,d):
    x = 0

    while x < r-1:
        if can_go_south(x,y):
            x,y = x+1,y
        elif can_go_west(x,y):
            x,y = x+1,y-1
            d = (d-1)%4
        elif can_go_east(x,y):
            x,y = x+1,y+1
            d = (d+1)%4
        else:
            break
    
    if x <= 1:
        # 골렘 정리
        init_forest()
        return 0
    
    # 골렘 영역 표시
    forest[x][y] = idx
    for i in range(4):
        forest[x+dx[i]][y+dy[i]] = idx
    exits.add((x+dx[d],y+dy[d])) # 출구

    return get_row(x,y)

ans = 0
for i in range(k):
    ans += go_down(i+1,*map(int,input().split()))

print(ans)