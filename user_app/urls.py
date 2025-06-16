from django.urls import path

from user_app import views


urlpatterns = [
    path('',views.Home_page, name='Home_page'),
    path('home',views.Home_page,name='Home_page'),
    path('about',views.about,name='about'),
    path('service',views.service,name='service'),
    path('gallery',views.gallery,name='gallery'),
    path('contact_us',views.contact_us,name='contact_us'),
    path('404',views.error,name='error'),
    
]