from django.contrib.auth.views import PasswordChangeView, PasswordChangeDoneView, PasswordResetView, \
    PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView, LogoutView
from django.urls import path, reverse_lazy
from . import views
# from .views import verify_email

app_name = "members"

urlpatterns = [
    path('membership/', views.membership, name='membership'),
    path('login/', views.LoginMember.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', views.RegisterMember.as_view(), name='register'),
    path('profile/', views.ProfileMember.as_view(), name='profile'),
    path('account_activation_sent/', views.account_activation_sent, name='account_activation_sent'),
    path('activate/<uidb64>/<token>/', views.activate, name='activate'),
    path('register/account_activation_complete/', views.account_activation_complete, name='account_activation_complete'),




    path('password-change/', views.UserPasswordChange.as_view(),  name='password_change'),
    path('password-change/done/', PasswordChangeDoneView.as_view(template_name="members/password_change_done.html"), name='password_change_done'),

    path('password-change/', views.UserPasswordChange.as_view(template_name="members/password_change_done.html"), name='password_change'),

    path('password-reset/',
         PasswordResetView.as_view(
             template_name="members/password_reset_form.html",
             email_template_name="members/password_reset_email.html",
             success_url=reverse_lazy("members:password_reset_done"),

         ),
         name='password_reset'),


    path('password-reset/done/',
         PasswordResetDoneView.as_view(template_name = "members/password_reset_done.html"),
         name='password_reset_done'),

    path('password-reset/<uidb64>/<token>/',
         PasswordResetConfirmView.as_view(
            template_name="members/password_reset_confirm.html",
            success_url=reverse_lazy("members:password_reset_complete")
         ),
         name='password_reset_confirm'),


    path('password-reset/complete/', PasswordResetCompleteView.as_view(template_name="members/password_reset_complete.html"), name='password_reset_complete'),


    # path('register_done/', views.register_done, name='register_done'),
]