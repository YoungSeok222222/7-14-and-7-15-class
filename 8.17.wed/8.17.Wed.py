# path 배열안에 문자를 비교하면서 조합을 출력하는 방법

arr=['a','b','c','d']
path=['']*3


def abc(level):
    if level==3:
        for i in range(3):
            print(path[i],end='')
        print()
        return

    for i in range(4):
        #1 path[level-1] -> 그전 단계에서 타고 들어온 곳
        #2 arr[i] -> 앞으로 들어갈 가지
        #3 그전 들어온 가지 < 앞으로 들어갈 가지  (True)
        if level>0 and path[level-1] >= arr[i]: continue
        path[level]=arr[i]
        abc(level+1)

abc(0)
####################################
#for문의 i값의 변화를 이용한 <조합> 출력하기 (앞 br에서 a를 선택했다면 다음 br에서  b c d로만 갈 수 있는

arr=['a','b','c','d']
path=['']*3

def abc(level,start):
    if level==3:
        for i in range(3):
            print(path[i],end='')
        print()
        return

    for i in range(start,4):
        path[level]=arr[i]
        abc(level+1,i+1)

abc(0,0)  #level start
#########################

#중복조합
arr=['a','b','c','d']
path=['']*3

def abc(level,start):
    if level==3:
        for i in range(3):
            print(path[i],end='')
        print()
        return

    for i in range(start,4):
        path[level]=arr[i]
        abc(level+1,i)
abc(0,0)