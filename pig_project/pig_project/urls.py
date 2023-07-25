"""pig_project URL Configuration

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
from django.urls import path
from monitor import views as monitor_views
from data1 import views as data1_views
from django.conf import settings

urlpatterns = [
    path('', data1_views.index, name='index'),
    path('casa/', monitor_views.casa, name='casa'),
    path('auto/', monitor_views.auto, name='auto'),
    path('indec/', monitor_views.indec, name='indec'),
    path('contacto/', monitor_views.contacto, name='contacto'),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)