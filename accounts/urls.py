from django.urls import path
from django.contrib.auth import views as auth_views
from accounts import views
from .views import usuariosaplicacionxls, usuariosaplicacion
from .views import LoginView, LogoutView

#JJ
urlpatterns =[
    path('', views.index, name='index'),
    #path('login', views.login, name='login'),
    path('login/', LoginView.as_view(), name='login'),
    #path('logout', views.logout, name='logout'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('password_change/',
        auth_views.PasswordChangeView.as_view(template_name='accounts/password_change_form.html'),
        name='password_change'),
    path('password_change/done/',
        auth_views.PasswordChangeDoneView.as_view(template_name='accounts/password_change_done.html'),
        name='password_change_done'),
    # reset password urls
    path('password_reset/',
        auth_views.PasswordResetView.as_view(template_name='accounts/password_reset_form.html'),
        name='password_reset'),
    path('password_reset/done/',
        auth_views.PasswordResetDoneView.as_view(template_name='accounts/password_reset_done.html'),
        name='password_reset_done'),
    path('reset/<uidb64>/<token>/',
        auth_views.PasswordResetConfirmView.as_view(template_name='accounts/password_reset_confirm.html'),
        name='password_reset_confirm'),
    path('reset/done/',
        auth_views.PasswordResetCompleteView.as_view(template_name='accounts/password_reset_complete.html'),
        name='password_reset_complete'),
    path('register/', views.register, name='register'),
    path('accounts/usuariosaplicacionxls/', usuariosaplicacionxls, name='usuariosaplicacionxls'),
    path('accounts/usuariosaplicacion/',usuariosaplicacion, name='usuariosaplicacion'),

]

