from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from fcm_django.models import FCMDevice



def register(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		c_password = request.POST['c_password']

		if password != c_password:
			return HttpResponse('<h1> Your password does not match. </h1>')
		else:
			user = User.objects.create_user(username=username, password=password)
			user = authenticate(username=username, password=password)
			login(request, user)

		return HttpResponse('<h1> Welcome {0} </h1>'.format(username))
	template = 'registration/register.html'
	return render(request, template)

def all_user(request):

	all_user = User.objects.all().exclude(is_superuser=True)

	context = {
		'all_user': all_user
	}

	template = 'registration/all_user.html'
	return render(request, template, context)

def user(request, username):
	context = {
		'username': username
	}
	template = 'registration/user.html'
	return render(request, template, context)

def notify(request, username):
	device = FCMDevice.objects.all().first()
	device.send_message(title="Hellow {0}".format(username), body="Hi {0} I am Mike.".format(username))
	return HttpResponse('<h1> Sent notification to {0} successfully</h1>'.format(username))
