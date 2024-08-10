from django.urls import path
from . import views


urlpatterns = [
    path('', views.check_registration, name='data_check'),
    #path('about/', views.about, name='about'),
    path('dashboard', views.check_registration, name='dashboard'),
    path('success', views.success, name='save_success'),

    
]