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
#===========================================================

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
#===================================================================
# 2805 농작물 수확하기
T = int(input())
for tc in range(1,T+1):
    N = int(input())
    lst = [list(map(int,input())) for _ in range(N)]
    ans = 0
    md = N//2
    for y in range(md+1):
        for x in range(md-y,md+y+1):
            ans += lst[y][x] + lst[N-y-1][x]    # 정사각형 마름모 기준 위쪽 좌표값 + 아래쪽 좌표값
    print(f"#{tc} {ans-sum(lst[md])}")          # 정가운데는 2번 더했기 때문에 다시 가운데 줄 전체를 한 번 빼준다.
#========================================================================
# 1258 [S/W 문제해결 응용] 7일차 - 행렬찾기
from collections import deque
def bfs(y,x):
    q = deque()
    visit[y][x] = 1
    q.append([y,x])
    while q:
        y,x = q.popleft()
        for i in range(4):
            dy,dx = y+move[i][0], x+move[i][1]
            if 0<=dy<N and 0<=dx<N and visit[dy][dx]==0 and lst[dy][dx]!=0:
                visit[dy][dx] = 1
                q.append([dy,dx])
    return dy+1,dx

T = int(input())
move = [[-1,0],[1,0],[0,-1],[0,1]]
for tc in range(1,T+1):
    N = int(input())
    lst = [list(map(int,input().split())) for _ in range(N)]
    visit = [[0]*N for _ in range(N)]
    cnt,ans = 0, []
    for i in range(N):
        for j in range(N):
            if lst[i][j] !=0 and visit[i][j]==0:
                cnt += 1
                y,x = bfs(i,j)
                ans.append([y-i,x-j])
    ans.sort(key=lambda x: (x[0]*x[1],x[0]))
    print(f"#{tc}",cnt,end=' ')
    for g in ans:
        print(*g,end=' ')
    print()
#====================================

# 1220 Magnetic 
for tc in range(1,11):
    N = int(input())
    lst = [list(map(int,input().split())) for _ in range(N)]
    ans = 0
    for y in range(N):
        for x in range(N):
            if lst[y][x] ==1:
                for yy in range(y+1,N):
                    if lst[yy][x]==2:
                        lst[yy][x] = 9
                        ans += 1
                        break
                    elif lst[yy][x]==9: break
    print(f"#{tc} {ans}")
    # for g in lst:
    #     print(*g)
'''
7
1 0 2 0 1 0 1
0 2 0 0 0 0 0
0 0 1 0 0 1 0
0 0 0 0 1 2 2
0 0 0 0 0 1 0
0 0 2 1 0 2 1
0 0 1 2 2 0 2
'''

# 1860 진기의 최고급 붕어빵
# for i (N)
# tmp(빵 개수) = (arr[i]//M 빵 개수) * K 초
T = int(input())
for tc in range(1,T+1):
    # N: 사람 수, M시간마다 K개 붕어빵 만듬
    N, M, K = map(int,input().split())
    # 0초 이후에 손님들이 도착하는 시간
    lst = list(map(int,input().split()))
    lst.sort()
    ans = 0
    for i in range(N):
        # 손님 도착 시간에 만들 수 있는 붕어빵의 수
        tmp = (lst[i]//M)*K
        # tmp -1: 현재 손님이 먹음, i: 이전 손님들이 먹은 수
        if tmp-1-i < 0:
            print(f"#{tc} Impossible")
            break
    else: print(f"#{tc} Possible")

# 9489 고대 유적
def treasure():
    Max = 0
    for i in range(N):
        c = 0
        for j in range(M):
            if lst[i][j]==1: c += 1
            if lst[i][j]==0 or j==M-1:
                Max = max(Max,c)
                c = 0               
    for x in range(M):
        c = 0
        for y in range(N):
            if lst[y][x]==1: c +=1
            if lst[y][x]==0 or y==N-1:
                Max = max(Max,c)
                c = 0
    return Max
T = int(input())
for tc in range(1,T+1):
    N,M = map(int,input().split())
    lst = [list(map(int,input().split())) for _ in range(N)]
    print(f"#{tc} {treasure()}")


# 백준 2578 빙고
def bingo(j,n):
    ans = 0
    for y in range(5):
        for x in range(5):
            if lst[y][x] == j:
                lst[y][x] = 0
                break                
    for y in range(5):
        cnt1,cnt2 = 0,0
        for x in range(5):
            if lst[y][x] ==0: cnt1 += 1
            if lst[x][y] ==0: cnt2 += 1
        if cnt1==5: ans += 1
        if cnt2==5: ans += 1

    cnt3,cnt4,idx = 0,0,0
    for y in range(4,-1,-1):
        if lst[y][y]==0: cnt3 += 1
        if lst[y][idx]==0: cnt4 += 1
        idx += 1
    if cnt3 ==5: ans += 1
    if cnt4 ==5: ans += 1
    return ans

lst = [list(map(int,input().split())) for _ in range(5)]
num = [list(map(int,input().split())) for _ in range(5)]
n ,ret= 1, 0 
for i in num:
    if ret>=3: break
    for j in i:
        ret = bingo(j,n)
        if ret >=3: 
            print(n)
            break
        n += 1

# 백준 2491 수열
N = int(input())
lst = list(map(int,input().split()))
dp1,dp2 = [0] * (N+1), [0]*(N+1)
ans = []
Max = 0
for i in range(1,N):
    if lst[i-1] <= lst[i]: 
        dp1[i] = dp1[i-1]+1

for i in range(1,N):
    if lst[i-1] >= lst[i]:
        dp2[i] = dp2[i-1] +1
print(dp2)
a,b = max(dp1),max(dp2)
print(max(a,b)+1)

# 백준 2309 일곱 난쟁이
def dfs(lv,st):
    global ret
    if sum(path)>100: return
    if lv==7:
        if sum(path)==100 and ret==0:
            path.sort()
            for g in path:
                print(g)
                ret = 1
        return
    for i in range(st,9):
        path[lv] = lst[i]
        dfs(lv+1,i+1)
        path[lv] = 0
lst = []
for i in range(9):
    lst.append(int(input()))
path = [0]*7
ret = 0
dfs(0,0)