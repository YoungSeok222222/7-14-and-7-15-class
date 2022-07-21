'''
문제:끝말잇기 단어 리스트가 주어진 경우 몇 번쨰 사람이 탈락하는지 
코드 작성

조건: 앞선 단어 끝 문자로 시작 /
 틀리거나 이전에 등장했던 것 사용시 패배/
 done 입력시 까지
'''

# print(words[0][1])
def daily_4_2():
    words = ['round','dream','magnet','tweet','tweet','trick','kiwi']
    # b = list(words)
    
    while True:
        count = 0
        count_1 = 0
        for x in words:
            count+=1
        # print(x)
            if count >=2:
                print(words[0+count_1][-1])
                break
                # if x[0]!= words[0+count_1][-1]:
                #     print('탈락입니다.')
                # break
                # if x in b:
                #     print('패배입니다.')
            else:
                count_1+=1
                continue
        else:
            continue   
 
            print(x)
    

            # count = 1
            # # count_1 = 0
            # b = input()
        
            # for x in input():
            #     count+=1
            #     # # b= [x]
            #     # # b.sort(reverse=True)
            #     # print(b)
            # if count == 2:
            #     if x[0]!= b[0]:
            #         print('탈락입니다.')
            # if count >= 3:
        # if input() == 'done':
        #     break
    
    
    # # print(b)
    # # while 'done':
        
    # 
daily_4_2()           


