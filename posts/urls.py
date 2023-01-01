from django.urls import path
from .views import PostsList, PostDetail, PostCreateNews, PostUpdate, PostDelete, SearchList, PostCreateArtcl

urlpatterns = [
    path('', PostsList.as_view(), name='post_list'),
    path('<int:pk>', PostDetail.as_view(), name='post_detail'),
    path('news/create/', PostCreateNews.as_view(), name='news_post_create'),
    path('news/<int:pk>/edit/', PostUpdate.as_view(), name='news_post_update'),
    path('news/<int:pk>/delete/', PostDelete.as_view(), name='news_post_delete'),
    path('articles/create/', PostCreateArtcl.as_view(), name='artcl_post_create'),
    path('articles/<int:pk>/edit/', PostUpdate.as_view(), name='artcl_post_update'),
    path('articles/<int:pk>/delete/', PostDelete.as_view(), name='artcl_post_delete'),
    path('search/', SearchList.as_view(), name='search_list'),
]
