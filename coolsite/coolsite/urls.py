"""
URL configuration for coolsite project.

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
from django.urls import path, include

from Ambrella.views import *

handler500 = 'myapp.views.handler500'
handler403 = 'myapp.views.handler403'
handler400 = 'myapp.views.handler400'
handler_csrf_failure = 'myapp.views.handler_csrf_failure'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Ambrella.urls')),

]

handler404 = pageNotFound
handler500 = FailServer
handler403 = AccessВenied
handler400 = ProcessingFail
