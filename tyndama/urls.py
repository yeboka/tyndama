from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('get_music', views.get_music, name='get_music'),
    path('register/', views.registerPage, name='register'),
    path('login/', views.loginPage, name='login'),

]