# 사용자의 요청을 제일 먼저 만나는 곳
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # articles 앱과 관련된 urls 는 articles 앱에서 관리하기 위해
    # artulces 에 urls.py 를 따로 만들어주고, 
    # 여기(project url) 에서 include 를 사용하여 연결
    path('articles/', include('articles.urls')),
]
    # 127.0.0.1:8000/articles/
