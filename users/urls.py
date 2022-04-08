from django.urls import path
from . import views


urlpatterns = [

	#Leave as empty string for base url
    path('', views.loginPage, name="login"),
	path('login', views.loginPage, name="login"),
    path('logout', views.logoutUser, name="logout"),
    path('register', views.registerPage, name="register"),
]