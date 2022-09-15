N = int(input())

lst = [
    ["A","B","C"],
    ["D","E","F"],
    ["G","H"],
    ["I","J"]
]
arr = [0] * 100
for i in range(len(lst)):
    for j in range(len(lst[i])):
        if j==0: continue
        arr[ord(lst[i][j])] = lst[i][0]

print(arr) 

def findboss(member):
    if arr[ord(member)] == 0: return member
    ret = findboss(arr[ord(member)])
    arr[ord(member)] = ret
    print(ret)
    return ret


def union(a,b):
    global cnt
    a_boss, b_boss = findboss(a), findboss(b)
    if a_boss == b_boss: return
    print(a_boss,b_boss)
    arr[ord(b_boss)] = a_boss
    


mix = [input().split() for _ in range(N)]
for i in range(len(mix)):
    union(mix[i][0],mix[i][1])

print(arr)
arr = set(arr)
print(f"{len(arr)-1}개")


