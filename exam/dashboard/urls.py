from django.urls import path
from . import views


urlpatterns = [
    path('', views.check_registration, name='data_check'),
    #path('about/', views.about, name='about'),
    path('dashboard', views.check_registration, name='dashboard'),
    path('success', views.success, name='save_success'),
    path('address', views.address_job_view, name='address'),
    path('ajax/load-upozillas/', views.load_upozillas, name='load_upozillas'),

    
]