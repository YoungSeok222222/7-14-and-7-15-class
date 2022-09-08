from django.shortcuts import render, redirect, get_object_or_404
from .models import Article
from django.views.decorators.http import require_http_methods
from .forms import ArticleForm

def index(request):
    articles  = Article.objects.all()
    context = {
        'articles' : articles
    }
    return render(request,'articles/index.html', context)


@require_http_methods(['GET','POST'])
def create(request):
    # 사용자의 입력 후 요청이 들어 왔을 떄
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        # 유효성 검사
        if form.is_valid():
            article = form.save()
            return redirect('articles:index')
        return redirect('articles:create')

    # 사용자가 처음으로 생성 페이지에 접근할 떄
    else:
        # form을 만들고
        form = ArticleForm()
    context = {
        'form' : form
    }
    return render(request, 'articles/create.html', context)


def detail(request,pk):
    # article = Article.objects.get(pk=pk)
    # get_object_or_404 -> 데이터를 조회하지 못하면 404 에러를 띄워라!
    # 일반적으로 웹에서 없는 데이터 조회 시 404 에러를 띄움
    # 웹 서버랑 연동하게 되면 더 자세히 이해할 수 있음
    article = get_object_or_404(Article, pk=pk)
    context={
        'article' : article,
    }
    return render(request, 'articles/detail.html', context)

@require_http_methods(['GET','POST'])
def update(request,pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == 'POST':
        form = ArticleForm(request.POST,instance=article)
        if form.is_valid():
            form.save()
            return redirect('articles:detail',article.pk)
        # return redirect(request, 'articles:update')
    else:
        form = ArticleForm(instance=article)
    context = {
        'article' : article,
        'form' : form
    }
    return render(request,'articles/update.html',context)


def delete(request,pk):
    article = get_object_or_404(Article,pk=pk)
    article.delete()
    return redirect('articles:index')


