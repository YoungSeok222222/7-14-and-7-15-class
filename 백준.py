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
    




