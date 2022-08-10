arr= [[3,5,4],[1,1,2],[1,3,9]]
y, x = map(int,input().split())

direct_y = [-1,1,0,0]
direct_x = [0,0,-1,1]
result = 0

for i in range(4):
    dy = direct_y[i]+y
    dx = direct_x[i]+x
    if dy <0 or dy >2 or dx < 0 or dx >2: continue
    result += arr[dy][dx]
print(result)