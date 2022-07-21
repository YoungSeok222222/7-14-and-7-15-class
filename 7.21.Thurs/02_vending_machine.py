from calendar import c


print('=================================')
print('         Vending Machine         ')
print('=================================')
print('[Menu]')
print('1. 콜라 500원')
print('2. 사이다 700원')
print('3. 레모네이드 4500원')
print('4. 오렌지주스 2000원')
print('5. 초코우유 1200원')
print('6. 아메리카노 3600원')
print('=================================')

menues = ['콜라', '사이다', '레모네이드', '오렌지주스', '초코우유', '아메리카노']  # 메뉴 이름
costs = [500, 700, 4500, 2000, 1200, 3600]  # 메뉴 가격
budget = 0  # 자판기에 넣은 총 누적 금액
dic_a = {}
while True:
    print()
    money = int(input('금액을 넣어주세요.(그만 넣으시려면 0을 입력하세요.) : '))

    # 여기부터 코드를 작성하세요.
    if   money<0:
        print("금액은 1원 이상 넣어주세요.")       
        continue 
    budget += money
    if money>0:
        print(f"현재 누적 금액은 {budget}원 입니다.")        
    elif money == 0:
        if budget<500:
            print(f'{budget}으로 구매 가능한 메뉴가 없습니다.')
        else:
            print(f'{budget}으로 구매 가능한 메뉴는 다음과 같습니다.')

            for x in range(len(costs)):
                #만약 구매 가능하다면
                if costs[x]<= budget:
                    print(f'{x+1},{menues[x]} {costs[x]}원')

        # 3 메뉴선택
        while True:
            try: 
                choice = int(input('구매하실 메뉴의 번호를 입력하세요.'))
                # 3-2 구매 가능한 메뉴를 선택했다면, 반복문 탈출
                if  costs[choice-1]<budget and 1<= choice <= 6:
                    break

                #3-3 구매 할 수 없는 메뉴를 고르면 문구 출력후 3-1로 돌아감
                print('구매할 수 없는 메뉴입니다.')
            except:
                print('1-6 사이의 숫자를 입력하세요.')
        # 4 거스름돈 반환
        # 4-1 어떤 메뉴를 선택했는지 문구 출력
        print(f'{menues[choice-1]}를 구매하셨습니다.')      
       
       
    # dic_a[menus[0]] = '500원'
    # dic_a[menus[1]] = '700원'
    # dic_a[menus[2]] = '4500원'
    # dic_a[menus[3]] = '2500원'
    # dic_a[menus[4]] = '1200원'
    # dic_a[menus[5]] = '3600원'   
       
       
       
        #     if budget >= 4500:
        #        pass 
        #     elif 3600< budget<4500:
        #         del dic_a['레모네이드']
                
        #     if 2000< budget <3600:
        #         del dic_a['아메리카노'], 
        #         del dic_a['레모네이드']
               
            
        #     if  1200 < budget < 2000:
        #         del dic_a['오렌지쥬스']
        #         del dic_a['아메리카노'], 
        #         del dic_a['레모네이드']
            
        #     if 700< budget<1200:
        #         del dic_a['초코우유']
        #         del dic_a['오렌지쥬스']
        #         del dic_a['아메리카노'], 
        #         del dic_a['레모네이드']
            
        #     if 500< budget<700:
        #         del dic_a['사이다']
        #         del dic_a['초코우유']
        #         del dic_a['오렌지쥬스']
        #         del dic_a['아메리카노'], 
        #         del dic_a['레모네이드']
                
        #     for index ,(key, values) in enumerate(dic_a.items()):
        #             print(index+1,key,values)

        # print('구매하실 메뉴의 번호를 입력하세요:') 



    ##############################################################            
                

            



           
            
  


