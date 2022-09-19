T = int(input())
for tc in range(1,T+1):
    N,lst = input().split()
    dic = {'A':10, 'B':11, 'C':12, 'D':13,'E':14, 'F':15}
    N,lst =int(N), list(lst)
    answer = []
    for i in range(N):
        if lst[i] in dic:
            lst[i] = dic.get(lst[i])
        else:
            lst[i] = int(lst[i])

    def isb(j):
        if j >8: ret = 0
        else: ret = 1
        result = []
        while True:
            result.append(j % 2)
            j = j //2
            if j//2 ==0:
                result.append(j)
                if ret:
                    result.append(j//2)
                return result   
     
            

    for j in lst:
        result=isb(j)
        for u in range(3,-1,-1):
            answer.append(result[u])
        
    print(f"#{tc}",end=' ')
    print(*answer,sep='')
 
    
    # for j in range(N):
    #     result.append(int(format(lst[j],'b')))
    
    # print(*result,sep='')
    # 0111 1001 1110 0001 0010
    
'''
47FE = 4*1000+ 7*100+15*10+14*1 
이걸 2진수로 바꾸려면
47EF = 
4 = 0100
7 = 1111
F = 15 = 1111
E = 14 = 1110
0100111111101111임
'''


100011111111110
10011111111110

print(hex(18430))

