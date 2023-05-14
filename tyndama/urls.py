from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('get_music', views.get_music, name='get_music'),
    path('register/', views.registerPage, name='register'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutPage, name='logout'),
    path('add_music/', views.add_music, name='add_music'),
    path('user_profile/', views.user_profile, name='user_profile'),
    path('playlist/<int:playlist_id>/', views.playlist_detail, name='playlist'),

]