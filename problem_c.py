import json
from optparse import Values
from pprint import pprint


def movie_info(movies, genres):
    # 여기에 코드를 작성합니다.  
    res={} #moive 1편 정보를 담는 딕셔너리
    result=[] #결과값이 들어갈 리스트
    li= ['id','title','poster_path','vote_average','overview','genre_ids']
    for movie in movies: 
    #movie=딕셔너리(영화1편 정보), movies=여러 영화들의 정보 리스트
        for key in li:
            res[key]=movie[key]  # 딕셔너리에   key와 value 값 넣음
        genre_ids=res['genre_ids']# [18,80]을 넣을 리스트 생성 
        genre_list=[] # 장르 이름을 넣을 빈 리스트 생성
        for genre in genres: #genre = {"id": 28, "name": "Action"}와 같은 형식
            if genre['id'] in genre_ids: 
                genre_list.append(genre['name'])
        # 위의 for문이 끝나면 genre_list=['Crime','Drama']
        res['genre_names']=genre_list # 영화 정보를 담은 result 딕셔너리에 genre_names라는 키를 생성하고, 값을 입력
        del res['genre_ids'] # 기존의 genre_ids는 불필요하니 삭제
        result.append(res)
    return result
    

        
# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='utf-8')
    movies_list = json.load(movies_json)

    genres_json = open('data/genres.json', encoding='utf-8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movies_list, genres_list))
