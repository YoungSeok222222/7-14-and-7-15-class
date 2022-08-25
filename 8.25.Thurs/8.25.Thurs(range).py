'''
For 문과 While 문은 언제 사용하나요 ?
for
    특정한 숫자가 순차적으로 증가하거나, 감소할 때 for문 사용

while
조건이 정해져있을 때
예를 들어, N 이 10보다 작을때, N = False 일 때 등등
혹은, 종료 조건이 정해져 있을 때
while 조건문: <- 조건문에서 종료 조건을 작성
    만약 N 이 10이라면 반복 종료
    while != 10:
while True: <- 반복하면서 종료 조건 만족 시 break 호출
   항상 무한루프 조심 ( 파이참 디버깅 툴 사용하거나, 손 디버깅 많이 해야함 )
'''

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# 순차적으로 탐색
for i in arr:
    i += 1
print(arr, end=' ')
print()

# range(a, b, c)
# range(10) = range(0, 10, 1)
# range(10, 20) = range(10, 20, 1)
# i 가 len(arr) - 1 이 될 때까지 1씩 증가하면서 반복
for i in range(len(arr)):
    arr[i] += 1
print(arr, end=' ')
print()

print('-------------------------------------------')
# 역순
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in range(len(arr)-1, -1, -1):
    print(arr[i], end=' ')
print()

print('-------------------------------------------')

# 2씩 증가하면서 출력(홀수 출력)
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in range(0, len(arr), 2):
    print(arr[i], end=' ')
print()

# 2씩 증가하면서 출력(짝수 출력)
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in range(1, len(arr), 2):
    print(arr[i], end=' ')
print()
print('-------------------------------------------')
# 역순으로 2칸씩
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in range(len(arr)-1, -1, -2):
    print(arr[i], end=' ')
print()

print('-------------------------------------------')
# 1 2 3 4 5 6 7 8 9 10
# 1 2 3 4 5 6 7 8 9 10
# 1 2 3 4 5 6 7 8 9 10
# 1 2 3 4 5 6 7 8 9 10
# 1 2 3 4 5 6 7 8 9 10
# 5줄
arr = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10] for _ in range(5)]

# 순차적으로 출력
for i in range(len(arr)):
    for j in range(len(arr[i])):
        print(arr[i][j], end=' ')
    print()

print('-------------------------------------------')
# 행마다 역순으로 출력
for i in range(len(arr)):
    for j in range(len(arr[i])-1, -1, -1):
        print(arr[i][j], end=' ')
    print()

print('-------------------------------------------')
# 출력 순서가 순차적이 아닐 경우
# 출력 순서를 가진 배열을 만들어서
# 인덱스를 증가시키며 출력 순서 배열을 통해 실제 배열에 접근
arr = [12, 9, 6, 3]
print_index = [0, 1, 3, 2]
for i in range(len(arr)):
    print(arr[print_index[i]])
print()
print('-------------------------------------------')

# x y
#     상 하 좌 우
arr = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10] for _ in range(5)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

x, y = 2, 1
print(f'arr[x][y] = {arr[x][y]}')
for i in range(4):
    new_x = x + dx[i]
    new_y = y + dy[i]
    print(arr[new_x][new_y], end=' ')