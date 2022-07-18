def add_numbers():
    result = 0
    for x in range(1, 1000):
        if x % 2 == 0 or x % 7 == 0:
            result = result + x

    print(result)
add_numbers()
'''
# 위의 코드와 아래의 코드가 동일하지만 값이 다르게 나오는 이유???


'''


def problem4():
    result = 0
    for x in range(1, 1000):
        if x % 2 == 0 or x % 7:
            result += x
    print(result)
problem4()


