N = int(input())
lst = list(map(int,input().split()))
dp1,dp2 = [0] * (N+1), [0]*(N+1)
ans = []
Max = 0
for i in range(1,N):
    if lst[i-1] <= lst[i]: 
        dp1[i] = dp1[i-1]+1

for i in range(1,N):
    if lst[i-1] >= lst[i]:
        dp2[i] = dp2[i-1] +1
print(dp2)
a,b = max(dp1),max(dp2)
print(max(a,b)+1)
    



# 2789 블랙잭(브루트포스)
N, M  = map(int,input().split())
ar = list(map(int,input().split()))
Max,ret =  0, 0 



# 3장 뽑아야 하기 때문에 3중 for문 사용
# ex. 5 21 
# 
# 인덱스 범위를 첫번째 for문의 범위를 
for i in range(N-2):    
    for j in range(i+1,N-1):
        for p in range(j+1,N):
            Sum = ar[i]+ ar[j] +ar[p]
            # print(Sum)
            if Sum <= M and ret < Sum: 
                ret = Sum


print(ret)