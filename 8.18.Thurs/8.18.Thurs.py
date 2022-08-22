## 비선형 구조 : 그래프(ex.지하철 노선도)
# 큐(que): ex. 맛 집 (First in First Out)
# 스택(stack): (Last in Last out)

# 1.인접행렬(이차원 배열)
name = ["A","B","C","D","E","F"]
arr = [
    [0,0,0,0,0,0],                                     #A(0)
    [0,0,0,0,0,0],                               #B(1)         #C(2)
    [0,0,0,0,0,0],                          #D(3)   #E(4)     #F(5)
    [0,0,0,0,0,0],
    [0,0,0,0,0,0],
    [0,0,0,0,0,0],
]

# 2.인접 리스트
brr = [
    [1,2],   #0번에서 갈 수 있는 곳
    [3,4],
    [5],
    [],
    [],
    []
]

# 3.이진트리에 한해서(일차원배열)





#############################################
# 1. 인접행렬 연습
# 가장 인기있는사람 출력하기
nname = ["A", "B", "C", "D", "E"]
arr = [
    [0, 1, 1, 0, 0],  # A(0)
    [0, 0, 0, 0, 1],  # B(1)         #C(2)
    [0, 1, 0, 0, 0],  # D(3)   #E(4)     #F(5)
    [0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0],
]
sum = 0
Max = 0
Maxindex = 0

for x in range(5):
    sum = 0 #
    for y in range(5):
        if arr[y][x] ==1:
            sum += 1
    if sum > Max:
        Max = sum
        Maxindex = x
print(name[Maxindex])

#####################
# 1.인접행렬 연습2
#형제 찾기
name = ["A", "B", "C", "D", "E","F"]
n = input()
n = ord(n) - 65
arr = [
    [0, 1, 1, 0, 0, 0],             # A(0)
    [0, 0, 0, 1, 1, 0],        # B(1)         #C(2)
    [0, 0, 0, 0, 0, 1],  # D(3)   #E(4)     #F(5)
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
]
ch=input()
idx=ord(ch)-65
answer=[]

for i in range(6):
    if arr[i][idx]==1:
        answer.append(i)

if len(answer)==0:
    print("형제없음")
else:
    result=[]
    for x in answer:
        for i in range(6):
            if arr[x][i]==1:
                result.append(i)
    result.remove(idx)
    if len(result)==0:
        print("형제없음")
    else:
        for x in result:
            print(chr(x+65))

###############
#
# 트리 DFS(깊이우선탐색)순서 출력하기
name = list(input().split())   # name = ["A","B","C","D","E","F"]
arr = [
    [0,1,1,0,0,0],                      #A
    [0,0,0,1,1,0],                  #B        #C
    [0,0,0,0,0,1],              #D    #E    #F
    [0,0,0,0,0,0],
    [0,0,0,0,0,0],
    [0,0,0,0,0,0],
]
answer = []
def dfs(now):
    global answer
    answer.append(name[now])  # DFS 탐색 순서 저장
    for i in range(6):        # range는 노드 수 / 가로축으로만 찾기 때문에 1증 포문
        if arr[now][i] ==1:
            dfs(i)

dfs(0) # 0 번 인덱스부터 깊이 우선탐색(dfs) 시작 / arr의 y축 0번부터 가로로 시작
print(*answer)
#####################

# 트리가 아닌 경우 중복 발생이 가능하기 때문에 used를 사용
name = list(input().split()) # B A C D
arr = [
     [0,0,1,1], #B
     [1,0,0,0], #A
     [0,1,0,1], #C
     [0,0,0,0], #D
]
result = []
used = [0] * 4


def dfs(now):
    global result
    result.append(name[now])
    for x in range(len(name)):
        if arr[now][x] == 1:
            if used[x] == 0:
                used[x] = 1
                dfs(x)

used[0] = 1
dfs(0) # B 부터 깊이우선 탐색 시작
print(result)
###########################

#DFS를 이용한 한 지점에서 다른 지점으로 가는 경로 탐색
name = list(input().split()) # B A C D
arr = [
     [0,0,1,1], #B
     [1,0,1,0], #A
     [1,0,0,1], #C
     [0,0,0,0], #D
]
used = [0] * 4
cnt = 0
def dfs(now):
    global cnt
    if now == 3:  #도착지점으로 설정된 D(3번)으로 간 경우 cnt +=1
        cnt += 1

    for x in range(4):
        if arr[now][x] ==1 and used[x] ==0:
                used[x] = 1
                dfs(x)
                used[x] = 0
used[1] = 1                          #시작지점이 A 이므로 used[1] =1 로 설정하고
dfs(1)                               #함수에 A의 값인 1을 지정
print(cnt)
############################

# 경로 탐색하여 최소비용 구하기 (글로벌 선언활용)
name = ["A","B","C","D","E"]
start = input()
start = ord(start) - 65
arr = [
     [0,4,0,0,0], #A
     [0,0,1,2,9], #B
     [5,0,0,7,0], #C
     [0,0,0,0,1], #D
     [0,0,0,0,0], #E
]
used = [0] * len(name)
Min = 20
sum = 0
def dfs(now):
    global Min
    global sum

    if now ==4:
        if sum < Min:
            Min = sum
        return
    for x in range(5):
        if arr[now][x] > 0 and  used[x] == 0:
            sum += arr[now][x]
            used[x] = 1
            dfs(x)
            used[x] = 0
            sum -= arr[now][x]

used[start] = 1
dfs(start)
print(Min)
######################

## 경로 탐색하여 최소비용 구하기(매개변수 활용)
name = ["A","B","C","D","E"]
arr = [
     [0,4,0,0,0], #A
     [0,0,1,2,9], #B
     [5,0,0,7,0], #C
     [0,0,0,0,1], #D
     [0,0,0,0,0], #E
]

start = input()
start_index = 0
used = [0] * len(name)
Min = 20
sum = 0

def dfs(now,sum):
    global Min
    if name[now] =="E":
        if sum < Min:
            Min = sum
        return

    for x in range(5):
        if arr[now][x] > 0 and  used[x] == 0:
            used[x] = 1
            dfs(x,sum + arr[now][x])   #매개변수로 sum 값 넘겨주기
            used[x] = 0


for i in range(5):              #들어갈  start지점 구하기
    if name[i] == start:
        start_index = i


used[start_index] = 1
dfs(start,0)
print(Min)































