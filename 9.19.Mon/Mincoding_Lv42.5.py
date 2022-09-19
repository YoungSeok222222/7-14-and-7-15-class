# 1번 가로 큐브 돌리기
n = int(input())
lst = [list(map(int,input().split())) for _ in range(n)]
Max = -21e8

def change(i):
    for j in range(n-1,0,-1):
        lst[i][j-1], lst[i][j] = lst[i][j], lst[i][j-1]
    
def getsum():
    global Max
    gop = 1
    for y in range(n):
        sum = 0
        for x in range(n):
            sum += lst[x][y]
        gop *= sum
    Max = max(Max,gop)
    

def dfs(lv):
    global Max
    if lv ==3:return
    for i in range(n):
        for j in range(n-1):
            getsum()
            change(i)
        dfs(lv+1)
dfs(0)
print(f"{Max}점")


'''
4
-1 2 3 3
-9 8 9 0
-1 -9 1 4
5 3 1 2
'''

# 2번 폭탄 투하 장소 선정
lst = [list(input()) for _ in range(4)]
n = int(input())

result = [0] *n
Max = 0 

def bomb(path):
    directy,directx = [0,-1,1,0,0], [0,0,0,-1,1]    # 자기자신 / 상 / 하 / 좌 / 우
    cnt = 0
    check = []                                      # 폭탄 투하시 앞서 투하했던 곳 check용
    for v in path:
        y,x = v[0],v[1]
        for i in range(5):
            dy,dx = y+directy[i],x+directx[i]
            if 0<=dy<4 and 0<=dx<4 and lst[dy][dx] !='_' and [dy,dx] not in check:      # 범위 이내 + 알파벳인 경우 + 앞서 투하했던 곳이 아니면
                cnt += 1                                                                # cnt += 1
                check.append([dy,dx])                                                   # 투하된 곳 중심을 check에 저장
    return cnt

def dfs(lv):
    global result, Max
    if lv==n:                         # 입력 받은 폭탄의 갯수만큼 path가 채워지면 
        cnt = bomb(path)              # bomb 함수로 보내서 count 세기
        if Max < cnt:
            Max = cnt                 # cnt가 Max로 된 경우
            for j in range(n):
                result[j] = lst[path[j][0]][path[j][1]] # 그 결과를 result에 넣어서 계속 갱신
        return
           
    for i in range(len(arr)):          # 좌표의 갯수 만큼 br을 설정
        if used[i] ==0:
            used[i] = 1
            path[lv] = arr[i]          # path 배열에 하나씩 저장
            dfs(lv+1)
            used[i] = 0

arr = []
for y in range(4):                      # 탐색으로 알파벳이 있는 경우, 좌표를 arr에 저장
        for x in range(4):
            if lst[y][x]!='_':
                arr.append([y,x])

path,used = [''] * n, [0] * len(arr)
dfs(0)
result.sort()
print(*result)
                
    
                