N, r, c = map(int,input().split())

ar = [[0] * (2**N) for _ in range(2**N)]
ac = [[0] * (2**(N-1)) for _ in range(2**(N-1))]
print(ar)
print(ac)

a = 2**(N) // 2
side = 0

def find(side):
    if side ==1:
        num = 0
    elif side == 2:
        num = 
    for i in range(2**(N-1)):
        for j in range(2**(N-1)):
            ac[i][j]

if r < a and c < a: side = 1
elif r < a and c >= a: side = 2
elif r >= a and c < a: side = 3
elif r >= a and c >= a: side = 4
find(side)


