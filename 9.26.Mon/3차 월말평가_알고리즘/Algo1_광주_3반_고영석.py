T = int(input())
for tc in range(1,T+1):
    N = int(input())
    lst = list(map(int,input().split()))

    cnt,same = 0,0
    for i in range(len(lst)):
        if len(lst)>1 and lst.count(lst[i]) ==len(lst): # 혹시나 배열이 1 이상이고 모든 산의 크기가 동일하다면 봉우리는 1개로 보기 때문에 cnt += 1하고 break
            cnt += 1
            break
        if len(lst)==1:                    # 만약 배열의 길이가 1 이라면 봉우리는 무조건 1개이기 때문에 cnt+=1 하고 break
            cnt += 1
            break
        elif len(lst)>1 and i==0:          # 만약 배열의 길이가 1보다 크고 i가 0이라면 i기준 i+1 봉우리와 비교해서 크면 +1
            if lst[i] > lst[i+1]: cnt += 1
        elif i == len(lst)-1:              # 만약 i가 마지막 인덱스 즉, 배열의 길이-1과 같다면 바로앞 인덱스와 비교해서 +1
            if lst[i] > lst[i-1]: cnt += 1
        elif (lst[i]>lst[i-1] and lst[i]==lst[i+1]) or (lst[i]==lst[i-1] and lst[i]>lst[i+1]): same += 1  # 만약 배열의 i번째가 i-1보다 크고 i+1과 같거나 혹은 i가 i-1과 같고 i+1보다 크다면  동일한 것이 붙어있기 때문에 same +=1
        elif lst[i]>lst[i-1] and lst[i]>lst[i+1]: cnt += 1                                                # i 앞 뒤 가 서로 다르고, i가 앞 뒤보다 크면 cnt += 1

    same = same//2                         # 동일한 봉우리 갯수를 2로 나누고
    cnt += same                            # 갯수에 더해준다.
    print(f"#{tc} {cnt}")

