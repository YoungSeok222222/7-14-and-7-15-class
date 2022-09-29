# Hash - 빠른 검색을 위해 사용 / 대표적으로 BST(바이너리 서치 트리; O(log n))와 Hash(O(1))

'''
해시
https://school.programmers.co.kr/learn/courses/30/parts/12077
레벨 1,2 먼저 풀기

오픈체팅방 : https://school.programmers.co.kr/learn/courses/30/lessons/42888
메뉴 리뉴얼 : https://school.programmers.co.kr/learn/courses/30/lessons/72411
뉴스 클러스터링 : https://school.programmers.co.kr/learn/courses/30/lessons/17677

레벨 3 풀어보기 
'''

from collections import Counter

a = [1,1,1,1,2,3,4]
b = [1,1,2,3]

print(Counter(a))
print(Counter(b))
print(Counter(a)-Counter(b))
print()
c = Counter(a) - Counter(b)
print(list(c.items()))
print(list(c.items())[0])
print(list(c.items())[0][1])

#========================================================================

# 프로그래머스 Hash 문제
# https://school.programmers.co.kr/learn/courses/30/lessons/42576 
participant = ["mislav","stanko","mislav","ana"]
completion = ["stanko",'ana','mislav']

pct = {}
for i in participant:
    if i not in pct:
        pct[i] = 1
    else:
        pct[i] += 1

for j in completion:
    pct[j] -= 1

answer = ''
for keys,values in pct.items():
    if values!=0: 
        answer = keys
print(answer)


# 교수님 풀이
def solution(participant, completion):
    participant.sort()
    completion.sort()

    for i in range(len(completion)):
        if completion[i]!=participant[i]:
            return participant[i]
    return participant[len(participant)-1]

#=====================================================
