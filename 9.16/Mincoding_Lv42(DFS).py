# 1번 김밥 속재료
arr = list(input())
n = len(arr)
path = [0] * 3



def dfs(lv,st):
    if lv==3:
        print(*path,sep='')

        return
    for i in range(st,n):
       
        path[lv] = arr[i]
    
        dfs(lv+1,i)
    

dfs(0,0)


# 2번 Best Number 선정하기
lst = list(map(int,input().split()))
Max,Min = -21e8, 21e8
used = [0] * 5
sum = 0
path = [0] * 5
def dfs(lv,gop):
    global Max,Min
    if lv==5:
        gop = path[0]*path[1]-path[2]*path[3]+path[4]
        Max = max(gop,Max)
        Min = min(gop,Min)
        return

    for i in range(5):
        if used[i] ==1: continue
        used[i] = 1
        path[lv] = lst[i]
        
        dfs(lv+1,gop)
        used[i] = 0
dfs(0,1)
print(Max,Min,sep='\n')


# 3번 가수 BTS와 SES
lst = ["BTS","SBS","BS","CBS","SES"]
word = input()

path,used = [''] * 5, [0] * 5


def dfs(lv):
    if ''.join(path) == word or lv==5:
        if ''.join(path) == word:
            print(lv)
        return


    for i in range(5):
        path[lv] = lst[i]
        
        dfs(lv+1)
        path[lv] = ''  
        
dfs(0)


# 4번 최소 동전 교환기
coin = [10,40,60]
Min = 21e8

def dfs(lv,n):
    global Min 
    if n ==0: 
        Min = min(Min,lv)
        return

    for i in range(3):
        if n % coin[i] ==0:
            dfs(lv+1, n - coin[i])        
        
        
n = int(input())
dfs(0,n)
print(Min)


# 5번 10을 만들자
n = int(input())
lst = [1,2,3,4,5,6,7,8,9]
path = [0] * 9
cnt = 0

def dfs(lv,):
    global cnt
    Sum = sum(path)
    if Sum ==10: 
        cnt += 1
        
    if lv==n: return

    for i in range(9):
        path[lv] = lst[i]
        dfs(lv+1,)

dfs(0)
print(cnt)

# 6번 다빈치 민코드
N, M = map(int,input().split())
lst = list(map(int,input().split()))
path,used = [0] * M, [0] * N
Min = 21e8
result = [0]*M
def dfs(lv):
    global Min,result
    if lv==M: 
        sum = 1
        for i in range(M):
           sum *= path[i]
        if Min > sum:
            Min = sum
            for j in range(M):
                result[j] = path[j]
        return  

    for i in range(N):
        if used[i] == 1: continue
        path[lv] = lst[i]
        used[i] = 1
        dfs(lv+1)
        used[i] = 0
dfs(0)
print(*sorted(result))

# 7번 구매팀 결재
thing = {"a": 15,"b" : 20,"c":44,"d":22,"e":55,"f":16,"g":45}
lst = list(input())
n = int(input())
Max = -21e8
used = [0] * len(lst)

def dfs(lv,sum):
    global Max
    if lv==len(lst)-n:
        if sum > Max and sum %10 == 0:
            Max = sum
        return
      
    for i in range(len(lst)):
        if used[i] == 1: continue
        used[i] = 1
        dfs(lv+1,sum+thing.get(lst[i]))
        used[i] = 0

dfs(0,0)
print(Max)

# 8번 레드마운틴
n = int(input())
arr = [list(map(int,input().split())) for _ in range(n)]
check = [['']*n for _ in range(n)]
used = [0] * 3
ret = 0

def dfs(y,x):
    global ret
    if y==n-1 and x==n-1: 
        ret = 1
        return 

    directy,directx = [-1,1,0,0], [0,0,-1,1]
    for i in range(4): # 하 좌 우 탐색
        dy,dx = y+directy[i], x+directx[i]
        if 0<=dy<n and 0<=dx<n :
            if arr[dy][dx] == 0 and check[dy][dx]!=0:
                check[y][x] = 0
                check[dy][dx] = 0
                dfs(dy,dx)
                check[y][x] =''
dfs(0,0) # y,x
if ret:
    print("가능")
else:
    print("불가능")

