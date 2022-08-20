n = ["A","B","C","D"]
arr = [list(input()) for _ in range(4)]
arr2 = [
    ["A","B","C","D"],
    ["B","B","A","B"],
    ["C","B","A","C"],
    ["B","A","A","A"],
]

def treasure(j):
    cnt = 0
    for y in range(4):
        for x in range(4):
            if n[j] == arr[y][x] and arr[y][x] == arr2[y][x]:
                cnt +=1
    return cnt


count = [0] * 4
Max = 0
for j in range(4):
    ret = treasure(j)
    count[j] = ret


index = 0
for p in range(1,len(count)):
    if count[index] < count[p]:
        index = p


print(n[index])
