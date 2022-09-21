# SWEA 1244
def solve(cnt):
    global max_amount, count
    # 시간을 줄여줄 방법이 필요합니다.
    count += 1
    #교환했을 때 모양
    num = ''.join(cards)
    num = int(num)
    if (cnt,num) in check:  # 이미 계산했던 케이스, 계산 수행하지 않음
        return
    # 이미 계산한 케이스인지 확인하기 위해서 삽입
    check.add((cnt,num))

    #교환을 완료했을 경우
    if cnt == N:
        if num > max_amount:
            max_amount = num
        return
    #교환을 완료하지 않았을 경우에는 바꿀 수 있는 모든 경우의 수를 고려
    #i는 교환하려고 하는 카드
    for i in range(len(cards)-1):
        #j 교환 대상 카드
        for j in range(i+1,len(cards)):
            cards[i], cards[j] = cards[j], cards[i]
            solve(cnt+1)
            # 원래 모양으로 돌려 놓고 다음교환 시도
            cards[i], cards[j] = cards[j], cards[i]


T = int(input())
for tc in range(1,T+1):
    # 모든 경우의 수를 다 고려할 건데
    # 교환 횟수와, 값이 같은 경우는 두 번은 계산하지 않는다.
    count = 0
    cards, N = input().split()
    cards = list(cards)
    N = int(N)
    check = set()   # 만들어봤던 case를 저장하는 set
    max_amount = 0
    solve(0)
    # print(count)
    print(f'#{tc} {max_amount}')