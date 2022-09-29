# 10157 자리배정(달팽이 문제와 유사)
C,R = map(int,input().split())
target = int(input())
lst = [[0]*C for _ in range(R)]
check = [[True]*C for _ in range(R)]
y,x,idx = 0,0,0
direct_y,direct_x = [1,0,-1,0], [0,1,0,-1]
for i in range(1,C*R+1):
    lst[y][x] = i
    check[y][x] = False
    dy,dx = y+direct_y[idx],x+direct_x[idx]
    if dy<0 or dx<0 or dy>R-1 or dx>C-1 or check[dy][dx] != True:
        idx = (idx+1)%4
        dy,dx = y+direct_y[idx], x+direct_x[idx]
    y,x = dy,dx
ret = 0
for i in range(R):
    if ret: break
    for j in range(C):
        if lst[i][j] == target:
            print(j+1,i+1,sep=' ')
            ret = 1
            break
if ret==0:
    print(0)
# 2563 색종이
def issquare(y,x):
    global cnt
    for i in range(y,y+10):
        for j in range(x,x+10):
            if ar[i][j]==0:
                ar[i][j] = 1
                cnt +=1
                
N = int(input())
lst =[list(map(int,input().split())) for _ in range(N)]
ar = [[0]*100 for _ in range(100)]

cnt = 0
for i in lst:
    issquare(i[1]-1,i[0]-1)

print(cnt)

# 2605 줄세우기
N = int(input())
orders = list(map(int,input().split()))
lst = [i for i in range(1,N+1)]
answer = []
for j in range(len(orders)):
    answer.insert(orders[j],lst[j])
print(*answer[::-1])


# 14696 딱지놀이
T = int(input())
for tc in range(1,T+1):
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    a.pop(0),b.pop(0)
    a_cnt,b_cnt = [],[]

    for i in range(4,0,-1):
        a_cnt.append(a.count(i))
        b_cnt.append(b.count(i))
  
    for j in range(len(a_cnt)):
        if a_cnt[j] > b_cnt[j]: 
            print("A")
            break
        elif a_cnt[j]< b_cnt[j]: 
            print("B")
            break
    else:
        print("D")


# 13300 방 배정
n,r = map(int,input().split()) # 총 학생수, 한 방에 배정 가능한 인원
# lst = [list(map(int,input().split())) for _ in range(n)]
# lst.sort(key=lambda x: (x[0],x[1]))
girls,boys = [0]*6,[0]*6

for i in range(n):
    s,y = map(int,input().split())
    if s==0: girls[y-1] += 1
    if s==1: boys[y-1] += 1

# print(girls,boys)
cnt = 0
for j in range(len(boys)):
    if girls[j] !=0:
        if girls[j]>=r: 
            cnt = girls[j] % r + girls[j]//r + cnt
        else: cnt += 1
    if boys[j] !=0:
        if boys[j]>=r:
            cnt = boys[j] % r + boys[j]//r + cnt
        else: cnt += 1
    
print(cnt)

'''
6 7
1 1
1 1
1 1
1 1
1 1
1 1
'''