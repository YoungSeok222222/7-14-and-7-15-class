# 14161 5209. [파이썬 S/W 문제해결 구현] 5일차 - 최소 생산 비용
def dfs(y,Sum):
    global Min
    if Sum > Min: return            # 언제든지 Sum 값이 크면 다시 back!!!!!!!!!!!!
    if y==N:                        # 만약 y가 N 과 같다면 최소값 갱신
        Min = min(Sum,Min)
        return

    for x in range(N):
        if used[x]==0:
            used[x] = 1             # used를 사용하여 행에서 사용한 것들 표시
            dfs(y+1,Sum+lst[y][x])
            used[x] = 0

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    lst = [list(map(int,input().split())) for _ in range(N)]
    used = [0] * N
    Min = 21e8
    dfs(0,0)
    print(f"#{tc} {Min}")

# 14160 5차시 5일차 - 전기버스2
def dfs(idx,cnt):
    global Min
    if cnt >= Min: return   # 백트랙킹!!!! 만약 dfs 돌다가 cnt가 이미 최소값 보다 크거나 같은 경우 볼 필요 없으므로 return
    if idx >= ed-1:         # 만약 idx가 마지막에 도달하거나 마지막보다 크다면
        if cnt < Min:       # 만약 최소값보다 더 작다면 
            Min = cnt       # 최소값 갱신
        return
    
    for i in range(lst[idx]):   # lst배열의 idx에 있는 배열 값만큼 갈 수 있음
        dfs(idx+i+1,cnt+1)

T = int(input())
for tc in range(1,T+1):
    lst = list(map(int,input().split()))
    ed = lst.pop(0)         # 배열의 맨 처음은 원소의 갯수이므로 pop해서 따로 빼냄
    Min = 21e8              
    dfs(0,0)
    print(f"#{tc} {Min-1}") # 출발지에서의 배터리 장착은 교환횟수에서 제외하므로 -1