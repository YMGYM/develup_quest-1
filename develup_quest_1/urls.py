"""develup_quest_1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from firstpage import urls as firstpage_urls
<<<<<<< HEAD
from findpet import urls as findpet_urls
=======
>>>>>>> b224e24f62b42ef4dc66789458a129c351235de0

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(firstpage_urls)),
<<<<<<< HEAD
    path('findpet', include(findpet_urls)),
=======
    
>>>>>>> b224e24f62b42ef4dc66789458a129c351235de0
]
