from heapq import heappop,heappush,heapify

waiting_url = set()
judging_domain = set()
waiting_queue = []
judging_machine = dict()
finished = dict()
resting = []
cnt = 0

q = int(input())

def ready(n, u):
    global resting, cnt
    resting = list(range(1, n + 1))
    heapify(resting)
    push_data(0,1,u)



def push_data(t, p, u):
    global cnt
    if u in waiting_url:
        return
    heappush(waiting_queue, (p, t, u))
    waiting_url.add(u)
    cnt += 1


def grading(start):
    global cnt
    temp = []
    while resting and waiting_queue:
        p, t, u= heappop(waiting_queue)
        domain, id = u.split("/")

        # 채점 될 수 없는 조건
        if domain in judging_domain:
            heappush(temp,(p,t,u))
            continue
        if domain in finished:
            s, gap = finished[domain]
            if s + 3*gap > start:
                heappush(temp, (p, t, u))
                continue

        waiting_url.remove(u)
        cnt -= 1
        jid = heappop(resting)
        judging_machine[jid] = (start,domain)
        judging_domain.add(domain)
        break

    # 못한 task는 다시 담기
    for x in temp:
        heappush(waiting_queue,x)


def finish(t, jid):
    if jid not in judging_machine:
        return
    s,domain = judging_machine.pop(jid)
    judging_domain.remove(domain)
    finished[domain] = (s,t-s)
    heappush(resting, jid)


def search(t):
    print(cnt)


for _ in range(q):
    task, *data = input().split()
    if task == "100":
        ready(int(data[0]),data[1])
    elif task == "200":
        push_data(int(data[0]),int(data[1]),data[2])
    elif task == "300":
        grading(int(data[0]))
    elif task == "400":
        finish(int(data[0]),int(data[1]))
    elif task == "500":
        search(int(data[0]))
    # 
    # print(resting)
    # print(waiting_queue)
    # print(judging_machine)
    # print(finished)
    # print()