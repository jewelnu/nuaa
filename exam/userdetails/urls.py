from django.urls import path
from .views import project_stage_view

urlpatterns = [
    path('', project_stage_view, name='project_stage'),
]