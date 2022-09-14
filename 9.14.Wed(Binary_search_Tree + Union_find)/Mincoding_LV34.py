# 1번 Binary Search
arr = [4, 4, 5, 7, 8, 10, 20, 22, 23, 24]
target = int(input())
st, ed = 0, 9
while 1:
    md = (st+ed) // 2
    if arr[md] == target:
        print("O")
        break
    elif arr[md] > target:
        ed = md - 1
    elif arr[md] < target:
        st = md + 1
    if st > ed:
        print("X")
        break


# 2번자동차 기름 채우기
arr = list(input())
st, ed, max = 0, 9, -1
while 1:
    md = (st+ed) // 2
    if arr[md] == '#':
        max, st = md, md+1
    elif arr[md] == '_':
        ed = md - 1
    if st > ed:
        break
print(f"{(max+1)*10}%")

# 3번 민코 북카페
N = int(input())
books = list(input().split())
books.sort()
M = int(input())

for member in range(M):
    book, chance = input().split()
    chance = int(chance)
    st, ed, cnt = 0, N-1, 0
    while 1:
        md = (st+ed) // 2
        if books[md] == book:
            print("pass")
            break
        elif ord(books[md][0]) > ord(book[0]):
            ed = md - 1
        elif ord(books[md][0]) < ord(book[0]):
            st = md + 1
        if st > ed:
            print("fail")
            break
        cnt += 1
        if cnt == chance:
            print("fail")
            break
