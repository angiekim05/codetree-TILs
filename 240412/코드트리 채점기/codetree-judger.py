from heapq import heappop,heappush,heapify
from collections import defaultdict

waiting_url = defaultdict(set)
judging_domain = set()
waiting_queue = dict()
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
    domain, id = u.split("/")
    if domain in waiting_queue:
        heappush(waiting_queue[domain], (p, t, id))
    else:
        waiting_queue[domain] = [(p, t, id)]
    waiting_url[domain].add(id)
    cnt += 1


def grading(start):
    global cnt
    if not resting:
        return
    min_domain = 0
    min_data = (50001,0,0)
    for d in waiting_queue.keys():
        if d in judging_domain:
            continue
        if d in finished:
            s,gap = finished[d]
            if s+3*gap > start:
                continue
        if waiting_queue[d]:
            temp = waiting_queue[d][0]
            if temp < min_data:
                min_data = temp
                min_domain = d

    if min_domain:
        p,t,id = heappop(waiting_queue[min_domain])
        waiting_url[min_domain].remove(id)
        jid = heappop(resting)
        judging_machine[jid] = (start,min_domain)
        judging_domain.add(min_domain)
        cnt -= 1

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

    # print(resting)
    # print(waiting_queue)
    # print(judging_machine)
    # print(finished)
    # print(waiting_url)
    # print()