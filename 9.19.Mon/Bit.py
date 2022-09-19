def Bbit_print(i):      # 7번 비트 -> 0번 비트 출력
    output = ""
    for j in range(7,-1,-1):
        output += '1' if (i&(1<<j)) else '0'
    print(output)

Bbit_print(5)
Bbit_print(-5)
Bbit_print(-6)
Bbit_print(-6>>1)