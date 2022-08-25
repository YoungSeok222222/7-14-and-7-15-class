# # 1번 구조체 삽입정렬
# n = int(input())
# arr = [''.join(input()) for _ in range(n)]
# result= []
# for i in range(len(arr)):
#     result.append(arr[i])
#     for j in range(i,0,-1):
#         if result[j-1] > result[j]:
#             result[j-1], result[j] = result[j], result[j-1]
#         else:
#             break
# for p in range(len(result)):
#     print(result[p])

# 2번 금메달 은메달 동메달
N = int(input())
arr = [input().split() for _ in range(N)]

for u in range(len(arr)):
    arr[u].append(u)
print(arr)

for i in range(len(arr)):
    result = sorted(arr[:i+1],key=lambda x: (-int(x[1]),-x[2]))[0:3]
    for j in range(len(result)):
        print(result[j][0],end=' ')
    print()
#
