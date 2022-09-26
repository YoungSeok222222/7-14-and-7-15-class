T = int(input())
for tc in range(1,T+1):
    N = int(input())
    bus = [list(map(int,input().split())) for _ in range(N)]
    bus_stop = [0] * 5001
    P = int(input())
    line = []

    for i in range(P):
        line.append(int(input()))

    for i in bus:
        for j in range(i[0],i[1]+1):
            bus_stop[j] += 1

    print(f"#{tc}",end=' ')
    for st in line:
        print(bus_stop[st],end=' ')
    print()

    
T = int(input())
for tc in range(1,T+1):
    N,Q = map(int,input().split())
    num = [0] * (N+1)
    lst = [list(map(int,input().split())) for _ in range(Q)]
    for i in lst:
        for j in range(i[0],i[1]+1):
            num[j] = i[0]

    print(f'#{tc}',end=' ')
    print(*num[1:])
    
    
    



