from django.urls import path
from . import views

app_name = 'lostpet'
urlpatterns = [
    path('', views.list, name='list'),
]
