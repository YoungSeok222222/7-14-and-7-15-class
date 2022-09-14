# 1232 사칙연산
def postorder(v):
    # 연산자에 따라서..
    # 왼쪽 자식 결과 - 오른쪽 자식 결과
    if value[v] not in '+-*/': return value[v]
    else:
        l_result = float(postorder(left[v]))
        r_result = float(postorder(right[v]))
        if value[v] == '*':
            return l_result * r_result
        elif value[v] == '/':
            return l_result / r_result
        elif value[v] == '-':
            return l_result - r_result
        else:
            return l_result + r_result

for tc in range(1,11):
    N = int(input())
    left = [0] * (N+1)      # 왼쪽 자식 정보를 저장할 배열
    right = [0] * (N+1)     # 오른쪽 자식 정보 저장
    value = [None] * (N+1)  # 값 또는 연산자를 저장할 배열

    for i in range(N):
        data = input().split()
        if len(data) ==2:   # 자식이 없는 경우, 단말 노드
            value[int(data[0])] = data[1]
        else:               # 자식이 있는 경우, 연산자
            value[int(data[0])] = data[1]
            left[int(data[0])] = int(data[2])
            right[int(data[0])] = int(data[3])
    # 후위순회 하면서 계산하기
    result = postorder(1)
    print(f"#{tc} {int(result)}")

    # print(left)
    # print(right)
    # print(value)

