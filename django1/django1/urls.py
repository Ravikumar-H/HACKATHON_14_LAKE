from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from quiz1 import views

urlpatterns = [
    path('', views.home, name='home'),
    path('admin/', admin.site.urls),
    path('quiz1/', include('quiz1.urls')),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    # Add this line for the default login path
    path('accounts/login/', auth_views.LoginView.as_view(), name='default_login'),
]
