# Union find 자료구조
'''
각각의 독립된 data를 그룹화 시켜 자료들을 관리할 때 사용하는 자료구조
'''
arr = [0] * 200

def findboss(member):
    global arr
    if arr[ord(member)] == 0: return member    # 매개변수에 해당하는 곳의 값이 0이라면 ->자기 자신이 보스!
    ret = findboss(arr[ord(member)])           # 배열에 적혀있는 값으로 다시 보스 찾아보기
    return ret                                


def union(a,b):
    global arr
    a_boss,b_boss = findboss(a),findboss(b)    # boss 찾기
    if a_boss == b_boss: return                # boss가 같다 -> 이미 같은 그룹이므로 return
    arr[ord(b_boss)] = a_boss               # 두 보스가 다르다면 b의 보스에 해당하는 값에 a의 보스 적기
                                            # 뒤 문자에 해당하는 arr배열에 앞의 문자 새기기 ex. E의 보스자리에 앞의 문자 F 새기기


union('A','B')  # 두 그룹을 하나의 그룹으로
union('D','E')  # 합쳐주는 함수
union('B','E')
union('B','D')
union('F','E')


y,x = input().split()
if findboss(y) == findboss(x):
    print("같은 그룹")
else: print("다른 그룹")
#########################################
# union find 자료구조를 이용하여 양방향 그래프에서의 cycle 존재여부 확인
# 4개의 정점을 연결하는데 필요한 최소한의 간선의 개수(정점의 개수 -1)/ 즉, 3개가 필요


n = int(input())        # 4
edge = []               
for _ in range(n):
    edge.append(input().split())    # A B / C E / D C /  A C / 
print(edge)
arr = [0] * 200


def findboss(member):
    global arr 
    if arr[ord(member)] == 0: return member
    ret = findboss(arr[ord(member)])
    arr[ord(member)] = ret
    return ret

# union 함수
def union(a,b):
    global arr
    a_boss, b_boss = findboss(a), findboss(b)
    if a_boss == b_boss: return 1
    arr[ord(b_boss)] = a_boss

answer = 0
for i in range(n):
    a,b = edge[i]
    ret = union(a,b)
    if ret==1:
        answer = 1
  
if answer: print("Cycle 발견")
else: print("Cycle 미발견")






