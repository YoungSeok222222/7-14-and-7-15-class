# 1번 더블 리모콘
from collections import deque
S = int(input())
D = int(input())

def bfs(st):
    q = deque()
    q.append([st,0])
    
    while q:
        n,cnt = q.popleft()
        if n ==D:
            print(cnt)
            return 
        if  0 <= n//2 <= 1000000 and visit[n//2]==0:
            visit[n//2] = 1 
            q.append([n//2,cnt+1])
        if 0 <= n*2 <= 1000000 and visit[n*2]==0:
            visit[n*2] = 1
            q.append([n*2,cnt+1])
        if 0 <= n+1 <= 1000000 and visit[n+1]==0:
            visit[n+1] = 1
            q.append([n+1,cnt+1])
        if 0 <= n-1 <= 1000000 and visit[n-1]==0:
            visit[n-1] = 1    
            q.append([n-1,cnt+1])

visit = [0] * 1000001
visit[S] = 1
bfs(S)

# 2번 여왕벌의 알집
from collections import deque
lst = [list(map(int,input().split()))for _ in range(4)]
move = [[-1,0],[1,0],[0,-1],[0,1]]


def bfs(y,x,n):
    global cnt
    
    q = deque()
    q.append([y,x])
    size = n
    while q:
        y,x = q.popleft()
        for i in range(4):
            dy,dx = y+move[i][0], x+move[i][1] 
            if 0<=dy<4 and 0<=dx<9 and used[dy][dx] ==0 and lst[dy][dx]==n:
                q.append([dy,dx])
                used[dy][dx] = 1
                size += n
                cnt += 1
    return [n,cnt,size]

used = [[0]*9 for _ in range(4)]
result = []
for i in range(4):
    for j in range(9):
        if lst[i][j] !=0 and used[i][j]==0:
            used[i][j],cnt = 1,1
            result.append(bfs(i,j,lst[i][j]))
          
result.sort(key=lambda x: -x[1])
print(result[0][2])

# 3번 해물새우파전
from collections import deque
lst = [list(map(int,input())) for _ in range(7)]
move = [[-1,0],[1,0],[0,-1],[0,1]]
flag = 1

def bfs(y,x,num):
    global flag
    q = deque()
    q.append([y,x,0])
    visit = [[0]*7 for _ in range(7)]
    visit[y][x] = 1
    while q:
        y,x,cnt = q.popleft()
        if num==3 and 0<cnt<3 and lst[y][x]==1:
            flag = 0
            return 
        elif num==2 and 0<cnt<4 and lst[y][x]==2:
            flag = 0
            return
        for i in range(4):
            dy,dx = y+move[i][0], x+move[i][1]
            if 0<=dy<7 and 0<=dx<7 and visit[dy][dx]==0:
                q.append([dy,dx,cnt+1])
                visit[dy][dx] = 1


for i in range(7):
    for j in range(7):
        if lst[i][j]==1:
            bfs(i,j,lst[i][j])
        elif lst[i][j]==2:
            bfs(i,j,lst[i][j])

if flag:
    print("pass")
else:
    print("fail")

# 4번 천지창조

# 5번 안나와 엘사

# 6번 BFS 배달맨