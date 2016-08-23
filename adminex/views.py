# -*- coding: utf8 -*-
from django.shortcuts import render
from login.login import check_user
from django.contrib.auth import logout as logout_view
import random


# Create your views here.
def index(request):
	if request.user.is_authenticated:
		return render(request, 'index.html')
	else:
		return render(request, 'login.html')


def login(request):
	if request.user.is_authenticated():
		return render(request, 'index.html')
	else:
		res = check_user(request)
		return res


def logout(request):
	logout_view(request)
	return render(request, 'login.html')


def eat(request):
	food_list = ['易食会', '地下一楼', '乌冬面', '嘿嘿嘿，逗你玩', '德克士', '麦金地', '味之都', '咖喱客',
				 '牛丼', '老碗']
	long_list = len(food_list)
	food = food_list[random.randint(0, long_list - 1)]
	return render(request, 'login.html', {'food': food})

# return  HttpResponse(food)
