# 1번 더블 리모콘
from collections import deque
S = int(input())            # 시작 채널
D = int(input())            # 목표 채널

def bfs(st):
    q = deque()
    q.append([st,0])        # 시작 채널과 cnt를 q에 추가
    
    while q:
        n,cnt = q.popleft()
        if n ==D:           # 만약 다음 채널이 목표채널과 같다면 출력하고 return
            print(cnt)
            return 
        if  0 <= n//2 <= 1000000 and visit[n//2]==0:    # 특정 연산하고 visit 배열도 연산값의 좌표에 1표시
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

visit = [0] * 1000001           # visit도 십만개 +1를 만들어서 각 채널 갈때마다 1로 표시
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
            if 0<=dy<4 and 0<=dx<9 and used[dy][dx] ==0 and lst[dy][dx]==n: # 범위이내고, used가 0이고, 값이 동일한 벌이면
                q.append([dy,dx])
                used[dy][dx] = 1                                            # used를 1로
                size += n                                                   # 사이즈 = 벌들의 숫자값 더하기
                cnt += 1                                                    # 군락의 크기 + 1
    return [n,cnt,size]                                                     # 탐색 끝나면 벌 번호, 군락 크기, 벌들의 합 return

used = [[0]*9 for _ in range(4)]
result = []
for i in range(4):
    for j in range(9):
        if lst[i][j] !=0 and used[i][j]==0:     # 0이 아니라 벌의 숫자고, visit배열(한 번들어가서 군락의 크기를 탐색한 곳은 안하려구)
            used[i][j],cnt = 1,1                # 시작 좌표 1, 갯수 1
            result.append(bfs(i,j,lst[i][j]))   # return 받은 벌 번호, 군락 크기, 벌들의 합 배열에 추가 
          
result.sort(key=lambda x: -x[1])                # 배열을 군락의 크기 순으로 내림차순 정렬
print(result[0][2])                             # 가장 큰 군락의 벌들의 합 출력

# 3번 해물새우파전
from collections import deque
lst = [list(map(int,input())) for _ in range(7)]
move = [[-1,0],[1,0],[0,-1],[0,1]]
flag = 1

def bfs(y,x,num):                                   # 좌표 + 해산물 번호
    global flag
    q = deque()
    q.append([y,x,0])
    visit = [[0]*7 for _ in range(7)]               
    visit[y][x] = 1
    while q:
        y,x,cnt = q.popleft()               
        if num==1 and 0<cnt<3 and lst[y][x]==1:     # 만약 다음 탐색 좌표값이 1(타이거 새우)이고 해산물 번호가 1, 범위가 3칸 이내면
            flag = 0                                # flag를 0으로 해서 False로 갱신하고 return
            return 
        elif num==2 and 0<cnt<4 and lst[y][x]==2:   # 만약 다음 탐색 좌표값이 2(오징어)고, 해산물 번호 2, 범위가 4칸이내면
            flag = 0                                # flag를 0으로 해서 False로 갱신하고 return
            return
        for i in range(4):
            dy,dx = y+move[i][0], x+move[i][1]
            if 0<=dy<7 and 0<=dx<7 and visit[dy][dx]==0: # 탐색 좌표가 범위이내고, visit가 0이면 무조건 탐색
                q.append([dy,dx,cnt+1])
                visit[dy][dx] = 1                        # visit를 1로

for i in range(7):
    for j in range(7):
        if lst[i][j]==1:            # 타이거 새우 찾으면 bfs 진입
            bfs(i,j,lst[i][j])
        elif lst[i][j]==2:          # 오징어 찾으면 bfs 진입
            bfs(i,j,lst[i][j])  

if flag:
    print("pass")
else:
    print("fail")

# 4번 천지창조
from collections import deque
lst = [list(input()) for _ in range(8)]
move = [[-1,0],[1,0],[0,-1],[0,1]]
def bfs(y,x,f):
    q = deque()
    q.append([y,x,0])
    visit = [[0]*9 for _ in range(8)]           # visit는 처음이나 2번쨰로 들어올 때마다 갱신
    visit[y][x] = 1                             # 들어가서 vist 표시
    if flag==0:                                 # 처음 탐색할때는 flag가 0이므로 처음 들어온 좌표를 3으로 표시
        lst[y][x] = 3
    while q:
        y,x,cnt = q.popleft()
        if  visit[y][x]==0 and lst[y][x]==3:    # 두번째 들어왔을 때 사용
            return cnt
            
        for i in range(4):
            dy,dx = y+move[i][0], x+move[i][1]
            if f==0:                            # flag가 0이므로 처음 탐색했을 떄 
                if 0<=dy<8 and 0<=dx<9 and lst[dy][dx]=="#":    # 범위 이내거나 #이면
                    lst[dy][dx] = 3                             # #을 3으로 바꾸고
                    visit[dy][dx] = 1                           # visit 표시하고
                    q.append([dy,dx,cnt+1])                     # 큐에 추가
            else:                               # flag가 1일떄 즉, 두번쨰 탐색할 떄
                if 0<=dy<8 and 0<=dx<9 and visit[dy][dx]==0:    # 좌표가 범위 이내, visit가 0
                    q.append([dy,dx,cnt+1])                     # 큐에 추가
                    if  visit[dy][dx]==0 and lst[dy][dx]==3:    # visit가 0이고 만약 탐색 좌표가 3이면
                        return cnt                              # 탐색 횟수 반환
                    visit[dy][dx] = 1                           # 아니라면 visit 배열 1표시
result = []
flag = 0                            # 처음 #을 탐색할 때는 flag를 0으로, 그 다음 #을 탐색할 때는 1로                                  
for i in range(8):
    for j in range(9):
        if lst[i][j]=="#":          # 맨 처음 #을 찾으면 
            result.append(bfs(i,j,flag))    # BFS로 탐색 시작
            flag = 1
result.pop(0)      
print(min(result))

# 5번 안나와 엘사

# 6번 BFS 배달맨
from collections import deque
n,m = map(int,input().split())
lst = [list(input()) for _ in range(n)]
move = [[-1,0],[1,0],[0,-1],[0,1]]      # 상하좌우
def bfs(y,x):               
    answer = []                         # 각 번호로 가는데 몇 번 걸리는지 담을 리스트
    visit = [[0]*m for _ in range(n)]
    visit[0][0] = 1                     # 처음 들어가서 visit 0,0을 1로 표시
    q = deque()
    q.append([y,x,0])                   # 처음 좌표 0,0이랑 cnt 추가
    target = 1                          # BFS 배달맨이 배달 시작할 넘버 1

    while q:
        y,x,cnt = q.popleft()           
        if lst[y][x]==target:           # 만약 다음에 탐색할 y,x가 타겟넘버와 같다면
            answer.append(cnt)          # 몇 번만에 갔는지 리스트에 추가
            visit = [[0]*m for _ in range(n)]   # 다음 넘버로 탐색하기 위해 지금까지 표시했던 visit배열 초기화
            target += 1                         
            cnt = 0                     # 횟수 초기화
            q = deque()                 # 큐 초기화
        
        for i in range(4):          
            dy,dx = y+move[i][0], x+move[i][1]
            if 0<=dy<n and 0<=dx<m and visit[dy][dx]==0 and lst[dy][dx]!="#":   # 만약 범위내에 있고, visit가 0이고, #이 아니라면
                q.append([dy,dx,cnt+1])                                         # 큐에 좌표와 cnt+1 추가
                visit[dy][dx] = 1                               
    return answer

for i in range(n):
    for j in range(m):      # 탐색해서 #이 아니면 먼저 정수로 변환
        if lst[i][j] !="#":
            lst[i][j] = int(lst[i][j])
answer = bfs(0,0)           # BFS 배달맨은 0,0 에서부터 시작
print(f"{sum(answer)}회")