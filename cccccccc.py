n = 6
arr =[list(map(int,input().split())) for _ in range(6)]
count = 0


for i in range(6):
    for j in range(1):
        if arr[i][j] < arr[i][j+1]:
            arr[i][j], arr[i][j+1] = arr[i][j+1], arr[i][j]
            count += 1

for p in arr:
    print(*p)
print(f"{count}명")



