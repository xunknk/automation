# -*- coding: utf8 -*-
from django.shortcuts import render
from django.contrib.auth import logout as logout_view
import random
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url='login.html')
def index(request):
	return render(request, 'index.html')


def login(request):
	if request.user.is_authenticated():
		return render(request, 'index.html')
	else:
		username = request.user.username
		querystr = request.META['QUERY_STRING']
		#password = request.user.password
		#if (username or password) is None:
		#print(request.user)
		if not querystr:
			UserID = '请输入用户名'
			PassWord = '请输入密码'
			return render(request, 'login.html', {'UserID': UserID, 'PassWord': PassWord})
		else:
			UserID = '用户名或密码不正确'
			PassWord = '用户名或密码不正确'
			return render(request, 'login.html', {'UserID': UserID, 'PassWord': PassWord})


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
