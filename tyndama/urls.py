from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('get_music', views.get_music, name='get_music'),
    path('register/', views.registerPage, name='register'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutPage, name='logout'),
    path('add_music/', views.add_music, name='add_music'),
    path('delete_music/<int:pk>', views.delete_music, name='delete_music'),
    path('user_profile/', views.user_profile, name='user_profile'),
    path('admin_panel/', views.admin_panel, name='admin_panel'),

]