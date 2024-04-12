n,q = map(int, input().split())
parent = [0]*(n+1)
parent[0] = -1
authority = [0]*(n+1)
block = [0] *(n+1)
noti = [[0]*22 for _ in range(n+1)]
cnt = [0]*(n+1)

def push_info(data):
    for i in range(n):
        p = data[i]
        a = min(20,data[n+i])
        parent[i+1] = p
        authority[i+1] = a

    for i in range(1,n+1):
        l = authority[i]
        cur = i
        noti[i][l] += 1
        while parent[cur] >= 0 and l > 0:
            l -= 1
            cur = parent[cur]
            cnt[cur] += 1
            noti[cur][l] += 1


def change_alam(data):
    x = data[0]
    if block[x]:
        block[x] = 0
        k = 1
    else:
        block[x] = 1
        k = -1

    cur = x
    depth = 1
    while parent[cur] != -1:
        cur = parent[cur]
        for i in range(1,21):
            m = noti[x][i]
            if m <= 0 or i-depth < 0:
                continue
            cnt[cur] += k * m
            noti[cur][i-depth] += k * m
        if block[cur]:
            break
        depth += 1


def change_power(data):
    x, new_a = data
    a = authority[x]
    noti[x][a] -= 1
    noti[x][new_a] += 1
    if not block[x]:
        cur = x
        for i in range(a-1,-1,-1):
            cur = parent[cur]
            noti[cur][i] -= 1
            cnt[cur] -= 1
            if block[cur] or parent[cur] == -1:
                break

    if not block[x]:
        cur = x
        for i in range(new_a-1,-1,-1):
            cur = parent[cur]
            noti[cur][i] += 1
            cnt[cur] += 1
            if block[cur] or parent[cur] == -1:
                break

    # while parent[cur] != -1 and max(new_a,a) > 0:
    #     if block[cur]:
    #         break
    #     a -= 1
    #     new_a -= 1
    #     cur = parent[cur]
    #     if a >= 0:
    #         noti[cur][a] -= 1
    #         cnt[cur] -= 1
    #     if new_a >= 0:
    #         noti[cur][new_a] += 1
    #         cnt[cur] += 1


def change_parent(data):
    c1,c2 = data
    c1_block = block[c1]
    c2_block = block[c2]
    if not c1_block:
        change_alam([c1])
    if not c2_block:
        change_alam([c2])

    # print("mid")
    # print(*noti,sep="\n")
    parent[c1], parent[c2] = parent[c2], parent[c1]

    if not c1_block:
        change_alam([c1])
    if not c2_block:
        change_alam([c2])


def get_alams(data):
    x = data[0]
    print(cnt[x])


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
        get_alams(data)

    #
    # print(qn,data)
    # print(*noti,sep="\n")
    # print(cnt)
    # print()