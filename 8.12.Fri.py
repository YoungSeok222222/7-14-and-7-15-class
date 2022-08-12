# 재귀함수

def abc(level):
    if level ==2:
        return

    abc(level+1)
    debug = 1
abc(0)
###############
def abc(num):
    print(num,end='')
    if num ==5:
        return

    abc(num+1)
    print(num,end='')


abc(1)
####
#654321123456
# def abc(num):
#     print(num,end='')
#     if num ==1:
#         print(num,end='')
#         return
#
#     abc(num-1)
#     print(num,end='')
#
#
# abc(6)

############# 심화
def abc(level):

    if level ==2:
        return

    abc(level+1)
    abc(level+1)
abc(0)

##심화 +2
def abc(level):
    if level == 2:
        return

    for i in range(2):
        abc(level + 1)


abc(0)
#################
#재귀연습 최종
def abc(level):
    print('#', end='')
    if level==2:
       #print('#', end='')
        return
    #print('#', end='')
    for i in range(2):
        #print('#', end='')
        abc(level+1)
        #print('#', end='')
    #print('#', end='')


abc(0)

####################
#슬라이딩 윈도우(sliding window)
n , m = map(int,input().split()) # n-입력받을 정수의 개수 // m -연속된 구간의 크기

arr = list(map(int,input().split())) #arr=[4,7,1,8,9,3,5,8,6,6,9]

Max, sum =0,0

for i in range(m): #처음 m 개의 구간 (0번 인덱스부터 인덱스)의 합 구하기
    sum += arr[i]

for i in range(n-m+1): #i가 0이면
    if sum > Max:
        Max =sum
    if i ==n-m: break
    sum += arr[i+m]
    sum -= arr[i]
print(Max)
##########################
#########################
#투포인터 알고리즘
n,target=map(int,input().split())   # n =6 / target = 5
arr=list(map(int,input().split()))  # 1 2 3 2 5 5


cnt,sum=0,0
high,low=0,0
while(1):
    if sum>target:        # 합이 타겟보다 크면.. (범위를 줄여야 하니까)
        sum-=arr[low]       # sum에서 뺴고
        low+=1              # low 의 index를 1증가
    elif high==n: break # 위의 if문 걸리면 안 하고 넘어감!
    else:
        sum+=arr[high]      # 합이 타겟보다 작거나 같다면
        high+=1             # sum에 더하고 high의 인덱스를 1증가
    if sum==target:
        cnt+=1
print(cnt)

######################
#2중 for문으로 상하좌우 더한 값 중 가장 큰 값 구하기 (8/10)에도 있음
#위아래좌우 좌표들의 합이 가장 큰 곳의 합과. 좌표값 출력하기
arr=[[1,2,3,4],
    [1,2,9,4],
    [1,9,3,9],
    [1,2,9,4]]

def isSum(y,x):  # 0,0
    directy=[-1,1,0,0]
    directx=[0,0,-1,1]
    sum=0
    for i in range(4):
        dy=directy[i]+y
        dx=directx[i]+x
        if dy<0 or dx<0 or dy>3 or dx>3: continue # 배열범위 벗어나면 안됨
        sum+=arr[dy][dx]
    return sum

Max=int(-21e8)
Maxi,Maxj=0,0
for i in range(4):
    for j in range(4):
        ret=isSum(i,j)    # 0,0 ~ 3,3
        if ret>Max:
            Max=ret
            Maxi=i
            Maxj=j
print(Max,Maxi,Maxj)

######################################
#for문 돌리기 feat. 호중님 정답
'''
반시계방향으로 45도 회전된 대각선 합
'''
result = [0]*(2*N-1)
for y in range(N):
    for x in range(N):
        result[(N-1-y)+x] += arr_2d[y][x]
print(result)


'''
왼쪽위 오른쪽 아래 삼각형 합
'''
sum_lu, sum_rd = 0, 0
for y in range(N):
    for x in range(N):
        if N-1-y > x:
            sum_lu += arr_2d[y][x]
        if N-1-y < x:
            sum_rd += arr_2d[y][x]
print(sum_lu, sum_rd)
