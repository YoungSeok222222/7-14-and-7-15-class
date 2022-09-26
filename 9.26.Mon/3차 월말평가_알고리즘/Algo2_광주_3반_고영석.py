T = int(input())
for tc in range(1,T+1):
    N = int(input()) # 정점의 개수
    node = N-1       # 노드의 개수
    lst = [0] * 20
    for i in range(1,N+1):
        lst[i] = i
    print(lst)

    pre,inor,post = [],[],[]

    def preorder(now):              # 전위순회하여 전위 리스트에 추가
        if lst[now]:
            pre.append(lst[now])
            preorder(now*2)
            preorder(now*2+1)
    preorder(1)
    print()

    def inorder(now):               # 중위순회하여 중위 리스트에 추가
        if lst[now]:
            inorder(now*2)
            inor.append(lst[now])
            inorder(now*2+1)
    inorder(1)
    print()

    def postorder(now):              # 후위순회하여 후위 리스트에 추가
        if lst[now]:
            postorder(now*2)
            postorder(now*2+1)
            post.append(lst[now])
    postorder(1)

    answer = []
    for i in range(len(pre)):      # 전위,중위,후위 순회한 값들 중 큰 값을 answer에 추가
        mix = []
        mix.append(pre[i])
        mix.append(inor[i])
        mix.append(post[i])
        answer.append(max(mix))

    # for i in range()
    print(*answer)



