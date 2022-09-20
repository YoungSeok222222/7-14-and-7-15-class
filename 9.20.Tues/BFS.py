# 돼지가 0,0에서 사료 3,0을 거쳐서 3,4로 가기
from collections import deque
arr = [
    [0,0,0,1,1],
    [1,0,0,1,0],
    [1,0,0,0,0],
    [0,0,0,0,0]
]
directy,directx = [-1,1,0,0], [0,0,-1,1]
answer = 0
def bfs(st_y,st_x,ed_y,ed_x):
    q = deque()
    q.append([st_y,st_x,0])
    used = [[False]*5 for _ in range(4)]
    used[st_y][st_x] = True
    while q:
        y,x,lv = q.popleft()
        if y==ed_y and x==ed_x:
            return lv
        for i in range(4):
            dy,dx = y+directy[i], x+directx[i]
            if 0<=dy<4 and 0<=dx<5 and used[dy][dx]==False and arr[dy][dx] ==0:
                q.append([dy,dx,lv+1])

answer = bfs(0,0,3,0) + bfs(3,0,3,4)
print(answer)


# 섬의 갯수 구하기
'''
5
0 0 1 0 0
0 0 1 0 0
0 1 1 1 0
0 0 1 0 0
0 0 0 0 0
'''
n = int(input())
lst = [list(map(int,input().split())) for _ in range(n)]
directy, directx = [-1,1,0,0], [0,0,-1,1]
cnt,Max,Min = 0,-21e8, 21e8
def bfs(y,x):
    q = deque()
    q.append([y,x])
    used = [[False]*5 for _ in range(5)]
    used[y][x] = True
    while q:
        yy,xx = q.popleft()
        for i in range(4):
            dy,dx = yy+directy[i], xx+directx[i]
            if 0<=dy<5 and 0<=dx<5 and used[dy][dx] ==False and lst[dy][dx] == 1:
                used[dy][dx] = True
                q.append([dy,dx])
                

for i in range(n):
    for j in range(n):
        if lst[i][j] ==1:
            cnt += 1
            bfs(i,j)
print(cnt)



# 섬 갯수 / 최대 섬의 갯수 / 최소 섬의 갯수
'''
5
1 0 1 0 0
0 0 1 0 0
0 1 1 1 0
0 0 1 0 0
1 1 0 1 1
'''
n = int(input())
lst = [list(map(int,input().split())) for _ in range(n)]
directy, directx = [-1,1,0,0], [0,0,-1,1]
cnt,Max,Min = 0,-21e8, 21e8
island = []
used = [[False]*5 for _ in range(5)]
def bfs(y,x):
    global Max, Min,cnt,island
    size = 1
    q = deque()
    q.append([y,x])
    used[y][x] = True
    while q:
        yy,xx = q.popleft()
        for i in range(4):
            dy,dx = yy+directy[i], xx+directx[i]
            if 0<=dy<5 and 0<=dx<5 and used[dy][dx] ==False and lst[dy][dx] == 1:
                cnt += 1
                used[dy][dx] = True
                q.append([dy,dx])
                size += 1
        
        Max = max(Max,size)
        Min = min(Min,size)
    island.append(size)     

for i in range(n):
    for j in range(n):
        if lst[i][j] ==1 and used[i][j]==False:
            bfs(i,j)
            
            
  
print(f"섬의 개수: {len(island)},\n최대 크기의 섬: {max(island)},\n최소 크기의 섬: {min(island)}")

# 교수님 코드
def bfs(y, x):
    global visited
    q = deque()
    q.append([y, x])
    size = 0
    while q:
        size += 1 # 섬 크기 size+1
        now = q.popleft()
        y, x = now
        dy = [0,1,0,-1]
        dx = [1,0,-1,0]
        for i in range(4):
            ny, nx = y+dy[i], x+dx[i]
            if ny > N-1 or nx > N-1 or ny< 0 or nx < 0: continue 
            if visited[ny][nx] == 1: continue
            if arr[ny][nx]==0: continue
            visited[ny][nx] = 1
            q.append([ny, nx])
    return size



arr = [ # 1: 섬 | 0: 바다
    [0,0,1,0,0],
    [0,0,1,0,0],
    [0,1,1,1,0],
    [0,0,1,0,0],
    [1,0,0,0,1],
]
N = len(arr) # int(input())

cnt = 0
visited = [[0]*N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if arr[i][j]==1 and visited[i][j]==0:
            visited[i][j] = 1   # 중복체크 해주고
            cnt+=1 # 섬의 갯수 +1
            print(f'{cnt}번 째 섬 크기 : {bfs(i, j)}')
print(f'섬의 총 갯수 : {cnt}')



# 0,0의 탱크를 가지고 왕자(3,5) 구출하기  
from collections import deque
import copy
N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

def bfs():
    visited = [[0] * M for _ in range(N)]
    visited[0][0]=1

    q=deque()
    q.append((0,0,0))  # y x level->몇칸이동하는지..

    while q:
        nowy,nowx,nowlevel=q.popleft()

        if nowy==3 and nowx==5:
            return nowlevel

        directy=[-1,1,0,0]
        directx=[0,0,-1,1]

        for i in range(4):
            dy=nowy+directy[i]
            dx=nowx+directx[i]
            # 배열범위
            if 0<=dy<N and 0<=dx<M:
                if graph[dy][dx]==1: continue # 벽 못감
                if visited[dy][dx]==1: continue # 방문했던곳
                visited[dy][dx]=1
                q.append((dy,dx,nowlevel+1))
    return 100

def sett():
    for i in range(N):
        for j in range(M):
            if graph[i][j]==1: #벽이라면
                wall.append((i,j))

wall=[]
sett()  # 벽 좌표 저장하고 시작
Min=21e8

backup=copy.deepcopy(graph) # 원상복구 할 배열 복사해 놓기

for i in range(len(wall)):
    for j in range(i+1,len(wall)): # for문 돌면서 허물 벽 2개를 선택
        graph = copy.deepcopy(backup) # 원상복구
        graph[wall[i][0]][wall[i][1]]=0 # 벽 허물기 1
        graph[wall[j][0]][wall[j][1]]=0 # 벽 허물기 2
        ret=bfs()
        Min=min(ret,Min)
print(Min)


##############################################################################

from collections import deque

# 4 6
# 0 0 1 1 1 1
# 0 0 1 0 0 1
# 0 0 1 0 0 1
# 0 1 1 1 1 0

# 최대 2번 벽 뚫기 가능

N, M = 4, 6

graph = [
    [0, 0, 1, 1, 1, 1],
    [0, 0, 1, 0, 0, 1],
    [0, 0, 1, 0, 0, 1],
    [0, 1, 1, 1, 1, 0]
]

moves = [
    [1, 0],
    [0, 1],
    [-1, 0],
    [0, -1]
]

# 시작점과 도착점 정의
starty, startx = 0, 0
desty, destx = N - 1, M - 1

queue = deque()

# 시작 좌표, count(움직임 횟수), 벽 뚫기 기회
queue.append((starty, startx, 0, 2))

# 중복 방문을 피하기 위한 visited 배열
visited = [[0] * M for _ in range(N)]

# 시작 좌표 방문처리
visited[starty][startx] = True

while queue:
    # 현재 위치 x, y, 현재까지 이동한 거리 count, 벽을 뚫을 남은 기회
    yy, xx, level, break_wall = queue.popleft()

    # 도착점에 도달하면 count 프린트 후 break
    if yy == desty and xx == destx:
        print(level)
        break

    # 4가지 이동 방식을 통해 이동할 위치 업데이트
    for i in range(4):
        dy, dx = moves[i][0] + yy, moves[i][1] + xx

        # 이동할 위치가 범위 내에 있고, 방문하지 않았을 때
        if 0 <= dy < N and 0 <= dx < M:
            if not visited[dy][dx]:
                # graph[dy][dx]가 0이면 바로 이동  -> 벽이 아닐경우
                if graph[dy][dx] == 0:
                    visited[dy][dx] = 1
                    queue.append((dy, dx, level + 1, break_wall))

                # graph[dy][dx]가 1일 때 -> 벽일경우
                else:
                    # 만약 벽을 뚫을 기회가 남아있다면 뚫고 가도록 하기 + 남은 벽 뚫기 기회 업데이트 해주기
                    if break_wall > 0:
                        visited[dy][dx] = 1
                        queue.append((dy, dx, level + 1, break_wall - 1))
