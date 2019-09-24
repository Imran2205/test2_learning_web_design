from django.urls import path
from .views import home, about
from . import views
from django.conf.urls import url
from django.contrib import admin
from .views import PostListView, postdetail, UserPostListView, PostUpdateView, PostDeleteView, PostUpdateImageView#, BasicUploadView


urlpatterns = [
    path('', views.home, name = 'home-home'),
    path('about/', views.about, name = 'home-about'),
    path('blog/', PostListView.as_view(), name = 'home-blog'),
    path('user/<str:username>', UserPostListView.as_view(), name = 'user-posts'),
    path('blog/', PostListView.as_view(), name = 'home-blog'),
    #path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/<int:post_id>/', postdetail, name='post-detail'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name = 'post-update'),
    path('post/<int:pk>/update-image/', PostUpdateImageView.as_view(), name = 'post-update-image'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),


]