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
