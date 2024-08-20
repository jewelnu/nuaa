from django.urls import path
from . import views

from .views import SuccessView, ContactView

urlpatterns = [
    path("contact/", ContactView.as_view(), name="contact"),
    path("success/", SuccessView.as_view(), name="success"),
    path('contact_us/', views.contact_us, name='contact_us'),
]