# 0,0의 탱크를 가지고 왕자(3,5) 구출하기 
from collections import deque

N,M = 4, 6
lst = [ # 4 6 
    [2,0,1,1,1,1],
    [0,0,1,0,0,1],
    [0,0,1,0,1,1],
    [0,0,1,0,1,0]
]
used = [[0]*6 for _ in range(4)]

move = [
    [-1,0],
    [1,0],
    [0,-1],
    [0,1]
]
# 시작점, 도착점 정의
st_y, st_x, ed_y, ed_x = 0, 0, 3, 5

# 큐에 시작점, 레벨, 총알 등록
q = deque()
q.append([st_y,st_x,0,2])

# used 배열에 시작점 등록
used[st_y][st_x] = True

while q:
    yy,xx,lv,bullet = q.popleft()
    print(yy,xx,lv,bullet)
    if yy==ed_y and xx==ed_x:
        print(lv)
        break
    for i in range(4):
        dy,dx = yy+move[i][0], xx+move[i][1]
        if 0<=dy<N and 0<=dx<M:
            if not used[dy][dx]:
                if lst[dy][dx]==0:
                    q.append([dy,dx,lv+1,bullet])
                    used[dy][dx] = 1
                else:
                    if bullet > 0:
                        used[dy][dx] = 1
                        q.append([dy,dx,lv+1,bullet-1])



        


