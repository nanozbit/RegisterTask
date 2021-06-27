from django.urls import path
from apps.security import views

urlpatterns = [
    path('login/', views.index, name="login"),
    path('logout/', views.logout_session, name="logout")
]

