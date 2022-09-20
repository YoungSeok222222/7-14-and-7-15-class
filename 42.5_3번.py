N = int(input())
n1,n2,n3 = map(int,input().split())
arr = ['!!','#','$','&']
path,used = [''] * N-1, [0] * 4



def calculation(a,b,i):
    if i == '!!':
        result = (a-b)*(a+b)
    elif i == '#':
        result = max(a,b)
    elif i== '$':
        result = a**2 - b**2
    else:
        result = (a+b)**2
    return result


def dfs(lv,n1,n2):
    if lv ==1:
        num = 
        return

    
    for i in range(4):
        if used[i] == 0:
            used[i] = 1
            path[lv] = calculation(n1,n2,arr[i])
            dfs()



ret = dfs(0,n1,n2)
answer = dfs(0,ret,n3)