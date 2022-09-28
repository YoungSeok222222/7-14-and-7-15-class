# 다익스트라 인접행렬로 표현

name = "ABCDE"
inf = int(21e8)

arr =[
    [0,3,inf,9,5],
    [inf,0,7,inf,1],
    [inf,inf,0,1,inf],
    [inf,inf,inf,0,inf],
    [inf,inf,1,inf,0]
]

used= [0] * 5
result = [0,3,inf,9,5] 
used[0] = 1 # 시작점 "A"라고 가정함

def select_ky():
    Min=int(21e8)
    Minindex = 0
    for i in range(5):
        if(used[i]==0 and result[i] < Min):
            Min = result[i]
            Minindex=i
    return Minindex
        
def dijkstra():
    for i in range(4):
        via=select_ky()         # 경유지 선택
        used[via] = 1

        for j in range(5):               # 모든 정점에 대한 비용을 비교
            baro=result[j]               # 시->도
            ky=result[via]+arr[via][j]   # 시->경->도
            if baro>ky:                  # 경유가 더 작은 비용이면 갱신
                result[j] =ky

dijkstra()
print(*result)


# 개선된 다익스트라 알고리즘 (1차원 배열)

'''
5 정점의 개수
7 간선의 개수

0 1 3 시작점 도착점 비용
0 3 9
0 4 5
1 2 7
1 4 1
2 3 1
4 2 1
0 3   시작점 알고자 하는 도착점(0번 인덱스에서 3번 인덱스 까지의 최소비용을 구하겠다.)

5
7
0 1 3
0 3 9
0 4 5
1 2 7
1 4 1
2 3 1
4 2 1
0 3
'''

import heapq

name = "ABCDE"
n = int(input())        # 정점의 개수
m = int(input())        # 간선의 개수
arr = [[] for _ in range(n)]

for _ in range(m):
    a,b,c = map(int,input().split())    # 시작점, 도착점, 비용
    arr[a].append((b,c))

st,ed = map(int,input().split())
inf = int(21e8)
result = [inf]*n
heap = []

def dijkstra(st):
    heapq.heappush(heap,(0,st))     # 시작점을 경유지로 놓기(비용, 경유지)
    result[st] = 0                  # 그 다음 부터는 heapq에서 최소 비용을 다음 경유지로 선택

    while heap:
        cost,via=heapq.heappop(heap)    # 시작점에서 경유지까지 비용, via = 선택한 경유지

        if result[via]<cost: continue   # result에서의 업데이트 되어있는 (시작->경유지 값) 비용  vs (방금 뽑은 시작->경유지) 비용

        for i in arr[via]:    # 모든 정점에 대해서(경유지에서 도착할 수 있는 정점을 비교)
            money=cost+i[1]    # money = 시작-> 경유지 비용 + 경유지에서 도착점까지 최소비용
            if money<result[i[0]]:   
                result[i[0]] = money
                heapq.heappush(heap,(money,i[0]))

dijkstra(st)
print(result)
