result = []
letter = input()
for i in range(4):
    arr = []
    for j in range(4):
        arr.append(letter)
    result.append(arr)

print(*[i for i in result])

