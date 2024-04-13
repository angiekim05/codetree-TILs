from collections import deque
n,m,p,c,d = map(int,input().split())
rr,rc = map(int,input().split())
land = [[0]*(n+1) for _ in range(n+1)]
santa = dict()
santa_score = [0]*(p+1)
can_not_move = [0]*(p+1) # 기절
for _ in range(p):
    pn, sr, sc = map(int,input().split())
    land[sr][sc] = pn
    santa[pn] = (sr,sc)
    santa_score[pn] = 0

def dist(r1,c1,r2,c2):
    return (r1-r2)**2 + (c1-c2)**2

def in_range(x,y):
    return 1<=x<=n and 1<=y<=n


def push_santa(sn, x, y, dr, dc):
    if not in_range(x,y):
        santa.pop(sn)
    else:
        if land[x][y]:
            nx,ny = x+dr,y+dc
            push_santa(land[x][y],nx,ny,dr,dc)
        land[x][y] = sn
        santa[sn] = (x,y)
    return


def attack_santa(rr, rc, dr, dc, sn):
    santa_score[sn] += c
    can_not_move[sn] += 2
    land[rr][rc] = 0
    nx,ny = rr+c*dr, rc+c*dc
    push_santa(sn,nx,ny,dr,dc)
    return

def attack_rodolph(rr,rc,dr,dc,sn):
    santa_score[sn] += d
    can_not_move[sn] += 1
    land[rr][rc] = 0
    nx,ny = rr+d*dr, rc+d*dc
    push_santa(sn,nx,ny,dr,dc)
    return


def move_rudolph():
    global rr, rc
    q = deque()
    q.append((rr,rc))
    visited = [[0]*(n+1) for _ in range(n+1)]
    d = 10001
    close_santa = []
    while q:
        x,y = q.popleft()
        for dx, dy in [(1, 1), (1, 0), (1, -1), (0, 1), (0, -1), (-1, 1), (-1, 0), (-1, -1)]:
            nx, ny = x+dx,y+dy
            if not in_range(nx,ny):
                continue
            if visited[nx][ny]:
                continue
            visited[nx][ny] = 1
            nd = dist(nx,ny,rr,rc)
            if nd > d:
                continue
            if land[nx][ny]:
                if nd == d:
                    close_santa.append((nx,ny))
                elif nd < d:
                    d = nd
                    close_santa = [(nx,ny)]
            else:
                q.append((nx,ny))
    close_santa.sort()
    sr, sc = close_santa[-1]
    nrr,nrc = rr,rc
    dr,dc = 0,0
    min_dist = 10000
    for dx, dy in [(1, 1), (1, 0), (1, -1), (0, 1), (0, -1), (-1, 1), (-1, 0), (-1, -1)]:
        nx,ny = rr+dx, rc+dy
        if not in_range(nx, ny):
            continue
        nd = dist(nx,ny,sr,sc)
        if nd < min_dist:
            nrr,nrc = nx,ny
            dr,dc = dx,dy
            min_dist = nd
    rr,rc = nrr,nrc
    if land[rr][rc]:
        attack_santa(rr,rc,dr,dc,land[rr][rc])
    return


def move_santa():
    for i in range(1,p+1):
        if can_not_move[i]:
            can_not_move[i] -= 1
            continue
        if i in santa:
            sx,sy = santa[i]
            d = dist(sx,sy,rr,rc)
            dr,dc = 0,0
            nsx,nsy = sx,sy
            for dx, dy in [(-1,0),(0,1),(1,0),(0,-1)]:
                nx,ny = sx+dx, sy+dy
                if not in_range(nx,ny):
                    continue
                if land[nx][ny]:
                    continue
                nd = dist(nx,ny,rr,rc)
                if nd < d:
                    d = nd
                    nsx, nsy = nx, ny
                    dr,dc = dx,dy
            if (nsx,nsy) != (sx,sy):
                land[sx][sy] = 0
                land[nsx][nsy] = i
                santa[i] = (nsx,nsy)
                if (nsx,nsy) == (rr,rc):
                    attack_rodolph(rr,rc,-dr,-dc,i)

    return


for turn in range(m):
    move_rudolph()
    move_santa()
    # print(*land, sep="\n")
    # print(can_not_move)
    # print()

    for i in santa.keys():
        santa_score[i] += 1
    if not santa:
        break
print(*santa_score[1:])