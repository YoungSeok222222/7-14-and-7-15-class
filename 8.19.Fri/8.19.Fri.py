# 과목평가 힌트 및 연습문제 풀이 / DFS 연습을 조금더 ...


#자료구조  = 자료를 관리하는 방식에 que first in first out /  stack last in last out

# stack 자료구조의 특성 선형
s = [0,1,2,3]
# push  는 스택에 자료 추가한다는 말 == append / pop은 자료 뺴기 (가장 나중에 들어온게 나간다)

#선택정렬을 이용하여 오름차순으로 정렬하시오.

#########################
# 1. 배열 전체 평균 구하기
# n 입력
# n*n 배열을 입력
'''
5
2 4 7 4 2
2 9 5 3 1
4 9 6 5 3
3 7 9 2 3
1 1 2 3 4
'''

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]


sum = 0

for i in range(5):
    for j in range(5):
        sum += arr[i][j]

avg = sum//(n*n)
print(int(avg))

# 1-2. 각 좌표값이 배열평균과 차이는 값들의 합 출력하기
sum_avg = 0
for i in range(5):
    for j in range(5):
        if arr[i][j] > avg:
            sum_avg += arr[i][j] - avg
        else:
            sum_avg += avg - arr[i][j]

print(int(sum_avg))

# 2. pattern 찾기

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
pattern = [[1, 1], [1, 0]]

# 0, 0 / 3, 2
def findpattern(dy, dx):
    # directy = [0, 0, 1, 1]
    # directx = [0, 1, 0, 1]
    for i in range(2):
        for j in range(2):
            if pattern[i][j] != arr[dy+i][dx+j]:
                return 0
    return 1
ret = 0
for i in range(4):
    for j in range(3):
        ret += findpattern(i, j)
print(ret)

'''
5 4
1 1 1 1
1 0 1 1
1 1 1 1
1 1 0 1
1 0 1 1
'''


# 3. 상하좌우 값이 좌표보다 작으면 좌표는 산봉우리 ㅇㅈ
'''
4 5
2 4 2 1 5
1 2 1 4 3
2 2 2 4 2
1 7 3 2 3
'''
n, m  = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(n)]

def isMountain(y,x):
    y_direction = [-1,1,0,0]
    x_direction = [0,0,-1,1]
    for i in range(4):
        dy = y_direction[i] + y
        dx = x_direction[i] + x
        if dy < 0 or dx < 0 or dy > 3 or dx > 4: continue
        elif arr[dy][dx] >= arr[y][x]: return 0
    else:
        return 1


cnt = 0
for y in range(n):
    for x in range(m):
        ret = isMountain(y,x)
        if ret:
            cnt += 1

print(cnt)
#####################
## dfs 심화1 (완전탐색)
#그림 1 참조 (경로 합 중 최대값 구하기)
arr=[
    [2,5,7],
    [8,4,-8],
    [-7,1,4],
    [5,1,9]
]
Max=int(-21e8)

def dfs(level, sum):
    global Max
    if level==4:
        if sum>Max:
            Max=sum
        return

    for i in range(3):
        dfs(level+1,sum+arr[level][i])

dfs(0,0) # level sum
print(Max)

###########################
# dfs 심화 2(완전탐색) (취객 3 방향으로만 가기)
# 그림 2 참조
arr = [
    [3,2,4,1],
    [0,1,0,5],
    [2,0,3,0],
    [5,4,0,2],
    [2,-5,0,3],
]
Max = int(-21e8)
def dfs(now,level,sum):     #여기서 level은 arr의 y좌표를 의미
    global Max
    if level == 5:
        if sum > Max:
            Max = sum
        return
    for i in range(3):
        direct = [-1,0,1]
        dy = level
        dx = now + direct[i]
        if dx < 0 or dx > 3: continue       # 맵 범위
        if arr[dy][dx] == 0: continue       # 내가 가고자 하는 방향이 벽(0)인 경우 넘어감
        dfs(dx,level+1,sum+arr[dy][dx])     # 여기서 dx는 x 좌표?


for i in range(4):
    dfs(i,0,0) # now level sum
print(Max)
#############################################
# dfs 심화 3
# 한쪽 길 arr[0][0]에서 arr[3][3]까지 갈 수 있는지
arr = [
    [0,0,0,0],   # 0 => 길 and 1 => 벽
    [1,0,1,0],
    [1,0,1,0],
    [0,0,0,0],
]
visit = [[0] * 4 for _ in range(4)]    #중복방지를 위한 배열
flag = 0 # 도착시 1로 바꿀 예정

def dfs(y,x):
    global flag
    if y ==3 and x ==3:
        flag =1
        return

    directy = [-1,1,0,0]                # y축으로 갈 방향
    directx = [0,0,-1,1]                # x축으로 갈 방향
    for  i in range(4):             # 상하좌우 탐색할꺼기 때문에 br이 4
        dy = y + directy[i]         # dy는 간  y축 방향
        dx = x + directx[i]         # dx는 간 x축 방향
        if dy < 0 or dx < 0 or dy > 3 or dx > 3: continue   # 배열범위 벗어나면 안됨
        if visit[dy][dx] ==1: continue                      # 이미 방문했던 곳이면 안 됨
        if arr[dy][dx] == 1: continue                        # 벽이면 못감
        visit[dy][dx] = 1
        dfs(dy,dx)
        if flag ==1: return # 옵션(더 빨리 끝낼 수 있음)

visit[0][0] = 1
dfs(0,0)  #y,x 좌표값
if flag ==1:
    print("갈 수 있어~~~")
else:
    print("도착할 수 없음")
##########################

# DFS 심화 3
# #미로 찾기 (0,0)에서 (1,3)으로 가는 최소 횟수 탐색
arr = [
    [0,0,0,0,1],
    [1,0,1,0,1],
    [1,0,1,0,1],
    [0,0,0,0,0],
]

visit = [[0]*5 for _ in range(4)]
cnt = 0
Min = int(21e10)
def dfs(y,x):
    global cnt, Min
    if y ==1 and x ==3:
        if cnt < Min:   #최소레벨 갱신
            Min = cnt
        return

    directy = [-1,1,0,0]
    directx = [0,0,-1,1]
    for i in range(4):
        dy = directy[i] + y
        dx = directx[i] + x
        if dy < 0 or dx < 0 or dy > 3 or dx > 3: continue
        if visit[dy][dx] ==1: continue
        if arr[dy][dx] ==1: continue

        visit[dy][dx] = 1
        cnt += 1
        dfs(dy,dx)
        visit[dy][dx] = 0
        cnt -= 1

visit[0][0] = 1
dfs(0,0) # y,x,cnt
print(Min)














#############################
# 그래프  = 비선형 자료구조
