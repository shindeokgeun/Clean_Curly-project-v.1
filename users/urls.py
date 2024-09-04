from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('loout/', views.logout_view, name='logout'),
    path('signup/', views.signup_view, name='signup'),
]