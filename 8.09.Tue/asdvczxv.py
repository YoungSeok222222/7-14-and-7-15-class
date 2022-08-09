
result = []

def Input():
    a = int(input())
    for j in range(3):
        arr = []
        for i in range(4):
            arr.append(a)
            a +=1
        result.append(arr)
    process(result)



def process(result):
    for i in range(3):

        for j in range(4):
            result[i][j] += 1
    output(result)
def output(result):
    for i in range(3):
        print(*result[i])







Input()