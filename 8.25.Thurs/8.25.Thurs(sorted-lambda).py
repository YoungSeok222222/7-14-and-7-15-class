arr = ['A', 'C', 'B', 'F', 'BB', 'G', 'DD', 'E', 'B', 'AA']
# 새로운 정렬된 리스트를 반환
# print(sorted(arr))
# print(arr)
#
# # 원본 데이터를 정렬된 데이터로 변경
# arr.sort()
# print(arr)

# list.sort()
#   원본 리스트를 직접 수정함
#       추가적인 메모리가 사용이 안됨(in-place)

# sorted()
#   정렬된 "새로운" 리스트를 반환
#       추가적인 메모리가 발생(out-of-place)

# 파이썬 내부
#   '병합 정렬' + '삽입 정렬' 아이디어를 합한 '하이브리드 방식'의 정렬 알고리즘
# - 병합 정렬 : 일반적으로는 퀵 정렬보다 느림
#       하지만, 최악의 경우에도  O(nlogn) 보장
print('-------------------------------------------')
## lambda x: 에서 x(==각 원소)
arr = ['A', 'C', 'B', 'F', 'BB', 'G', 'DD', 'E', 'B', 'AA']
sort1 = sorted(arr, key=lambda x: len(x))
print(sort1)

print('-------------------------------------------')

arr = ['A', 'C', 'B', 'F', 'BB', 'G', 'DD', 'E', 'B', 'AA']
sort2 = sorted(arr, key=lambda x: x)
print(sort2)

print('-------------------------------------------')

arr = ['A', 'C', 'B', 'F', 'BB', 'G', 'DD', 'E', 'B', 'AA']
sort3 = sorted(arr, key=lambda x: (len(x), x))
print(sort3)

print('-------------------------------------------')
# 길이가 가장 긴 단어를 출력하라.
# 단, 길이가 같은 경우 사전적으로 우선인 단어를 먼저 출력한다.
result = sorted(arr, key=lambda x: (-len(x), x))
print(result[0])

print('-------------------------------------------')
arr = [(1, 3), (0, 3), (1, 4), (1, 5), (0, 1), (2, 4)]

sort4 = sorted(arr, key=lambda x: x[0])
print(sort4)

# 0 번째 인덱스 기준으로 정렬 후
# 1 번째 인덱스 기준으로 정렬
sort5 = sorted(arr, key=lambda x: (x[0], x[1]))
print(sort5)

print('-------------------------------------------')
arr = ['A', 'B', 'Z', 'Z', 'A', 'Y', 'Y', 'Y', 'A', 'T']

# 빈도수가 가장 많은 문자를 출력해라
# 단, 빈도수가 같다면 사전적으로 빠른 문자를 출력해라.
sort6 = sorted(arr, key=lambda x: (-arr.count(x), x))
print(sort6)

print('-------------------------------------------')
# 가장 작은 수 출력
arr = [1, 3, 2, 4, 5, 8, 3, -2, -3]
print(sorted(arr, key=lambda x: x)[0])