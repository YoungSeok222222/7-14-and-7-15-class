# ####
#리스트 중 max값 구하기
# number = [3,6,21,4,7]
# max = 0
# for num in number:
#     if max < num:
#         max = num
# print(max)

####
#리스트 안 값들의 합 구하기
# number = [3,6,21,4,7]

# total = 0

# for i in number:
#     total += i
# print(total)


#####
#리스트 안에 최대값과 그 최대값의 등장 횟수구하기
# number = [21,6,21,4,7]
# max = 0
# count = 0
# for num in number:
#     if max < num:
#         max = num

# for i in number:
#     if  i == max:
#         count +=1
# print(max,count)

#####
# 리스트 안 요소 하나씩 출력
# for i in range(len(number)):
#     print(number[i])

##########################################
# 선택 정렬
# a = [4,7,1,3,5,2]

# for i in range(len(a)-1):
#     for j in range(i+1,len(a)):
#         if a[i] > a[j]:
#             #swap
#             a[i],a[j] = a[j],a[i]

# for i in range(len(a)):
#     print(a[i], end='')
#############################

# insert sort(삽입 정렬) / O(n**2)

# a = [4,7,1,3,5,2]
# result = []
# for i in range(len(a)):
#     result.append(a[i])  # 값 하나씩 내리기
#     for j in range(i,0,-1): #뒤에서부터.. 앞으로 가면서
#         if result[j-1] > result[j]: # 현재 vs 앞의 값 비교
#             result[j],result[j-1] = result[j-1], result[j]
#         else:
#             break
# print(result)
#######################################    
#bubble sort(버블 정렬)
# a = [8,3,12,10,1]
# for i in range(len(a)-1,0,-1): # 4 3 2 1
#     for j in range(0,i): # i가 4일 때 0123 i가 3일 때 012...
#         if a[j] > a[j+1]:
#             a[j], a[j+1] = a[j+1], a[j]



# a = [8,3,12,10,1]


# for i in range(len(a)): # 0 1 2 3
#     for j in range(0,len(a)-2-i): # 0부터 3 2 1 0
#         if a[j] > a[j + 1]:
#             a[j], a[j+1] = a[j+1], a[j]

#######################################
# Direct Addressing Table 자료구조 (빠른 검색을 위해)
#단점: 리스트 안에 음수가 들어간 경우 사용하기 힘듬 / range의 범위가 크면 메모리를 비효율적으로 사용

#기본 풀이법
# a = [4,7,1,3,4,1,2,4]
# b = list(map(int,input().split())) # 3 4 5 7
# cnt = 0
# for i in range(len(b)):
#    for j in range(len(a)):
#     if b[i] == a[j]:
#         cnt += 1
#     print(f"{b[i]}의 갯수: {a[j]}")

#Direct Addressing Table로
# a = [4,7,1,3,4,1,2,4]
# n = int(input())
# b = list(map(int,input().split())) # 3 4 5 7


#b리스트의 값이 a 리스트 안에 각각 몇개 존재 출력
# bucket = [0] * 10
# #a의 값을 bucket에 등록
# for i in range(len(a)):
#     bucket[a[i]] += 1

# for i in range(len(b)):
#     print(f"{b[i]}: {bucket[b[i]]}개 존재")

####
# n = int(input())
# a = list(map(int,input().split()))
# bucket = [0] * 101

# for i in range(n):
#     bucket[a[i]] += 1
    
# for i in range(len(b)):    
#     if bucket[i] > 0:
#         print(f"{i} : {bucket[i]}개 존재함")

###


#######################
#카운팅 개수 정렬
# n = int(input())
# a = list(map(int,input().split()))
# bucket = [0] * 101
# #dat 등록

# for i in range(n):
#     bucket[a[i]] += 1


# for j in range(1,len(bucket)):
#     bucket[j] += bucket[j-1]
#     #buck[j] = bucket[j] + bucket[j-1]


# #값 넣기
# result = [0] * 101
# for i in range(n):
#     index = a[i]
#     result[bucket[index]-1] = index
#     bucket[index] -= 1

# for i in range(n):
#     print(result[i],end=' ')



####################
#그리디 정렬

coin = [100, 50, 10]
change = int(input()) #거슬러 줄 돈
answer = 0     #  총 동전 사용 개수

index = 0
while (1):
    cnt = change// coin[index]    #cnt = 
    change = (cnt*coin[index])    # 나머지 거슬러 줘야 할 돈 50
    answer += cnt
    index += 1 # 그 다음 50원 동전 사용하기 위해 index 1 증가
    if index ==3:
        break
print(answer)

########################
arr=[3,6,5,8,5,3,5,8,5,3,3,1,1,3]
pattern=[3,5,8,4]
flag=0
def isPattern(index):
    for i in range(4):
        if arr[index+i]!=pattern[i]:
            return 0
    return 1

for i in range(11):   # 0 ~ 10
    ret=isPattern(i)
    if ret==1:
        flag=1
        break

if flag:
    print("패턴존재")
else:
    print('패턴은 존재하지 않음')
#######################################
#응용
board = [
    ["A", "B", "G", "K"],
    ["T", "T", "A", "B"],
    ["A", "C", "T", "T"]
]

ptn = [list(input()) for _ in range(2)]

def findptn(dy,dx):
    for i in range(2):
        for j in range(2):
            if board[dy+i][dx+j]!=ptn[i][j]:
                return 0
    return 1


cnt=0
for y in range(2):
    for x in range(3):
        if findptn(y,x):    #0,0 ~~ 1,2
            cnt+=1
if not cnt:
    print("미발견")
else:
    print("발견")