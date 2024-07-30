from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('<str:task_id>', views.result, name='result'),
]
