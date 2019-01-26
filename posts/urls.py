from django.urls import path, include
from . import views

app_name = 'posts'

urlpatterns = [
    path('create/', views.create, name='create'),
    path('upvote/<int:pk>/', views.upvote, name='upvote'),
    path('downvote/<int:pk>/', views.downvote, name='downvote'),
    path('user/<int:fk>/', views.userposts, name='userposts'),
]
