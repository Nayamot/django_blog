"""dev_mozilla URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path,include
from App_local import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('App_local.urls')),
    path('blog/',views.blogpost, name='blog'),
    path('contact/',views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('lalbag/', views.lalbag, name='lalbag'),
    path('mountainpakistan/', views.mountainpakistan, name='mountainpakistan'),
    path('pyramid_egypt/', views.pyramid_egypt, name='pyramid_egypt'),



]
