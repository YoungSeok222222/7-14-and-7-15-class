n = int(input())
lst = list(map(int,input().split()))
Max = 0 

def dfs(lv):
    global Max
    if 0 not in fire:
        Max = max(sum(path),Max)
        return

    for i in range(len(lst)):
        if used[i] ==0 and fire[i]==0:
            path[lv] = lst[i]
            if i ==0:
                used[i] = 1
                fire[i] += 1
                fire[i+1] += 1
            elif i== len(lst)-1:
                used[i] = 1
                fire[i] += 1
                fire[i-1] += 1
            else:
                used[i] = 1
                fire[i-1] += 1
                fire[i]  += 1
                fire[i+1] += 1
            dfs(lv+1)
            path[lv] = 0
            if i ==0:
                used[i] = 0
                fire[i] -= 1
                fire[i+1] -= 1
            elif i== len(lst)-1:
                used[i] = 0
                fire[i] -= 1
                fire[i-1] -= 1
            else:
                used[i] = 0
                fire[i-1] -= 1
                fire[i]  -= 1
                fire[i+1] -= 1

fire = [0] * n    
used,path = [0]*len(lst), [0]*3
dfs(0)
print(Max)







  
            