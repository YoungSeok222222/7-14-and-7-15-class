
##제너레이터 
# num = input(num)
# def fn_d():
#     result = 0
#     for x in range(len(num)):
#         result += int(num[x])
  
#     result = result + int(num)    
#     print(result)

# fn_d(num)
# #
# def is_selfnumber():


###################################
#월말평가 6번




# def caesar(word,n):
#     li = list(word)
#     print(li)
#     #소문자는 소문자로 / 대문자는 대문자로 암호화
#     #문자열의 islower(), isupper() 메서드로 소문자, 대문자 여부를 알 수 있다.
#     for i in range(len(li)):
#         if li[i].isupper():
#             li[i] = chr(65 + ((ord(li([i])) - 65 + n) % 26))
#         elif li[i].islower():
#             li[i] = chr(97 + ((ord(li[i])- 97 + n)%26))
        
#     return ''.join(li)    
        
# print(caesar('apple',5))
#################################################


#1번
def count_vowels(x):
    result = 0
    voewels = ['a','e','i','o','u']
    for vowel in voewels:
        result += x.count(vowel)
    
    return result
print(count_vowels('apple'))
print(count_vowels('banana'))
### 또다른 방법
def count_vowels(word):
    vowels = 'aeiou'
    count = 0
    for voewl in vowels:
        count += word.count(vowel)
    return count
print(count_vowels('apple'))
print(count_vowels('banana'))

# #2번 4번?

#3번########################
only_square_area= ([32,55,63],[13,32,40,55])
def only_square_are(L1,L2):
    new_list = []
    for i in range(len(L1)):
        for j in range(len(L2)):
            if L1[i] == L2[j]:
                new_list.append(L1[i]*L2[j])
    return new_list 

           
print(only_square_are([32,55,63],[13,32,40,55]))

####또다른 방법
def only_square_area(widths,heights):
    combination_list = []
    for width in widths:
        if width in heights:
            combination_list.append(width**2)
    return combination_list
print(only_square_are([32,55,63],[13,32,40,55]))


       

  
      
        

















