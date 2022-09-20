def htob(c):
    if c.isdecmial():
        intC = int(c)
    else:
        intC = ord(c)-ord('A')+10

    result = ''
    for i in range(4):
        result =  str(intC%2)+result
        intC //=2
