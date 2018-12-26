from django.urls import path
from django.contrib.auth import views as auth_views
from . import views


app_name = 'apply'

urlpatterns = [
    path('login/', views.login_user, name='login_user'),
    path('register/', views.register_user, name='register_user'),
    path('logout/', views.logout_user, name='logout_user'),
    path('detail/<int:pk>', views.detail, name='detail'),
    path('profile/<int:pk>', views.profile, name='profile'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('', views.index, name='index'),
]
