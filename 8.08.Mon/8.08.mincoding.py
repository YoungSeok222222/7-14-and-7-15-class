# 민코딩 Level 16-4번
# A = list(map(int,input().split()))
# B = list(map(int,input().split()))
# result = [0]*4
# for i in range(1,len(A)+1):    #4 0~3
#     result[i-1] = (A[i-1] + B[4-i])
# result = ' '.join(map(str,result))
# print(result)


# 민코딩 Level 16-5번
# word = input()
# index = int(input())

# print(word[:index] + word[index+1:])

# 민코딩 Level 16-6번
# n = list(map(int,input().split()))
# for i in range(1,len(n)):
#     n[i] = n[i-1] + n[i]
# n = ' '.join(map(str,n))
# print(n)

# 민코딩 Level 16-7번
# word1 = input()
# word2 = input()
# word3 = input()

# if "M" in word1 or "M" in word2 or "M" in word3:
#     print("M이 존재합니다")
# else:
#     print("M이 존재하지 않습니다")

# 민코딩 Level 16-5 /1번
# a, b, c = map(int,input().split())
# for i in range(c):
#     result = []
#     for j in range(a, b + 1):
#         result.append(j)
#     print(' '.join(map(str,result)))

#민코딩 Level 16-5/2번
# n_list = []
# for i in range(6):
#     arr = []
#     uni = 65-i
#     for j in range(17,4,-6):
#         arr.append(chr(uni+j))
#     n_list.append(arr)
# print(n_list)

# n, m = map(int,input().split())
# print(n_list[n][m])


#민코딩 Level 16-5 / 3번
n = list(map(int,input().split()))

for i in range(2):
    arr = []
    num = +i
    for j in range(3):
        arr.append(n[j])





#민코딩 Level 16-5/4번
# index0, index1 = map(int,input().split())

# result = []
# result.append(index0)
# result.append(index1)
  
# for j in range(2,6):
#     result.append(result[j-1] * result[j-2])
# print(result[j])


#민코딩 Level 16-5 / 5번
# word = input()
# a = input()
# b = input()

# print(word.replace(a,b))

#민코딩 Level 16-5/6번
# word = list(input())

# print(word.index(max(word)))
# print(word.index(min(word)))
'''print(word.index(word[len(word)-1]))
print(word.index(word[0]))'''

#민코딩 Level 16-5/9번
# a,b,c = input().split()
# for i in range(int(a)):
#     print(c*int(b))

