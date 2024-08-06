from django.urls import path, include
from rest_framework import routers
from . import views
from . import views as content_views
from . import api_views

routers = routers.DefaultRouter()

urlpatterns = [
    path('posts/', views.posts_list, name='posts_list'),
    path('posts/<int:post_id>/', views.post_details, name='post_details'),
    path('hello/<str:username>/', views.hello, name='say_hello'),
    path('index/', views.index ,name="posts_index"),
    path('post/<int:post_id>/', views.post_detail, name='post_detail'),
    path('post/<int:post_id>/like/', views.like_post, name='like_post'),
    path('post/<int:post_id>/dislike/', views.dislike_post, name='dislike_post'),
    path('create/', views.create_post, name='create_post'),
    path('', content_views.post_list)
    #path("api/post/", views.api_posts, name="posts_")

]