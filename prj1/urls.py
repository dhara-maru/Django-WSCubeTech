"""
URL configuration for prj1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from prj1 import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('about1/', views.about1, name='about1'),
    path('contact1/', views.contact1, name='contact1'),
     path('saveenquiry1/', views.saveenquiry1, name='saveenquiry1'),
    path('service1/', views.service1, name='service1'),
    path('userform1/', views.userform1, name='userform1'),
    path('submitform1/', views.submitform1, name='submitform1'),
    path('calc1/', views.calc1),
    path('evenorodd1/',views.evenorodd1),
    path('marksheet1/',views.marksheet1),
    
    path('newsdetail1/<id>',views.newsdetail),
    path('signup1/', views.signup1, name='signup1'),
    path('loginform1/', views.loginform1, name='loginform1')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)