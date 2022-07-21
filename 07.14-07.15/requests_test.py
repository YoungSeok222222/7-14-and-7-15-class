# import requests를 사용하기 위해 터미널 창에 pip version 확인 후, pip install requests 입력
# ctrl + shift + p 로 python 확인(에러 뜨는 경우)
#.json() =  웹에서 제공하는 형태
import requests
'''
# 1021 회차 정보를 요청하는 주소
url = 'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=1021'

# 요청한 값에 따른 응답을 response 변수에 저장
response = requests.get(url).json()

# 응답(response) 에서 원하는 값 추출
print('첫 번째 뽑힌 번호 : ', response.get('drwtNo1'))
print('두 번째 뽑힌 번호 : ', response.get('drwtNo2'))
print('세 번째 뽑힌 번호 : ', response.get('drwtNo3'))
print('네 번째 뽑힌 번호 : ', response.get('drwtNo4'))
print('다섯 번째 뽑힌 번호 : ', response.get('drwtNo5'))
print('여섯 번째 뽑힌 번호 : ', response.get('drwtNo6'))
print('보너스 번호 : ', response.get('bnusNo'))
'''




import requests

url = 'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=1021'
response = requests.get(url).json()
print(response)
# print(response.get('name'))
# print(response.get('age'))

#drwtNo1: 12 / drwtNo2: 15 / drwtNo3: 17 / drwt No4:24 / drwtNo5:29 / drwtno6: 45 / bnusno: 16
url2 = "http://google.com"
response2 = requests.get(url2)
print(response2)


