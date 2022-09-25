# SWEA 추가 list 추가문제

# 13893 주사위
N, M, x,y,K = map(int,input().split())
Map = [list(map(int,input().split())) for _ in range(N)]
orders = list(map(int,input().split()))
dice = [0,0,0,0,0,0] # 위0 / 아래1 / 정면2 / 후면3 / 좌4 / 우5
move = [[0,1],[0,-1],[-1,0],[1,0]]  # 동 서 북 남
for i in orders:
    # 명령 대로 굴려~
    dy,dx = y+move[i-1][0],x+move[i-1][1]
    if dy<0 or dx<0 or dy>=N or dx>=M: continue

    if i==1:
        dice[0],dice[5],dice[4],dice[1] = dice[4],dice[0],dice[1],dice[5]
    if i==2:
        dice[0],dice[4],dice[5],dice[1] = dice[5],dice[0],dice[1],dice[4]
    if i==3:
        dice[0],dice[1],dice[2],dice[3] = dice[3],dice[2],dice[0],dice[1]
    if i==4:
        dice[0],dice[1],dice[2],dice[3] = dice[2],dice[3],dice[1],dice[0]
    
    if Map[dy][dx] ==0:         # 지도 좌표가 0이면 주사위 값 넣기
        Map[dy][dx] = dice[1]
    else:                       # 지도 좌표 0 아니면 지도 좌표값을 주사위에 넣기
        dice[1] = Map[dy][dx]
        Map[dy][dx] = 0
    y,x = dy,dx                 # 현 좌표 갱신
    print(dice[0])


# 13748 진기의 최고급 붕어빵
T = int(input())
for tc in range(1,T+1):
    _,m,k = map(int,input().split())
    cs_sec = list(map(int,input().split()))
    bucket = [0]*11112
    for c in cs_sec:
        bucket[c] += 1
    for i in range(1,len(bucket)):
        bucket[i] += bucket[i-1]
    flag = 1
    for sec in cs_sec:
        num = bucket[sec] # sec에 해당하는 손님
        stock = (sec//m) * k
        if num>stock:
            flag = 0
            break
    if flag:
        print(f"#{tc} Possible")
    else:
        print(f"#{tc} Impossible")
    
# 1979 어디에 단어가 들어갈 수 있을까
def find(i):
    cnt,result  = 0,0
    for j in range(N):
        if lst[i][j]==1: cnt+= 1
        if lst[i][j] ==0: 
            if cnt==K: 
                result += 1
            cnt = 0
    if cnt==K: result += 1

    cnt = 0
    for j in range(N):
        if lst[j][i]==1: cnt +=1
        if lst[j][i]==0: 
            if cnt==K:
                result += 1
            cnt = 0
    if cnt==K: result += 1
    return result

T = int(input())
for tc in range(1,T+1):
    ret = 0
    N,K = map(int,input().split())
    lst = [list(map(int,input().split())) for _ in range(N)]
    for i in range(N):
        ret += find(i)
    print(f"#{tc} {ret}")

# 1210 Ladder1
for tc in range(1,11):
    n = int(input())
    lst = [list(map(int,input().split())) for _ in range(100)]
    print(f"#{tc}",end=' ')

    for i in range(100):
        if lst[99][i]==2:
            y,x = 99,i

    idx = 0
    move = [[0,-1],[0,1],[-1,0]]
    visit = [[0]*100 for _ in range(100)]
    while y!=0:
        for j in range(3):
            dy,dx = y+move[j][0],x+move[j][1]
            if 0<=dy<100 and 0<=dx<100 and lst[dy][dx]==1 and visit[dy][dx]==0:
                lst[dy][dx] = 3
                visit[y][x] = 1
                y,x = dy,dx
                break
    print(dx)