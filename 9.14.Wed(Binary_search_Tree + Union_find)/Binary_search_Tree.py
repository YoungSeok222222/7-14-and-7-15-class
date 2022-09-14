# Binary Search Tree                            4
arr = [0] * 20                          #     2   9
lst = [4,2,9,7,15,1,3]                  #   1  3  7  15        [0,4,2,9,1,3,7,15,....]


def insert(target):
    now = 1
    while (1):
        if arr[now] == 0:
            arr[now] = target
            return
        if arr[now] < target: now =now*2+1
        else: now = now*2
    
def search(target):
    now = 1
    while 1:
        if now>=20: return 0   # 배열범위 벗어날 경우(이 조건을 항상 맨 위에 적어야함)
        if arr[now]==0: return 0    # 찾고자 하는 값이 없는 경우 
        if arr[now] ==target: return 1 # 찾았을 경우
        if arr[now]<target: now = now*2+1   # 찾고자 하는 값이 좌표에 있는 값보다 크면 now*2+1
        else: now *= 2                      # 찾고자 하는 값이 좌표값보다 작은 경우 now*2
 

for i in range(len(lst)):
    insert(lst[i])       # arr 배열(트리)에 값 저장하는 함수



n = int(input())        # 숫자 하나 입력 받고
answer = search(n)      # 입력받은 숫자가 존재하는지 search하는 함수
if answer:print("존재")
else: print("없는숫자")