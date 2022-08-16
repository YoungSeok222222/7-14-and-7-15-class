###### 재귀로 누적합 구하기
# 전역변수 선언하고 구하기
arr = [3, 4, 5, 1, 6, 9]
sum = 3


def abc(index):
    global sum
    if index == 5:
        print(sum)
        return

    print(index)
    sum += arr[index]
    abc(index + 1)


abc(0)
###################################################
#매개변수로 누적합 구하기
arr = [3, 4, 5, 1, 6, 9]
def abc(level, sum):
    if level == 5:
        print(sum)
        return
    print(sum)
    abc(level+1,sum + arr[level+1])


abc(0,3)
#######################
arr=[3,4,5,1,6,9]

# 그전에는 누적합을 3 7 12 13 19 28 이렇게 출력 했다면..
# 이번에는 28 19 13 12 7 3
###매개 변수로 구하기

def abc(level,sum):
    if level==5:
        print(sum)
        return
    abc(level+1,sum+arr[level+1])
    print(sum)

abc(0,3)


######################
#전역변수로 구하기
sum=3
def abc(level):
    global sum
    if level==5:
        print(sum)
        return
    sum+=arr[level+1]
    abc(level+1)
    sum-=arr[level+1]
    print(sum)

abc(0)
###########
#누적합 구해서 출력하고 역으로 또 출력
#매개변수
#5 14 21 24 25 30 36 40 36 30 25 24 21 14 5
arr = [5,9,7,3,1,5,6,4]

def abc(index,sum):
    sum += arr[index]
    print(sum)

    if index ==7:
        return


    abc(index+1,sum)
    print(sum)

abc(0,0)
###

#누적합 구해서 출력하고 역으로 또 출력
#전역변수
arr = [5,9,7,3,1,5,6,4]
#5 14 21 24 25 30 36 40 36 30 25 24 21 14 5
sum = 5
def abc(index):
    global sum
    if index ==7:
        print(sum,end=' ')
        return
    print(sum,end=' ')
    sum += arr[index+1]
    abc(index+1)
    sum -= arr[index+1]
    print(sum,end=' ')

abc(0)
##################
#개구리 점프 / 0번 인덱스 값 2 -> 2만큼 점프 -> 2번 인덱스 값 1-> 1만큼 점프
arr = [2,0,1,1,3,5,1]
def abc(index):
    if index >6:
        return


    abc(index+arr[index])
    print(arr[index],end=' ')

abc(0)
##########
# 3개의 카드 묶음에서 1장씩 뽑았을때
# 나올 수 있는 모든 합들을 출력해 주세요
#매개변수
# lv=3
# br=4
arr = [3,7,1,5]


#lv= 3
#br = 4
def abc(level, sum):
    if level ==3:
        print(sum,end=' ')
        return

    for i in range(4):
        abc(level+1,sum+arr[i])

abc(0,0) # level sum

########
#전역변수
sum = 0
def abc(level):
    global sum
    if level==3:
        print(sum, end=' ')
        return

    for i in range(4):
        sum+=arr[i]
        abc(level+1)
        sum-=arr[i]

abc(0) # level

#########
# 최소동전사용개수 (동전교환기)
changes = int(input())
coin = [100,70,10]
# br = 3
# lev ??  -> changes가 음수
Min = int(21e8)
def abc(level,chan):
    global Min
    if chan < 0:
        return

    if chan == 0:
        if level < Min:
            Min = level
        #최소레벨 확인


    for i in range(3):
        abc(level+1,chan-coin[i])


abc(0,changes)
print(Min)
#################
# 재귀경로 출력하기
arr = ["A","B","C"]
path = [''] * 5
def abc(lv):

    if lv == 2:
        for i in range(lv):
            print(path[i],end=' ')
        print()
        return

    for i in range(3):
        path[lv] = arr[i]
        abc(lv+1)
        path[lv] = 0

abc(0)
##################
#주사위 n개 합 (중복순열)
n = int(input())     #주사위 갯수
dice =  [1,2,3,4,5,6]
path = ['']  * n  # 최대 레벨까지 size 맞추면 오케이

def abc(lv):
    if lv ==n:
        for i in range(lv):
            print(path[i], end=' ')
        print()
        return

    for i in range(6):
        path[lv] = dice[i]
        abc(lv+1)


abc(0)
####################
#순열
n = int(input())
path = [''] * n  # 최대 레벨 까지 size 맞추면 오케이
dice = [1, 2, 3, 4, 5, 6]
used = [0] * 6  # br의 개수 만큼 만들기


def abc(level):
    if level == n:
        for i in range(level):      #몇 개 까지 출력할껀지
            print(path[i], end=' ')
        print()
        return

    for i in range(6):      # br(가지) 갯수

        # if used[i]==0:
        if used[i] == 1: continue
        path[level] = dice[i]
        used[i] = 1
        abc(level + 1)
        used[i] = 0
        path[level] = 0


abc(0)
####################
## abcd 중 c로 시작하는 경우를 모두 제외하고 출력하기
arr = ["A", "B", "C", "D"]
path = [0] * 10


def abc(lv):
    # if lv ==3 and path[lv-1] == "C": return # C로 시작하는 것만 빼고 출력하는 경우

    if lv == 3:
        for i in range(lv):
            print(path[i], end=' ')
        print()
        return

    for i in range(4):
        # if lv ==0 and arr[i] == "c":continue      # C로 시작하는 것만 빼고 출력하는 경우
        # if path[0] == "C": continue               # C로 시작하는 것만 빼고 출력하는 경우
        path[lv] = arr[i]
        abc(lv + 1)
        path[lv] = 0


abc(0)
#################
#모든 B 빼고 출력
def abc(lv):
    if lv > 0 and path[level-1] == "B": return
    if lv ==3:
        for i in range(lv):
            print(path[i],end=' ')
        print()
        return
    for i in range(4):
        if i== 1: continue
        path[lv] = arr[i]
        used[i] = 1
        abc(lv+1)
        used[i] = 0
        path[lv] = 0

abc(0)
###################

#ABCD 중에 연속해서 2장의 카드가 나오면 안되는 경우!!
arr=['A','B','C','D']
path=['']*10


def abc(level):
    if level>1 and path[level-1]==path[level-2]: return
    if level==3:
        for i in range(level):
            print(path[i],end=' ')
        print()
        return

    for i in range(4):
        if level>0 and (path[level-1]== arr[i]):continue
        path[level]=arr[i]
        abc(level+1)

abc(0)
