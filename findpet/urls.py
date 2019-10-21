from django.urls import path
from . import views

app_name = 'findpet'
urlpatterns = [
    path('', views.list, name='list'),
]
