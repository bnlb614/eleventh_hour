from django.shortcuts import render, get_object_or_404, render_to_response
from hour11.forms import User11HourForm, User11HourProfileForm
from django.template import RequestContext, loader
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login 
from hour11.models import User11Hour

def index(request):
	return render_to_response('hour11/index.html', context_instance=RequestContext(request))

def user_login(request):
	
	template = loader.get_template('hour11/login.html')
	context = RequestContext(request)

	if request.method == 'POST':

		username = request.POST['username']
		password = request.POST['password']

		user = authenticate(username=username, password=password)
		# two conditions:
		# 1. Is user already logged in? 
		# 2. Are these actual user details (eg, did they make a mistake
		# or are they actual members yet?)
		for special_user in User11Hour.objects.all():
			if username == special_user.user.username and not user:
				print("Username matches, but password doesn't")
			else:
				continue

		if user: 
			if user.is_active:
				login(request, user)
				return HttpResponseRedirect('/')

			else:
				return HttpResponse("Your account is disabled.")
		else:
			return HttpResponse("Invalid login details.")
	else:
		return render_to_response('login.html',{}, context)


def register(request):

	template = loader.get_template('hour11/register.html')
	context = RequestContext(request)

	registered = False

	if request.method == 'POST':

		user_form = User11HourForm(data=request.POST)
		profile_form = User11HourProfileForm(data=request.POST)

		if user_form.is_valid() and profile_form.is_valid():

			user = user_form.save()

			user.set_password(user.password)
			user.save()

			profile = profile_form.save(commit=False)
			profile.user = user

			# if 'picture' in request.FILES:
			# 	profile.picture = request.FILES['picture']

			profile.save()

			registered = True

		else:

			print(user_form.errors, profile_form.errors)

	else:
		user_form = User11HourForm()
		profile_form = User11HourProfileForm()

	return render_to_response('register.html',
							{'user_form':user_form, 
							'profile_form':profile_form, 
							'registered':registered},
							context)