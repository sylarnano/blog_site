from django.urls import path
from .feeds import LatestPostsFeed
from .views import PostCreateView, PostUpdateView, PostDeleteView
from . import views

app_name = 'blog'

urlpatterns = [
# post views
            # funtion base view
    path('post/create/', views.create_post, name='post_create'),
    path('post/<int:id>/delete/', views.delete_post, name='post_delete'),
    path('post/<int:id>/', views.update_post, name='post_update'),

    


    # path('post/<int:pk>/', PostUpdateView.as_view(), name='post_update'),
    # path('post/create/', PostCreateView.as_view(), name='post_create'),
    # path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),


    path('feed/', LatestPostsFeed(), name='post_feed'),
    path('', views.post_list, name='post_list'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/', views.post_detail, name='post_detail'),
    path('tag/<slug:tag_slug>/', views.post_list, name='post_list_by_tag'),

]