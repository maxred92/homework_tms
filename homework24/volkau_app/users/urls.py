from django.urls import path, reverse_lazy, include
from django.contrib.auth import views as auth_views
from . import views
from . import forms

app_name = 'users'

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(next_page='store:index', template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='store:index'), name='logout'),
    path('change-password/', views.CustomPasswordChange.as_view(), name='change-password'),
    path('change-pass-confirm/',
        auth_views.PasswordResetDoneView.as_view(
            template_name="users/password_success.html"
        ),
        name="password_change_done",
    ),
    path('password-reset', auth_views.PasswordResetView.as_view(
        email_template_name='users/password_reset_mail.html',
        template_name='users/password_reset.html',
        success_url=reverse_lazy('users:pass-reset-done')),
        name='pass-reset'),
    path('password-reset-done', auth_views.PasswordResetDoneView.as_view(
        template_name='users/password_reset_done.html'),
        name='pass-reset-done'),
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        success_url=reverse_lazy('users:reset_complete'),
        template_name='users/password_reset_confirm.html'),
        name='password_reset_confirm'),
    path('password-reset-complete', auth_views.PasswordResetCompleteView.as_view(
        template_name='users/password_reset_complete.html'),
        name='reset_complete'),
]