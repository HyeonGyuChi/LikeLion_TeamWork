from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('post/<int:post_id>', views.detail, name ='detail'),
    path('new/', views.new, name = 'new'),
    path('create/', views.create, name = 'create'),
    path('modify/<int:post_id>', views.modify, name = 'modify'),
    path('newmodify/<int:post_id>', views.newmodify, name = 'newmodify'),
    path('delete/<int:post_id>', views.delete, name = 'delete'),
    path('update/<int:post_id>', views.update, name = 'update'),
    path('newpost/', views.newpost, name = "newpost"),
]