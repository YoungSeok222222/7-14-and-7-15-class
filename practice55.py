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

