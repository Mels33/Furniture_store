from django.urls import path

from users import views

app_name = 'users'

urlpatterns = [
    path('login/', views.login, name='login'),
    path('registration/',views.registration, name='registration'),
    path('profile/', views.profile, name='profile'),
    path('users_cart/', views.users_cart, name='users_cart'),
    path('logout/', views.logout, name='logout'),
    path('change_password/', views.ChangePassword.as_view(), name='change_password'),
    path('reset_password/', views.ResetPassword.as_view(), name='reset_password'),
    path('reset_password_done/', views.ResetPasswordDone.as_view(), name='reset_password_done'),
    path('reset_password/confirm/<uidb64>/<token>/', views.ResetPasswordConfirm.as_view(), name='reset_password_confirm')

]
