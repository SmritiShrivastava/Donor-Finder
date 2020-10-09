from django.urls import path
from . import views

urlpatterns = [
    path('', views.homeView, name = "home"),
    path('signup', views.signUpView, name="signup"),
    path('login', views.logInView, name = "login"),
    path('logout', views.logoutView, name = "logout"),
    path('donate', views.donateView, name = "donate"),
    path('detail', views.detailView, name = "detail"),
    path('receive', views.receiveView, name = "receive"),
    path('find', views.findDonorView, name = "find")
]