# N = int(input())

# arr = [list(map(int,input().split())) for _ in range(N)]
# farm = [[0]*3 for _ in range(3)]


# crop = []
# for i in range(len(arr)):                        # 농작물 따로 보관
#     crop.append(int(str(arr[i].pop())))

# for i in range(len(arr)):                        # 농작물 농장에 심기
#     farm[arr[i][0]][arr[i][1]] = crop[i]
# # print(farm)

# t = int(input())
# typhoon = list(map(int,input().split()))         # 태풍 발생

# for p in typhoon:
#     for y in range(3):
#         for x in range(3):
#             if farm[y][x] ==0: continue
#             elif farm[y][x]%10 > p:              # 태풍에 유실
#                 farm[y][x] -= p
#             else:
#                 farm[y][x] = farm[y][x] // 10

# result = []

# for y in range(3):
#     for x in range(3):
#         if farm[y][x]:
#             result.append(str(farm[y][x]))

# print(len(''.join(result)))
###################################################

# 새로운 회원관리 시스템
# N = int(input())

# arr = list(input() for _ in range(N))
# for i in range(N):
#     if arr[i][0].isupper() and arr[i][0:].islower():
#         continue
#     elif arr[i][1:].islower():
#         arr[i] = arr[i].title()
#     else:
#         arr[i] = arr[i].upper()
# result = sorted(arr, key=lambda x: x)
# for j in range(N):
#     print(result[j])
##################################

# 9번 알파벳 카드 선정 
# arr = list(input())
# n = int(input())
# arr.sort(reverse=True)
# result = arr[0:n]
# maxn = 0

# for i in result:
#     if result.count(i) > maxn:
#         maxn = result.count(i)
#         idx = i
# print(idx)
##############################

# 10번 Bit 번호 추천 프로그램
# n = int(input())
# arr = [list(map(int,input().split())) for _ in range(n)]
# Bit = [list(map(int,input().split())) for _ in range(n)]

# result = []
# for y in range(n):
#     for x in range(n):
#         if Bit[y][x] ==1:
#             result.append(arr[y][x])

# result = sorted(result, key=lambda x: (-result.count(x),x))
# print(*result)
#######################################

# LV 32.5 1번 민코딩 검색엔진
# arr = [
#     ["A","B","C","D"],
#     ["A","B","c","E"],
#     ["A","G","E","H"],
#     ["E","I","E","I"],
#     ["F","E","Q","E"],
#     ["A","B","A","D"]
# ]
# search = list(input())

# idx = 0
# for i in range(len(search)):
#     if search[i] != "?":
#         n, idx = search[i], i

# cnt = 0
# for y in range(6):
#     for x in range(4):
#         if x == idx and arr[y][x] ==n:
#             cnt += 1
# print(cnt)
#######################################

# 2번 창밖에 흐르는 알파벳
# arr = list(input())
# print(*arr,sep='')
# while arr.count("_") < len(arr):
    
#     for i in range(len(arr)):
#         if arr[i] == "A" or arr[i]=="_":   
#             arr[i] = "_"
#         else:
#             arr[i] = chr(ord(arr[i]) -1)
#     print(*arr,sep='')
#######################################

# 3번 붕어빵 뒤집기

arr = [["A","B","C","E","F","G"],["H","I","J","K","L","M"],["N","O","P","Q","R","S"]]
copy_arr = [["A","B","C","E","F","G"],["H","I","J","K","L","M"],["N","O","P","Q","R","S"]]
bung = list(input())

def bung_A(y,x,b):
    direct_y, direct_x = [-1,1,0,0,0], [0,0,-1,1,0]
    if arr[y][x] != b:
        return 0
    else:
        for i in range(5):
            dy,dx = direct_y[i] + y, direct_x[i] + x
            if dy<0 or dx<0 or dy>2 or dx>5: continue
            else:
                if arr[dy][dx] == "#":
                     arr[dy][dx]  = copy_arr[dy][dx]
                else:
                    arr[dy][dx] = "#"
idx = 0
for b in bung:
    for y in range(3):
        for x in range(6):
            ret = bung_A(y,x,b)

for y in range(3):
    print(*arr[y],sep='')


#############################################################