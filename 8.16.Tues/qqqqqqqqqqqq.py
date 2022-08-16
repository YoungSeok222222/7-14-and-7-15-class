arr = ["A","B","C","D"]
path = [0] * 10

def abc(lv):
    # if lv ==3 and path[lv-1] == "C": return # C로 시작하는 것만 빼고 출력하는 경우


    if lv ==3:
        for i in range(lv):
            print(path[i],end=' ')
        print()
        return



    for i in range(4):
        # if lv ==0 and arr[i] == "c":continue  # C로 시작하는 것만 빼고 출력하는 경우
        #if path[0] == "C": continue
        path[lv] = arr[i]
        abc(lv+1)
        path[lv] = 0


abc(0)