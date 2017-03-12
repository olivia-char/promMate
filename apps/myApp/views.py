from django.shortcuts import render, redirect, HttpResponse
from .models import User
from django.contrib import messages

# Create your views here.

def index(request):
	print "at index"
	return render(request, "myApp/index.html")

def register(request):
	print "data sent to register"
	if request.method == 'POST':
		fname = request.POST['first_name']
		lname = request.POST['last_name']
		email = request.POST['email']
		pw = request.POST['password']
		cpw = request.POST['c_password']

	newUser = User.userManager.register(fname, lname, email, pw, cpw) 
	print "sent to db"

	if newUser[0] == False:
		print newUser[1]['errorMessage']
		errorMessage = newUser[1]['errorMessage']
		for i in errorMessage:
			messages.error(request, i)
		return redirect('/')
	else:
		request.session['id'] = newUser[1].id
		print newUser[1].id	
		return redirect("/homePage")

def login(request):
	print "login page"
	if request.method == 'POST':
 		email = request.POST['email']
		password = request.POST['password']
		loginUser = User.userManager.login(email, password)

		if loginUser[0] == False:
			errorMessage = loginUser[1]['errorMessage']
			for i in errorMessage:
				messages.error(request, i)
			return redirect('/') 
		else:
			print loginUser[1]
			request.session['id'] = loginUser[1].id 
			print "What's in session", request.session['id']
		
		return redirect('/homePage')

def homePage(request):
	return render(request, "myApp/homepage.html")

def cart(request):
	return render(request, "myApp/cart.html")

def userPage(request):
	return render(request, "myApp/userpage.html")

def match(request):
	return render(request, "myApp/match.html")

def addDress(request):
	return render(request, "myApp/addDress.html")
