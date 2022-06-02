from django.urls import path
from .views import user_logout,register,user_login,profile
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("logout/",user_logout,name="logout"),
    path("register/",register,name="register"),
    path("login/",user_login,name="user_login"),
    path("profile/",profile,name="profile"),
    path('reset-password/', auth_views.PasswordResetView.as_view(template_name='users/reset_password.html'), name='reset_password'),
    # path('reset-password/', auth_views.PasswordResetView.as_view(template_name = "users/reset_password.html"), name ='reset_password'),
    # path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name = "users/password_reset_sent.html"), name ='password_reset_done'),
    # path('reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(template_name = "users/password_reset_form.html"), name ='password_reset_confirm'),
    # path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name = "users/password_reset_done.html"), name ='password_reset_complete'),


]