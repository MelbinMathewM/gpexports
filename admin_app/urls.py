

from django.urls import path
from admin_app import views


urlpatterns = [

    path('user_list',views.register_user,name='register_user'),
    path('quatations',views.quotes,name='quotes'),
    path('feedback',views.feedback,name='feedback'),
    path('login_admin',views.login_admin,name='login_admin'),
    path('logout_user',views.logout_user,name='logout_user'),
    
]