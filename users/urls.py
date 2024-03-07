from django.urls import path
from django.contrib.auth.views import PasswordResetView,PasswordResetConfirmView,PasswordResetDoneView,PasswordResetCompleteView

from .views import Login,Logout,UserProfile,signup
urlpatterns = [
    path('login/', Login.as_view(), name='login'),
    path('logout/', Logout.as_view(), name='logout'),
    path('profile/', UserProfile.as_view(), name='profile'),
    path('signup/', signup, name='signup'),
    path('password-reset/', PasswordResetView.as_view(template_name='users/reset.html'), name='password_reset'),
    path('password-reset-confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(template_name='users/confirm.html'), name='password_reset_confirm'),
    path('password-reset/done/', PasswordResetDoneView.as_view(template_name='users/done.html'), name='password_reset_done'),
    path('password-reset/complete', PasswordResetCompleteView.as_view(template_name='users/complete.html'), name='password_reset_complete'),
]