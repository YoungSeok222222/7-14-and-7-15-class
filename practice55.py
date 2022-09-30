def omok(y,x):
    for i in range(1,N):
        for j in range(8):

move = [[-1,0],[1,0],[0,-1],[0,1],[-1,1],[1,1],[1,-1],[-1,-1]]
T = int(input())
for tc in range(1,T+1):
    N = int(input())
    lst = [list(input()) for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if lst[i][j] =='o': omok(i,j)