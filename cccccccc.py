n = int(input())
members= [0,1,2,3,4,5,6]
company =[list(map(int,input().split())) for _ in range(7)]


boss = 0
boss_index = 0
under = []

for x in range(7):
    if company[0][x] == 1:
        under.append(x)
print(under)

for y in range(5):
    boss = 0
    for x in range(5):
        if company[y][x] == 1:
            boss += 1
    if
