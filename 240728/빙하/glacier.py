# from collections import deque

# n,m = map(int,input().split())
# arr = [list(map(int,input().split())) for _ in range(n)]
# # 1 = 빙하, 0 = 물
# total = 0
# for i in range(n):
#     for j in range(m):
#         if arr[i][j]:
#             total += 1

# dx = [0,0,-1,1]
# dy = [-1,1,0,0]

# def can_go(x,y):
#     return 0<=x<n and 0<=y<m

# def melted():
#     new = [[arr[i][j] for j in range(m)] for i in range(n)]
#     visited = [[0]*m for _ in range(n)]

#     q = deque()
#     q.append((0,0))
#     cnt = 0
#     while q:
#         x,y = q.popleft()

#         for i in range(4):
#             nx,ny = x+dx[i], y+dy[i]

#             if not can_go(nx,ny):
#                 continue
#             if visited[nx][ny]:
#                 continue
#             visited[nx][ny] = 1
            
#             if arr[nx][ny] == 1:
#                 new[nx][ny] = 0
#                 cnt += 1
#             else:
#                 q.append((nx,ny))
#     return cnt,new

# t = 0
# while total:
#     cnt,arr = melted()
#     t += 1
#     total -= cnt
#     if total == 0:
#         print(t,cnt)
#         break

# 빙하 문제는 바깥쪽에 있는 물에 빙하가 닿아 있으면 해당 빙하가 녹는다는 점이 포인트 입니다!
# 안쪽에 있는 물은 빙하에 영향을 미치지 않죠.
# 이 부분을 고민해보시면 좋을 것 같습니다.

import sys
inpu=sys.stdin.readline
#
n,m=map(int, inpu().split())
amap=[ list(map(int, inpu().split())) for _ in range(n)]
ones=[]
for i in range(n):
    for j in range(m):
        if amap[i][j]==1:
            ones.append([i,j])
visited=[[False]*m for _ in range(n)]
di=[0,0,-1,1]
dj=[1,-1,0,0]
from collections import deque



def bfs2(v):#인접0다가가기로 벽만날수있으면->1화  

    visited2=[[False]*m for _ in range(n)]
    visited2[v[0]][v[1]]=True
    aque2=deque([v]) #~ 이름v

    while(aque2):
        v2=aque2.popleft()
        # 출력
        
        for i in range(4):
            ni,nj=v2[0]+di[i],v2[1]+dj[i]#v2[0]+di[0],v2[1]+dj[1]
            if 0<=ni<n and 0<=nj<m and visited2[ni][nj]==False and amap[ni][nj]==0:
                aque2.append([ni,nj])  # aque2 # 2헷갈리니 아예이름이 다른게 낫
                visited2[ni][nj]=True #visited2
                
                if ni==1 or nj==1 or ni==n-2 or nj==m-2:
                    return True
    return False


def bfs(v):
    visited[v[0]][v[1]]=True
    aque=deque([v])
    # print(v)
    while(aque):
        w=aque.popleft()
        
        for i in range(4):
            ni,nj=w[0]+di[i],w[1]+dj[i] # i대신 0,1실화냐
            if 0<=ni<n and 0<=nj<m and visited[ni][nj]==False and amap[ni][nj]==0:
                if bfs2([ni,nj])==True:#인접0다가가기로 벽만날수있으면->1의 0화     
                    # 한번에 바껴야함 amap[v[0]][v[1]]=0
                    return True# 걍 자신이 변하는지 하나씩 볼거라. 어라 복잡하게 풀었네 걍 네곳 보면 되는데.(아마 초반에 1<->0변함관계잘못봐서)
    return False
              
alln=len(ones)
numb=0
another=[]
cnt=0
while(ones):#numb!=alln):# 다음초
    visited=[[False]*m for _ in range(n)]
    cnt+=1
    left=len(ones)

    post=0
    change=[]
    for i in range(len(ones)): 
        # 전체 검사
        i+=post
        if bfs(ones[i])==True: # True면 pop, 바뀔놈
            change.append(ones[i])

            ones.pop(i)
            post-=1

    for v in change :
        amap[v[0]][v[1]]=0

print(cnt,left )#~