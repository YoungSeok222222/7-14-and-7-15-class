a = 'abcab'
b = 'aabbcbbaa'
print(sorted(a),sorted(b))
cnt = 0
if sorted(a)==sorted(b[0:len(a)]): cnt += 1

for i in range(len(b)-len(a)):
    if sorted(a)==sorted(b[i:len(a)]): cnt += 1
print(cnt)