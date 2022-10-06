m,n = map(int,input().split())
m,n = m+1, n+1
x,y = map(int,input().split())
t = int(input())
lst = [[0]*m for _ in range(n)]
num = 1
lst[y][x] = num

move = [[1,1],[1,-1],[-1,-1],[1,-1]]
idx = 0
for i in range(1,t+1):
    lst[y][x] = i
    dy,dx = y+move[idx][0], x+move[idx][1]
    if dy<0 or dy>=n or dx<0 or dx>=m: 
        idx = (idx+1) % 4
        dy,dx = y+move[idx][0], x+move[idx][1]

    y,x = dy,dx

for y in range(n):
    for x in range(m):
        if lst[y][x] == t:
            ay,ax = y,x
            break
print(y,x)
