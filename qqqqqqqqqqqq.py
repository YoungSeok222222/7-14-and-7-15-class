n = int(input())
arr = list(map(int,input().split()))
result = []


for i in range(len(arr)-1):
    if i < 3:
        result.append(arr[i])
    elif result[-1] == result[-2] and result[-1] == arr[i]: continue
    else:
        result.append(arr[i])

print(result)

#











# result = []
# for i in range(len(arr)):
#     result.append(arr[i])
#     if result.count(arr[i]) > 2:
#         result.pop(i)
#         result.pop(i-1)
#         result.pop(i-2)
#
# print(result)