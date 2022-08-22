#바이너리 서치
n = int(input())
arr = list(map(int, input().split()))
target = int(input())



def binary_search(st, ed, value):  # 미드값 찾기
    while (1):  # 찾을 경우
        mid=(st + ed) // 2
        if arr[mid] == value:  # 찾고자 하는 값이 더 작으면
            return 1
        elif arr[mid] > value:  # 찾고자하는 값이 미드 값보다 더 크면
            ed = mid - 1
        elif arr[mid] < value:  # 찾고자 하는 값이 미드값 보다 더 크면
            st = mid + 1
        if st > ed:             # st index와 ed index가 교차되면 ... 없는 숫자
            return 0
arr.sort()

ret = binary_search(0, n - 1, target)

if ret:
    print("찾음")
else:
    print("없는숫자")


###########################
#Parametic search
bettery = "*******____"


def parametric_search(st, ed):
    Max = -1
    while (1):
        mid = (st + ed) // 2
        if bettery[mid] == "_":
            ed = mid - 1
        elif bettery[mid] == "*":
            Max = mid
            st = mid + 1
        if st > ed:
            break
    return Max + 1


answer = parametric_search(0, 9)
print(*answer)
########################
#응용
curser=[   # 6*10 size 리스트 (배열)
 '##########',
 '##########',
 '###_______',
 '__________',
 '__________',
 '__________',
]

# 워드작업 중 정전으로 인하여 컴퓨터가 강제로 종료가 되었습니다.
# 다시 전기가 들어어 컴퓨터를 켰더니 다행이도 자동복구가 실행 되었습니다.
# 우리는 자동복구가 되었을때 커서의 위치가 어디인지를 알려줘야 합니다.
# 커서의 위치를 알려주는 프로그래밍을 완성해 주세요.
# 시간복잡도 (On^2)보다 빨라야 합니다.

def bs1(st,ed):
 Max=-1
 while(1):
  mid=(st+ed)//2
  if curser[mid][0]=='_':
   ed=mid-1
  elif curser[mid][0]=='#':
   Max=mid
   st=mid+1
  if st>ed:
   break
  return Max+1

def bs2(st,ed,yy):
 Maxx = -1
 while (1):
  mid = (st + ed) // 2
  if curser[yy][mid] == '_':
   ed = mid - 1
  elif curser[yy][mid] == '#':
   Maxx = mid
   st = mid + 1
  if st > ed:
   break
 return Maxx + 1   # 인덴트 때문에 버그 !!

yaxis=bs1(0,5)
xaxis=bs2(0,9,yaxis-1)
print(yaxis-1,xaxis)

##################
#for문 연습
#1번
arr = [[0]*3 for _ in range(3)]
cnt = 1
for x in range(3):
    for y in range(3):
        arr[y][x] += cnt
        cnt += 1
print(arr)

#2번
arr = [[0]*3 for _ in range(3)]
cnt =1
for x in range(2,-1,-1):
    for y in range(2,-1,-1):
        arr[y][x] =cnt
        cnt += 1

print(arr)

#3번
arr = [[0]*3 for _ in range(3)]
cnt =1
for y in range(3):
    if  y% 2==0:
        for x in range(3):
            arr[y][x] = cnt
            cnt += 1
    else:
        for x in range(2,-1,-1):
            arr[y][x] = cnt
            cnt += 1

# 4번문제 (반 갈라서 합 구하기)

N=int(input())
arr=[list(map(int,input().split())) for _ in range(N)]

# 풀이 1
sum1, sum2= 0, 0
for i in range(N):
    for j in range(N):
        if i>j:
            sum1+=arr[i][j]
        elif i<j:
            sum2+=arr[i][j]
print(sum1, sum2)

# 풀이 2
sum1, sum2= 0, 0
for i in range(N):
    for j in range(i+1,N):
        sum1 += arr[j][i]
        sum2 += arr[i][j]

print(sum1, sum2)


# 5번 문제 (각 대각선의 합)

N=int(input())
arr=[list(map(int,input().split())) for _ in range(N)]

lst= [0] * (2 * N - 1)

for i in range(N):
    for j in range(N):
        lst[i + j]+=arr[i][j]

print(lst)