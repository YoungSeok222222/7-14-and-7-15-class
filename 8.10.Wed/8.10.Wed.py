# 다이렉트 배열? 배열 상하좌우 합 구하기( 2차원 배열 델타탐색)
arr= [[3,5,4],[1,1,2],[1,3,9]]
y, x = map(int,input().split()) # 1 1

directy = [-1,1,0,0]
directx = [0,0,-1,1]
sum =0

for i in range(4):
    dy = directy[i]+y
    dx = directx[i]+x
    if dy <0 or dy >2 or dx<0 or dx>2: continue  # if dy >= 0 and dy >=2 and dx >=0 and dx<=2:
    sum += arr[dy][dx]
    dummy =1
print(sum)


# ### 파이썬의 다른 방법
# sum = 0
# for i, j in (-1,0),(1,0),(0,-1),(0,1):
#     dy,dx= i+y, j+x
#     if 0<=dy<=2 and 0<=dx<=2:
#         sum += arr[dy][dx]

##############################
#자기 자신을 포함한 상하좌우 합 중 가장 큰 값
arr= [[3,5,4],[1,1,2],[1,3,9]]
directy= [0,-1,1,0,0]
directx=[0,0,0,-1,1]
Max = int(-21e8)  #-21*10의 8승
# Max = float('-inf') # -무한대의 값
Maxy=0
Maxx=0
def getSum(y,x):
    sum = 0
    for i in range(5):
        dy= directy[i]+y
        dx= directx[i]+x
        if dy <0 or dy>2 or dx>2 or dx <0: continue
        sum += arr[dy][dx]
    return sum




for i in range(3):
    for j in range(3):
        ret = getSum(i,j) #0,0 ~2,2
        if ret> Max:
            Max = ret
            Maxy =i
            Maxx =j
print(Maxy,Maxx)
print(Max)

#디버깅
#
'''
Ctrl + F8 : Toggle breakpoint
shift + f9 : 디버깅 시작
F8 : Step over
Ctrl + F2 : 디버깅 종료
F7 : Step into    함수 안으로 진입
F9 : resume (다음 break point까지 실행)
ctrl + F12: 디버깅 종료
'''
####
## 입력
# 3 5
# 1 2 8 9 7
# 1 2 9 9 9
# 1 6 4 2 7
N,M=map(int,input().split())
arr=[list(map(int,input().split())) for _ in range(N)]
Max=int(-21e8)
dy,dx=0,0

def getSum(y,x):  # 전달받은 좌표값 기준으로 sum 구한 후
    sum=0
    for i in range(2):
        for j in range(3):
            sum+=arr[i+y][j+x]
    return sum  # 구한 sum 리턴


for i in range(2):
    for j in range(3):
        ret=getSum(i,j)  # 0,0 부터 1,2 까지 좌표값 전달
        if ret>Max: # 리턴받은값 갱신
            Max=ret
            dy=i
            dx=j
print(Max)  # 최대값과   / Max 값 51
print(dy,dx) # 그 좌표값 까지 출력   / 0 2 (좌표)








