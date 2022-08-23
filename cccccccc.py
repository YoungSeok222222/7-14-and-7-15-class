
##############################################

#
# result = [list(map(int,input().split())) for _ in range(3)]
# Max = result[0]
#
# for i in range(len(result)-1):
#     if len(Max) > len(result[i+1]):
#        Max = i
#
#     elif len(Max) < len(result[i+1]):
#         Max = i+1
#
#     else:
#         for j in range(len(result[i])):
#             if Max[j] > result[i+1][j]:
#                 Max = Max
#                 break
#             elif Max[j] == result[i+1][j]: continue
#             else:
#                 Max = result[i+1]
#                 break
#
# for p in Max:
#     print(p,end='')

##################
# arr = list(input())
# n = int(input())
# path = [0] * n
# def dfs(lv):
#     if lv == n:
#         for i in range(lv):
#             print(path[i],end='')
#         print()
#         return
#
#     for i in range(len(arr)):
#         path[lv] = arr[i]
#         dfs(lv+1)
#
# dfs(0)
#

########################
# name = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
#
# n = int(input())
# result = [list(input()) for _ in range(n)]
# path = [0] * 4
# cnt = 0
#
# def dfs(lv):
#     global cnt
#     if lv ==4:
#         cnt += 1
#         if path not in result: return
#         else:
#             print(cnt)
#         return
#
#     for i in range(len(name)):
#         path[lv] = name[i]
#         dfs(lv+1)
# dfs(0)

##############################

arr = list(map(int,input().split()))

sum = 0
cnt = 0
path = [0] * len(arr)

def dfs(lv):
    global sum, cnt
    sum = 0
    for i in range(lv):
        sum += path[i]

    if sum >= 10 and 20 >= sum:
        cnt += 1
        print(sum,path)

    if lv == len(arr):
        return


    for i in range(len(arr)):
        if lv > 0 and path[lv-1] >= arr[i]: continue
        path[lv] = arr[i]
        dfs(lv+1)
        path[lv] = 0


dfs(0)
print(cnt)



