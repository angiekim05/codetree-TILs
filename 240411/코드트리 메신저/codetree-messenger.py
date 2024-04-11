n,q = map(int, input().split())
Tree = []
noti = [[0]*22 for _ in range(n+1)]

class Node:
    def __init__(self, p, a):
        self.parent = p
        self.authority = a
        self.block = False
        self.cnt = 0

def push_info(data):
    global Tree
    Tree = [Node(data[i-1],data[n+i-1]) if i != 0 else Node(None,None) for i in range(n+1)]
    for i in range(n):
        a = data[n+i]
        cur = Tree[i+1]
        noti[i+1][a] += 1
        while a > 0:
            a -= 1
            p = cur.parent
            cur = Tree[p]
            cur.cnt += 1
            noti[p][a] += 1

def change_alam(data):
    x = data[0]
    if not Tree[x].block:
        Tree[x].block = True
        k = -1
    else:
        Tree[x].block = False
        k = 1
    for i in range(1,21):
        level = i
        m = noti[x][level]
        cur = Tree[x]
        if m == 0:
            continue
        while cur.parent is not None and level:
            level -= 1
            p = cur.parent
            cur = Tree[p]
            noti[p][level] += m*k
            cur.cnt += m*k



def change_power(data):
    x, new_a = data
    cur = Tree[x]
    a = cur.authority
    noti[x][a] -= 1
    noti[x][new_a] += 1
    while max(new_a,a) > 0:
        if cur.block:
            break
        a -= 1
        new_a -= 1
        p = cur.parent
        cur = Tree[p]
        if a >= 0:
            noti[p][a] -= 1
            cur.cnt -= 1
        if new_a >= 0:
            noti[p][new_a] += 1
            cur.cnt += 1




def change_parent(data):
    c1,c2 = data
    c1_block = Tree[c1].block
    c2_block = Tree[c2].block
    if not c1_block:
        change_alam([c1])
    if not c2_block:
        change_alam([c2])

    Tree[c1].parent, Tree[c2].parent = Tree[c2].parent, Tree[c1].parent

    if not c1_block:
        change_alam([c1])
    if not c2_block:
        change_alam([c2])


def get_alams(data):
    x = data[0]
    return Tree[x].cnt


for _ in range(q):
    qn, *data = map(int,input().split())
    if qn == 100:
        push_info(data)
    elif qn == 200:
        change_alam(data)
    elif qn == 300:
        change_power(data)
    elif qn == 400:
        change_parent(data)
    else:
        print(get_alams(data))