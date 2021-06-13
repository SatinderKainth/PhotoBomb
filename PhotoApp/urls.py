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
    path('add-image/<int:id>',views.add_image),
    path('delete_photo/<int:id>',views.delete_photo),
    path('gallery',views.gallery),
    path('photo/<int:id>/', views.viewPhoto),
    path('add',views.addPhoto),
    path('delete_profile/<int:user_id>',views.delete_profile),

]
