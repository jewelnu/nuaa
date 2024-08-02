from django.urls import path
from . import views


urlpatterns = [

    path('', views.homepage, name=''),
    path('register', views.register, name='register'),
    path('my-login', views.my_login, name='my-log'),
    path('dashboard', views.Dashboard, name='dashboard'),
    path('logout', views.User_logout, name='logout'),
   

]