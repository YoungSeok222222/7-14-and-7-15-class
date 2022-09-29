# SWEA Brute_force (완전검색) (7)

# 14156 [파이썬 S/W 문제해결 구현] 2일차 - 전자카트
# 결국 순열을 구하는 문제
def dfs(lv,):
    if lv==N:
        Sum  = 0
        for i in range(N-1):                # 순열을 구했다면 
            Sum += lst[path[i]][path[i+1]]  # 좌표값에 해당하는 값을 더해줘서 반환
        Sum += lst[path[-1]][path[0]]        
        answer.append(Sum)
        return 
            
    for i in range(1,N):                    # 0번칸은 0을 채웠기 때문에 1번부터 시작
        if used[i] ==0:
            used[i] = 1
            path[lv] = number[i]            # 해당 수를 삽입
            dfs(lv+1)
            used[i] = 0
Min = 21e8
T = int(input())
for tc in range(1,T+1):
    answer = []                 # tc돌 때마다 새로운 빈 리스트로 갱신
    N = int(input())
    number =  [j for j in range(N)]     # 0부터 해당 숫자 N까지 리스트로 생성
    used,path = [0] * N, [0] * N
    lst = [list(map(int,input().split())) for _ in range(N)] 
    used[0],path = 1, 0
    dfs(1)                      # 1부터 dfs 시작
    print(f"#{tc} {min(answer)}")
# ar = []
# for i in range(1,3+1):
#     for j in range(1,3+1):
#         if i==j: continue
#         if j 
#         ar.append([i,j])
# print(ar)
# ar.pop()
#----------------------------------------------------

# 14155 [파이썬 S/W 문제해결 구현] 2일차 - 최소합
T = int(input())
for tc in range(1,T+1):
    N = int(input())
    lst = [list(map(int,input().split())) for _ in range(N)]
    for i in range(1,N):            # 밑에 1번과정 참조
        lst[0][i] += lst[0][i-1]
        lst[i][0] += lst[i-1][0]

    for y in range(1,N):            # 밑에 2번과정 참조
        for x in range(1,N):
            lst[y][x] += min(lst[y-1][x],lst[y][x-1])
    print(f"#{tc} {lst[N-1][N-1]}")
'''
1 2 3        
2 3 4
3 4 5
------
1 3 6   # 1번 과정은 0,1 = 0,0 + 0,1  / 0,2 =  0,1 + 0,2
3 6 10  
6 10 15 # 2번 과정은 위에 좌표와 좌측 좌표 값 중 가장 작은 값을 더해서 최종적으로 N-1,N-1 좌표에는 최소값이 생성
'''
#----------------------------------------------------

# 2382 [모의 SW 역량테스트] 미생물 격리

# 1486 장훈이의 높은 선반
def dfs(Sum,st):
    global Min,used
    if Sum >= B: 
        Min = min(Min,abs(Sum-B))
        return 

    for i in range(st,N):               # 조합이기 때문에 st 넣고 아래에서 다음 dfs 들어갈때 +1
        if used[i]==0:
            used[i] = 1
            dfs(Sum+lst[i],i+1)         # 268 61 201 이나 61 268 201이나 똑같은 조합이기 때문에 보지않고 넘어간다.
            used[i] = 0 

T = int(input())
for tc in range(1,T+1):
    N,B = map(int,input().split())       # 10(원소 개수) 2780(책장 높이)
    lst = list(map(int,input().split())) # 예를들어 268 61 201 535 464 168 491 275 578 153
    lst.sort(reverse=True)
    used = [0] * N
    Min = 21e8
    if len(lst)==1:
        Min = sum(lst)
    else:
        dfs(0,0)
    print(f"#{tc} {Min}") 

# 1249 [S/W 문제해결 응용] 4일차 - 보급로
from collections import deque

def bfs(y,x):
    q = deque()
    q.append([y,x])

    while q:
        y,x = q.popleft()
        for i in range(4):
            dy,dx = y+move[i][0], x+move[i][1]
            if 0<=dy<N and 0<=dx<N:                     # 배열 안에 있고
                if acc[dy][dx] == -1:                   # acc 배열이 초기값 -1이라면
                    acc[dy][dx] = acc[y][x]+lst[dy][dx] # 원본 lst의 dy,dx 값과 acc 배열 y,x를 더한 값을 acc에 삽입
                    q.append([dy,dx])
                elif acc[dy][dx] != -1 and acc[y][x] + lst[dy][dx] < acc[dy][dx]:   # 만약 acc가 초기 값 -1이 아니고(이미 갱신된 상태고), 갱신하려는 acc[dy][dx]가 작으면
                    acc[dy][dx] = acc[y][x] + lst[dy][dx]                           # 다시 갱신
                    q.append([dy,dx])
            
move = [[-1,0],[1,0],[0,-1],[0,1]]
directy = [-1,1,0,0]
directx = [0,0,-1,1]
T = int(input())
for tc in range(1,T+1):
    N = int(input())
    lst = [list(map(int,input())) for _ in range(N)]
    acc = [[-1]*N for _ in range(N)]                    # 원본 배열과 비교할 배열 하나 -1을 넣어 생성
    acc[0][0] = lst[0][0]                               # 첫 0,0 좌표에 lst[0][0] 값 삽입
    bfs(0,0)                                            # bfs에 0,0부터 시작
    # for g in acc:
    #     print(*g)
    print(f"#{tc} {acc[-1][-1]}")
