# 11718 사냥꾼
def hunting(y,x):
    global cnt
    for i in range(8):                                        # 8방향
        for j in range(1,N):                                  # 한 방향씩 1부터 배열의 크기까지 뻗어나감
            dy,dx = y+move[i][0]*j,x+move[i][1]*j       
            if 0<=dy<N and 0<=dx<N:                             
                if lst[dy][dx]==3: break                      # 벽(3) 만나면 break하고 다음 방향
                elif lst[dy][dx]==2: cnt +=1                  # 토끼(1) 만나면 cnt += 1

move = [[-1,0],[-1,1],[0,1],[1,1],[1,0],[1,-1],[0,-1],[-1,-1]] # 8방향 탐색
T = int(input())
for tc in range(1,T+1):
    N = int(input())
    lst = [list(map(int,input().split())) for _ in range(N)]
    cnt = 0 
    for i in range(N):
        for j in range(N):
            if lst[i][j]==1:                            # 사냥꾼이면 함수로 보내기
                hunting(i,j)          
    print(f"#{tc} {cnt}")
#=====================================================================
# 11671 기지국 
def findhouse(y,x,chr):
    cnt = 0
    for i in range(1,chr+1):
        for j in range(4):
            dy,dx = y+move[j][0]*i, x+move[j][1]*i
            if 0<=dy<n and 0<=dx<n :
                if lst[dy][dx] =="H" and visit[dy][dx]==0: 
                    visit[dy][dx] = 1
                    cnt += 1
    return cnt
move = [[-1,0],[1,0],[0,-1],[0,1]]
T = int(input())
for tc in range(1,T+1):
    n = int(input())
    lst = [list(input()) for _ in range(n)]
    visit = [[0]*n for _ in range(n)]
    ret = 0
    for i in range(n):
        for j in range(n):
            if lst[i][j]=="H": ret += 1
     
    for i in range(n):
        for j in range(n):
            if lst[i][j]=="A":
                ret -= findhouse(i,j,1)
            elif lst[i][j]=="B":
                ret -= findhouse(i,j,2)
            elif lst[i][j]=="C":
                ret -= findhouse(i,j,3)
 
    print(f"#{tc} {ret}")

# 혜승이 풀이
def cover(y,x,k):
    dy = [-1,1,0,0]
    dx = [0,0,-1,1]
    for i in range(4):
        for j in range(1,k+1):
            ny = y + (dy[i] * j)
            nx = x + (dx[i] * j)
            if ny < 0 or nx < 0 or ny > N-1 or nx > N-1:continue
            if arr[ny][nx] == 'H':
                arr[ny][nx] = 'X'
 
T = int(input())
for testcase in range(1,T+1):
    dict1 = {'A':1,'B':2,'C':3}
    N = int(input())
    arr = [list(input()) for _ in range(N)]
    cnt = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] != 'H' and arr[i][j] != 'X':
                k = dict1[arr[i][j]]
                cover(i,j,k)
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 'H':
                cnt += 1
    print(f'#{testcase} {cnt}')
#======================================================================

# 11646 중력
T = int(input())
for tc in range(1,T+1):
    N = int(input())
    lst = list(map(int,input().split()))
    Max = 0                             # 우측 블록에 작은 값이 가장 많이 있는 블록이 결국 낙차가 가장 크다
    for i in range(N):
        cnt = 0
        for j in range(i+1,N):          
            if lst[i]>lst[j]:  cnt += 1 # 만약 기준 블록보다 우측 블록이 작다면 cnt += 1
        Max = max(Max,cnt)
        # print(Max)
    print(f"#{tc} {Max}")
    

# 6190 정곤이의 단조 증가하는 수
def danjo(gop):
    gop = str(gop)
    if len(gop)==1: return 1
    for i in range(len(gop)-1):
        if gop[i] > gop[i+1]: return 0
    else:
        return 1

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    lst = list(map(int,input().split()))
    Max = 0
    for i in range(N):
        for j in range(i+1,N):
            gop = lst[i] * lst[j]
            ret = danjo(gop)
            if ret:
                Max = max(Max,gop)
    if Max !=0: print(f"#{tc} {Max}")
    else: print(f"#{tc} -1")

# 2805 농작물 수확하기
T = int(input())
for tc in range(1,T+1):
    N = int(input())
    lst = [list(map(int,input())) for _ in range(N)]
    ans = 0
    md = N//2
    for y in range(md+1):
        for x in range(md-y,md+y+1):
            ans += lst[y][x] + lst[N-y-1][x]
    print(f"#{tc} {ans-sum(lst[md])}")
