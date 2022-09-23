# SWEA Brute_force (완전검색) (7)

# 14156 [파이썬 S/W 문제해결 구현] 2일차 - 전자카트
# 결국 순열을 구하는 문제
def dfs(lv,):
    if lv==N:
        Sum  = 0
        for i in range(N-1):                # 순열을 구했다면 
            Sum += lst[path[i]][path[i+1]]  # 좌표값에 해당하는 값을 더해줘서 반환
        Sum += lst[path[-1]][path[0]]        
        answer.append(Sum)
        return 
            
    for i in range(1,N):                    # 0번칸은 0을 채웠기 때문에 1번부터 시작
        if used[i] ==0:
            used[i] = 1
            path[lv] = number[i]            # 해당 수를 삽입
            dfs(lv+1)
            used[i] = 0
Min = 21e8
T = int(input())
for tc in range(1,T+1):
    answer = []                 # tc돌 때마다 새로운 빈 리스트로 갱신
    N = int(input())
    number =  [j for j in range(N)]     # 0부터 해당 숫자 N까지 리스트로 생성
    used,path = [0] * N, [0] * N
    lst = [list(map(int,input().split())) for _ in range(N)] 
    used[0],path = 1, 0
    dfs(1)                      # 1부터 dfs 시작
    print(f"#{tc} {min(answer)}")
# ar = []
# for i in range(1,3+1):
#     for j in range(1,3+1):
#         if i==j: continue
#         if j 
#         ar.append([i,j])
# print(ar)
# ar.pop()
#----------------------------------------------------

# 14155 [파이썬 S/W 문제해결 구현] 2일차 - 최소합
T = int(input())
for tc in range(1,T+1):
    N = int(input())
    lst = [list(map(int,input().split())) for _ in range(N)]
    for i in range(1,N):            # 밑에 1번과정 참조
        lst[0][i] += lst[0][i-1]
        lst[i][0] += lst[i-1][0]

    for y in range(1,N):            # 밑에 2번과정 참조
        for x in range(1,N):
            lst[y][x] += min(lst[y-1][x],lst[y][x-1])
    print(f"#{tc} {lst[N-1][N-1]}")
'''
1 2 3        
2 3 4
3 4 5
------
1 3 6   # 1번 과정은 0,1 = 0,0 + 0,1  / 0,2 =  0,1 + 0,2
3 6 10  
6 10 15 # 2번 과정은 위에 좌표와 좌측 좌표 값 중 가장 작은 값을 더해서 최종적으로 N-1,N-1 좌표에는 최소값이 생성
'''
#----------------------------------------------------

# 2382 [모의 SW 역량테스트] 미생물 격리


# 1249 [S/W 문제해결 응용] 4일차 - 보급로