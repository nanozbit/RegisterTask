from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from django.http import HttpResponseRedirect
from forms.security.LoginForm import LoginForm
# Create your views here.

title = "Register Task"


def index(request):

    if request.method == 'POST':
        try :
            data = request.POST
            user = authenticate(username=data['username'], password=data["password"])
            if user is not None:
                login(request, user)
                print("Login success")
                return HttpResponseRedirect('/task/')
            else:
                print("You didn't login")
                return render(request, 'security/login.html', )
        except :
            print("Error:")

    return render(request, 'security/login.html', )


def logout_session(request):
    logout(request)
    return HttpResponseRedirect('/login/')
