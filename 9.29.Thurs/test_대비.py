# 폭탄이 터지는데 안전지대는 몇 군데 인가
test = [                # 3 벽 / 1 폭탄 
    [0,0,3,0,0],
    [0,3,1,0,3],
    [0,3,1,0,3],
    [3,0,0,1,0],
    [0,3,1,0,3],

]
cnt = 0
move = [[-1,0],[1,0],[0,-1],[0,1]]
def nuclear(y,x):
    global cnt
    for j in range(4):
        for i in range(1,5):
            dy,dx = y+move[j][0] * i, x+move[j][1]*i
            if 0<=dy<5 and 0<=dx<5:
                if test[dy][dx] ==3: break
                else: 
                    test[dy][dx] = 9

for i in range(5):
    for j in range(5):
        if test[i][j] ==1:
            test[i][j] = 9
            nuclear(i,j)

for i in range(5):
    for j in range(5):
        if test[i][j] ==0: cnt += 1
for g in test:
    print(*g)
print(cnt)

#================================================

# 은혁이형 코드
def bomb(y, x):
    dy = [0,1,0,-1]
    dx = [1,0,-1,0]
    for i in range(4):
        k = 1
        while True:
            ny, nx = y+dy[i]*k, x+dx[i]*k
            if ny>n-1 or nx>n-1 or ny<0 or nx<0: 
                break
            if arr[ny][nx]==3: break
            arr[ny][nx]=2
            k+=1

arr = [
    [0,0,3,0,0],
    [0,3,1,0,3],
    [0,3,1,0,3],
    [3,0,0,1,0],
    [0,3,1,0,3]
]
n = len(arr)
for i in range(n):
    for j in range(n):
        if arr[i][j]==1:
            bomb(i, j)
cnt =0
for i in range(n):
    for j in range(n):
        if arr[i][j]==0:
            cnt+=1
# print(cnt)