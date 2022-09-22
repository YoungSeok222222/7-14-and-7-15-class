# from collections import deque


# lst = [list(input()) for _ in range(8)]
# move = [[-1,0],[1,0],[0,-1],[0,1]]
# def bfs(y,x,n):
#     q = deque()
#     q.append([y,x,0])
#     visit = [[0]*9 for _ in range(8)]
#     visit[y][x] = 1

#     while q:
#         y,x,cnt = q.popleft()
#         if n==1 and lst[y][x]==3: 


#         for i in range(4):
#             dy,dx = y+move[i][0], x+move[i][1]
#             if 0<=dy<8 and 0<=dx<9 and lst[y][x]=="#":
#                 lst[dy][dx] = 3
#                 # visit[dy][dx] = 1
#                 q.append([dy,dx,cnt+1])
# result = []
# check = [[0]*9 for _ in range(8)]
# for i in range(8):
#     for j in range(9):
#         if lst[i][j]=="#":
#             bfs(i,j,0)
#             bfs(i,j,1)





