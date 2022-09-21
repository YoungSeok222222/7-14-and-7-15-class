# 민코딩 LV.37
# 1번 바이러스
from collections import deque

N = int(input())
y1,x1,y2,x2 = map(int,input().split())
lst = [[0]*N for _ in range(N)]
lst[y1][x1] = 1
lst[y2][x2] = 1

q = deque()
q.append([y1,x1]), q.append([y2,x2])

move = [[-1,0],[1,0],[0,-1],[0,1]]
while q:
    yy,xx = q.popleft()
    for i in range(4):
        dy,dx = yy+move[i][0], xx+move[i][1]
        if 0<=dy<N and 0<=dx<N and lst[dy][dx]==0:
            q.append([dy,dx])
            lst[dy][dx] = lst[yy][xx]+1
for i in lst:
    print(*i,sep='')

# 2번 BBQ 장작 
from collections import deque
N,M = map(int,input().split())
lst = [list(map(int,input().split())) for _ in range(N)]
y,x = map(int,input().split())

q = deque()
lst[y][x] = 0
q.append([y,x])
move = [[-1,0],[1,0],[0,-1],[0,1]]
used = [[0]*N for _ in range(N)]
used[y][x] = 1

while q:
    y,x = q.popleft()
    for i in range(4):
        dy,dx = y+move[i][0], x+move[i][1]
        if 0<=dy<N and 0<=dx<N and lst[dy][dx]==0 and used[dy][dx]==0:
            used[dy][dx] = 1
            q.append([dy,dx])
            lst[dy][dx] = lst[y][x] + 1
Max = 0
for i in range(N):
    for j in range(N):
        Max = max(Max,lst[i][j])
print(Max)


# 3번 폭죽놀이
from collections import deque
lst = [list(map(int,input().split())) for _ in range(4)]
move = [[-1,0],[-1,1],[0,1],[1,1],[1,0],[1,-1],[0,-1],[-1,-1]]
q = deque()

for i in range(4):
    for j in range(5):
        if lst[i][j]==1:
            q.append([i,j,0])
while q:
    y,x,lv = q.popleft()
    for i in range(8):
        dy,dx = y+move[i][0], x+move[i][1]
        if 0<=dy<4 and 0<=dx<5 and lst[dy][dx]==0:
            q.append([dy,dx,lv+1])
            lst[dy][dx] = 1
print(lv)



# 4번 무인도의 크기
from collections import deque
lst = [list(map(int,input().split())) for _ in range(4)]
move = [[-1,0],[1,0],[0,-1],[0,1]]
used = [[0]*4 for _ in range(4)]
def bfs(y,x):
    size = 1
    q = deque()
    q.append([y,x])
    while q:
        y,x = q.popleft()
        for i in range(4):
            dy,dx = y+move[i][0], x+move[i][1]
            if 0<=dy<4 and 0<=dx<4 and lst[dy][dx] ==1 and used[dy][dx]==0:
                q.append([dy,dx])
                used[dy][dx] = 1
                size += 1
    print(size)
used[0][0] = 1
bfs(0,0)


# 5번 BFS로 미로찾기
from collections import deque
lst = [
    [0,0,0,0],
    [1,1,0,1],
    [0,0,0,0],
    [1,0,1,0]
]
move = [[-1,0],[1,0],[0,-1],[0,1]]
def bfs(st_y,st_x,ed_y,ed_x):
    q = deque()
    q.append([st_y,st_x,0])
    while q:
        y,x,lv = q.popleft()
        if y==ed_y and x==ed_x:
            print(f"{lv}회")
            break
        for i in range(4):
            dy,dx =y+move[i][0], x+move[i][1]
            if 0<=dy<4 and 0<=dx<4 and lst[dy][dx]==0 and used[dy][dx]==0:
                q.append([dy,dx,lv+1])
                used[dy][dx] = 1

arr = [list(map(int,input().split())) for _ in range(2)]
used = [[0]*4 for _ in range(4)]
used[arr[0][0]][arr[0][1]] = 1
bfs(arr[0][0],arr[0][1],arr[1][0],arr[1][1])


# 6번 고기가 좋아
from collections import deque
lst = [list(map(int,input().split())) for _ in range(4)]
move = [[-1,0],[1,0],[0,-1],[0,1]]
q = deque()
q.append([0,0])
used = [[0]*6 for _ in range(4)]
used[0][0] = 1
cnt = 0
while q:
    y,x = q.popleft()
    for i in range(4):
        dy,dx = y+move[i][0], x+move[i][1]
        if 0<=dy<4 and 0<=dx<6 and used[dy][dx]==0 and lst[dy][dx]!=1:
            if lst[dy][dx]==2: cnt += 1
            q.append([dy,dx])
            used[dy][dx] = 1
print(cnt)


# 7번 친구만나러 가는길
from collections import deque
N,M = map(int,input().split())
lst = [list(input().split()) for _ in range(N)]
move = [[-1,0],[1,0],[0,-1],[0,1]]

def bfs(st_y,st_x,ed_y,ed_x):
    used = [[0]*M for _ in range(N)]
    q = deque()
    q.append([st_y,st_x,0])
    used[st_y][st_x] = 1
    while q:
        y,x,lv = q.popleft()
        if y==ed_y and x==ed_x:
            return lv
            
        for i in range(4):
            dy,dx = y+move[i][0],x+move[i][1]
            if 0<=dy<N and 0<=dx<M and used[dy][dx]==0 and lst[dy][dx]!='x':
                q.append([dy,dx,lv+1])
                used[dy][dx] = 1
sy,sx = 0,0
dy,dx = 0,0
cy,cx = 0,0
for i in range(N):
    for j in range(M):
        if lst[i][j]=='S':
            sy,sx = i,j
        elif lst[i][j]=='D':
            dy,dx = i,j
        elif lst[i][j]=='C':
            cy,cx = i,j
answer = bfs(sy,sx,cy,cx) + bfs(cy,cx,dy,dx)
print(answer)


# 8번 섬 찾아 삼만리
from collections import deque
N,M = map(int,input().split())
lst = [list(map(int,input().split())) for _ in range(N)]
move = [[-1,0],[1,0],[0,-1],[0,1]]
used = [[True]*M for _ in range(N)]
def bfs(y,x):
    q = deque()
    q.append([y,x])
    used[y][x] = False
    while q:
        yy,xx = q.popleft()
        for i in range(4):
            dy,dx = yy+move[i][0], xx+move[i][1]
            if 0<=dy<N and 0<=dx<M and used[dy][dx]==True and lst[dy][dx]==1:
                q.append([dy,dx])
                used[dy][dx] = False

cnt = 0
for i in range(N):
    for j in range(M):
        if lst[i][j]==1 and used[i][j]:
            bfs(i,j)
            cnt += 1
print(cnt)
