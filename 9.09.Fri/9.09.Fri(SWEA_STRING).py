# SWEA STRING

# 13761 가장 빠른 문자열 타이핑
# T = int(input())
# for t in range(T):
#     word, letter = input().split()
#     sum = 0
#     sum += word.count(letter)
#     sum += len(word)- word.count(letter)*len(letter)
#     print(f"#{t+1} {sum}")

# 13741 글자수
# T = int(input())
# for t in range(T):
#     str1 = input()
#     str2 = input()
#     max = 0
#     for i in range(len(str1)):
#         if str2.count(str1[i]) > max:
#             max = str2.count(str1[i])
#     print(f"#{t+1} {max}")

# 13740 회문(string)
# T = int(input())
# for t in range(T):
#     N,M = map(int,input().split())
#     arr = [list(input()) for _ in range(N)]

#     for y in range(N):
#         row,column = [], []
#         for j in range(M):
#             row.append(arr[y][j])
#             column.append(arr[j][y])
#         for i in range(N-M+1):
#             rev_row = list(reversed(row))
#             rev_column = list(reversed(column))
#             if row == rev_row and len(rev_row)==M:
#                 result = rev_row
#                 break
#             if column==rev_column and len(rev_column):
#                 result = rev_column
#                 break
#             if i == N-M: break
#             if len(row) == N: break
#             row.append(arr[y][i+M]), column.append(arr[i+M][y])
#             row.pop(0), column.pop(0)
#     print(f"#{t+1}",end=' ')
#     print(*result,sep='')

# 13738 문자열 비교
# T = int(input())
# for t in range(T):
#     a = input()
#     b = input()
#     c = b.count(a)
#     print(f"#{t+1} {c}")

# 1221 GNS
T = int(input())
num = {'ZRO':0, 'ONE':1, 'TWO':2,'THR':3, "FOR":4, "FIV":5, "SIX":6, "SVN":7, "EGT":8, "NIN":9}
new = {}
for key,value in num.items():
    new[value] = key

for t in range(T):
    tc, number = input().split()
    print(tc)
    arr = list(input().split())
    for i in range(len(arr)):
        arr[i] = num.get(arr[i])
    arr.sort()
    for j in range(len(arr)):
        arr[j] = new.get(arr[j])
    print(*arr,sep=' ')


