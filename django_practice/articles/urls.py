from django.urls import path
from . import views

urlpatterns= [
   
    path('index/', views.index, name= 'index'),
    path('inherit/',views.inherit,name='inherit'),
    path('throw/',views.throw,name='throw'),
    path('catch/', views.catch,name='catch'),
    path('dinner/', views.dinner,name='dinner'), 
    path('hello/<name>/', views.hello,name='hello'),
]