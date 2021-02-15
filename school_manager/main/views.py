from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def home(request):
	if request.user.is_authenticated:
		if request.user.is_confirmed:
			return render(request, 'mainPage/home.html')
		else:
			return render(request, 'mainPage/home_unconfirmed.html')
	else:
		return render(request, 'mainPage/home.html')
