A, B, V = map(int,input().split())

ret = V // (A - B)

goal,d = 0, 0
while goal < V:
    goal += A
    goal -=B
    if goal == V: break
    d += 1
    # print(goal)
print(ret)





