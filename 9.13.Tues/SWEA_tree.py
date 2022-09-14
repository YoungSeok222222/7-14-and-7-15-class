# 1231 중위순회
for t in range(10):
    n = int(input())
    arr = [list(input().split()) for _ in range(n)]
    tree = ['#']
    for i in range(n):
        tree.append(arr[i][1])
    print(f"#{t+1}",end=' ')
  
    def inorder(now):
        if now >= len(tree): return
        inorder(now*2)
        print(tree[now],end='')
        inorder(now*2+1)
    inorder(1)
    print()

# 15301 subtree
T = int(input())
for t in range(T):
    E, N = map(int,input().split())         # 간선 수, 탐색할 간선 번호
    arr = list(map(int,input().split()))
    ch1,ch2,cnt = [0]*(E+2), [0]*(E+2), 0   # 예를 들어 노드가 6이면 간선(부모노드와 연결한 선)의 수는 5이다. 루트노드는 1부터 시작하기 때문에 노드+1이 필요하므로 간선 보다 2개가 더 필요  

    for i in range(E):                      # 부모를 인덱스로 자식 저장
        p,c = arr[i*2],arr[i*2+1]
        if ch1[p]==0:
            ch1[p] = c
        else:
            ch2[p] = c
    def preorder(now):
        global cnt
        if now: 
            cnt += 1
            preorder(ch1[now])
            preorder(ch2[now])
        
    preorder(N)
    print(f"#{t+1} {cnt}")

# 15303 노드의 합
T = int(input())
for t in range(T):
    N,M,L = map(int,input().split())
    tree,cnt = [0] * (N+1), 0
    arr = [list(map(int,input().split())) for _ in range(M)]
    for i in range(M):
        tree[arr[i][0]] = arr[i][1]
    
    def postorder(now):
        global cnt
        if now>= len(tree): return
        postorder(now*2)
        postorder(now*2+1)
        cnt += tree[now]
    postorder(L)
    print(f"#{t+1} {cnt}")