import random

is_playing = True

# answer = int(input("답을 입력하세요."))
counts = 0  # 몇 번만에 정답을 맞혔는지 담는 변수
answer = random.randint(1, 1000)  # 1이상 10000이하의 난수

while is_playing:
    print('================================')
    print('        Up and Down Game        ')
    print('================================')
    a = int(input('1이상 1000이하의 수를 입력하세요:'))
        # 여기부터 코드를 작성하세요.
    counts+=1
    if a<0:
        print('잘못된 범위의 숫자를 입력하셨습니다. 다시 입력하여 주세요.')
    elif a == answer:
        print(f'정답입니다. {counts}번만에 맞히셨습니다.')
        answer = random.randint(1, 1000)
        print(answer)
        counts =0
        chance = input("게임을 재시작하려면 y, 종료하시려면 n을 눌러주세요:")
        if chance == 'y':
            continue
        elif chance =='n':
            print('이용해주셔서 감사합니다. 게임을 종료합니다.')
            is_playing = False
        else:
            print('잘못된 값을 입력하셨습니다. 게임을 종료합니다.')
    if answer > a:
        print('up!!')
        
    elif answer < a:
        print('down!!  ')
        
 
    
    
    
    
   

        
        



