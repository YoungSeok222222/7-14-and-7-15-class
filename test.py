T = int(input())
for t in range(T):
    N, k_Min, k_Max = map(int,input().split())
    score = list(map(int,input().split()))
    A,B,C = [],[],[]
    result,exception_list = [], []
    result.append(A)
    result.append(B)
    result.append(C)
    bucket = [0] * 101
    ret = 0
    for b in range(len(score)):
        bucket[score[b]] += 1

    T1,T1_cnt = 0, 0
    T2,T2_cnt = 0, 0
    for i in range(len(bucket)):
        if bucket[i] >= T2_cnt:
            T2 = i
            T2_cnt = bucket[i]
    bucket[T2] = 0

    for i in range(len(bucket)):
        if bucket[i] >= T1_cnt and i not in exception_list:
            T1 = i
            T1_cnt = bucket[i]
            exception_list.append(bucket[T1])


    for j in score:
        if T2 <= j:
            A.append(j)
        elif T1<= j < T2:
            B.append(j)
        else:
            C.append(j)

    if len(A) < k_Min or len(A) > k_Max:
        # continue
        print(f"#{t+1} -1")
    elif len(B) < k_Min or len(B) > k_Max:
        # continue
        print(f"#{t+1} -1")
    elif len(C) < k_Min or len(C) > k_Max:
        # continue
        print(f"#{t+1} -1")
    elif len(A) ==0 or len(B) ==0 or len(C)==0:
        # continue
        print(f"#{t + 1} -1")
    else:
        re = sorted(result, key=lambda x: len(x))

        print(f"#{t+1} {len(re[-1]) - len(re[0])}")


    # if ret:
    #     print(f"#{t + 1} -1")

