# Floyd Warshall 최단경로(최소비용)
'''
플로이드와샬 연습문제

경로찾기
https://www.acmicpc.net/problem/11403

타임머신
https://www.acmicpc.net/problem/11657

키순서
https://www.acmicpc.net/problem/2458
'''

'''
최단 경로 검색 알고리즘
Dijkstra -> 음수 X
Bellmanford -> 음수 가능(음의 cycle 없어야함)
Floy Warshall -> 음수 가능(음의 cycle 없어야함)
'''
#======================================================
inf = int(21e8)
lst = [
    [0,5,inf,8],
    [7,0,9,inf],
    [2,inf,0,4],
    [inf,inf,3,0]
]

for via in range(4):
    for s in range(4):
        for e in range(4):
            if lst[s][e] > lst[s][via] + lst[via][e]:
                lst[s][e] = lst[s][via] + lst[via][e]

for g in lst:
    print(*g)
print()

for i in range(4):
    for j in range(4):
        print(lst[i][j],end=' ')
    print()