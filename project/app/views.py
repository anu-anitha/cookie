from django.shortcuts import render
from datetime import datetime,timedelta
# Create your views here.
def setcookie(request):
	response=render(request,'setcookie.html')
	# response.set_cookie('name','sonam')
	response.set_cookie('name','sonam',max_age=60)#cookie will expires within 60sec
	response.set_cookie('name','sonam',expires=datetie.utcnow()+timedelta(days=2)) 
	return response


def getcookie(request):
	# name=request.COOKIES['name']
	name=request.COOKIES.get('name') #if we use get method ,by default name is None
	name=request.COOKIES.get('name','Guest') #when u dont want to get None value ..then add another name as guest.
	return render(request,'getcookie.html',{'xyz':name})

def delcookie(request):
	response=render(request,'delcookie.html')
	response.delete_cookie('name')
	return response


