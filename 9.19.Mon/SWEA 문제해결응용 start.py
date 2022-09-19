# SWEA 15360
T = int(input())
for tc in range(1,T+1):
    N = float(input())
    arr = []
    while True:
        N = N * 2
        arr.append(int(format(N//1,".0f")))
        N = N % 1
        if N ==0: break
    if len(arr)>=13:
        print(f"#{tc} overflow")
    else:
        print(f"#{tc}",end=' ')
        print(*arr,sep='')
# https://woo-dev.tistory.com/93