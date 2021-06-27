from django.urls import path
from apps.task import views

urlpatterns = [
   path('',  views.index, name='tasks'),
   path('add/', views.new_task, name="newTask")
]