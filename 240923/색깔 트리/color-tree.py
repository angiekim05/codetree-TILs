node = dict()
pid = dict()
childs = dict()
childs[-1] = []
color = dict()
max_d = dict()
max_d[-1] = 100000
color_changed = dict()

# 노드 추가
def add_node(mid,p,c,m,idx):
    if max_d[p] == 1:
        return
    pid[mid] = p
    childs[mid] = []
    childs[p].append(mid)
    color[mid] = c
    max_d[mid] = min(m,max_d[p]-1)
    node[mid] = idx
    return

# 색변경
def change_color(mid, c, idx):
    color_changed[mid] = idx
    color[mid] = c
    return

# 색조회
def print_color(mid):
    x = mid
    c = color[mid]
    while True:
        if pid[x] in color_changed and node[x] < color_changed[pid[x]] :
            c = color[pid[x]]
        x = pid[x]
        if x == -1:
            break
    print(c)
    return

# 점수조회
def print_score():
    res = 0
    for c in childs[-1]:
        s,cp = count_score(c, 0, 0)
        res += s

    print(res)
    return

# 점수계산
def count_score(x, nc, idx):
    if x in color_changed:
        if color_changed[x] > idx:
            idx = color_changed[x]
        else:
            color[x] = nc
        color_changed.pop(x)
    else:
        if node[x] < idx:
            color[x] = nc
        else:
            idx = 0
    
    c = color[x]
    score = 0
    cp = 1 << c

    if not childs[x]:
        return 1, cp
    
    for cx in childs[x]:
        s,cp_ = count_score(cx, c, idx)
        score += s
        cp |= cp_
    
    score += sum([1 for b in bin(cp) if b == "1"])**2
    return score, cp

    



n = int(input())
for i in range(n):
    q, *datas = map(int,input().split())
    if q == 100:
        add_node(*datas,i)
    elif q == 200:
        change_color(*datas,i)
    elif q == 300:
        print_color(*datas)
    elif q == 400:
        print_score()