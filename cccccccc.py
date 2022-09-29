def dfs(Sum):
    global Min
    if Sum >= B: 
        Min = min(Min,abs(Sum-B))
        return 

    for i in range(N):
        if used[i]==0:
            used[i] = 1
            dfs(Sum+lst[i])
            used[i] = 0 

T = int(input())
for tc in range(1,T+1):
    N,B = map(int,input().split())
    lst = list(map(int,input().split()))
    used = [0] * N
    Min = 21e8
    if len(lst)==1:
        Min = sum(lst)
    else:
        dfs(0)
    print(f"#{tc} {Min}")
    