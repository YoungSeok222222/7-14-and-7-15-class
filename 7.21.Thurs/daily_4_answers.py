
#daily 4-2
#1. 문제: 득표가 많은 순서대로 출력
#2. 조건: 딕셔너리만 사용할 것 + 외부 패키지 사용 x 
dic_a = {}
for x in students:
    if x not in dic_a:
        dic_a[x] = 1
    else:
        dic_a[x]=  dic_a[x] + 1
sorted(dic_a.values(), reverse = True)   
print(dic_a)
for p in dic_a:
    print(p,dic_a.get(p))

#daily 4-3#################
'''
1. 문제: 정수 0부터 9까지 이루어진 list 중 연속된 것 제거하고 출력
2. 조건: 순서는 그대로

'''
numbers = list(map(int,input().split()))

print(numbers.count(1))
for x in numbers: 
    if numbers.count(x) > 1:
        numbers.remove(x)
print(numbers)




# daily 4-4###########################
word1 = input('첫 번째 이름을 입력하세요 : ')
word2  = input('두 번째 이름을 입력하세요 : ')


a = list(word1)
b = list(word2)

def good():
    numbers_1= 0
    numbers_2= 0
    for x in a:
        numbers_1 += ord(x)
    
    for p in b:
        numbers_2 += ord(p)
   
    if numbers_1 >numbers_2:
        print(numbers_1)
    else:
        print(numbers_2)

   
good()

#daily 실습 4_5######################
words_dict = {'proper' : '적절한',
'possible' : '가능한',
'moral' : '도덕적인',
'patient' : '참을성 있는',
'balance' : '균형',
'perfect' : '완벽한',
'logical' : '논리적인',
'legal' : '합법적인',
'relevant' : '관련 있는',
'responsible' : '책임감 있는',
'regular' : '규칙적인'}

'''
 문제: in의 변화형을 제어문을 사용하여 반의어의 모음으로 만들고, 
오름차순으로 만들고 출력
조건: 
'''
new_list = list(words_dict.keys())
new=[]
for x in new_list:
    if x[0] in['b', 'm', 'p']:
        x = 'im' + x
    elif x[0] in['l']:
        x = 'il' + x
    elif x[0]in ['r']:
        x = 'ir' + x
    new.append(x)
new.sort()
print(new)


#daily 과제 4-2 끝말잇기########################################################
words = ["round" , "dream", "magnet" , "tweet" , "tweet", "trick", "kiwi"]

# 문제: 몇 번째 사람이 탈락하는지 확인하는 코드를 작성하시오.

#조건: 비밀번호를 3번 이상 틀리면, 반복입력 기회는 없이 종료된다./ 'done'을 입력할 때 까지

words = ['round','dream','magnet','tweet','tweet','trick','kiwi']


def problem_daily_4_2():
    count = 0
    spoken_list = []
    if input("start를 입력하거나 그만두려면 done을 입력하세요.") == 'done':
        print('끝말잇기 게임을 종료합니다.')
    else:
        for word in words:
            
            count += 1
            spoken_list.append(word)
            if count >= 2:
                
                if word[0] != spoken_list[count-2][-1]:
                    print(f'탈락입니다. 앞선 단어의 마지막 문자로 말하지 않았습니다.{count}번째 사람이 탈락입니다.')
                    break
                
                
                elif word in spoken_list[0:count-1]:
                    print(f'탈락입니다. 앞서 나왔던 단어입니다.{count}번째 사람이 탈락입니다.')
                    break 
                else:
                    continue    
                                        
            else:
                continue
problem_daily_4_2()
  

#daily과제 4-4. 문자열 애너그램##########################################
words = ["eat", "tea", "tan", "ate", "nat", "bat"]

anagram_dict = {}  # 애너그램단위로 묶은 결과가 들어있는 딕셔너리
# key : 해당 단어를 정렬한 결과
# value : key와 같은 애너그램 그룹에 있는 단어들의 모음을 리스트로 만든다.

for word in words:
    sorted_word = "".join(sorted(word))  # sorted() => 결과가 리스트, 문자열로 변환해야한다. ==> join()
    # word = "eat"
    # sorted(word) = ["a" , "e" , "t"]
    # "".join(sorted(word)) = "aet"
    # ".".join(sorted(word)) = "a.e.t"
    print(sorted_word)
    if anagram_dict.get(sorted_word):  # 딕셔너리에 애너그램 그룹이 존재한다.
        anagram_dict[sorted_word].append(word)  # 존재하면 리스트에 추가를 해준다.
    else:
        anagram_dict[sorted_word] = [word]  # 존재하지 않으면 리스트를 새로 만들어준다.

print(anagram_dict)






