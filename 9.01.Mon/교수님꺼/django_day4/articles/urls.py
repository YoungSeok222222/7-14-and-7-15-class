from django.urls import path
from . import views

# 네임스페이스 설정
app_name="articles"
urlpatterns = [
    # 온라인 실습실 1번 문제
    path('', views.index, name="index"),

    # 첫 날 복습
    path('throw/', views.throw, name="throw"),
    path('catch/', views.catch, name="catch"),
    # ------------------------------------------

    # 게시판 파트
    path('main/', views.main, name='main'),
    path('new/', views.new, name='new'),
    path('create/', views.create, name='create'),
    path('<int:pk>/', views.detail, name='detail'),
    path('<int:pk>/edit/', views.edit, name='edit'),
    path('<int:pk>/update/', views.update, name='update'),
    path('<int:pk>/delete/', views.delete, name='delete'),
]
