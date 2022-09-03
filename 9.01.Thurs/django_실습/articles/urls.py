from django.urls import path
from . import views


app_name = 'articles'
urlpatterns = [
    path('index/',views.index, name ='index'), # name은 별칭
    path('throw/', views.throw, name = 'throw'),
    path('catch/', views.catch, name = 'catch'),
#--------------------------------------------------------

    path('main/', views.main, name = 'main'),
    path('new/', views.new, name = 'new'),
    path('create/', views.create, name='create'),
    path('<int:pk>', views.detail, name = 'detail'),
    # 수정
    path('<int:pk>/edit/', views.edit, name='edit'),
    path('<int:pk>/update/', views.update, name = 'update'),
    # 삭제
    path('<int:pk>/delete/', views.delete, name='delete'),
]





