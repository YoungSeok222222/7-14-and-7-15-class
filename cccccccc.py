arr = ["B","T","S","K","R"]
n = int(input())
used=  [0] * len(arr)
path = [0] * n
cnt = 0
def abc(lv):
    global cnt


    if lv == n:
        if used[2] == 1:
            cnt +=1
        return

    for i in range(5):
        if used[i] == 0:
            path[lv] = arr[i]
            used[i] = 1
            abc(lv+1)
            path[lv] = 0
            used[i] = 0
abc(0)
print(cnt)