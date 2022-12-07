# 10807 개수 세기(1차원 배열)
n = int(input())
ar = list(map(int,input().split()))
t = int(input())

print(ar.count(t))
#===============================================

# 2869 달팽이는 올라가고 싶다(기본수학1)
A,B,V = map(int,input().split())
d = (V-B) / (A-B)  # 걸리는 일수 = 올라가야하는 높이 / 하루동안 등반하는(낮에 올라갔다 밤에 내려오는) 높이

# 만약 걸리는 일수가 소수점이 안 나오면(딱 맞아 떨어지면 그대로 출력 / 아니면 4.2일 같은 날은 1일이 더 걸리므로 +1)
print((int(d) if int(d) == d else int(d)+1)) 

#===============================================

# 2789 블랙잭(브루트포스)
N, M  = map(int,input().split())
ar = list(map(int,input().split()))
Max = 0
# 3장 뽑아야 하기 때문에 3중 for문 사용
 
# 인덱스 범위를 첫번째 for문의 범위를 N-2까지 즉, [5, 6, 7, 8, 9] 총 5장인 경우 2번 인덱스까지만 해당
for i in range(N-2):    
    for j in range(i+1,N-1):            # 2번째 for문은 [5, 6, 7, 8, 9] 에서 i+1에서 N-1 즉, 3번 인덱스까지
        for p in range(j+1,N):          # 3번째 for문은 [5, 6, 7, 8, 9] 에서 j+1에서 N까지 즉, 4번 인덱스까지
            Sum = ar[i]+ ar[j] +ar[p]   # 합계 (중요한 건 합계가 계속해서 바뀌기 때문에 미리 선언하지 않는 것!)
            if Sum <= M and Max < Sum:  # 만약 합계가 M(목표 숫자)보다 작거나 같고 그리고 Max 변수보다 크다면 
                Max = Sum               # Max 갱신 => 결과적으로 M보다 같거나 작으면서 가장 큰 수가 들어가게 됨
print(Max)
#=============================================================

# 7568 덩치(브루트포스)
n = int(input())
ar = [list(map(int,input().split())) for _ in range(n)] #1
re = []

for i in range(n):
    num = 1
    for j in range(n):
        if ar[i][0] < ar[j][0] and ar[i][1] < ar[j][1]: num += 1    #2
    re.append(num)
print(*re)
#========================================================

#1018 체스판 다시 칠하기(브루트포스)
def find(i,j):
    global Min
    idx =0
    while idx < 2:
        cnt = 0
        if idx == 0: standard = 'B'
        elif idx==1: standard = 'W'
        for y in range(8):
            for x in range(8):
                if y%2==0 and x%2==0 and ar[y+i][x+j] != standard or x%2==1 and y%2==0 and ar[y+i][x+j] == standard : cnt += 1
                if y%2==1 and x%2==0 and ar[y+i][x+j] == standard or x%2==1 and y%2==1 and ar[y+i][x+j] != standard: cnt += 1
        idx += 1
        Min = min(Min,cnt)

N,M = map(int,input().split())
ar = [list(input()) for _ in range(N)]
Min = 21e8
for i in range(N-8+1):
    for j in range(M-8+1):
        find(i,j)
print(Min)
#=============================================================

# 2231 분해합(브루트포스)
n = int(input())

for i in range(1,n+1):
    num = 0
    ar = [int(p) for p in str(i)]
    for j in range(len(ar)):
        num += ar[j]
    if i+num == n: break
    else: i = 0
print(i)
#==========================================================

# 10815 숫자 카드(집합과 맵)
N = int(input())
cards = list(map(int,input().split()))  #1. 현재 가지고 있는 카드 
M = int(input())
exist = list(map(int,input().split()))  #2. 확인할 카드
cards.sort()                            #3. 가지고 있는 카드 정렬

def find(target,st,ed):                 #7. 찾을 카드, 시작점(0), 끝점(가지고 있는 카드 배열 길이 - 1 )
    while (1):
        md = (st + ed) // 2             #8. 가운데 인덱스 = (시작점+끝점) // 2
        if st > ed:                     #9. 만약 찾을 카드가 없어서 시작 인덱스가 끝 인덱스를 넘어버리면 None return
            return None
        elif cards[md] == target:       #10. cards(가지고 있는 배열)의 중간 idx가 찾을 숫자 카드면 return
            return md
        elif cards[md] > target:        #11. mid idx 값이 target보다 크면 ed를 md 바로 앞으로(ed=md-1)
            ed = md - 1
        elif cards[md] < target:        #12. mid idx 갑이 target보다 작으면 st를 md 바로 뒤로(st=md+1)
            st = md + 1

for i in range(len(exist)):             #4. 확인할 숫자 카드 배열만큼 for문 돌린다.
    if find(exist[i],0,N-1) != None:    #5. 만약 이진탐색함수(find)에서 반환값이 None이 아니면 1출력한다.
        print(1,end=' ')
    else:                               #6. 반환값이 None이면 0출력
        print(0,end=' ')

#===============================================================

# 1260 DFS와 BFS (알고리즘 분류 - 그래프 이론)
from collections import deque
N, M, V = map(int,input().split())
ar = [[0]*N for _ in range(N)]      #1. 그래프를 만들기 위해 0으로 초기화 한 배열
for _ in range(M):                  #2. a정점에서 b정점으로 가는 걸 입력받아 인접행렬(ar배열==2차원배열)에 갱신 
    a,b = map(int,input().split())  
    ar[a-1][b-1] = 1
    ar[b-1][a-1] = 1                #3. 양방향 그래프이기 때문에 반대로도 갈 수 있다. 따라서 역으로도 갱신해준다.

used = [0] * N                      #5. dfs, bfs에서 이미 방문한 곳은 방문하지 않기 위해 used배열 사용
def dfs(st):
    if st ==0: return               
    print(st, end=' ')              #6. 그래프에서 방문하면 출력
    for i in range(N):
        if ar[st-1][i] == 1 and used[i] !=1:    #7. 인접행렬에서 1이고, used배열도 0이라면 방문한다.
            used[i] = 1
            # print(i+1)
            dfs(i+1)
used[V-1] = 1                       #4. 처음 시작하는 정점에 해당하는 used 배열 값을 1로 표시하고 dfs 시작
dfs(V)
print()

used = [0] * N                      #8. bfs에 사용하기 위해 used배열 재사용
def bfs(st):
    q = deque()
    q.append(st)
    while q:
        c = q.popleft()
        if used[c] == 1: continue   #10. 만약 used배열이 이미 1이라면 아래 코드들 생략(continue)
        else: used[c] = 1           # 처음에는 continue가 아니라 break를 해서 전체 정점을 방문하지 않았는데
        print(c+1,end=' ')          # 종료 되버렸다. 
        for i in range(N):
            if ar[c][i] == 1 and used[i]!=1:
                q.append(i)
bfs(V-1)                            #9. 시작지점(V) - 1이 시작점이된다. (인덱스는 0부터 시작하기 때문에)

#========================================================================================

# 2178 미로탐색(BFS)
from collections import deque
N, M = map(int,input().split())
ar = [list(map(int,input()))for _ in range(N)]
visit = [[0] * M for _ in range(N)]     #1. 방문한 곳 중복체크 할 visit배열
move = [[-1,0], [1,0], [0,-1], [0,1]]
Min =  21e8

def bfs(y,x,cnt):
    global Min
    q = deque()
    q.append([y,x,cnt])                 #3. q(queue)에 처음 y좌표, x좌표, 움직인 횟수(1)을 추가해준다.

    while q:
        yy,xx,cnt = q.popleft()         #4. queue에 담긴 y좌표, x좌표, 카운트를 꺼낸다.
        if yy== N-1 and xx== M-1:       #5. 만약 BFS를 도는 와중에 마지막 좌표에 도달하면 최소값 갱신해준다.
            Min = min(Min,cnt)
            # return
        for i in range(4):
            dy,dx = yy+move[i][0], xx+move[i][1]
#6. 이동할 좌표 dy,dx가 범위이내에 있고, 이동할 미로(ar) 좌표값이 1이며 visit(중복체크)가 0이면 visit를 표시해주고 queue에 추가해준다.
            if 0<=dy<N and 0<=dx<M and ar[dy][dx]==1 and visit[dy][dx]==0:  
                visit[dy][dx] = 1
                q.append([dy,dx,cnt+1])

visit[0][0] = 1                         #2. 시작 좌표를 1로 표시
bfs(0,0,1)
print(Min)

# DFS로 푸니 시간초과가 발생했다.
def dfs(y,x,cnt):
    global Min
    if y == N-1 and x == M-1:
        Min = min(cnt,Min)
        return
    for i in range(4):
        dy,dx = y+move[i][0], x+move[i][1]
#2. 내가 이동할 좌표 dy,dx가 범위를 안 벗어나고, 방문(visit)한 곳이 아니고, 미로(ar)가 1이면 방문
        if 0<=dy<N and 0<=dx<M and visit[dy][dx]==0 and ar[dy][dx]==1:
            visit[dy][dx] = 1   #3. 방문하기 전에 visit 1로 표시(중복 방문 방지)
            dfs(dy,dx,cnt+1)
            visit[dy][dx] = 0   #4. dfs로 돌아오면 다시 vist배열 0으로 갱신

visit[0][0] = 1
dfs(0,0,1)          #1. dfs(y시작 좌표, x시작 좌표, 횟수 1로 두고 시작) 
print(Min)
#=====================================================================================================

# 2606 바이러스(DFS+BFS)

C = int(input())
line = int(input())
ar = [[0]*C for _ in range(C)]  #1. 0으로 채워진 입접행렬(2차원 배열 생성) ar생성
used = [0] * C                  #2. 무한 루프 방지를 위한 used 배열 생성

for _ in range(line):           #3. 간선만큼 위에 만들어 놓은 ar배열에 1 채워넣기
    a,b = map(int,input().split())
    ar[a-1][b-1] = 1
    ar[b-1][a-1] = 1            #4. 양방향이기 때문에 역으로도 1표시
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# DFS version
def dfs(st):
    for i in range(C):      #!!! 이 부분에서 C가 아닌 line을 넣어서 indexerror발생 배열은 정점만큼 있어야 하는데 멍청하게 간선만큼 돌리려고 했음
        if ar[st][i] == 1 and used[i] ==0:  #7. 만약 2차원배열(ar배열)을 1줄씩 봤을 때, 1이 있고 + used배열이 0인경우(한 번도 방문하지 않은 경우)
            used[i] = 1                     #8. 1로 표시하고 
            dfs(i)                          #9. 다음 dfs로 진입

used[0] = 2                     #5. 처음 시작점이 무조건 1이고, 인덱스는 0부터 시작하기 때문에 used 배열 0번에 2로 표시
dfs(0)                          #6. 1번부터 시작되므로(인덱스는 0부터기 때문에) dfs에 0 넣고 시작 
print(sum(used)-2)              #10. used배열의 합계에서 2를 뺀 이유는 [2, 1, 1, 0, 1, 1, 0]와 같이 used배열은 작성된다. 
                                #    배열을 만들어 방문한 곳을 넣거나, 변수로 해서 cnt를 더해주는 것보다 2(초기 시작점을 2로 했으므로)만 빼면 답이 나온다.

# BFS version
def bfs(st):
    q = []                      #5. deque쓰기 귀찮아서 일반 배열로해서 pop(0)로 리스트 가장 좌측을 사용
    q.append(st)

    while q:                    #6. q가 차있는 동안 반복
        st = q.pop(0)           #7. q의 가장 좌측 추출
        for i in range(C):      
            if ar[st][i] ==1 and used[i] ==0:   #8. 2차원 배열을 한 줄씩 봤을 때 1로 되어있고, used배열의 갑이 0이면
                used[i] = 1                     #9. used 배열을 1로 표시하고 
                q.append(i)                     #10. q에 해당 값을 추가

used[0] = 2
bfs(0)
print(sum(used)-2)
#===============================================================================

# 2667 단지번호 붙이기

from collections import deque
N = int(input())
ar = [list(map(int,input())) for _ in range(N)]
check = [[0]*N for _ in range(N)]   #1. for문으로 1을 찾을 때, 동일한 단지내에 안 들어가기 위해 체크용 배열 생성
move = [[-1,0],[1,0],[0,-1],[0,1]]  #2. move = [[y상 , x상], [y하, x하], [y좌, x좌], [y우, x우]]

# BFS version #
def bfs(y,x):
    global ans
    q = deque()
    q.append([y,x])
    home = 1                        #8. 초기 집의 개수는 1부터 시작
    while q:
        yy,xx = q.popleft()
        for d in range(4):
            dy,dx = yy+move[d][0], xx+move[d][1]
            if 0<=dy<N and 0<=dx<N and ar[dy][dx]==1 and check[dy][dx]==0:  #9. 집이 ar배열이내에 있고, 중복되지 않으면
                check[dy][dx] = 1   #10. 중복체크 배열 바꿔주고
                home += 1           #11. 집의 개수 +1 해주고
                q.append([dy,dx])   #12. 해당 좌표 큐(queue)에 추가
    ans.append(home)                #13. queue가 비어서 while문이 종료되면 bfs 함수 종료 직전에 ans에 집이 몇 개 였는지 담아준다. 

ans = []        #3. 각 단지별로 집이 몇 개 존재하는지 담을 배열 생성
total = 0       #4. 각 단지(붙어있는 집의 수)가 몇 개인지 셀 변수
for i in range(N):
    for j in range(N):
        if ar[i][j] == 1 and check[i][j]==0:    #5. 2중 for문 돌면서 ar배열 값이 1이고, 중복으로 들어가는 걸 방지할 check 배열의 값이 0이면
            check[i][j] = 1                     #6. 중복체크 배열에 1로 만들어주고
            bfs(i,j)                            #7. 좌표가지고 bfs 진입
            total += 1                          #14. 함수를 돌고 나서는 집들이 모여있는 단지 개수 +1을 해준다.
ans.sort()
print(total)                                    #15. 아파트 단지를 정렬해주고, 총 단지 개수 출력
print(*ans,sep='\n')                            #16. 배열에 담긴 각 단지내 집의 수를 차례대로 출력
#~~~~~~~~~~~~~~~~~~~~
# DFS Version #
apt = 1                                         #3. 각 단지내에 몇개의 아파트가 있는지 확인할 변수
def dfs(y,x):
    global apt
    for i in range(4):
        dy,dx = y+move[i][0], x+move[i][1]
        if 0<=dy<N and 0<=dx<N and check[dy][dx]==0 and ar[dy][dx]==1:  #8. 만약 다음으로 들어갈 좌표가 ar배열 안에 있고, check 배열도 0이며 ar배열 값이 1이라면
            apt += 1                            #9. 아파트 개수 + 1을 해주고 check(중복확인) 배열에도 1로 표시한 이후에 다음 좌푤로 DFS를 타고 들어간다.
            check[dy][dx] = 1
            dfs(dy,dx)

ans=  []                                        #4. 각 단지내 아파트 개수를 담아줄 ans 배열생성
total = 0                                       #5. 단지(구역의 수)가 몇개인지 셀 변수
for i in range(N):
    for j in range(N):
        if ar[i][j]==1 and check[i][j]==0:      #6. 만약 ar배열이 1이고, check배열도 0이라면
            check[i][j] = 1                     #7. check 배열에 1을 표시하고, DFS 돌입
            dfs(i,j)
            ans.append(apt)                     #10. DFS가 끝나면 아파트 개수를 ans 배열에 추가해주고
            apt = 1                             #11. 아파트(apt) 변수를 다시 1로 초기화 해준다. ※사실 이 부분에서 apt = 0으로 해서 아파트 개수가 - 1씩 적게 나왔다.
            total += 1                          #12. DFS를 한 번 들어갔다 나왔다는 것은 단지를 1개 발견했다는 뜻이므로 total 변수에도 + 1을 해준다.
ans.sort()                                      #13. ※이 부분도 마찬가지로 간과하고 제출했다가 틀렸다. 문제를 제대로 안 읽어서 정렬하고 제출해야한다는 걸 까먹었다.
print(total)
print(*ans,sep='\n')                            #14. *ans는 ans배열의 원소들을 하나씩 출력하라는 뜻이고, sep='\n'의 의미는 출력되는 원소들(sep)을 한 칸씩 띄어준다.
#_________________________________________________________________________________________________________________________________

# 1012 유기농 배추(DFS, BFS)

from collections import deque

T = int(input())
for tc in range(T):
    M, N, K = map(int,input().split())      #0. M(가로), N(세로), k(K줄의 배추 정보)
    ar = [[0]*M for _ in range(N)]          #1. 2차원 배열(배추밭)
    check=  [[0]*M for _ in range(N)]       #2. DFS나 BFS 들어갈 때 중복을 피하기 위한 2차원 배열 
    move = [[-1,0], [1,0], [0,-1], [0,1]]   #3. move = [[y상 ,x상], [y하 ,x하], [y좌, x좌], [y우, x우]]

    for u in range(K):                      #4. K줄만큼 배추밭의 정보를 받아 ar배열 갱신
        x,y = map(int,input().split())
        ar[y][x] = 1

    # BFS 풀이
    def bfs(i,j):
        q = deque()
        q.append([i,j])

        while q:
            y,x = q.popleft()
            for d in range(4):
                dy,dx = y+move[d][0], x+move[d][1] 
                                                #8. dy,dx가 배열 범위 이내이고, check배열도 0이며 ar배열의 값이 1(배추가 있으면) 
                if 0<=dy<N and 0<=dx<M and check[dy][dx] == 0 and ar[dy][dx]==1:   
                    check[dy][dx] = 1           #9. 중복배열 갱신해주고 queue에 추가
                    q.append([dy,dx])
            
    ans = 0                                     #5. 필요한 배추흰지렁이 수
    for i in range(N):
        for j in range(M):                      #6. 2중 for문 돌면서 ar배열에 1이 있고, check(중복확인)이 0이면
            if ar[i][j]==1 and check[i][j]==0:  #7. check배열을 1로 갱신하고 bfs 돌입
                check[i][j] = 1
                bfs(i,j)
                ans += 1                        #10. bfs 끝나고 나오면 ans(배추흰지렁이) + 1
    print(ans)  

    # DFS 풀이
    import sys                                  
    sys.setrecursionlimit(100000)   
    '''            
    ※ 가장 중요한 부분, dfs로 돌리다가 25%에서 에러가 나면 최대 깊이가 1000이라서 error가 
    발생했을 수도 있다. 따라서 위 2줄을 넣어줘야 최대깊이를 늘려줄 수 있다.
    '''

    def dfs(y,x):
        for d in range(4):
            dy,dx = y+move[d][0], x+move[d][1]  
                                                #8. dy,dx가 배열 범위 이내이고, check배열도 0이며 ar배열의 값이 1(배추가 있으면)
            if 0<=dy<N and 0<=dx<M and check[dy][dx] == 0 and ar[dy][dx]==1:
                check[dy][dx] = 1                #9. 중복배열 갱신해주고 queue에 추가
                dfs(dy,dx)

    ans = 0                                     #5. 필요한 배추흰지렁이 수
    for i in range(N):                          
        for j in range(M):                      #6. 2중 for문 돌면서 ar배열에 1이 있고, check(중복확인)이 0이면                        
            if ar[i][j] == 1 and check[i][j]==0: #7. check배열을 1로 갱신하고 bfs 돌입
                check[i][j] = 1
                dfs(i,j)
                ans += 1
    print(ans)
#____________________________________________________________________________________________________________

# 7576 토마토(BFS)
from collections import deque                           # 1 = 익은 토마토, 0 = 익지 않은 토마토, -1 = 빈 칸
M, N = map(int,input().split())                         #0. N=세로, M=가로
ar = [list(map(int,input().split())) for _ in range(N)] #1. 토마토를 담을 2차원 배열
move = [[-1,0], [1,0], [0,-1], [0,1]]                   #2. 상,하,좌,우
t = []                                                  #3. 익은 토마토만 담을 리스트
for i in range(N):
    for j in range(M):
        if ar[i][j] == 1:                               #4. 2차원 배열을 돌면서 1(익은 토마토)의 좌표를 발견하면
            t.append([i,j])                             #5. t(익은 토마토 배열)에 추가한다.

def bfs(tomato):
    q = deque()
    for g in tomato:                                    #!!!! 사실 이 부분 때문에 2시간 정도 고민했다. 
        q.append([*g,0])                                # 예제 3번처럼 2곳에서 동시에 시작하는 경우가 있기 때문이다.
                                                        # 결론적으로 바깥에서 2중 for문으로 하나씩 시작하기보다
    while q:                                            # 아예 bfs안으로 1차원 배열을 들고 들어가서 queue에 하나씩
        yy,xx,day = q.popleft()                         # 추가하면 간단하게 해결되는 문제였다.

        for d in range(4):
            dy,dx = yy+move[d][0], xx+move[d][1]
            if 0<=dy<N and 0<=dx<M and ar[dy][dx] ==0:
                ar[dy][dx] = 1
                
                q.append([dy,dx,day+1])
    return day

ret = 21e8                                  #6. 결과를 담을 변수 ret(큰 값으로 초기화)
if t != []:                                 #7. 만약 익은 토마토 배열이 비어있지 않다면
    ret = min(ret,bfs(t))                   #8. bfs로 t(익은 토마토 배열) 전체를 보내고 반환되는 값 중 최소값 선택
else:                                       #9. t배열이 비어있다면 == 익은 토마토가 1개도 없다면 ret = -1
    ret = -1

for a in range(N):                          #10. 마지막 2중 for문 돌면서 익지 않은 토마토가 있는지 확인
    for b in range(M):
        if ar[a][b] ==0:                    #11. 익지 않은 토마토가 있다면 ret = -1로 갱신
            ret = -1
print(ret)                                  #12. 정답은 토마토가 익은 날짜거나 혹은 모든 토마토가 익어있으면 0, 
                                            #    모두 익지 못하는 상황이면 -1 출력
#___________________________________________________________________________________________________


# 1697 숨바꼭질(BFS)
from collections import deque
N, K = map(int,input().split())
Max = int(10e4)                 #1. 최대 10만까지이므로 최대값 설정
dp = [0] * (Max+1)              #2. 최대값만큼 0으로 채운 배열(이동횟수를 표시할 배열) 생성

def bfs(N):
    q = deque()
    q.append(N)
    while q:
        now = q.popleft()       
        if now == K:            #3. queue에서 꺼낸 값이 K(목표값)와 같으면
            print(dp[now])      #4. dp배열에서 K만큼(혹은now만큼) 이동한 횟수를 출력
            return

        for i in (now-1,now+1,now*2):       #5. now-1 / now+1 / now*2 세 가지 값이 
            if 0<=i<=Max and dp[i] == 0:    #6. 0과 10만 이내이고, dp[i] 값 즉, 이동값이 없으면
                dp[i] = dp[now]+1           #7. 현재의 이동값 = 이전 이동값 + 1 
                q.append(i)                 #8. now-1 / now+1 / now*2 값을 각각 queue에 추가
bfs(N)
