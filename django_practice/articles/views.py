from django.shortcuts import render
import random

# Create your views here.

def index(request):
    name = "치킨은 존맛"
    lunch = ['치킨','비빔밥','짜장면','팔보채']
    word = 'SSAFY'
    flag = 2
    context = {
        'name' : name,
        'lunch' : lunch,
        'word' : word,
        'flag': flag
    }
    return render(request,'index.html',context)

def inherit(request):
    return render(request,'inherit.html')

def throw(request):
    return render(request, 'throw.html')

def catch(request):
   

    message = request.GET.get('message')
    context = {
        'message' : message
    }
    return render(request,'catch.html',context)

def dinner(request):
    foods = ['족발','햄s버거','치킨','초밥']
    pick = random.choice(foods)
    context ={
        'pick' : pick,
        'foods' : foods,
    }
    return render(request,'dinner.html',context)

def hello(request,name):
    context = {
        'name' : name,
    }
    return render(request, 'hello.html',context)