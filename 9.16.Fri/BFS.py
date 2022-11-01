from collections import deque

q = deque()  # 데크를 쓰면 왼쪽으로 append 하거나 왼쪽을 pop할 수도 있음

q.append(2)
q.append(3)
q.append(4)
q.append(5)

q.appendleft(9)
print(*q)


x= q.popleft()
print(x)
print(*q)
###################################

# BFS-1

arr = [
    [0,1,0,1,0,0], # A                  A
    [0,0,1,0,1,0], # B              B      D
    [0,0,0,0,0,0], # C            C   E   f
    [0,0,0,0,0,1], # D
    [0,0,0,0,0,0], # E 
    [0,0,0,0,0,0], # F

]
name=list(input().split())
answer=[]

def bfs(st):
    global answer
    queue=deque()
    queue.append(st)
    while queue:
        now = queue.popleft()
        answer.append(name[now])
        for i in range(6):
            if arr[now][i]==1:
                queue.append(i)

bfs(0)
print(*answer)

# BFS-2
name=list(input().split()) #A B C D
arr=[
    [0,1,1,0],
    [0,0,1,1],
    [0,1,0,1],
    [0,0,0,0],
]
used=[0]*4
answer=[]
def bfs(st):
    global answer
    q=deque()
    q.append(st)
    while q:
        now=q.popleft()
        answer.append(name[now])
        for i in range(4):
            if arr[now][i]==1:
                if used[i]==0:
                    used[i]=1
                    q.append(i)


used[1]=1 # 시작 index에 1체크
bfs(1) # 시작 index 적고 시작
print(*answer)


# BFS - Flood fill
n = int(input())
arr = [[0] * n for _ in range(n)]
y,x = map(int,input().split())

arr[y][x] = 1
q = deque()
q.append([y,x])

while q:
    directy,directx = [-1,1,0,0], [0,0,-1,1]
    y,x = q.popleft()
    if arr[0][0] !=0:
        print(f"{arr[0][0]-1}일 후")
        break
    for i in range(4):
        dy,dx = directy[i] + y, directx[i] + x
        if 0<=dy<n and 0<=dx<n:
            if arr[dy][dx] == 0:
                q.append([dy,dx])
                arr[dy][dx] = arr[y][x] +1 



###################################
# 교수님 풀이법
n=int(input()) # map 사이즈 입력
y,x=map(int,input().split()) # 시작점 입력
arr=[[0]*n for _ in range(n)]

arr[y][x]=1
q=deque()
q.append((y,x,0))

answer=0
while q:
    y,x,level=q.popleft()
    # if y==0 and x==0: answer=level
    directy=[0,0,1,-1]
    directx=[1,-1,0,0]
    for i in range(4):
        dy=y+directy[i]
        dx=x+directx[i]
        if 0<=dy<n and 0<=dx<n:
            if arr[dy][dx]==0:
                arr[dy][dx]=arr[y][x]+1
                q.append((dy,dx,level+1))
                # if dy==0 and dx==0:
                #     answer=level+1
for i in arr:
    print(*i)
print(answer)


# BFS - blooming flower
# 전체 화단에 씨앗이 만개하기까지 몇 일이 걸리는가
n = int(input())
seed = [list(map(int,input().split())) for _ in range(2)]
arr = [[0] * n for _ in range(n)]
q = deque()

for i in seed:
    arr[i[0]][i[1]] = 1
    q.append([i[0],i[1]])



while q:
    directy,directx = [-1,1,0,0], [0,0,-1,1]
    y,x = q.popleft()

    for i in range(4):
       dy,dx = directy[i] + y, directx[i] + x
       if 0<=dy<n and 0<=dx<n and arr[dy][dx] ==0:
        arr[dy][dx] = arr[y][x] + 1
        q.append([dy,dx])


Max = -21e8
for i in range(n):
    for j in range(n):
        if Max < arr[i][j]:
            Max = arr[i][j]
print(Max)   
         

###
# 교수님 풀이 
n = int(input()) # 배열 크기입력
flower = list(map(int, input().split())) # 좌표 입력
y1, x1 = flower[0], flower[1]
y2, x2 = flower[2], flower[3]
flower = [(y1, x1,1), (y2, x2,1)]
arr = [[0] * n for _ in range(n)]  # 화단 선언

answer=0

def bfs(flower):
    global n, arr,answer
    q=deque(flower)

    while q:
        nowy,nowx,level=q.popleft()

        arr[nowy][nowx]=level
        answer=level

        directy=[-1,1,0,0]
        directx=[0,0,-1,1]

        for i in range(4):
            dy=nowy+directy[i]
            dx=nowx+directx[i]
            if not(0<=dy<n and 0<=dx<n):continue # 배열범위
            if arr[dy][dx]!=0: continue # 이미 꽃이 심어진곳 안됨
            arr[dy][dx]=arr[nowy][nowx]+1 # 화단에 표시해주기
            q.append((dy,dx,level+1)) # 큐에 푸쉬하기

bfs(flower)

for row in arr:
    print(*row,sep="")
print(answer)










