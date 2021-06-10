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
    #path('update/<int:user_id>',views.update),
    path('add-image',views.add_image),
    path('search/<int:user_id>',views.search),
    path('album',views.album)
]
