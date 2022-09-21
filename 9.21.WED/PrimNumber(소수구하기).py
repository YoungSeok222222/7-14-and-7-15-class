# prime number (소수 구하기)
import math


# 소수 - 1과 자기 자신으로만 나눌 수 있는 수
#
# a=int(input())
# flag=True
# if a>2:
#     for i in range(2,a):
#         if a%i==0:
#             flag=False
#             break
# if flag:print("소수임")
# else: print("소수가 아님")

#에라토스테네스의 체

# a=int(input())
# answer=[]
# check=[True]*(a+1)
# for i in range(2,a+1): #2부터 입력받은 수 까지 모두 확인
#     if check[i]==True: answer.append(i)
#     for j in range(i+i,a+1,i): # 확인하고자 하는 배수에 해당하는 값을 false
#         check[j]=False
# print(*answer)



a=int(input())
answer=[]
check=[True]*(a+1)
for i in range(2,int(math.sqrt(a))+1): #2부터 입력받은 수의 제곱근 까지 모두 확인
    if check[i]==False: continue
    for j in range(i+i,a+1,i): # 확인하고자 하는 배수에 해당하는 값을 false
        check[j]=False

# 위에 for문이 끝나면.. 소수가 아닌 곳에는 false 체크가 되어 있고
# 남은 숫자들에는 True 가 남아 있다.

for i in range(2,a+1):
    if check[i]==True:
        print(i,end=' ')

