# 12712 파리퇴치3
def killfly(y,x):
    move_cross, cross_cnt = [[-1,0],[1,0],[0,-1],[0,1]], 0      # +모양, 카운트
    move_x, x_cnt = [[-1,-1],[-1,1],[1,1],[1,-1]], 0            # X모양, 카운트
    for j in range(1,M):
        for i in range(4):
            dy,dx = y+move_cross[i][0]*j, x+move_cross[i][1]*j  # y좌표 + 방향 + 세기
            if 0<=dy<N and 0<=dx<N: cross_cnt += lst[dy][dx]
    cross_cnt += lst[y][x]                                      # 마지막에 lst[y][x] 좌표값 (자기자신) 더하기

    for j in range(1,M):
        for i in range(4):
            dy,dx = y+move_x[i][0]*j, x+move_x[i][1]*j          # y좌표 + 방향 + 세기
            if 0<=dy<N and 0<=dx<N: x_cnt += lst[dy][dx]
    x_cnt += lst[y][x]                                          # 마지막에 lst[y][x] 좌표값 (자기자신) 더하기
    return cross_cnt, x_cnt

T = int(input())
for tc in range(1,T+1):
    Max = -21e8
    N,M = map(int,input().split())
    lst = [list(map(int,input().split())) for _ in range(N)]

    for y in range(N):                      # 모든 좌표 함수로 보내기
        for x in range(N):
            cross,x_cnt = killfly(y,x)      # 십자 모양, X모양으로 죽인 파리 수 
            Max = max(Max,cross,x_cnt)      # 최고값 갱신
    print(f"#{tc} {Max}")

# 1954 달팽이 숫자
T = int(input())
for tc in range(1,T+1):
    N = int(input())
    lst = [[0]*N for _ in range(N)]
    check = [[False]*N for _ in range(N)]
    move = [[0,1],[1,0],[0,-1],[-1,0]]
    y,x,idx = 0,0,0
    for i in range(1,N*N+1):
        lst[y][x] = i
        check[y][x] = True
        dy,dx = y+move[idx][0],x+move[idx][1]
        if dy<0 or dy>N-1 or dx<0 or dx>N-1 or check[dy][dx] and lst[dy][dx] !=0:
            idx = (idx+1) %4
            dy,dx = y+move[idx][0],x+move[idx][1]
        y,x = dy,dx
    print(f"#{tc}")
    for g in lst:
        print(*g)
