from django.urls import path, include

from . import views

urlpatterns = [
	path('', views.home, name="home"),
    path('register', views.register, name="register"),
	path('login', views.login, name="login"),
	path("logout", views.logout, name="logout"),
    path("occupants", views.occupant, name="occupants"),
    path("floors", views.floor, name="floors"),
    path("units", views.unit, name="units"),
]