'''
 - 무향 그래프(Undirected Graph)
 - 유향 그래프(Directed Graph)
 - 가중치 그래프(Weighted Graph)
 - 사이클 없는 방향 그래프(DAG, Directed Acyclic Graph)

 - 완전 그래프: 정점들에 대해 가능한 모든 간선들을 가진 그래프
 - 부분 그래프: 원래 그래프에서 일부의 정점이나 간선을 제외한 그래프


'''

'''
6 8  마지막 정점번호(0번부터 시작), E 간선의 수
0 1 0 2 0 5 0 6 4 3 5 3 6 4 5 4
'''
V,E = map(int,input().split())
arr = list(map(int,input().split()))

# 인접행렬
adjM = [[0]*(V+1) for _ in range(V+1)]  # 인접행렬
adjList = [[] for _ in range(V+1)]

for i in range(E):
    n1,n2 = arr[i*2], arr[i-2+1]
    adjM[n1][n2] = 1
    adjM[n2][n1] = 1    # 방향이 있으면 이걸 삭제


    adjList[n1].append(n2) # 1차원 배열에 저장
    adjList[n2].append(n1) # 1차원 배열에 저장

print()


