# 우선순위 큐(Priority Queue)

# 큐 : FIFO
# 스택 : FILO

import heapq # 우선순위 큐를 사용하기 위한 모듈

arr = [] # 모듈함수를 사용할 떄 이 arr 리스트에 인자값을 담을것이다.

heapq.heappush(arr,4)   # 최소힙 디폴트-> 값이 가장 작은 것이 우선순위 따라서 0번 인덱스에 2가 있음
heapq.heappush(arr,15)
heapq.heappush(arr,2)
heapq.heappush(arr,7)
heapq.heappush(arr,5)
heapq.heappush(arr,9)

# print(heapq.heappop(arr))   # 출력되는 것은 log n 속도로 우선순위가 가장 높은 값을 출력
# print(heapq.heappop(arr))
# print(heapq.heappop(arr))
# print(heapq.heappop(arr))
# print(heapq.heappop(arr))
for i in range(len(arr)):
    print(heapq.heappop(arr),end=' ')

# ------------------------------------------------------------------

import heapq
# pq 사용하여 최소값부터 출력이 되도록 코드 적어보기

# 1번 방법
arr = [4,3,4,24,8,23,87,7,4] # pq 사용하여 최소값부터 출력이 되도록 코드 적어보기

lst = []
for i in range(len(arr)):               # 빈 리스트 lst에 heappush로 arr 원소들을 추가
    heapq.heappush(lst,arr[i])

for j in range(len(arr)):               # 추가된 lst 배열들을 heappop으로 출력
    print(heapq.heappop(lst),end=' ')


# 2번 방법
MM = [4,3,4,24,8,23,87,7,4] 
heapq.heapify(MM)   # MM 배열을 한 번에 heap 자료형으로 바꾸기(즉, pop 전에는 루트노드만 가장 작은 수 와있고 정렬은 안 됐음)

for i in range(len(MM)):                # pop할때 뺴고 정리되고 하는 식
    print(heapq.heappop(MM))

#----------------------------------------------------------------------------------

# 최대값 구하기
# 1번 방법
arr = [4,3,4,24,8,23,87,7,4] 

lst = []
for i in range(len(arr)):
    heapq.heappush(lst,-arr[i])             # Max heap을 출력하는 내장함수가 없기 때문에 -를 붙여서 저장 
    print(lst)                              # [-87, -8, -24, -7, -4, -4, -23, -3, -4]

for j in range(len(arr)):
    print(heapq.heappop(lst)*-1,end=' ')    # -로 저장됐기 때문에 출력할 때 -1을 곱한다.
print()

# 튜플을 이용한 방법
# 2번 방법
M = [4,3,4,24,8,23,87,7,4] 
MM = []
for i in range(len(M)):
    heapq.heappush(MM,(-M[i],M[i]))

for i in range(len(M)):
    print(heapq.heappop(MM)[1])


# lambda를 이용한 방법
vect = [3,6,3,1,7,9]
rev = lambda x: x*-1            # 함수 생성
heap1 = list(map(rev,vect))     # 함수를 적용한 것을 heap1이라는 리스트에 저장  [-3, -6, -3, -1, -7, -9]

heapq.heapify(heap1)            # heap의 형태로 저장 [-9,-7,-3,-1,-6,-3]


for i in range(len(vect)):
    print(-heapq.heappop(heap1))

# -------------------------------------------------------------------------

# 카드 섞기 문제 
import heapq
n = int(input())
card = []

for i in range(n):
    heapq.heappush(card,int(input()))

answer = 0
while len(card)>1:
    temp1=heapq.heappop(card)
    temp2=heapq.heappop(card)
    answer += (temp1+temp2)
    heapq.heappush(card,temp1+temp2)


