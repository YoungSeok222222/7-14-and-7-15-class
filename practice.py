def caesar(word,n):
    li = list(word)
    print(li)
    #소문자는 소문자로 / 대문자는 대문자로 암호화
    #문자열의 islower(), isupper() 메서드로 소문자, 대문자 여부를 알 수 있다.
    for i in range(len(li)):
        if li[i].isupper():
            li[i] = chr(65 + ((ord(li([i])) - 65 + n) % 26))
        elif li[i].islower():
            li[i] = chr(97 + ((ord(li[i])- 97 + n)%26))
        
    return ''.join(li)    
        
print(caesar('apple',5))
print(caesar('Python', 10))