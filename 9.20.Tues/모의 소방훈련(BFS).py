from collections import deque
N = int(input())
lst = [list(input()) for _ in range(N)]
y,x = map(int,input().split())
move = [[-1,0],[1,0],[0,-1],[0,1]]             # 상하좌우

def bfs(st_y,st_x,ed_y,ed_x):                  # 시작좌표 y,x / 도착좌표 y,x
    check = [[0]*N for _ in range(N)]          # bfs안에 경로 체크할 check 생성(들어올때마다 새로 갱신)
    check[st_y][st_x] = 1                      
    q = deque()
    q.append([st_y,st_x,0])

    while q:
        yy,xx,lv = q.popleft()
        if yy==ed_y and xx==ed_x:              # 만약 q에서 꺼낸 좌표가 목적지 좌표라면 lv 반환 
            return lv
        if lst[ed_y][ed_x] =='$':              # 만약 현재 가고 있는 도착지점이 불이라면
            for i in range(4):
                dy,dx = yy+move[i][0], xx+move[i][1]
                if 0<=dy<N and 0<=dx<N and check[dy][dx]==0 and lst[dy][dx]!='#':   # 벽 빼고 경로 탐색
                    q.append([dy,dx,lv+1])
                    check[dy][dx] = 1
        else:                                  # 만약 현재 가고 있는 도착지점이 소화기라면
            for i in range(4):
                dy,dx = yy+move[i][0], xx+move[i][1]
                if 0<=dy<N and 0<=dx<N and check[dy][dx]==0 and lst[dy][dx]!='#' and lst[dy][dx]!='$':  # 범위 이내의 벽과 불 빼고 q에 추가
                    q.append([dy,dx,lv+1])
                    check[dy][dx] = 1

fire_y,fire_x = 0,0
extinguisher = []                       # 소화기 좌표 받을 빈 리스트
for i in range(N):
    for j in range(N):
        if lst[i][j]=='A':              # 좌표가 소화기라면, 리스트에 추가
            extinguisher.append([i,j])
        elif lst[i][j]=='$':            # 불이라면 불y, 불x에 좌표 갱신
            fire_y,fire_x=i,j
Min = 21e8
answer = 0
for i in range(len(extinguisher)):      # 시작 좌표 -> 소화기 -> 불로 가는 경로들 중 최소값 구하기
    Min = min(Min,bfs(y,x,extinguisher[i][0],extinguisher[i][1]) + bfs(extinguisher[i][0],extinguisher[i][1],fire_y,fire_x))
print(Min)

'''
8
________
____A___
####____
__A#____
___#__A_
_#______
__###___
_$______
4 4

10
-------------------------
3
_$A
_#_
___
0 0

7
--------------------------
4
____
$##_
__#_
A__A
0 0

11

'''