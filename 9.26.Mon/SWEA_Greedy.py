# 14159 베이비진 게임
T = int(input())
for tc in range(1,T+1):
    num = list(map(int,input().split()))
    player_1, player_2 = [], []
    ret = 0
    
    for i in range(len(num)):
        if ret!=0: break
        if i%2==0: player_1.append(num[i])
        else: player_2.append(num[i])
        player_1.sort(), player_2.sort()
        # print(player_1,player_2,i)

        for j in range(len(player_1)):
            if player_1.count(player_1[j]) ==3: 
                ret = 1
                break
            if i%2:
                if player_2.count(player_2[j]) ==3: 
                    ret = 2
                    break
        if i>=2:
            for j in range(len(player_1)):
                    if player_1[j] - player_1[j-1]==1 and player_1[j]-player_1[j-2]==2: 
                        ret = 1
                        break
                    if  i%2:
                        if player_2[j] - player_2[j-1]==1 and player_2[j]-player_2[j-2]==2: 
                            ret = 2
                            break
    print(f"#{tc} {ret}")
# --------------------------------------------------
def iswinner(player):
    # 동일한 숫자 3개이상인지 check
    for i in range(len(player)):
        if player[i]>=3: return True
    #연속된숫자판별
    for i in range(8):
        if player[i]>0 and player[i+1]>0 and player[i+2]>0: return True

T = int(input())
for tc in range(1,T+1):
    cards = list(map(int,input().split()))
    p1,p2 = [0]*10, [0]*10
    ret = 0
    for i in range(len(cards)):
        # 플레이어 1 뽑기
        if i%2==0:
            p1[cards[i]] += 1
            if iswinner(p1):
                ret = 1         # p1이 이기면 result를 0으로 만들어주고 break
                break
        # 플레이어 2 뽑기
        if i%2:
            p2[cards[i]] += 1
            if iswinner(p2):
                ret = 2         # p2가 이기면 result를 0으로 만들어주고 break
                break
    print(f"#{tc} {ret}")
#-----------------------------------------------------------------------
# 14158 화물 도크
T = int(input())
for tc in range(1,T+1):
    N = int(input())
    lst = [list(map(int,input().split())) for _ in range(N)]
    lst.sort(key=lambda x: x[1])    # 먼저 시간대별로 정렬

    ed,cnt =  -1, 0                 # 시작시간이 끝나는 시간보다 크거나 같다면 그 작업 수행(=시작시간이 곧 이전타임의 끝나는 시간)
    for i in range(len(lst)):
        if lst[i][0]>=ed:
            ed = lst[i][1]
            cnt += 1
    print(f"#{tc} {cnt}")


# 14157 컨테이너 운반
T = int(input())
for  tc in range(1,T+1):
    N,M = map(int,input().split())
    cargo = list(map(int,input().split()))
    truck = list(map(int,input().split()))
    cargo.sort(reverse=True), truck.sort(reverse=True)  # 무거운 순으로 역순으로 정렬
    
    weight,chance,idx = 0, len(truck),0                 # 무게, 트럭 대수만큼의 기회, 트럭 idx
    for i in range(len(cargo)):
        if chance ==0: break
        if cargo[i] <= truck[idx]:                      # 화물이 트럭에 들어가면 
            weight += cargo[i]                          # 그 무게만큼 싣고
            chance -=1                                  # 트럭 대수 -1하고
            idx += 1                                    # 다음 트럭으로 idx 옮겨주고
    
    print(f"#{tc} {weight}")

# 1970 쉬운 거스름돈
Money = [50000,10000,5000,1000,500,100,50,10]
T = int(input())
for tc in range(1,T+1):
    N = int(input())
    bucket = [0] * len(Money)       # 각 단위별 버켓 생성
    for i in range(8):
        if N//Money[i] !=0:         # 잔돈을 나눴을 때 몫이 0이 아닌경우 즉, 나눌 수 있다면
            cnt= N//Money[i]        # 잔돈을 큰 단위의 돈부터 나눠보고
            N -= cnt * Money[i]     
            bucket[i] += cnt        # 해당 갯수만큼 단위에 +
    print(f"#{tc}")
    print(*bucket)






