from django.urls import path
from . import views

urlpatterns = [
    path('', views.splash, name="splash"),
    path('firstpage/', views.frontpage, name="firstpage"),
]
