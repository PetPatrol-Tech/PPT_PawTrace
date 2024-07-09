"""pet_management URL Configuration

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
from django.urls import path
from . import views,search,record

urlpatterns = [
    path("dbtest/",record.record),
    path("admin/", admin.site.urls),
    path("search/",search.search),
    path("search-form/",search.search_form),
    path("informationOfLivers/",views.information),
    path("choices",views.option),
    path('option1/', views.option1, name='option1'),
    path('option2/', views.option2, name='option2'),
    path('option3/', views.option3, name='option3'),
]
