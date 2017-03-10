# -*- coding: utf8 -*-
from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.contrib.auth import logout as logout_django
import random
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url='login.html')
def index(request):
	return render(request, 'index.html')


def login(request):
	if 'login_user' in request.GET:
		username = request.GET['login_user']
		password = request.GET['login_pwd']
		if (username and password) is True:
			user = authenticate(username=username, password=password)
			if user is not None:
				if user.is_active:
					return render(request, 'index.html')

			else:
				UserID = '用户名或密码不正确'
				PassWord = '用户名或密码不正确'
				return render(request, 'login.html', {'UserID': UserID, 'PassWord': PassWord})
		else:
			UserID = '请输入用户名'
			PassWord = '请输入密码'
			return render(request, 'login.html', {'UserID': UserID, 'PassWord': PassWord})
	else:
		UserID = '请输入用户名'
		PassWord = '请输入密码'
		return render(request, 'login.html', {'UserID': UserID, 'PassWord': PassWord})


def logout(request):
	UserID = '请输入用户名'
	PassWord = '请输入密码'
	logout_django(request)
	return render(request, 'login.html', {'UserID': UserID, 'PassWord': PassWord})


def eat(request):
	UserID = '请输入用户名'
	PassWord = '请输入密码'
	food_list = ['易食会', '地下一楼', '乌冬面', '嘿嘿嘿，逗你玩', '德克士', '麦金地', '味之都', '咖喱客',
				 '牛丼', '老碗']
	long_list = len(food_list)
	food = food_list[random.randint(0, long_list - 1)]
	return render(request, 'login.html', {'food': food, 'UserID': UserID, 'PassWord': PassWord})

# return  HttpResponse(food)
