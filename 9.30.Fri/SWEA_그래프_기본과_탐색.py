# 14166 5251. [파이썬 S/W 문제해결 구현] 7일차 - 최소 이동 거리
import heapq

def dijkstra(st):
    heapq.heappush(heap,[0,st])   # heap에 비용, 경유지 넣기!
    result[st] = 0                # 시작 정점에 0을 놓고 시작
    while heap:
        cost,via = heapq.heappop(heap)  # 힙에 넣은 비용과 경유지를 뽑아내서 
        if result[via]<cost: continue   # 만약 result배열에 있는 경유지로 가는값(혹은 바로 도착지로 가는 값)이 작으면 다음 heappop으로
        for i in lst[via]:              # 배열
            money = cost+i[1]
            if money<result[i[0]]:
                result[i[0]] = money
                heapq.heappush(heap,[money,i[0]])
    
T = int(input())
for tc in range(1,T+1):
    N,E = map(int,input().split())  # 도착 번호, 간선 개수
    lst = [[] for _ in range(N+1)]  # 출발,도착,비용을 넣을 배열 생성
    result = [21e8]*(N+1)           # 비용 기록할 result 생성(처음에는 가장 큰 값 넣어놓기)
    st,ed = 0,N                     # 0번 정점, 목표 정점
    heap = []
    for i in range(E):
        a,b,c = map(int,input().split())
        lst[a].append([b,c])        # 출발,도착,비용을 받아서 -> 배열의 [출발] idx에 경유번호와 비용 넣기
    dijkstra(st)            
    print(f"#{tc} {result[N]}")