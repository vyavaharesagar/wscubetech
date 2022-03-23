"""wscubetech URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from wscubetech import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homepage, name = "home"),
    path('blog/', views.blog, name="blog"),
    path('contact-us/', views.contact, name ="contact"),
    path('about-us/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('blog-details/', views.blog_details, name='blog-details'),
    path('index-2/', views.index2, name='index-2'),
    path('index-3/', views.index3, name='index-3'),
    path('index-4/', views.index4, name='index-4'),
    path('course/', views.course, name='course'),
    path('team/', views.team, name='team'),
    path('userform/', views.userform, name='userform'),
    path('submitform/', views.submitform, name='submitform'),
    # path('course/<int:course_id>', views.courseDetail, name='Course Detail'),
    # path('course/<str:course_str>', views.courseDetailWithStr, name='Course Detail With String'),
    path('course/<course_name>', views.courseDetailWithAnyType, name='course_name'),
    path('calculator/', views.calculator, name='calculator'),
    path('newsdetail/<news_id>', views.newsDetail, name='newsdetail'),
]
