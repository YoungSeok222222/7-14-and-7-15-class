# 14165 5250. [파이썬 S/W 문제해결 구현] 7일차 - 최소 비용(bfs + 추가 배열)
from collections import deque
def bfs(y,x):
    q = deque()
    q.append([y,x])
    while q:
        y,x = q.popleft()
        for i in range(4):
            dy,dx = y+move[i][0], x+move[i][1]
            if 0<=dy<N and 0<=dx<N:
                d = lst[dy][dx]-lst[y][x]
                if d < 0: d = 0  
                if ar[y][x]+d+1 < ar[dy][dx]:
                    ar[dy][dx] = ar[y][x]+d+1
                    q.append([dy,dx])

move = [[-1,0],[1,0],[0,-1],[0,1]]
T = int(input())
for tc in range(1,T+1):
    N = int(input())
    lst = [list(map(int,input().split())) for _ in range(N)]
    ar = [[int(21e8)]*N for _ in range(N)]
    ar[0][0] = 0
    bfs(0,0)
    print(f"#{tc} {ar[N-1][N-1]}")
# 14164 [파이썬 S/W 문제해결 구현] 7일차 - 최소 신장 트리 (크루스칼 알고리즘)
def find(member):
    if ar[member]==member: return member
    ret = find(ar[member])
    ar[member] = ret
    return ret

def union(a,b,cost):
    global ans, cnt
    fa,fb = find(a),find(b)
    if fa==fb: return 
    ans += int(cost)
    cnt += 1
    ar[fb] = fa

T = int(input())
for tc in range(1,T+1):
    V,E= map(int,input().split())
    V,E = int(V)+1, int(E)
    lst = [list(map(int,input().split())) for _ in range(E)]
    lst.sort(key=lambda x: int(x[2]))
    ar = list(i for i in range(V))

    ans, cnt = 0,0
    for i in lst: 
        if cnt==V-1: 
            print(f"#{tc} {ans}")
            break
        union(i[0],i[1],i[2])
        