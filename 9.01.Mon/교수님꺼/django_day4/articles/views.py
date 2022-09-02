from django.shortcuts import render, redirect
from .models import Article

# 온라인 실습실 1번 문제
# 변수 선언 후 index.html template 으로 데이터 전달
def index(request):
    name = '금기륜'
    fruit_list = ['귤', '딸기', '사과', '감', '바나나', '파인애플']
    hate = ['사과', '구아바']

    context = {
        'name': name,
        'fruit_list': fruit_list,
        'hate': hate,
    }

    return render(request, "articles/index.html", context)


# throw / catch 예제
def throw(request):
    return render(request, 'articles/throw.html')


# throw.html 의 form 태그 -> `action="{% url 'articles:catch' %}" method="GET"`
# 위 코드에 따라 catch 함수의 request 에 요청 정보가 들어감
# method 가 GET 이므로 request.GET 을 통해 데이터 추출 -> JSON 데이터
# JSON 데이터에서 특정 데이터 꺼내는 함수 : .get()
def catch(request):
    message = request.GET.get('message')

    context = {
        'message': message,
    }

    return render(request, 'articles/catch.html', context)

 
 # 게시판 메인 페이지
def main(request):
    # DB 의 Article 전체 데이터를 조회
    articles = Article.objects.all()

    # context 라는 이름의 dictionary 로 묶어서 template 으로 전달
    context = {
        'articles': articles,
    }

    return render(request, 'articles/main.html', context)


# 게시글 생성 파트 --------------------------------
# 1. 사용자의 입력을 받을 페이지
def new(request):
    return render(request, 'articles/new.html')


# 2. 입력 데이터를 이용하여 DB 에 넣는 함수
def create(request):
    # new.html 의 form 태그에서 method = POST 로 들어옴
    # 따라서 아래와 같이 request.POST 를 통해 JSON 데이터 추출
    title = request.POST.get('title')
    content = request.POST.get('content')

    # 원하는 방식대로 혹은 정해진 방식대로 데이터를 검증
    # == 유효성 검사

    article = Article(title=title, content=content)
    article.save()

    return redirect('articles:main')
# -------------------------------------------------

# 상세 페이지 조회
def detail(request, pk):
    # 단일 데이터 추출 API 코드
    article = Article.objects.get(pk=pk)

    context = {
        'article': article,
    }
    return render(request, 'articles/detail.html', context)


# 삭제
def delete(request, pk):
    article = Article.objects.get(pk=pk)
    article.delete()
    return redirect('articles:main')


# 수정 파트 -------------------------------------------------
# 1. 사용자의 입력을 받을 페이지
def edit(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article': article,
    }
    return render(request, 'articles/edit.html', context)


# 2. 실제로 DB 에 수정된 데이터를 넣는 함수
def update(request, pk):
    article = Article.objects.get(pk=pk)
    # edit.html 의 form 태그에서 POST 요청이 들어오므로 아래와 같이 작성
    article.title = request.POST.get('title')
    article.content = request.POST.get('content')
    article.save()
    return redirect('articles:detail', article.pk)

# -------------------------------------------------    