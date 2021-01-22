from django.shortcuts import render
from forms.security.LoginForm import LoginForm
# Create your views here.


def index(request):
    form = LoginForm()
    return render(request, 'security/login.html', {'form': form})
