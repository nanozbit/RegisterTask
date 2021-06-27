from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required(login_url="/login/")
def index(request):
    return render(request, "task/index.html", {})


@login_required(login_url="/login/")
def new_task(request):
    return render(request, "task/NewTask.html", {})
