from django.urls import path
from . import views

from .views import SuccessView, ContactView

urlpatterns = [
    path('', views.contact_us, name='contact_us'),
    path("contact/", ContactView.as_view(), name="contact"),
    path("success/", SuccessView.as_view(), name="success"),
]