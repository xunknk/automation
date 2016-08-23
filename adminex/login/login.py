# -*- coding: utf8 -*-
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login


def check_user(request):
	login_user = request.GET.get('login_user', None)
	login_pwd = request.GET.get('login_pwd', None)
	#    user_from_db=models.
	#    query_user = query.
	user_views = authenticate(username=login_user, password=login_pwd)
	if user_views is not None:
		if user_views:
			login(request, user_views)
			return render(request, 'index.html')
		else:
			return render(request, 'login.html')
	else:
		return render(request, 'login.html')
