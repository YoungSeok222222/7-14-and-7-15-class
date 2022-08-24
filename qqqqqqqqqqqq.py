for t in range(10):
    dump = int(input())
    arr = list(map(int,input().split()))
    min, max = 9999, 0
    max_idx, min_idx = 0,0
    for j in range(dump):
        for i in range(len(arr)):
            if arr[i] >= max:
                max = arr[i]
                max_idx = i
            if arr[i] <= min:
                min = arr[i]
                min_idx = i
        print(max, min)
        max -= 1
        min += 1
    print(f"#{t+1} {max -min}")
#
# a = 10
# b = a
# b -= 1
# print(a,b)