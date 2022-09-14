'''
정점 번호 V : 1~(E+1)                  1
간선 수                             2     3
부모 - 자식 수                           4  5
4
1 2 1 3 3 4 3 5
'''
def find_root(V):
    for i in range(1,V+1):
        if par[i] == 0: # 부모가 없으면 root
            return i


# 전위순회
def preorder(n):    
    if n:
        print(n)
        preorder(ch1[n])
        preorder(ch2[n])

# 중위 순회
def inorder(n):
     if n:
        inorder(ch1[n])
        print(n)
        inorder(ch2[n])

# 후위 순환
def postorder(n):
     if n:
        postorder(ch1[n])
        postorder(ch2[n])
        print(n)

'''
높이가 h인 이진트리가 가질 수 있는 노드의 최소 개수는 (h+1)개가 되며, 최대 개수는 (2**(h+1) -1)개
즉, 높이가 2인 이진트리의 최대 개수는 2**(2+1) -1 -> 2**3 -1 이므로 7개
- 정점== 노드
- 포화 이진 트리(Full Bianry Tree): 모든 레벨에 노드가 포화상태로 차 있는 이진 트리
- 완전 이진 트리(Complete Binary Tree): 높이가 h이고 노드 수가 n개일 때, 포화 이진 트리의 노드 번호 1번부터 n번까지 빈 자리가 없는 이진 트리
- 편향 이진 트리(Skewed Binary Tree): 높이 h에 대한 최소 개수의 노드를 가지면서 한쪽 방향의 자식 노드만을 가진 이진 트리 ex. 왼쪽 편향 이진 트리 / 오른쪽 편향 이진 트리
- 순회: 트리의 각 노드를 중복되지 않게 전부 방문하는 것; ex. 전위순회(preorder traversal) == 부모-좌-우 / 중위 순회(inorder traversal)==좌-부모-우 / 후위순회(postorder traversal) ==좌-우-부모
'''

######################                
E = int(input())                      # 간선(부모노드와 자식노드 연결하는 선)의 갯수 / 차수: 자식노드의 수 / 단말노드: 자식 노드 없는 노드
arr = list(map(int,input().split()))  # 1 2 1 3 3 4 3 5
V = E +1
root = 1

ch1 = [0]*(V+1)
ch2 = [0]*(V+1) 

# 부모를 인덱스로 자식 번호 저장
for i in range(E):
    p, c  = arr[i*2], arr[i*2+1]   # 왼쪽 가지, 오른쪽 가지
    if ch1[p] ==0: # 아직 자식이 없으면
        ch1[p] = c # 자식1로 저장
    else:
        ch2[p] = c
###############################      
preorder(root)
inorder(root)
postorder(root)


print(ch1)
print(ch2)

# for j in range(0,E*2,2):  다른 방법
#     p,c = arr[j], arr[j+1]
####################################

# 자식을 인덱스로 부모 번호 저장

par = [0] * (V+1)
for i in range(E):
    p,c = arr[i*2], arr[i*2+1]
    if ch1[9] == 0:
        ch1[p] =c
    else:
        ch2[p] = c
    par[c] = p
root = 0
root = find_root()
##############

# 최대힙
def enq(n):
    global last 
    last += 1       # 마지막 정점 추가
    heap[last] = n  # 마지막 정점에 key 추가
    
    c = last
    p = c // 2 # 완전이진트리에서 부모 정점 번호 
    while p and heap[p] < heap[c]: # 부모가 있고, 부모 < 자식인 경우 자리 교환
        heap[p], heap[c] = heap[c], heap[p]
        c = p
        p = c // 2

# 힙에서의 삭제
def deq():
    global last
    tmp = heap[1]           # 루트 백업
    heap[1] = heap[last]    # 삭제할 노드의 키를 루트에 복사
    last -= 1               # 마지막 노드 삭제
    p = 1                   # 루트에 옮긴 값을 자식과 비교
    c = p * 2               # 왼쪽 자식
    while c <= last:        # 자식이 하나라도 있으면
        if c + 1 <= last and heap[c] < heap[c+1]:   # 오른쪽 자식도 있고, 오른쪽 자식이 더 크면
            c += 1                                  # 비교 대상을 오른쪽 자식으로 정함 
        if heap[p] < heap[c]: # 자식이 더 크면 최대힙 규칙에 어긋나므로
            heap[p], heap[c] = heap[c], heap[p]
            p,c = c, p * 2    # 자식을 새로운 부모로
        else:                 # 부모가 더 크면
            break             # 비교 중단,

    return tmp


heap = [0] * 100
last = 0

enq(2)
enq(5)
enq(7)
enq(3)
enq(4)
enq(6)

while last:
    print(deq())

####################################################################
#############################################################################
##############################################################################

# 최민호 교수님 강의

arr = '#ABCDEFG'                                                      #   A
def preorder(now): # 1 2 4 5                                         #  B   C
    if now > len(arr) -1: return                                    #  D E  F G
    print(arr[now],end=' ') # 전위 순회하면서 출력
    preorder(now*2)
    preorder(now*2+1)

preorder(1)

def postorder(now): # 
    if now > len(arr) -1: return
    postorder(now*2)
    postorder(now*2+1)
    print(arr[now],end=' ') # 후위 순회하면서 출력

def inorder(now):
    if now > len(arr) -1: return
    inorder(now*2)
    print(arr[now],end=' ')
    inorder(now*2+1)


postorder(1) # 전위순회  A B D E C F G
print()
postorder(1) # 후위순회  D E B F G C A 
print()
inorder(1)   # 중위순회  D B E A F C G





