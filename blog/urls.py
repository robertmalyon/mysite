from django.urls import path
from . import views
from .views import PostListView, PostDetailView


urlpatterns = [
    path('', views.home, name='blog-home'),
    path('animated-me', views.animated_me, name='animated-me'),
    path('blog/', PostListView.as_view(), name='blog'),
    path('post/<int:pk>/', PostDetailView.as_view(),
         name='blog-post-detail'),
]
