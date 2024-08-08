from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('members/alumni/', views.alumni_members, name='alumni_members'),
    path('members/committee/', views.committee_members, name='committee_members'),
    path('notice/', views.notice, name='notice'),
    path('downloads/', views.downloads, name='downloads'),
    path('gallery/', views.gallery, name='gallery'),
    path('message/', views.message, name='message'),
    path('faq/', views.faq, name='faq'),
    path('contact_us/', views.contact_us, name='contact_us'),
]
