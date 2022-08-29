N = int(input())

arr = [list(map(int,input().split())) for _ in range(N)]
farm = [[0]*3 for _ in range(3)]


crop = []
for i in range(len(arr)):                        # 농작물 따로 보관
    crop.append(int(str(arr[i].pop())))

for i in range(len(arr)):                        # 농작물 농장에 심기
    farm[arr[i][0]][arr[i][1]] = crop[i]
# print(farm)

t = int(input())
typhoon = list(map(int,input().split()))         # 태풍 발생

for p in typhoon:
    for y in range(3):
        for x in range(3):
            if farm[y][x] ==0: continue
            elif farm[y][x]%10 > p:              # 태풍에 유실
                farm[y][x] -= p
            else:
                farm[y][x] = farm[y][x] // 10

result = []

for y in range(3):
    for x in range(3):
        if farm[y][x]:
            result.append(str(farm[y][x]))

print(len(''.join(result)))



# arr = [input() for _ in range(N)]