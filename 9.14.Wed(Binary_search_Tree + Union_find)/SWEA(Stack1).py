# 15036 그래프 경로(DFS 경로 존재하는지 탐색하는 문제)
T = int(input())
for t in range(T):
    V,E = map(int,input().split())
    arr = [[0]* V for _ in range(V)]
    num = [list(map(int,input().split())) for _ in range(E)]
    st,ed = map(int,input().split())
    used = [0] * V
    for i in range(E):
        arr[num[i][0]-1][num[i][1]-1] = 1

    ret = 0
    def dfs(now):
        global ed,ret
        if now == ed-1: 
            ret = 1
            return

        for i in range(V):
            if arr[now][i] == 1 and used[i] ==0:
                used[i] = 1
                dfs(i)
                used[i] = 0
    used[st-1] = 1
    dfs(st-1)
    print(f"#{t+1} {ret}")
#########################################

#

    



