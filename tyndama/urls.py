from django.urls import path
from django.urls import include, path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('get_music', views.get_music, name='get_music'),
    path('register/', views.registerPage, name='register'),
    path('', views.login_page, name='login'),
    path('logout/', views.logout_page, name='logout'),
    path('add_music/', views.add_music, name='add_music'),
    path('add_playlist/', views.add_playlist, name='add_playlist'),
    path('delete_music/<int:pk>', views.delete_music, name='delete_music'),
    path('user_profile/', views.user_profile, name='user_profile'),
    path('playlist/<int:playlist_id>/', views.playlist_detail, name='playlist'),
    path('admin_panel/', views.admin_panel, name='admin_panel'),
    path('add_to_playlist/', views.add_to_playlist, name='add_to_playlist'),

]
