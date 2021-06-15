from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path('sign_in',views.sign_in),
    path('login',views.login),
    path('welcome',views.welcome),
    path('register',views.register),
    path('new',views.new),
    path('home',views.success),
    path('logout',views.logout),
    path('edit/<int:user_id>/update',views.edit_profile),
    path('add-image/<int:user_id>',views.add_image),
    path('delete_photo/<int:id>',views.delete_photo),
    path('photo/<int:id>/', views.viewPhoto),
    path('delete_account/<int:user_id>',views.delete_profile),
]
