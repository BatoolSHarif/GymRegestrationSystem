"""GymMembershipN URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from mainapp import views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from django.urls import include, path
from rest_framework import routers
from api import views as api_views

router = routers.DefaultRouter()
router.register(r'users', api_views.UserInfoViewSet)



urlpatterns = [
    path('router', include(router.urls)),
    path('admin/', admin.site.urls),
    path('',views.UserCreatView.as_view() , name = 'user_url'),
    path('sub/',views.SubscriptionCreatView.as_view() , name = 'sub_url'),
    path('trans/',views.TransactionHistoryCreatView.as_view() , name = 'transaction_url'),
    path('visit/',views.VistisCreatView.as_view() , name = 'visit_url'),
    path('temp/',views.index),
    path('temp/base.html',views.index,name = 'base_url'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('json/', views.jsonview,name = 'jsonurl'),
    # path('batool/',api_views.snippet_list),
    path('api/',api_views.UserInfoList.as_view()),


]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)