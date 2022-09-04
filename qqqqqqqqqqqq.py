arr = [["A","B","C","E","F","G"],["H","I","J","K","L","M"],["N","O","P","Q","R","S"]]
copy_arr = [["A","B","C","E","F","G"],["H","I","J","K","L","M"],["N","O","P","Q","R","S"]]
bung = list(input())


def bung_A(y,x,b):
    direct_y, direct_x = [-1,1,0,0,0], [0,0,-1,1,0]
    if arr[y][x] != b:
        return 0
    else:
        for i in range(5):
            dy,dx = direct_y[i] + y, direct_x[i] + x
            if dy<0 or dx<0 or dy>2 or dx>5: continue
            else:
                if arr[dy][dx] == "#":
                     arr[dy][dx]  = copy_arr[dy][dx]
                else:
                    arr[dy][dx] = "#"
        return 1

idx = 0
for b in bung:
    for y in range(3):
        for x in range(6):
            ret = bung_A(y,x,b)

for y in range(3):
    print(*arr[y],sep='')





