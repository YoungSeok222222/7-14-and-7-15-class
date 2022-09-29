
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
