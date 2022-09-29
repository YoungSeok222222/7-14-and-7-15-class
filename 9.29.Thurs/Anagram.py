# DAT를 이용한 비교
arr1=input()
arr2=input()
board1=[0]*26
board2=[0]*26
for i in arr1:
    board1[ord(i)-ord('a')]+=1
for i in arr2:
    board2[ord(i) - ord('a')] += 1
    
flag=1
for i in range(26):
    if board1[i]!=board2[i]:
        flag=0
        break
if flag: print('anagram')
else: print('not anagram')


# sort를 이용한 비교
vect1=input()
vect2=input()
if sorted(vect1)==sorted(vect2):
    print('아나그램')
else: print('아나그램 아님')

#================================================
# 최대 아나그램 만들기 위해 빼야 하는 문자 갯수
a='aabbc'
b='eebbffa'

dat=[0]*26
for i in a:
    dat[ord(i)-ord('a')]+=1 

for i in b:
    dat[ord(i)-ord('a')]-=1

cnt=0
for i in range(26):
    if dat[i]!=0:                       
        cnt+=abs(dat[i])

print(cnt)

#===================================================

s1=input()  # abcab
s2=input()  # aabbcbbaa
# 슬라이딩윈도

cnt=0
if sorted(s1)==sorted(s2[0:len(s1)]):  #s2의 문자열에서 맨 처음(0번인덱스부터) s1의 길이만큼 아나그램 확인)
    cnt+=1
for i in range(len(s2)-len(s1)):
    if sorted(s1)==sorted(s2[i:i+len(s1)]):
        cnt+=1
print(cnt)