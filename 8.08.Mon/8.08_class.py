'''
N =
9
7 4 2 0 0 6 0 7 0
'''

N= int(input())

arr = list(map(int,input().split()))
print(arr)
maxV = arr[0] #첫 원소를 최대값으로 가정 / max
for i in range(1,N): #나머지 모든 원소에 대해 index1부터 진행 즉 2번쨰 값
    if arr[i] > maxV:
        maxV = arr[i] # / amxV = i
print(maxV)
                                            #최대값 -> 최소값 -> 겹치면 오른쪽 값값

# if arr[0] < arr[i]:
#

#최대값의 위치, 같은 값이 있을때는 맨 오른쪽

N1= int(input())
arr1 = list(map(int,input().split()))
maxIdx = 0
for  i  in range(1, N1):
    if arr1[maxIdx] <= arr1[i]:   # = 는 같은 값이면 오른쪽에 있는 것을 넣는 것
        maxIdx = i
print(maxIdx)


#버블 소트 가장 큰 수 맨 오른쪽으로 보내고, 남은 수 검사/ 2개 남을 떄까지

N2= int(input())
arr2 = list(map(int,input().split()))
for i in range(N2-1, 0, -1): #구간의 맨 끝 인덱스
    for j in range(i): #인접원소 중 왼쪽 원소 인덱스
        if arr2[j] > arr2[j+1]:   #오름차순, 더 큰 수를 오른쪽으로
            arr2[j], arr2[j+1] = arr2[j+1], arr2[j]
print(arr)


#counting 카운트 정렬

N3= int(input())
arr3 = list(map(int,input().split()))
tmp = [0] * N3
c = [0] * 101 # 0부터 100까지 숫자 개수, 인덱스가 100까지 있어야 함
for i in range(N3):
    c[arr[i]] += 1
#print(c)
for j in range(1,101): # 개수 누적
    c[j] += c[j-1]
#print(c)

for i in range(N-1,-1,-1): #원본을 뒤에서부터 읽으면서 정렬 결과를 tmp에 저장
    c[arr[i]] -= 1
    tmp[c[arr[i]]] = arr[i]
print(tmp)