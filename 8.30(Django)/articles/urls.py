
from django.urls import path
#  articles의 view를 사용한다
from . import views



urlpatterns = [
    path('index/', views.index, name ='index'),
    path('inherit/', views.inherit, name='inherit'),
    path('throw/', views.throw,name='throw'),
    path('catch/', views.catch, name='catch'),
    path('hello/<str:name>/', views.hello),
]
