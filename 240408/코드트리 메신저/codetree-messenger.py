n,q = map(int, input().split())
Tree = []

class Node:
    def __init__(self, i):
        self.idx = i
        self.p = None
        self.a = None
        self.alam = True
        self.child = set()

    def push_data(self, p, a):
        self.p = p
        self.a = a

def ready(data):
    global Tree
    Tree = [Node(i) for i in range(n+1)]
    for i in range(n):
        p = data[i]
        a = data[n+i]
        cur = i+1
        Tree[cur].push_data(p,a)
        Tree[p].child.add(Tree[cur])


def change_alam(data):
    cur = data[0]
    if Tree[cur].alam:
        Tree[cur].alam = False
    else:
        Tree[cur].alam = True


def change_power(data):
    cur, p = data
    Tree[cur].a = p


def change_parent(data):
    c1,c2 = data
    p1,p2 = Tree[c1].p, Tree[c2].p
    Tree[c1].p, Tree[c2].p = p2,p1
    Tree[p1].child.remove(Tree[c1])
    Tree[p2].child.remove(Tree[c2])
    Tree[p1].child.add(Tree[c2])
    Tree[p2].child.add(Tree[c1])


def get_alams(data):
    cur = data[0]
    cnt = 0
    stack = [(Tree[cur], 0)]
    visited = [0]*(n+1)

    while stack:
        cur_node, dist = stack.pop()

        for next_node in cur_node.child:
            if not next_node.alam: # 꺼져있으면 더이상 안가도 됨 어차피 도달 못함
                continue
            if visited[next_node.idx]:
                continue
            visited[next_node.idx] = 1
            stack.append((next_node, dist+1))
            if next_node.a > dist:
                cnt += 1
    return cnt

for _ in range(q):
    qn, *data = map(int,input().split())
    if qn == 100:
        ready(data)
    elif qn == 200:
        change_alam(data)
    elif qn == 300:
        change_power(data)
    elif qn == 400:
        change_parent(data)
    else:
        print(get_alams(data))