
big =[]
small =[]

for i in range(1):
    arr = input().split()


for i in arr:
    if i.isupper():
        big.append(i)
    else:
        small.append(i)
print(f"big={''.join(big)}",f"small={''.join(small)}",sep='\n')




