import json
from pprint import pprint


def movie_info(movie, genres):
    result={} #원하는 정보만 담을 빈 딕셔너리 생성
    li= ['id','title','poster_path','vote_average','overview','genre_ids']
    for key in li:
        result[key]=movie[key]  # 딕셔너리에   key와 value 값 넣음
    genre_ids=result['genre_ids']# genre_ids의 value 값[18,80]을 넣을 리스트 생성 
    genre_list=[] # 장르 이름을 넣을 빈 리스트 생성
    for genre in genres: #genre = {"id": 28, "name": "Action"}와 같은 형식
        if genre['id'] in genre_ids: 
            genre_list.append(genre['name'])
    # 위의 for문이 끝나면 genre_list=['Crime','Drama']
    result['genre_names']=genre_list # 영화 정보를 담은 result 딕셔너리에 genre_names라는 키를 생성하고, 값을 입력
    del result['genre_ids'] # 기존의 genre_ids는 불필요하니 삭제
    return result





# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('data/movie.json', encoding='utf-8')
    movie = json.load(movie_json)

    genres_json = open('data/genres.json', encoding='utf-8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movie, genres_list))
