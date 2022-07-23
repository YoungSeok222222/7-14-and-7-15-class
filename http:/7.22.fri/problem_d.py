import json
from re import X

from problem_b import movie_info


def max_revenue(movies):
   # movies를 순회하면서 영화 하나씩 변수 저장
    res=[]
    for movie in movies:
        movie_id=movie['id']
        movie_founded = open(f'data/movies/{movie_id}.json', encoding='utf-8')
        movie_info = json.load(movie_founded)
   # 저장된 변수의 id값을 이용해서 movies폴더에서 id값에 해당하는 파일을 찾기
   # 찾아온 파일을 변수에 저장
    res.append([movie_info['title'], movie_info['revenue']])
    res=sorted(res, key=lambda x:x[1], reverse=True)
   
   # 저장된 변수에서 revenue를 찾기

    return res[0][0]





        
# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='utf-8')
    movies_list = json.load(movies_json)
    
    print(max_revenue(movies_list))
