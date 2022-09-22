# atm 문제 (Greedy?)
N = int(input())
lst = list(map(int,input().split()))
bucket = [0] * (N+1)

lst.sort()


for j in range(1,len(lst)):
    lst[j] += lst[j-1]
print(sum(lst))

# ----------------------------------------------
# 교수님 풀이법

n=int(input())
time_w=list(map(int,input().split()))

time_w.sort(reverse=True)   # 내림차순으로 정리
print(time_w)
answer=0
for i in range(1,n+1):
    answer+=(i*time_w[i-1]) # 가장 큰거 1명 기다리고 
                            # 그 다음 큰 거 2명 기다리고..
print(answer)
#---------------------------------------------------------------

# 파티룸 예약 문제(최대한 많은 타임을 예약 받기)  Greedy
n = int(input())
lst = [list(map(int,input().split())) for _ in range(n)]
lst.sort(key=lambda x: x[1])

result = []
result.append(lst[0])

cnt,idx = 1,0
for i in range(1,len(lst)):
    if lst[i][0] >= result[idx][1]:
        result.append(lst[i])
        cnt += 1
        idx += 1

print(cnt)
    

# 교수님 풀이법
arr=[]
n=int(input())
for _ in range(n):
    arr.append(list(map(int,input().split())))

arr.sort(key=lambda x:x[1])

before_time=-1
cnt=0

for i in range(n):
    if before_time<=arr[i][0]:
        before_time=arr[i][1]
        cnt+=1
print(cnt)
#------------------------------------------------------------------
# 최소 비용 경로(DP)
lst = [
    [0,1,1,9],
    [4,2,2,3],
    [1,3,4,1],
    [3,7,8,0]
]

for i in range(1,4):
    lst[0][i] += lst[0][i-1]
    lst[i][0] += lst[i-1][0]

for y in range(1,4):
    for x in range(1,4):
        lst[y][x] += min(lst[y-1][x],lst[y][x-1])

for g in lst:
    print(*g)

# -----------------------------------------------------------------
# knapsack (DP의 대표적인 유형)

# 교수님 코드
n, k = map(int, input().split())
knapsack = [[0 for _ in range(k + 1)] for _ in range(n + 1)]  # 배열

item = [[0, 0]]
for i in range(1, n + 1):  # 아이템 입력
    item.append(list(map(int, input().split())))

for i in range(1, n + 1):  # 아이템 개수만큼 반복
    for j in range(1, k + 1):  # 최대무게까지 반복

        weight = item[i][0]
        value = item[i][1]

        if j < weight:  # 가방에 넣을 수 없으면
            knapsack[i][j] = knapsack[i - 1][j]  # 위에 값 그대로 가져오기
        else: # 가방에 넣을 수 있으면
            knapsack[i][j] = max(knapsack[i - 1][j],value + knapsack[i][j - weight])
            # 위에 값 vs
            # 현재 아이템 가치 + 그전 단계에서 구한 남은무게의 가치

print(knapsack[n][k])

#---------------------------------------------
# 동전 교환 문제(DP)로 풀기
coin=[1,7,10]
n=int(input())
arr = [[0 for _ in range(n+1)] for _ in range(3)]  # 배열
for i in range(3):
    for j in range(n+1):
        mok=j//coin[i]
        if j%coin[i]==0: arr[i][j]=mok
        else:
            if mok==0: arr[i][j]=arr[i-1][j]
            else:
                arr[i][j]=min(arr[i-1][j],mok+arr[i][j%coin[i]])
print(arr[2][n])
