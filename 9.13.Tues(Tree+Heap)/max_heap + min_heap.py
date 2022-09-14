arr = [4,7,9,1,3,8,44,13]
heap = [0] *20                  # Max HEAP 1차원 리스트
h_index = 1                     # heap의 1번 인덱스    / 처음에는 4가 들어감

def insert(value):
    global heap,h_index
    heap[h_index]  = value
    now = h_index               # now : 처음에는 방금 추가가 된 자식
    h_index += 1                # 다음에 들어올 친구

    while 1:
        parents = now // 2      # 부모 인덱스
        if parents ==0: break   # 1 번 인덱스 // 2는 0이 나옴(처음 루트 노드에 값이 들어가면 비교할 값이 없으니까)
        if heap[parents] > heap[now]: break         # 부모>자식
        heap[parents], heap[now] = heap[now], heap[parents] # 자식이 더 크면 swap
        now = parents               #스왑 후 올라간 그 위의 부모랑 또 비교 

def top():
     global heap,h_index
     return heap[1]         # 루트노드 값 반환(우선순위가 가장 높은 값 반환)

def pop():
    global heap,h_index
    heap[1] = heap[h_index-1]
    heap[h_index-1] = 0
    h_index -=1
    
    now = 1
    while 1:
        son = now*2     # 왼쪽 자식
        rson = son+1    # 오른쪽 자식
        if heap[rson] !=0 and heap[son]<heap[rson]: son = rson  # 오른쪽 자식이 있으면 오른쪽과 왼쪽 자식을 비교해서 부모랑 비교할 대상 지정
        if heap[now] >= heap[son]: break            # 부모(now)랑 아들이랑 비교해서 부모가 크면 break
        heap[now], heap[son] = heap[son], heap[now] # 부모가 더 작으면 swap
        now = son   # swap 후 또 그 아래의 아들과 비교


for i in range(len(arr)):
    insert(arr[i])          # 이진트리의 형태로 저장을 하는

for i in range(len(arr)):
    print(top(),end=' ')    # 1번 인덱스 출력
    pop()                   # 트리에서 값 제거 후 자식들과 비교

#################################################
# min heap

arr=[4,7,9,1,3,8,44,13]
heap=[0]*20     # MAX HEAP    1차원 리스트
hindex=1

def insert(value):
    global heap,hindex
    heap[hindex]=value
    now=hindex
    hindex+=1

    while 1:
        parents=now//2
        if parents==0: break
        if heap[parents]>=heap[now]: break      # 수정
        heap[parents],heap[now]=heap[now],heap[parents]
        now=parents



def top():
    global heap
    return heap[1]

def pop():
    global heap,hindex
    heap[1]=heap[hindex-1]
    heap[hindex]=0          # 수정
    hindex-=1

    now=1
    while 1:
        son=now*2
        rson=son+1

        if rson<=hindex and heap[son]<heap[rson]: son=rson  # 수정
        if son>hindex or heap[now]>heap[son]: break         # 수정
        heap[now],heap[son]=heap[son],heap[now]
        now=son

for i in range(len(arr)):
    insert(arr[i])          # 이진트리의 형태로 저장을 하는

for i in range(len(arr)):
    print(top(),end=' ')    # 1번인덱스 출력
    pop()                   # 트리에서 값 제거 후 자식들과 비교

