# -*- coding: utf8 -*-
from django.shortcuts import render
import login.logo as func_logo
import random
from django.http import HttpResponse


# Create your views here.
def index(request):
    return render(request, 'index.html')


def login(request):
    return render(request, 'login.html')


def eat(request):
    food_list = ['易食会', '地下一楼', '乌冬面', '嘿嘿嘿，逗你玩', '德克士', '麦金地', '味之都', '咖喱客',
                 '牛丼']
    long_list = len(food_list)
    food = food_list[random.randint(0, long_list - 1)]
    return render(request, 'login.html', {'food': food})
    # return  HttpResponse(food)
