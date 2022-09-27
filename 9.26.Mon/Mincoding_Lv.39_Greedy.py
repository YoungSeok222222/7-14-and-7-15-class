# 1번 화장실 대기시간 줄이기
lst = list(map(int,input().split()))
lst.sort(key=lambda x: -x)      # 역순 정렬

answer = 0
for i in range(len(lst)-1,-1,-1):   
    answer += i*lst[i]          # 역순 정렬한 것을 바탕으로 for문을 역으로 3부터 돌려서 가장 마지막(가장 작은 값)을 i만큼(3->2->1->0) 곱한걸 더해줌
print(answer)

# 2번 동전교환
coin = [10,50,100,500]
coin.sort(key=lambda x: -x)

change = int(input())
answer = 0

for i in range(4):
    if change // coin[i] !=0:       # 잔돈을 코인으로 나눴을 때 몫이 0이 아닌 경우(즉 ,나눌 수 있는 경우)
        cnt = change//coin[i]       # 몇 개로 나눌 수 있는지 갯수 구하고
        change -= cnt*coin[i]       # 잔돈 -= 갯수*동전
        answer += cnt               # 동전 몇개 썼는지 각 동전별 개수 만큼 더하기
print(answer)

# 3번 회의실 배정
n = int(input())
lst = [list(map(int,input().split())) for _ in range(n)]
lst.sort(key=lambda x: x[1])    # 처음에 끝나는 시간별로 정렬

cnt = 1
st = lst[0][1]                  # st를 정렬 맨 앞 회의시간의 끝나는 시간으로 설정 
for i in range(n):              # for문 돌면서 처음 회의의 끝나는 시간보다 같거나 이후면 갱신하고 cnt += 1
    if st <= lst[i][0]:
        st = lst[i][1]
        cnt +=1

print(cnt)


# 4번 막대 블럭 채우기
block = 100
n = int(input())
lst = list(map(int,input().split()))
lst.sort(key=lambda x: x)           # 오름차순으로 정렬

cnt = 0
for i in range(n):                  
    if block-lst[i]<0: break        # 100cm에서 배열의 작은 것들을 하나씩 빼는데 만약 뻈을 때 0보다 작으면 그 즉시  break
    block -= lst[i]                 # block을 그 길이만큼 뺌
    cnt += 1                        # 갯수 +1

print(cnt)
