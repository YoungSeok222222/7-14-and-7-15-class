# 1번 Cycle을 찾아라 
N = int(input())
lst = [list(input().split()) for _ in range(N)]
arr = [0] *100


def findboss(member):
    if arr[ord(member)] ==0: return member
    ret = findboss(arr[ord(member)])
    arr[ord(member)] = ret

def union(a,b):
    a_boss, b_boss = findboss(a), findboss(b)
    if a_boss == b_boss: return 1
    arr[ord(b_boss)] = a_boss


for i in range(N):
    result = union(lst[i][0],lst[i][1])
    if result: break

if result:
    print("발견")
else:
    print("미발견")


# 2번 원시부족
