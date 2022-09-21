n = int(input())
lst = list(map(int,input().split()))


def dfs(lv):
    if 0 not in used:
        print(sum(path))
        return

    for i in range(len(lst)):
        if used[i] ==0:
            path.append(lst[i])
            if i ==0:
                used[i], used[i+1]= 1,1
            elif i== len(lst)-1:
                used[i], used[i-1] = 1,1
            else:
                used[i-1],used[i],used[i+1] = 1,1,1
            dfs(lv)
             
for i in range(len(lst)):
    used,path = [0]*len(lst), []
    dfs(i)










  
            