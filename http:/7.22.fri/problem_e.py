import json

from problem_a import movie_info


def dec_movies(movies):

    # 여기에 코드를 작성합니다.
    dec = []
    for movie in movies:
        movie_dec = movie['release_date']
        movie_date_found = open(
            f'data/movies/{movie_dec}.json', encoding='utf-8')
        movie_info = json.load(movie_date_found)
    dec.append([movie_info['title'], movie_info['release_date']])
    # for result in dec:
    #     print(result)
    return dec


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='utf-8')
    movies_list = json.load(movies_json)

    print(dec_movies(movies_list))
