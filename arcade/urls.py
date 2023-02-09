"""arcade URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from arcade import views
from users import urls as user
from mypage import urls as mypage
from games import urls as games


urlpatterns = [
    path('admin/', admin.site.urls),
    # re_path(r'^$', views.HomeView.as_view(), name="arcade"),
    re_path(r'^$', views.redirectPage, name="checkRedirectPage"),
    path('users/', include(user)),
    path('mypage/', include(mypage)),
    path('games/', include(games)),
]

urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL,  document_root = settings.MEDIA_ROOT)