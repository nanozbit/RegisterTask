from django.contrib.auth import authenticate
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from forms.security.LoginForm import LoginForm
# Create your views here.


def index(request):

    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data["password"])
            print(user)
            if user is not None:
                print("Login success")
            else:
                print("You didn't login")

            return HttpResponseRedirect('/login/')

    return render(request, 'security/login.html', {'form': form})

