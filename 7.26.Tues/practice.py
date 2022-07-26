# 소금물 농도 = 소금의양/소금물의 양 *100
# 소금의 양 = 소금물 농도*소금물의 양 /100

def mass():
    salt = 0
    total_water = 0
    for _ in range(4): #최대 5번 반복
        salty = list(map(str,input('농도와 소금물의 양을 최대 5번까지 입력하고, Done을 입력하는 경우 계산합니다.').split())) # 농도와 소금물을 입력받음
        if salty[0] == 'Done':   # 입력받는 도중 농도에 'Done'을 입력하는 경우
            break
        else:
            perc, s_water = int(salty[0]), int(salty[1]) # 입력받은 값을 농도와 소금물로
            salt += perc * s_water / 100       # 소금 = 농도*소금물 /100
            total_water += s_water     # 입력받은 소금물 더하기
    percent = salt / total_water * 100 # 농도 = 소금 / 소금물 *100
    return f'농도: {percent}%, 소금물: {total_water}g.'
    
print(mass())