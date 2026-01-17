from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', views.register, name='signup'),
    path('login/', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('profile/', views.profile_detail, name='perfil_detail'),
    path('profile/edit/', views.profile_change, name='profile_change'),
    path('password/', auth_views.PasswordChangeView.as_view(
        template_name='users/password_change.html',
        success_url='/users/profile/'
    ), name='password_change'),
]