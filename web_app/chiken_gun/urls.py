"""
URL configuration for chiken_gun project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from camera_app.views import camera_source_view, stream_view, main_view, archive_view
from registration.views import login_view, registration_view

urlpatterns = [
    path('login/', login_view, name='login-view'),
    path('registration/', registration_view, name='registration-view'),
    path('camera_source/', camera_source_view, name='camera-source'),
    path('stream/', stream_view, name='stream'),
    path('main_page/', main_view, name='main-view'),
    path('archive/', archive_view, name='archive-view'),
    path('admin/', admin.site.urls),
]
