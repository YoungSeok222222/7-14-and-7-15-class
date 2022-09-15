# 복습
'''
각 항에서 1~4 사이의 숫자를 1개씩 택해서 다
더했을떄 10이 나오는 경우는 몇가지 인가요?
n 개의 항에서 1~4 사이의 숫자를 택할 것입니다.
'''

# def dfs(lv,sum):
#     global cnt
#     if lv ==n: 
#         if sum==10:
#             cnt += 1
#         return

#     for i in range(1,5):
        
#         dfs(lv+1,sum+i)
        


# n = int(input())
# cnt = 0
# dfs(0,0)
# print(cnt)



#####
'''
# 4명이 놀이동산에 갔습니다. [M B T I]
# 놀이기구를 타는데 1 unit에 3명이 앉을 수 있습니다.
# 4명중에 1명이 고소공포증이 있어서 놀이기구를 안탄다고 합니다.
# 놀이기구를 탈 조합을 모두 출력해 주세요.
'''
# arr = ["M", "B", "T", "I"]

# path = [0] * 3

# def dfs(lv,st):
#     if lv ==3: 
#         for i in range(lv):
#             print(path[i],end=' ')
#         print()
#         return
    
#     for i in range(st,4):
#         path[lv] = arr[i]
#         dfs(lv+1,i+1)
#         path[lv] = 0
      
# dfs(0,0)


#########
'''
line1=[3,7,1,-3,-6,1]
line2=[7,-4,1,-5,3,2]

두 라인에서 숫자를 1개씩 번갈아 가며 선택을
하고자 합니다. 
첫번째 라인에서 숫자를 1개 택한 후 *1을 하고
두번째 라인에서 숫자를 1개 택한 후 *2를 하고
첫번쨰 라인에서 숫자를 1개 택한 후 *3을 하고..
두번째 라인에서 숫자를 1개 택한 수 *4를 하는등
가중치가 1씩 증가되는 값으로 뽑은 숫자에 곱해 줍니다.

가중치를 곱한 후 모두 더했을때 
합이 0에 가장 가까운 수를 구하고자 합니다.
이때 총 합은 몇일까요?
(각 라인의 숫자는 1번씩만 사용하여 모든 숫자를 한번씩 뽑습니다.)
'''

# 설계 시...
# 그림 그려보기
# dfs 함수 (매개변수 or 전역변수) // 리턴 조건 // dfs 몇 번 호출 // used 사용 여부


# line1 = [3,7,1,-3,-6,1]
# line2 = [7,-4,1,-5,3,2]

# path1,used1 = [0] * 6, [0] * 6
# path2,used2 = [0] * 6, [0] * 6


# min = 21e8
# answer = 21e8

# def dfs(lv,sum):
#     global min, answer
#     if lv == 12: 
#         # 0에 가장 가까운 sum
#         if min > abs(sum):
#             min = abs(sum)
#             answer = sum
       
#         return

#     if lv %2==0:
#         for i in range(6):
#             if used1[i] == 1:continue
#             used1[i] = 1
#             dfs(lv+1, sum+line1[i]*(lv+1))
#             used1[i] = 0
#     else:
#         for i in range(6):
#             if used2[i] ==1: continue
#             used2[i] =1
#             dfs(lv+1, sum+line2[i]*(lv+1))
#             used2[i] = 0
# dfs(0,0)  # lv, sum
# print(answer)
#################

'''
# power=[50,40,99,5,25,6,37]
#            a  ,b ,c  ,d, e ,f, g

# 서바이벌 게임
# a ~ g 를 두팀으로 나누어서 
# 게임을 하고자 합니다.
# 두 팀으로 나누었을때
# 두 팀의 전투력 차이가 최소가 되었을때
# 최소 전투력 차이는 몇일까요?
# 모든 선수는 경기에 참가를 하며
# 1인팀도 가능 합니다.
'''
# power = [50,40,99,5,25,6,37] # A B C D E F G
# used = [0] * len(power)
# Min = 21e8

# def dfs(lv,st,sum):
#     global Min, power
#     against = 0
#     for i in range(7):
#         if used[i] == 0:
#             against += power[i]
#     gap = abs(sum - against)
#     Min = min(Min,gap)

#     if lv==6:
#         return

#     for i in range(st,7):
#         if used[i] == 1: continue
#         used[i] = 1
#         dfs(lv+1,i+1,sum+power[i])
#         used[i] = 0

# dfs(0,0,0) # lv,st, sum
# print(Min)
##########################################
'''
[7 3 5 4]
각각의 숫자에 
2를 곱하거나 또는
3으로 나누거나 또는
5를 더해서 숫자를 바꾼 후

바뀐 4개의 숫자들의 곱을 구한 후
그 곱의 Max값을 출력해 주세요.

(추가설명)
7 3 5 4 가 있다면
7에 2를 곱하거나 3으로 나누거나 5을 더한 값으로 바꿈
3에 2를 곱하거나 3으로 나누거나 5을 더한 값으로 바꿈
5에 2를 곱하거나 3으로 나누거나 5을 더한 값으로 바꿈
4에 2를 곱하거나 3으로 나누거나 5을 더한 값으로 바꿈

바뀐 숫자들을 모두 곱했을때 MAX 값 출력하기
'''
# n = int(input()) # 4 입력 받았다고 가정 
# arr = [7,3,5,4]

# Max = 21e8
# '''
# lv = n(4)
# br = 3 (*2,//3,+5)
# '''
# def dfs(lv,gop):
#     global Max
#     if lv == n: 
#         Max = max(Max,gop)       
#         return

#     for i in range(3):
#         pass

#     dfs(lv+1,gop*(arr[lv]*2))
#     dfs(lv+1,gop*(arr[lv]//3))
#     dfs(lv+1,gop*(arr[lv]+5))

# dfs(0,1)
# print(Max)

#####
# 다른 풀이법 (원상복구)
# n = int(input()) # 4 입력 받았다고 가정 
# arr = [7,3,5,4]
# Max = 21e8

# def dfs(lv):
#     global Max
#     if lv==4:
#         gop = 1
#         for i in range(4):
#             gop *= arr[i]
#             Max = max(max,gop)
#         return
#     backup = arr[lv]

#     arr[lv] *= 2
#     dfs(lv+1)
#     arr[lv] = backup     # 원상복구

#     arr[lv] /= 3
#     dfs(lv+1)
#     arr[lv] = backup     # 원상복구 arr[level]*=3 (X)

#     arr[lv] += 5
#     dfs(lv+1)
#     arr[lv] = backup     # 원상복구

# dfs(0)
# print(Max)
#######


'''
땅파기 문제
땅을 개척작업을 통해 
가치를 올리고자 합니다.
(위아래좌우그리고 자기자신의 가치가 *7한수 %10한 값으로 바뀜)

총 3곳을 개발할 예정..
중복가능( 한번 개발한 했던곳을 또 개발 가능)
개발후 3*3배열의 땅의가치가 MAx가 되었을때
그 MAx값을 출력해 주시면 됩니다.
'''
arr = [
    [4,2,1],
    [5,3,9],
    [7,8,1]
]

import copy

Max=-21e8

def digging(y,x):
    directy=[0,-1,1,0,0]
    directx=[0,0,0,-1,1]
    for i in range(5):
        dy=directy[i]+y
        dx=directx[i]+x
        if dy<0 or dx<0 or dy>2 or dx>2: continue
        arr[dy][dx]=(arr[dy][dx]*7)%10

def getsum():
    sum=0
    for i in range(3):
        for j in range(3):
            sum+=arr[i][j]
    return sum

def dfs(level):
    global Max,arr
    backup=copy.deepcopy(arr)

    if level==3:                    # 3번 땅파기 때문에 3이면 return
        ret=getsum()                # 3번 파놓은 arr의 총 합 비교를 위해 getsum함수 호출
        Max=max(Max,ret)            # Max 값과 ret 값 중 큰 값이 곧 Max 값
        return

    for i in range(3):              # 총 9번 탐색(0,0 ~ 2,2)
        for j in range(3):              
            digging(i,j)            # 땅파고
            dfs(level+1)            # 함수 호출
            arr=copy.deepcopy(backup)   # 리턴되고 원상복구

dfs(0)
print(Max)

















