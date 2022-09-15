'''
Minimum Span Tree(최소 신장트리)

Kruskal 알고리즘(Kruskal의 기초는 union find)


5       정점의 개수
8       간선의 개수
C D 1   간선의 정보 입력
A B 9
A C 3
A E 7
B D 11
A D 20
B C 14
C E 5

입력 후 비용 기준으로  sort
간선의 개수 만큼 for문 돌리면서 union(그룹화)하기
단 그룹화를 (간선의 개수 -1)개 시키는데..
그룹화에 성공하면 비용을 더해 준다.
이미 같은 그룹이면 넘어가기!!

'''


N = int(input())    # 정점 개수
M = int(input())    # 간선 개수

lst = [list(input().split()) for _ in range(M)]
lst.sort(key=lambda x: int(x[2]))
arr = [0] * 200




def findboss(member):
    if arr[ord(member)] == 0: return member
    ret = findboss(arr[ord(member)])
    arr[ord(member)] = ret
    return ret




def union(a,b,i):
    global answer,cnt
    a_boss,b_boss = findboss(a), findboss(b)
    if a_boss == b_boss: return
    answer += int(lst[i][2])    # 비용 더하기
    cnt += 1                    # 간선의 개수 더하기
    arr[ord(b_boss)] = a_boss





answer = 0 # 비용을 더할 변수
cnt = 0 # 간선의 개수를 더할 변수
for i in range(M):
    if cnt == N-1: # cnt 간선의 개수 -1 개와 같으면
        print(answer)
        break
    union(lst[i][0],lst[i][1],i)

























