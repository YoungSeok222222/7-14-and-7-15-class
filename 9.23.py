# from collections import deque

# move = [[-1,0],[1,0],[0,-1],[0,1]]

# T = int(input())
# for tc in range(1,T+1):
#     N = int(input())
#     lst = [list(input()) for _ in range(N)]
#     for i in range(N):
#         for j in range(N):
#             lst[i][j] = int(lst[i][j])
    # for i in range(N-2,-1,-1):
    #     lst[N-1][i] += lst[N-1][i+1]
    #     lst[i][N-1] += lst[i+1][N-1]

    # for y in range(N-2,-1,-1):
    #     for x in range(N-2,-1,-1):
    #         lst[y][x] += min(lst[y+1][x],lst[y][x+1])
    # print(f"#{tc} {lst[0][0]}")
   
    # # for i in range(1,N):
    # #     lst[0][i] += lst[0][i-1]
    # #     lst[i][0] += lst[i-1][0]
    # for y in range(1,N):
    #     for x in range(1,N):
    #         lst[y][x] += min(lst[y-1][x],lst[y][x-1])

    # print(f"#{tc} {lst[N-1][N-1]}")
#-----------------------------------------------------------------------    
    # visit = [[0]*N for _ in range(N)]
    # def bfs(y,x):
    #     check = [[10]*N for _ in range(N)]
    #     q = deque()
    #     q.append([y,x,lst[y][x]])
    #     visit[y][x] = 1
    #     Sum = 0
    #     check[0][0] = 0
    #     while q:

    #         y,x,num = q.popleft()
    #         Sum += num
    #         if y==N-1 and x==N-1:
    #             return
    #         for i in range(4):
    #             dy,dx = y+move[i][0], x+move[i][1]
    #             if 0<=dy<N and 0<=dx<N:
    #                 if lst[y][x]+lst[dy][dx] >= check[dy][dx]: continue
    #                 check[dy][dx] = lst[y][x]+lst[dy][dx]
    #                 q.append([dy,dx,lst[dy][dx]])
    #                 visit[dy][dx] = 1
    #     return Sum
    
    # Sum = bfs(0,0)
    # print(lst[N-1][N-1])
#and visit[dy][dx] ==
#     dy,dx = 0,0
#     Sum = 0
#     for y in range(dy,N):
#         for x in range(dx,N):
#             num = []
#             for i in range(4):
#                 dy,dx = y+move[i][0],x+move[i][1]
#                 if 0<=dy<N and 0<=dx<N:
#                     num.append(lst[dy][dx])
#                     # print(num)
#             # num.sort(key=lambda x: )
#             Sum += min(num)

# print(Sum)




# def dfs(y,x):
#     y1,x1 = y-1,x
#     y2,x2 = y+1,x
#     y3,x3 = y,x-1
#     y4,x4 = y,x+1
#     ret = min(lst[y1][x1],lst[y2][x2],lst[y3][x3],lst[y4][x4])
#     return ret


# Sum = 0
# for y in range(N):
#     for x in range(N):
#         Sum += dfs(y,x)
# print(Sum)

# Min = 21e8
# def dfs(lv):
#     global Min,path
#     if sum(path) > B and abs(sum(path)-B) < Min:
#         Min = abs(sum(path)-B)

#     if lv==N:
#         return

#     for i in range(N):
#         if used[i]==0:
#             path[lv] = lst[i]
#             used[i] = 1
#             dfs(lv+1)
#             used[i] = 0
#             path[lv] = 0

T = int(input())
for tc in range(1,T+1):
    N,B = map(int,input().split())
    lst = list(map(int,input().split()))


    for i in range(N):
        for j in range(N):
            if i==j: continue
            ret = (lst[i]+lst[j])
            print(ret)








    # path = [0] * N
    # used = [0] * N
    # # dfs(0)
    # print(f"#{tc} {Min}")
 








    