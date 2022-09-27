lst = [list(map(int,input().split())) for _ in range(4)]

for i in range(1,4):
    lst[0][i] += lst[0][i-1]
    lst[i][0] += lst[i-1][0]

result = [[0,0]]
for i in range(1,4):
    for j in range(1,4):
        if lst[i-1][j] < lst[i][j-1]:
            lst[i][j] += lst[i-1][j]
            result.append([i-1,j])
        else:
            lst[i][j] += lst[i][j-1]
            result.append([i,j-1])
print()
for g in lst:
    print(*g)