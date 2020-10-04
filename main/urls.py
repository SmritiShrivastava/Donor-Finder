from django.urls import path
from . import views

urlpatterns = [
    path('', views.homeView, name = "home"),
    path('signup', views.signUpView, name="signup"),
    path('login', views.logInView, name = "login"),
]