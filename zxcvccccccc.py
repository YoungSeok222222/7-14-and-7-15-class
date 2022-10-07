n,m = map(int,input().split())
n,m = n+1, m+1
y,x = map(int,input().split())
t = int(input())
lst = [[0]*m for _ in range(n)]
# num = 1
# lst[y][x] = num

move = [[1,1],[-1,1],[-1,-1],[-1,-1]]
idx = 0
for i in range(1,t+2):
    lst[y][x] = i
    dy,dx = y+move[idx][0], x+move[idx][1]
    if dy>=n and dx>=m: idx = 3
    elif dy>=n: idx = 1
    elif dx>=m: idx = 2
    elif dx<0: idx = 1
    elif dy<0: idx = 0
    dy,dx = y+move[idx][0], x+move[idx][1]
    y,x = dy,dx


for y in range(n):
    for x in range(m):
        if lst[y][x] == t+1:
            ay,ax = y,x
            break
print(ax,ay)



# M, N = map(int,input().split())
# store = int(input())

# lst = [list(map(int,input().split())) for _ in range(N)]

# d = 0
# for i in lst:
#     if i[0]==1 or i[0]==2:
#         d = min(10-i[1], i[1]-10)



# y,x = map(int,input().split())  

# ans = 0










