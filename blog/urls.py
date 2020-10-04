from django.urls import path, include
from .views import blog_view, create_post,users_blog
from .views import PostDeleteView


app_name="Blogs"

urlpatterns=[
    path('', blog_view, name='blog'),
    path('post/',create_post,name='create_post'),
    path('userblogs/',users_blog,name='users_blogs'),
    path('post/<int:pk>/delete', PostDeleteView.as_view(), name='post-delete'),
 ]