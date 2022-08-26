T = int(input())
for t in range(T):
    N = int(input())
    bus = [list(map(int,input().split())) for _ in range(N)]
    bus_stop = [0] * 5001

    p = int(input())

    idx = []
    for i in range(p):
        idx.append(int(input()))

    for i in bus:
        for j in range(i[0],i[1]+1):
            bus_stop[j] += 1
    print(f"#{t+1}",end=' ')
    for x in idx:
        print(bus_stop[x],end=' ')
    print()
    #



