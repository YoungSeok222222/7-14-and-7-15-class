# 많이 나오는 입력 형태
# 테스트 케이스 입력
# 그 다음 줄엔 배열의 길이
# 그 다음 줄엔 배열의 내용
# 예시 --------------------------
# 5
# 10
# 1 2 3 4 5 6 7 8 9 10
# 10
# 1 2 3 4 5 6 7 8 9 10
# 10
# 1 2 3 4 5 6 7 8 9 10
# 10
# 1 2 3 4 5 6 7 8 9 10
# 10
# 1 2 3 4 5 6 7 8 9 10
# --------------------------


# 입력이 int
N = int(input())

# 입력이 2~3개다
N, M = map(int, input().split())

# 입력이 공백으로 나뉘어서 들어온다
arr = list(map(int, input().split()))
print(arr)

# 입력이 쉼표로 나뉘어서 들어온다
arr = list(map(int, input().split(',')))
print(arr)

# 많은 문자열 입력이 들어왔다
# A B C D E F G
arr2 = input().split()
print(arr2)

# 숫자가 붙어서 입력된다
# 0123456789
arr = list(map(int, input()))
print(arr)

# 문자가 붙어서 입력된다
# ABCDEFGH
arr2 = list(input())
print(arr2)

# 2차원 이상의 배열의 경우 아래와 같이 많이 입력된다
# 배열 개수, 배열 길이
# 4 10
# 0123456789
# 0123456789
# 0123456789
# 0123456789

N, M = map(int, input().split())
arr = [list(map(int, input())) for _ in range(N)]
print(arr)

# 테스트 케이스 + 출력을 사용할 때는 반복문과 f-string 을 잘 활용해야 한다.
#1 3
#2 5
#5 7
T = int(input())
for test_case in range(1, T+1):
    ~~~ result 구하기
    print(f'#{test_case} {result}')