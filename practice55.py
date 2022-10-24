n = int(input())
if n == 0:          # 0이면 0출력
    print(0)
elif n==1:          # 1이면 1출력
    print(1)
else:               # 2이상이면 재귀 함수 호출
    st,ex = 1, 0
    def abc(lv,Sum):
        global st,ex
        if lv==n:   # n과 같다면 합계 출력
            print(Sum)
            return
        Sum = st + ex   # 합계는 이전 + 현재
        ex = st         # 이전을 현재로 갱신
        st = Sum        # 현재를 합계로 갱신
        abc(lv+1,Sum)
    abc(1,0)



