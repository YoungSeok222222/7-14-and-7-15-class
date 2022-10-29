n = int(input())
ar = [list(map(int,input().split())) for _ in range(n)]
re = []
for i in range(n):
    num = 1
    for j in range(n):
        if ar[i][0] < ar[j][0] and ar[i][1] < ar[j][1]: num += 1
    re.append(num)
print(*re)
