word = list(input())
letter = list(input().split())
bucket = [0] * 10

for i in range(len(word)):
    bucket[i] = i


print(bucket)

result = [0]*2
for i in range(len(word)):
    if letter[0] == word[i]:
        result[0] = i
    elif letter[1] == word[i]:
        result[1] = i


for i in range(2):
    if bucket[0] == result[i]:
        word[result[0]-1] = "#"
    elif word[] == reuslt[i]
print(result)

print(word)