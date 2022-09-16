# N = int(input())

# lst = [
#     ["A","B","C"],
#     ["D","E","F"],
#     ["G","H"],
#     ["I","J"]
# ]
# arr = [0] * 100
# for i in range(len(lst)):
#     for j in range(len(lst[i])):
#         if j==0: continue
#         arr[ord(lst[i][j])] = lst[i][0]

# print(arr) 

# def findboss(member):
#     if arr[ord(member)] == 0: return member
#     ret = findboss(arr[ord(member)])
#     arr[ord(member)] = ret
#     print(ret)
#     return ret


# def union(a,b):
#     global cnt
#     a_boss, b_boss = findboss(a), findboss(b)
#     if a_boss == b_boss: return
#     print(a_boss,b_boss)
#     arr[ord(b_boss)] = a_boss
    


# mix = [input().split() for _ in range(N)]
# for i in range(len(mix)):
#     union(mix[i][0],mix[i][1])

# print(arr)
# arr = set(arr)
# print(f"{len(arr)-1}개")
##################################
from collections import deque

n = int(input())
seed = [list(map(int,input().split())) for _ in range(2)]
arr = [[0] * n for _ in range(n)]
q = deque()

for i in seed:
    arr[i[0]][i[1]] = 1
    q.append([i[0],i[1]])



while q:
    directy,directx = [-1,1,0,0], [0,0,-1,1]
    y,x = q.popleft()

    for i in range(4):
       dy,dx = directy[i] + y, directx[i] + x
       if 0<=dy<n and 0<=dx<n and arr[dy][dx] ==0:
        arr[dy][dx] = arr[y][x] + 1
        q.append([dy,dx])


Max = -21e8
for i in range(n):
    for j in range(n):
        if Max < arr[i][j]:
            Max = arr[i][j]
print(Max)   
         


